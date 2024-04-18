# S3 Uploader

This is a package to upload files to AWS s3.

## Function defination

```
def upload_file(file, object_name, bucket=settings.S3_BUCKET)
```

## Parameters description

### file: file object, for example request.FILES['file']

### object_name: filename in S3 Bucket

### bucket: bucket name
