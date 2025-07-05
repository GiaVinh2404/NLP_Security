import boto3
import os
from config import AppConfig

def list_s3_files(bucket_name):
    """
    Liệt kê file trong bucket S3
    """
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
    )
    response = s3.list_objects_v2(Bucket=bucket_name)
    files = [item['Key'] for item in response.get('Contents', [])]
    return files

def download_s3_file(bucket_name, file_key, save_path):
    """
    Tải file từ S3 về local
    """
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
    )
    s3.download_file(bucket_name, file_key, save_path)
