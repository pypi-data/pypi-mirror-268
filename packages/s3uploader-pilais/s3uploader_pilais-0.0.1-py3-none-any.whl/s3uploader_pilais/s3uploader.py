import boto3
from django.conf import settings


# Upload file to s3
def upload_file(file, object_name, bucket=settings.S3_BUCKET):

    # Construct public URL of image
    image_url = f'https://{bucket}.s3.amazonaws.com/{object_name}'

    # Upload the file
    s3_client = boto3.client('s3')
    response = s3_client.upload_fileobj(
        file, bucket, object_name)

    # Set file can be accessed publicly
    s3_client.put_object_acl(
        Bucket=bucket,
        Key=object_name,
        ACL='public-read'
    )

    return image_url
