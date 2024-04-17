import json
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Union

from pyspark.sql import DataFrame
from pyspark.sql.functions import lit
from pyspark.sql.types import StructType

from ng_data_pipelines_sdk.aws_interface import AWSInterface
from ng_data_pipelines_sdk.interfaces import (
    DATE_FORMATTER,
    DataFrameReadWriteParams,
    DatePartition,
    FileType,
    FnKind,
    InputDataFrameParams,
    InputDataFrameParamsDict,
    OutputDataFrameParams,
    OutputDataFrameParamsDict,
    S3BucketParams,
    S3ReadJsonParams,
    StepParams,
    StepParamsDict,
    TransformParams,
    TransformParamsDict,
    DataFrameDict,
)
from ng_data_pipelines_sdk.custom_logger import logger
from ng_data_pipelines_sdk.spark_manager import SparkManager
from ng_data_pipelines_sdk.utils import (
    handle_pyspark_timestamp_in_schema,
)

logger.setLevel("INFO")


class DataFrameManager:
    def __init__(
        self,
        file_system: str,
        aws_interface: AWSInterface,
        spark_manager: SparkManager,
    ):
        """
        Initializes a new instance of the DataFrameManager class.

        Args:
            file_system (str): The file system to be used by the DataFrameManager.
            aws_interface (AWSInterface): An instance of the AWSInterface class.
            spark_manager (SparkManager): An instance of the SparkManager class.

        Returns:
            None
        """
        self.file_system = file_system
        self.aws_interface = aws_interface
        self.spark_manager = spark_manager
        self.completed_steps = []
        logger.info("DataFrameManager initialized.")

    def _get_bucket_url(self, bucket_params: S3BucketParams) -> str:
        return f"{self.file_system}://{bucket_params.bucket_name}"

    def _get_processing_date_partition_path(
        self, df_params: Union[DataFrameReadWriteParams, DataFrameReadWriteParams]
    ) -> str:
        if df_params.processing_date_partitions is None:
            return ""

        if not isinstance(df_params.processing_date, datetime):
            raise ValueError(
                f"processing_date must be a datetime object to calculate partition path. Received: '{df_params.processing_date}'"
            )

        partition_path_segments = [
            f"{date_part.value}={DATE_FORMATTER[date_part.value.replace('part_', '')](df_params.processing_date)}"
            for date_part in df_params.processing_date_partitions
        ]

        processing_date_partition_path = "/".join(partition_path_segments)

        return processing_date_partition_path

    def _get_dataframe_path_with_date_partitions(
        self, df_params: DataFrameReadWriteParams
    ) -> str:
        dataframe_path_with_date_partitions = f"{df_params.path_to_dataframe_root}/{self._get_processing_date_partition_path(df_params)}"

        return dataframe_path_with_date_partitions.strip("/")

    def convert_schema_object_to_pyspark_schema(
        self, schema_object: Dict[str, Any]
    ) -> StructType:
        logger.debug("Converting schema object to PySpark StructType...")
        pyspark_schema = StructType.fromJson(schema_object)
        pyspark_schema = handle_pyspark_timestamp_in_schema(pyspark_schema)
        logger.debug(f"Schema converted sucessfully: {pyspark_schema}")

        return pyspark_schema

    def retrieve_schema_from_s3(
        self, s3_read_schema_params: S3ReadJsonParams
    ) -> StructType:
        """
        Retrieve the schema for the data from an AWS S3 bucket.

        Returns:
            pyspark.sql.types.StructType: The retrieved schema.

        Raises:
            ValueError: If there is an issue retrieving or handling the schema.
        """

        if s3_read_schema_params is None:
            raise ValueError(
                "s3_schema_path_params must be provided to retrieve schema from S3"
            )

        if s3_read_schema_params.bucket_params.bucket_name is None:
            raise ValueError("bucket_name must be provided to retrieve schema from S3")

        bucket_name = s3_read_schema_params.bucket_params.bucket_name
        path_to_file = s3_read_schema_params.path
        full_s3_file_path = f"{self.file_system}://{bucket_name}/{path_to_file}"

        logger.debug(f"Retrieving schema from path '{full_s3_file_path}'...")
        try:
            # Retrieve the schema object from AWS S3
            schema_object = self.aws_interface.get_object_aws(
                env=s3_read_schema_params.bucket_params.env,
                bucket_name=bucket_name,
                object_name=path_to_file,
            )

            # Decode the object to a string
            schema_str = schema_object.decode("utf-8").strip()

            # Convert the string to JSON
            schema_json = json.loads(schema_str)

            # Convert the JSON schema to a PySpark StructType
            pyspark_schema = StructType.fromJson(schema_json)

            logger.debug(f"Schema retrieved sucessfully: {pyspark_schema}")

            # Handle any timestamp issues in PySpark schema, if necessary
            return handle_pyspark_timestamp_in_schema(pyspark_schema)
        except Exception as e:
            error_message = (
                f"Error retrieving or handling schema from {full_s3_file_path}: {e}"
            )
            logger.error(error_message)
            raise ValueError(error_message)

    def read_dataframe(self, df_params: InputDataFrameParams) -> DataFrame:
        read_params = df_params.df_params
        bucket_url = self._get_bucket_url(read_params.bucket_params)
        if read_params.specific_path:
            path = f"{bucket_url}/{read_params.specific_path}"
        else:
            path = f"{bucket_url}/{self._get_dataframe_path_with_date_partitions(read_params)}"

        if df_params.pyspark_schema_struct:
            schema = self.convert_schema_object_to_pyspark_schema(
                schema_object=df_params.pyspark_schema_struct
            )
        elif df_params.s3_schema_path_params:
            schema = self.retrieve_schema_from_s3(df_params.s3_schema_path_params)
        else:
            schema = None

        logger.info(f"Reading DataFrame from {path}...")

        df = self.spark_manager.read(
            env=read_params.bucket_params.env,
            path=path,
            file_type=df_params.df_params.file_type,
            schema=schema,
        )

        return df

    def write_schema(
        self, df: DataFrame, write_params: DataFrameReadWriteParams
    ) -> None:
        """
        Write the schema of the DataFrame to the specified location.

        Parameters:
        - df (DataFrame): The DataFrame whose schema is to be written.

        Raises:
        - ValueError: If there is an issue with writing the schema object to AWS S3.
        """
        pyspark_schema_json = df.schema.jsonValue()
        bucket_name = write_params.bucket_params.bucket_name

        if bucket_name is None:
            raise ValueError("bucket_name must be provided to write schema to S3")

        if write_params.specific_path:
            logger.warning(
                "Specific path is set for writing the schema. Schema will be written to the same path."
            )
            path_to_schema = write_params.specific_path
        else:
            if write_params.path_to_dataframe_root is None:
                raise ValueError(
                    "Neither 'specific_path' nor 'path_to_dataframe_root' is set for writing the schema."
                )

            parent_folder_of_dataframe_root = "/".join(
                write_params.path_to_dataframe_root.split("/")[:-1]
            )
            path_to_schema = f"{parent_folder_of_dataframe_root}/schema.json"

        try:
            self.aws_interface.put_object_aws(
                env=write_params.bucket_params.env,
                bucket_name=bucket_name,
                object_name=path_to_schema,
                object_data=pyspark_schema_json,
            )
        except Exception as e:
            raise ValueError(
                f"Error writing schema to {bucket_name}/{path_to_schema}: {e}"
            )

    def _add_date_partitions_columns(
        self, df: DataFrame, date_partitions: DatePartition
    ) -> DataFrame:
        for date_part, value in date_partitions:
            if value is not None:
                df = df.withColumn(
                    date_part,
                    lit(DATE_FORMATTER[date_part](value)),
                )

        return df

    def _get_partitions(self, write_params: DataFrameReadWriteParams) -> List[str]:
        date_partition_columns: List[str] = []
        if write_params.processing_date_partitions:
            for date_partition in write_params.processing_date_partitions:
                date_partition_columns.append(date_partition.value)

        # Choose the order of adding partitions based on the `date_partition_first` flag
        primary_partitions = (
            date_partition_columns
            if write_params.processing_date_partitions_first
            else write_params.column_partitions
        )
        secondary_partitions = (
            write_params.column_partitions
            if write_params.processing_date_partitions_first
            else date_partition_columns
        )

        partitions: List[str] = []
        if primary_partitions:
            partitions.extend(primary_partitions)
        if secondary_partitions:
            partitions.extend(secondary_partitions)

        return partitions

    def write_dataframe_specific_path(
        self, df: DataFrame, df_params: OutputDataFrameParams
    ) -> None:
        write_params = df_params.df_params
        bucket_url = self._get_bucket_url(write_params.bucket_params)
        write_path_url = f"{bucket_url}/{write_params.path_to_dataframe_root}"

        logger.info(f"Writing DataFrame to path: {write_path_url}...")
        self.spark_manager.write(
            env=write_params.bucket_params.env,
            df=df,
            path=write_path_url,
            file_type=df_params.df_params.file_type,
            partitions=None,
        )

        if (
            df_params.write_schema_on_s3
            or df_params.df_params.file_type != FileType.PARQUET
        ):
            self.write_schema(df, write_params)

        logger.info("Dataframe written successfully.\n")

    def write_dataframe(self, df: DataFrame, df_params: OutputDataFrameParams) -> None:
        write_params = df_params.df_params
        bucket_url = self._get_bucket_url(write_params.bucket_params)
        write_path_url = f"{bucket_url}/{write_params.path_to_dataframe_root}"
        logger.debug(f"Write root path: {write_path_url}")

        partitions = self._get_partitions(write_params)
        logger.debug(f"Using partitions: {partitions}")

        path = f"{bucket_url}/{self._get_dataframe_path_with_date_partitions(write_params)}"

        # Add the date partitions columns to the DataFrame
        df_with_date_partitions = df
        if write_params.processing_date_partitions:
            for date_partition in write_params.processing_date_partitions:
                formatted_date_part_value = DATE_FORMATTER[
                    date_partition.value.replace("part_", "")
                ](write_params.processing_date)

                df_with_date_partitions = df_with_date_partitions.withColumn(
                    date_partition.value, lit(formatted_date_part_value)
                )

        if df_params.overwrite:
            logger.info(
                f"Overwrite is set to True. Deleting existing objects under path {path}"
            )
            try:
                self.aws_interface.delete_objects_aws(
                    write_params.bucket_params.env,
                    write_params.bucket_params.bucket_name,
                    path,
                )
            except Exception as e:
                raise ValueError(f"Error deleting dataframe objects: {e}")

            logger.info("Objects deleted successfully.")

        logger.info(
            f"Writing DataFrame to {write_path_url} with partitions {partitions}..."
        )
        self.spark_manager.write(
            env=write_params.bucket_params.env,
            df=df_with_date_partitions,
            path=write_path_url,
            file_type=df_params.df_params.file_type,
            partitions=partitions if partitions else None,
        )

        if (
            df_params.write_schema_on_s3
            or df_params.df_params.file_type != FileType.PARQUET
        ):
            self.write_schema(df, write_params)

        logger.info("Dataframe written successfully.\n")

    @staticmethod
    def read_and_validate_step_json(step_params_json_file_path):
        """
        Reads and validates a JSON file containing step parameters.

        Args:
            step_params_json_file_path (str): The file path to the JSON file.

        Returns:
            StepParams: An instance of the StepParams class representing the step configuration.

        Raises:
            ValueError: If there is an error loading or decoding the JSON file.
        """
        try:
            with open(step_params_json_file_path, "r") as f:
                step_config = json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            raise ValueError(f"Error loading config file: {e}") from e

        return StepParams(**step_config)

    def read_input_dataframes_params(
        self, input_df_params_dict: InputDataFrameParamsDict
    ) -> DataFrameDict:
        """Reads multiple input dataframes based on the provided configuration."""
        dfs: DataFrameDict = {}

        for df_name, input_df_params in input_df_params_dict.items():
            logger.info(f"Starting read operation for DataFrame '{df_name}'...")
            dfs[df_name] = self.read_dataframe(df_params=input_df_params)
            logger.info(f"Dataframe '{df_name}' read successfully.\n")

        return dfs

    def _select_transformation_function(self, transform_params: TransformParams):
        """Select the transformation function based on direct or indirect reference."""
        if transform_params.fn_direct:
            return transform_params.fn_direct
        elif transform_params.fn_indirect:
            raise NotImplementedError("Indirect function references are not supported.")
        else:
            raise ValueError(
                "TransformParams must have either 'fn_direct' or 'fn_indirect' set."
            )

    def apply_transform_to_df(
        self, df: DataFrame, transform_params: TransformParams
    ) -> DataFrame:
        """Apply transformation to a single DataFrame."""
        transform_fn = self._select_transformation_function(transform_params)
        fn_kwargs = transform_params.fn_kwargs or {}

        return transform_fn(df, **fn_kwargs)

    def apply_transform(
        self, input_dfs_dict: DataFrameDict, transform_params: TransformParams
    ) -> DataFrameDict:
        """Apply transformations to single or multiple DataFrames."""
        transform_fn = self._select_transformation_function(transform_params)

        fn_kwargs = transform_params.fn_kwargs or {}

        dfs_to_transform = transform_params.apply_only_on or list(input_dfs_dict.keys())

        if transform_params.fn_kind == FnKind.SINGLE:
            for df_name in dfs_to_transform:
                if df_name in input_dfs_dict:
                    input_dfs_dict[df_name] = transform_fn(
                        input_dfs_dict[df_name], **fn_kwargs
                    )
                else:
                    logger.warning(f"DataFrame '{df_name}' not found.")
        elif transform_params.fn_kind == FnKind.BATCH:
            input_dfs_dict = transform_fn(input_dfs_dict, **fn_kwargs)

        return input_dfs_dict

    def apply_all_transforms(
        self,
        input_dfs_dict: DataFrameDict,
        transform_params_dict: TransformParamsDict,
    ) -> DataFrameDict:
        """Apply a list of transformations to the given DataFrames."""
        for transform_id, transform_params in transform_params_dict.items():
            logger.info(
                f"Applying transformation '{transform_id}': {transform_params.transform_label}..."
            )
            input_dfs_dict = self.apply_transform(input_dfs_dict, transform_params)
        return input_dfs_dict

    def write_output_dataframes(
        self,
        dfs_to_output: DataFrameDict,
        output_df_params_dict: OutputDataFrameParamsDict,
    ) -> None:
        for df_name, df in dfs_to_output.items():
            logger.info(f"Starting write operation for DataFrame '{df_name}'...")
            output_df_params = output_df_params_dict.get(df_name)

            if output_df_params is None:
                raise ValueError(
                    f"No OutputDataFrameParams found for dataframe '{df_name}'"
                )

            if output_df_params.df_params.specific_path:
                self.write_dataframe_specific_path(df=df, df_params=output_df_params)
            else:
                self.write_dataframe(df=df, df_params=output_df_params)

    def process_step(
        self,
        step_params_json_file_path: Optional[str] = None,
        step_params: Optional[StepParams] = None,
        processing_date: Optional[datetime] = None,
    ) -> Optional[DataFrameDict]:
        """
        Reads the configuration, processes input dataframes, applies transformations, and writes output dataframes.
        """
        if step_params_json_file_path is None and step_params is None:
            raise ValueError(
                "Either 'step_params_json_file_path' or 'step_params' must be provided"
            )

        if step_params_json_file_path is not None and step_params is not None:
            raise ValueError(
                "Only one of 'step_params_json_file_path' or 'step_params' should be provided"
            )

        if step_params_json_file_path:
            logger.info("Reading and validating step configuration...")
            step_params = self.read_and_validate_step_json(step_params_json_file_path)
            logger.info("Step configuration read and validated.")

        assert step_params is not None, "'step_params' was unexpectedly None"

        if processing_date is not None:
            logger.debug(
                f"Injecting processing date '{processing_date}' into step parameters..."
            )
            step_params = self.inject_processing_date_into_step_params(
                step_params=step_params,
                processing_date=processing_date,
            )
            logger.debug("Processing date injected successfully.")

        try:
            print("\nPhase 1: Read Input DataFrames\n" + "-" * 80)
            input_dfs_dict = self.read_input_dataframes_params(
                step_params.input_dataframes_params
            )
            logger.info("Read all Input DataFrames successfully!")

            print("\nPhase 2: Apply Transformations\n" + "-" * 80)
            if step_params.transform_params:
                dfs_to_output_dict = self.apply_all_transforms(
                    input_dfs_dict, step_params.transform_params
                )
                print("")
                logger.info("Applied all Transformations successfully!")
            else:
                print("No transformations to apply. Moving to Phase 3.")
                dfs_to_output_dict = input_dfs_dict

            if step_params.output_dataframes_params:
                print("\nPhase 3: Write Output DataFrames\n" + "-" * 80)
                self.write_output_dataframes(
                    dfs_to_output_dict, step_params.output_dataframes_params
                )
                logger.info("Wrote all Output DataFrames successfully!")
            else:
                return dfs_to_output_dict
        except Exception as e:
            logger.exception(f"Error during processing step: {e}")
            raise e from None  # Re-raise to propagate the exception

    def inject_processing_date_into_dataframe_params(
        self,
        params: Union[DataFrameReadWriteParams, DataFrameReadWriteParams],
        processing_date: datetime,
    ) -> Union[DataFrameReadWriteParams, DataFrameReadWriteParams]:
        modified_params = params

        if params.processing_date == "{{processing_date}}":
            modified_params.processing_date = processing_date
        elif params.processing_date == "{{processing_date_previous}}":
            modified_params.processing_date = processing_date - timedelta(days=1)

        return modified_params

    def inject_processing_date_into_step_params(
        self, step_params: StepParams, processing_date: datetime
    ) -> StepParams:
        modified_step_params = step_params

        for df_name, df_params in modified_step_params.input_dataframes_params.items():
            new_read_params = self.inject_processing_date_into_dataframe_params(
                df_params.df_params, processing_date
            )
            if not isinstance(new_read_params, DataFrameReadWriteParams):
                raise ValueError(
                    f"Expected DataFrameReadParams, but received: {new_read_params}"
                )
            modified_step_params.input_dataframes_params[
                df_name
            ].df_params = new_read_params

        if modified_step_params.output_dataframes_params:
            for (
                df_name,
                df_params,
            ) in modified_step_params.output_dataframes_params.items():
                new_write_params = self.inject_processing_date_into_dataframe_params(
                    df_params.df_params, processing_date
                )
                if not isinstance(new_write_params, DataFrameReadWriteParams):
                    raise ValueError(
                        f"Expected DataFrameWriteParams, but received: {new_write_params}"
                    )
                modified_step_params.output_dataframes_params[
                    df_name
                ].df_params = new_write_params

        return modified_step_params

    def process_step_dict(
        self,
        step_params_dict: Union[StepParamsDict, Dict[str, str]],
        processing_date: Optional[datetime] = None,
    ) -> Optional[DataFrameDict]:
        """
        Reads the configuration, processes input dataframes, applies transformations, and writes output dataframes.
        """
        for step_num, (step_id, step_params) in enumerate(
            step_params_dict.items(), start=1
        ):
            if step_id in self.completed_steps:
                logger.info(f"Step '{step_id}' has already been processed. Skipping...")
                continue
            try:
                if isinstance(step_params, str):
                    logger.debug(
                        f"Step params for '{step_id}' is a file path. Reading and validating..."
                    )
                    step_params_json_file_path = step_params
                    step_params = self.read_and_validate_step_json(
                        step_params_json_file_path
                    )
                    logger.debug(
                        f"Step params for '{step_id}' read and validated successfully."
                    )

                print("=" * 80)
                print(
                    f"Processing step {step_num}/{len(step_params_dict)}: '{step_id}'"
                )
                print("=" * 80)
                self.process_step(
                    step_params=step_params.model_copy(deep=True),
                    processing_date=processing_date,
                )

                print("\n" + "-" * 80)
                print(f"Step '{step_id}' processed successfully!\n")
                print("\n" + "-" * 80)

                self.completed_steps.append(step_id)
            except Exception as e:
                logger.exception(f"Error during processing step '{step_id}': {e}")
                raise e from None

        self.completed_steps = []
        print("=" * 80)
        print("All steps processed successfully!")
        print("=" * 80)
