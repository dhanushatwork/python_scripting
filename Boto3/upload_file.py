import boto3
from botocore.exceptions import ClientError

bucket_name = "akumax-devops-boto3-demo-12345"
file_name = "sample.txt"
object_name = "upload/sample.txt"

s3 = boto3.client('s3')

try:
    s3.upload_file(file_name, bucket_name, object_name)
    print("File uploaded successfully")

except ClientError as e:
    print("Upload failed:", e)