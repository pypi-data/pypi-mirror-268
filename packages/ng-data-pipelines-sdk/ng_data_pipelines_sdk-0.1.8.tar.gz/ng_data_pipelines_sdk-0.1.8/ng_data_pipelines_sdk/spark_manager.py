from typing import Dict, List, Optional

from pyspark.conf import SparkConf
from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import StructType

from ng_data_pipelines_sdk.interfaces import AWSCredentials, Env, FileType


class SparkManager:
    def __init__(
        self,
        app_name: str,
        aws_credentials_dict: Optional[Dict[Env, AWSCredentials]] = None,
    ):
        self.aws_credentials_dict = aws_credentials_dict
        spark_config = self.create_spark_config(app_name)
        self.spark = SparkSession.builder.config(conf=spark_config).getOrCreate()  # type: ignore
        self.spark.sparkContext.setLogLevel("ERROR")

    def _set_aws_credentials(self, env: Env):
        if not self.aws_credentials_dict:
            return

        aws_credentials = self.aws_credentials_dict[env]

        jsc = getattr(self.spark.sparkContext, "_jsc")
        hadoopConfiguration = jsc.hadoopConfiguration()

        hadoopConfiguration.set("fs.s3a.access.key", aws_credentials.aws_access_key_id)
        hadoopConfiguration.set(
            "fs.s3a.secret.key", aws_credentials.aws_secret_access_key
        )

    def create_spark_config(self, app_name: str):
        config: SparkConf = SparkConf().setAppName(app_name)

        config.set("spark.sql.parquet.datetimeRebaseModeInRead", "LEGACY")
        config.set("spark.sql.parquet.datetimeRebaseModeInWrite", "LEGACY")
        config.set("spark.sql.parquet.int96RebaseModeInWrite", "LEGACY")
        config.set("spark.sql.eagerEval.enabled", "true")
        config.set(
            "spark.hadoop.fs.s3a.impl", " org.apache.hadoop.fs.s3a.S3AFileSystem"
        )
        config.set("com.amazonaws.services.s3.enableV4", "true")

        # Set the packages to be used by Spark for Hadoop AWS integration
        config.set("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.2.2")

        if self.aws_credentials_dict:
            config.set(
                "spark.hadoop.fs.s3a.aws.credentials.provider",
                "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider",
            )

        return config

    def read(
        self,
        env: Env,
        path: str,
        file_type: FileType,
        schema: Optional[StructType] = None,
    ):
        self._set_aws_credentials(env)

        if schema:
            return self.spark.read.format(file_type).schema(schema).load(path)
        else:
            return self.spark.read.format(file_type).load(path)

    def write(
        self,
        env: Env,
        df: DataFrame,
        path: str,
        file_type: FileType,
        partitions: Optional[List[str]] = None,
    ):
        self._set_aws_credentials(env)

        if partitions:
            df.write.partitionBy(partitions).format(file_type).mode("append").save(path)
        else:
            df.write.format(file_type).mode("append").save(path)
