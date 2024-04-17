from typing import Dict
import boto3
import json

from ng_data_pipelines_sdk.interfaces import AWSCredentials, Env


class AWSServiceClient:
    def __init__(self, aws_credentials: AWSCredentials, region_name: str):
        self.s3_client = boto3.client(
            "s3",
            region_name=region_name,
            aws_access_key_id=aws_credentials.aws_access_key_id,
            aws_secret_access_key=aws_credentials.aws_secret_access_key,
        )
        self.s3_resource = boto3.resource(
            "s3",
            region_name=region_name,
            aws_access_key_id=aws_credentials.aws_access_key_id,
            aws_secret_access_key=aws_credentials.aws_secret_access_key,
        )
        self.secrets_manager_client = boto3.client(
            "secretsmanager",
            region_name=region_name,
            aws_access_key_id=aws_credentials.aws_access_key_id,
            aws_secret_access_key=aws_credentials.aws_secret_access_key,
        )


class AWSInterface:
    def __init__(
        self, region_name: str, aws_credentials_dict: Dict[Env, AWSCredentials]
    ):
        self.client_managers = {
            env: AWSServiceClient(credentials, region_name)
            for env, credentials in aws_credentials_dict.items()
        }

    def get_service_client(self, env: Env) -> AWSServiceClient:
        if env not in self.client_managers:
            raise ValueError(f"No AWS credentials found for environment {env.value}")
        return self.client_managers[env]

    def get_object_aws(self, env: Env, bucket_name: str, object_name: str) -> bytes:
        client_manager = self.get_service_client(env)
        response = client_manager.s3_client.get_object(
            Bucket=bucket_name, Key=object_name
        )
        return response["Body"].read()

    def put_object_aws(
        self, env: Env, bucket_name: str, object_name: str, object_data: dict
    ) -> None:
        client_manager = self.get_service_client(env)
        client_manager.s3_client.put_object(
            Bucket=bucket_name,
            Key=object_name,
            Body=bytes(json.dumps(object_data), encoding="UTF-8"),
        )

    def put_file_aws(self, env: Env, bucket_name: str, object_name: str, file) -> None:
        client_manager = self.get_service_client(env)
        client_manager.s3_client.put_object(
            Bucket=bucket_name,
            Key=object_name,
            Body=file,
        )

    @staticmethod
    def concat_multiple_data_events(events):
        mult_data = ""

        for event in events:
            mult_data += json.dumps(event) + "\n"

        return mult_data[:-1].encode("UTF-8")

    def put_multiple_objects_aws_single_file(
        self, env: Env, bucket_name, object_name, objects
    ):
        client_manager = self.get_service_client(env)

        concat_mult_objects = self.concat_multiple_data_events(objects)

        return client_manager.s3_client.put_object(
            Bucket=bucket_name,
            Key=object_name,
            Body=concat_mult_objects,
        )

    def list_objects_key_aws(self, env: Env, bucket_name, path):
        client_manager = self.get_service_client(env)

        bucket_resource = client_manager.s3_resource.Bucket(bucket_name)
        objects_key = []

        for object_summary in bucket_resource.objects.filter(Prefix=path):
            objects_key.append(object_summary.key)

        return objects_key

    def list_objects_url_aws(self, env: Env, bucket_name, path):
        client_manager = self.get_service_client(env)

        bucket_resource = client_manager.s3_resource.Bucket(bucket_name)
        objects_url = []

        for object_summary in bucket_resource.objects.filter(Prefix=path):
            objects_url.append(
                f"s3://{object_summary.bucket_name}/{object_summary.key}"
            )

        return objects_url

    def delete_objects_aws(self, env: Env, bucket_name, path):
        client_manager = self.get_service_client(env)

        bucket = client_manager.s3_resource.Bucket(bucket_name)
        return bucket.objects.filter(Prefix=path).delete()

    def get_secret_aws(self, env: Env, secret_name: str) -> dict:
        client_manager = self.get_service_client(env)

        get_secret_value_response = (
            client_manager.secrets_manager_client.get_secret_value(SecretId=secret_name)
        )
        return json.loads(get_secret_value_response["SecretString"])
