import boto3
import os
from botocore.exceptions import ClientError

os.environ["AWS_ACCESS_KEY_ID"] = "x23203595AccessKeyIDPipelineStaging"
os.environ["AWS_SECRET_ACCESS_KEY"] = "x23203595AccessKeyPipelineStaging"
os.environ["AWS_SESSION_TOKEN"] = "x23203595SessionTokenPipelineStaging"

class PipelineStagingManager:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client('s3')

    def list_stages(self):
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
            stages = [obj['Key'] for obj in response.get('Contents', [])]
            return stages
        except ClientError as e:
            print(f"An error occurred while listing stages: {e}")
            return []

    def add_stage(self, stage_name):
        try:
            self.s3_client.put_object(Bucket=self.bucket_name, Key=stage_name)
        except ClientError as e:
            print(f"An error occurred while adding stage {stage_name}: {e}")

    def delete_stage(self, stage_name):
        try:
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=stage_name)
        except ClientError as e:
            print(f"An error occurred while deleting stage {stage_name}: {e}")