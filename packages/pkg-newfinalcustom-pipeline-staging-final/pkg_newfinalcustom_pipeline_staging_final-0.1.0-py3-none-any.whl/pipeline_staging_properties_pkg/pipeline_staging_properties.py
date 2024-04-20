import boto3
import os
from botocore.exceptions import ClientError

class PipelineStagingManager:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client('s3')

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