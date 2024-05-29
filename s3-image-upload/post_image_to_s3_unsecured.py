#Posts image to S3 without any authentication enabled.
#The image is Base64 encoded before POST request is called


import requests
import base64
import json
from config import example_img, host

#Add image name, s3 bucket name and  key
encoded_string = example_img
payload = {
	"image_name": "my-image.jpg",
	"s3_bucket_name" : "mybucket",
	"key": "upload_image",
	"image": encoded_string
}
# Provide your endpoint name below
r = requests.post(f'https://{host}', json=payload, timeout=60)
print('\nRESPONSE++++++++++++++++++++++++++++++++++++')
print('Response code: %d\n' % r.status_code)
print(r.text)
