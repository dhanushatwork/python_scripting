import boto3
from botocore.exceptions import ClientError

# Create S3 client
s3 = boto3.client('s3', region_name='ap-south-1')

bucket_name = "akumax-devops-boto3-demo-12345"  # MUST be globally unique

try:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1'
        }
    )
    print(f"Bucket '{bucket_name}' created successfully")

except ClientError as e:
    print("Error creating bucket:", e)
