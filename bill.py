import time
import datetime
import requests
import boto3
	


s3 = boto3.resource('s3',aws_access_key_id=AWS_Access_Key_Id,aws_secret_access_key=AWS_Secret_Key)
for bucket in s3.buckets.all():
	print(bucket.name)
data = open('C:\\Users\\IRFAN\\Downloads\\test_clip.mp4', 'rb')
upload =s3.Bucket('automate01').put_object(Key='SONY_1_FUN.mp4', Body=data)
print(upload)

# response=s3.list_buckets().get('Buckets')
# # data = response['Owner']['DisplayName']
# print(response)