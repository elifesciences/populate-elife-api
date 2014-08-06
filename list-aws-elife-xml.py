from boto.s3.connection import S3Connection
import boto
from boto_creds import aws_access_key_id as aws_key
from boto_creds import aws_secret_access_key as aws_secret

conn = S3Connection(aws_key, aws_secret)

mybucket = conn.get_bucket('elife-cdn') # Substitute in your bucket name
elife_cdn = mybucket.list()
for key in elife_cdn:
	name = key.name
	if "elife-articles" in name and ".xml" in name:
		print "{name}\t{size}\t{modified}".format(
			name = key.name,
			size = key.size,
			modified = key.last_modified,
			)

		awskey = mybucket.get_key(name)
		local_name = 'elife-xml/' + name.split("/")[-1]
		awskey.get_contents_to_filename(local_name)
		print ("downloaded xml to "+ local_name)
