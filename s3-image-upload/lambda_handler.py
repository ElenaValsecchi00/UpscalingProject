import json
import base64
import boto3
import urllib3
import os
import uuid

BUCKET_PREFIX = 'images'

def lambda_handler(event, context):
    print (f'Executing Lambda function {event}')

    # Get the payload from the event
    data = json.loads(json.dumps(event))
    payload = data["body"]
    encoded_image = payload['image']
    image_name = payload['image_name']
    upscale = payload['upscale']
    harmonize = payload['harmonize']
    filters = payload['filters']
    basename, ext = os.path.splitext(image_name)
    filename = basename + str(uuid.uuid4()) + ext
    file_path = filename
    
    # Decode the image
    decoded_image = base64.b64decode(encoded_image)
    s3_client = boto3.client('s3')
    # Get the bucket if already exists
    response = s3_client.list_buckets()
    name = ""
    for bucket in response['Buckets']:
        if BUCKET_PREFIX in bucket['Name']:
            name = bucket['Name']
    if name == "":
        # Create a bucket in the S3 service
        name = f'{BUCKET_PREFIX}_{str(uuid.uuid4())}'
        bucket_response = s3_client.create_bucket(Bucket=name)
    
    # Upload the image to S3
    content_type = 'image/jpeg' if 'jpg' in filename or 'jpeg' in filename else 'image/png'
    s3_client.put_object(Body=decoded_image, Bucket=name, Key=file_path, ContentType=content_type, ACL='bucket-owner-full-control')
    
    '''
    # Get the load balancer external URL
    elb_client = boto3.client('elbv2')
    response = elb_client.describe_load_balancers(Names=['default/eks-editor-service'])
    load_balancer_dns = response['LoadBalancers'][0]['DNSName']
    print(f'Load balancer DNS: {load_balancer_dns}')
    '''
    
    # Send a request to the editor service
    encoded_body = json.dumps({
        'image': file_path,
        'upscale': upscale,
        'harmonize': harmonize,
        'filters': filters
    })
    http = urllib3.PoolManager()
    response = http.request('POST', f'http://a5ba66d9328c14666a96081dee0ca03a-1144026218.us-east-1.elb.amazonaws.com/api/edit',
        headers={'Content-Type': 'application/json'},
        body=encoded_body
    )

    # Return the response
    return {
        'statusCode': response.status,
        'body': response.data
    }