import boto3
import uuid
import os

# Load the AWS Credentials from the current path
os.environ['AWS_SHARED_CREDENTIALS_FILE'] = './aws-credentials.cfg'
os.environ['AWS_CONFIG_FILE'] = './aws-config.cfg'

# Create an S3 client and resource
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

BUCKET_PREFIX = 'images'

def create_bucket(s3_connection: boto3.client) -> tuple[str, bool]:
    """
    Create an S3 bucket if it does not exist.

    Args:
        bucket_prefix: Prefix for the bucket name
        s3_connection: Boto3 S3 connection

    Returns:
        str: Name of the bucket
        bool: True if the bucket was created successfully
    """
    # Check if already exists
    response = s3_connection.list_buckets()
    for bucket in response['Buckets']:
        if BUCKET_PREFIX in bucket['Name']:
            return bucket['Name'], True
        
    # Create a bucket in the S3 service
    name = f"{BUCKET_PREFIX}_{str(uuid.uuid4())}"
    bucket_response = s3_connection.create_bucket(
        Bucket=name
    )

    # Check if the bucket was created successfully
    if bucket_response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return name, True
    
    # Return False if the bucket was not created
    return name, False

def upload_file_to_aws(file_path: str, bucket: str, filename: str) -> tuple[str, bool]:
    """
    Upload a file to an S3 bucket.

    Args:
        file_path: Path to the file to upload
        bucket: Name of the bucket
        filename: Name of the file in the bucket

    Returns:
        str: Name of the file in the bucket
        bool: True if the file was uploaded successfully
    """
    try:
        filename = f"{filename}_{str(uuid.uuid4())}"
        s3_client.upload_file(file_path, bucket, filename)
        return filename, True
    except Exception as e:
        print(f"Error: {e}")
        return "", False

def upload_to_aws(content: bytes, bucket: str, filename: str) -> tuple[str, bool]:
    """
    Upload a file to an S3 bucket.

    Args:
        content: Content to upload
        bucket: Name of the bucket
        filename: Name of the file in the bucket

    Returns:
        str: Name of the file in the bucket
        bool: True if the file was uploaded successfully
    """
    try:
        filename = f"{filename}_{str(uuid.uuid4())}"
        s3_client.put_object(Bucket=bucket, Key=filename, Body=content)
        return filename, True
    except Exception as e:
        print(f"Error: {e}")
        return "", False

def download_from_aws(bucket: str, filename: str) -> bytes:
    """
    Download a file from an S3 bucket.

    Args:
        bucket: Name of the bucket
        filename: Name of the file in the bucket

    Returns:
        bytes: Content of the file
    """
    try:
        response = s3_client.get_object(Bucket=bucket, Key=filename)
        return response['Body'].read()
    except Exception as e:
        print(f"Error: {e}")
        return b""

def main():
    bucket_name, response = create_bucket(s3_connection=s3_resource.meta.client)
    if response:
        print(f"Bucket Created: {bucket_name}")
        #upload_file_to_aws("../services/upscaler/DAT/images/baboon.png", bucket_name, "baboon.png")
        file_name, status = upload_to_aws(b"Hello World", bucket_name, "hello.txt")
    else:
        print(f"Bucket Not Created: {bucket_name}")
    s3_client.download_file(bucket_name, file_name, 'newfile.txt')

if __name__ == '__main__':
    main()