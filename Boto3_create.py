import boto3
s3 = boto3.client('s3', region_name='us-west-2')
bucket_name = 'danawsboto2310301955'
response = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
print()
print("--------------AWS Response--------------")
print(response)
print()
print("--------------AWS S3 Listing--------------")
s3buckets = boto3.resource('s3')
for bucket in s3buckets.buckets.all():
    print(bucket.name)