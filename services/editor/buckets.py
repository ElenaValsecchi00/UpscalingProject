import boto3
import uuid
import os
import numpy as np
import cv2

# Create an S3 client and resource
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

BUCKET_PREFIX = 'images'

def load_image(bucket_name: str, image_path: str) -> dict:
    """
    Take a path to an image and return a dictionary containing the image as a tensor.

    Args:
        bucket_name (str): Name of the AWS S3 bucket.
        image_path (str): Path to the image in AWS S3 bucket.
    """
    # Load image from AWS S3 bucket
    data = download_from_aws(bucket_name, image_path)

    # Decode image
    buffer = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(buffer, -1)
    img = img.astype(np.float32) / 255.

    
    return img


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

def upload_to_aws(sr_img: np.ndarray, bucket: str, filename: str) -> tuple[str, bool]:
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
        # Convert the image to bytes
        bytes_img = cv2.imencode('.png', sr_img)[1].tobytes()
        # Save the image to the S3 bucket
        filename = f"{filename}_{str(uuid.uuid4())}.png"
        s3_client.put_object(Bucket=bucket, Key=filename, Body=bytes_img)
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

