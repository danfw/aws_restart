#Cada apartado es un pythonFile diferente
#Este lo utilice para escuchar
import boto3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
    
    
#Este lo utilice para crear un bucket
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
    
#Este lo utilice para crear subir un archivo
import boto3

s3 = boto3.client('s3', region_name='us-west-2')
bucket = 'danawsboto2310301921'
filename = 'danger.txt'

# Open the file in binary mode
with open(filename, 'rb') as f:
    # Upload the file to S3
    response = s3.upload_fileobj(f, bucket, filename)

print()
print("--------------AWS Response--------------")
print(response)
