import re
from datetime import datetime

from pyspark.sql.types import StructType, TimestampType


def handle_pyspark_timestamp_in_schema(pyspark_schema: StructType) -> StructType:
    """Recursive function that modifies StructType pyspark schema field to handle timestamp inconsistency when
    parsing JSON-Schema types.

    Parameters
    ----------
    pyspark_schema : StructType
        Pyspark schema

    Returns
    -------
    StructType
        the resultant schema in pyspark StructType format
    """

    def is_struct_type(field):
        return field.simpleString()[:6] == "struct"

    def is_array_type(field):
        return field.simpleString()[:5] == "array"

    # for each field in schema
    for field in pyspark_schema.fields:
        field_metadata = field.metadata
        if is_struct_type(field.dataType):
            handle_pyspark_timestamp_in_schema(field.dataType)  # type: ignore
        elif is_array_type(field.dataType):
            if is_struct_type(field.dataType.elementType):  # type: ignore
                handle_pyspark_timestamp_in_schema(field.dataType.elementType)  # type: ignore
        # if 'format' is in field metadata key and the value is 'date-time' or 'date'
        # convert field type to TimestampType
        elif "format" in field_metadata.keys():
            field_format = field_metadata["format"]
            if field_format in ("date-time", "date"):
                field.dataType = TimestampType()
    return pyspark_schema


def import_from_custom_package(package_name, variable):
    # importing variable from custom package
    return getattr(__import__(package_name), variable)


def import_table_current_step_params(params, table, current_step):
    # importing table current step params from database params
    return params[table][current_step]


def handle_execution_date_args(dt: str):
    match = re.search(r"(?<=\.).+?(?=\:)", dt)
    if match:
        dt = dt.replace(f".{match.group()[:-3]}", "")
    return datetime.strptime("".join(dt.rsplit(":", 1)), "%Y-%m-%dT%H:%M:%S%z")


def handle_input_api(env, params, ng_prefix="ng"):
    layer_format_map = {
        "landing": "json",
        "raw": "parquet",
        "trusted": "parquet",
    }

    layer = params["layer"]
    file_type = params.get("file_type", layer_format_map.get(layer))
    object_path = params["object_path"]
    partition = params.get("partition", "part_year/part_month/part_day")
    input_dict = {
        "env": env,
        "bucket_name": f"{ng_prefix}-datalake-{layer}-{env}",
        "object_path": object_path,
        "partition": partition,
        "file_type": file_type,
    }
    if params.get("schema_path") is not None:
        input_dict["schema_path"] = {
            "bucket_name": f"{ng_prefix}-repository-{env}",
            "object_path": params["schema_path"],
        }
    return input_dict


def handle_dataframe_manager_path_input_api(env, params, ng_prefix="ng"):
    layer_format_map = {
        "landing": "json",
        "raw": "parquet",
        "trusted": "parquet",
    }

    layer = params["layer"]
    file_type = params.get("file_type", layer_format_map.get(layer))
    object_path = params["object_path"]
    partition = params.get("partition", "part_year/part_month/part_day")
    input_dict = {
        "env": env,
        "bucket_name": f"{ng_prefix}-datalake-{layer}-{env}",
        "object_path": object_path,
        "partition": partition,
        "file_type": file_type,
    }
    return input_dict
