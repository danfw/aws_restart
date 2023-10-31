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
