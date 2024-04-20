import boto3
import os
from botocore.exceptions import ClientError

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
            
    def check_stage_exists(self, stage_name):
        try:
            self.s3_client.head_object(Bucket=self.bucket_name, Key=stage_name)
            return True
        except ClientError as e:
            if e.response['Error']['Code'] == '404':
                return False
            else:
                print(f"An error occurred while checking if stage '{stage_name}' exists: {e}")
                return False
            
    def upload_stage(self, stage_name):
        try:
            response = self.s3_client.get_object(Bucket=self.bucket_name, Key=stage_name)
            current_content = response['Body'].read().decode('utf-8')
            modified_content = modify_content(current_content)
            self.s3_client.put_object(Bucket=self.bucket_name, Key=stage_name, Body=modified_content.encode('utf-8'))
        except ClientError as e:
            print(f"An error occurred while editing stage {stage_name}: {e}")

def modify_content(current_content):
    modified_content = current_content + "\nModified content"
    return modified_content