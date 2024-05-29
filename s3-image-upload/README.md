# s3-image-upload

## Functions 

- *lambda_handler.py* - Create a lambda function inside the aws console using this code in the "Code" section. In the same panel you should find "Configuration" and then in the "Function URL" panel, ensure to also have one url created with NONE authentication. Use the url generated inside the config.py file.
- *post_img_to_s3.py* - Invokes call to public API (unsecured, used with NONE authentication).
- *post_image_to_s3_unsecured.py* - Invokes call to public API securely using AWS Signature version 4.

### Credentials

In order to use the secure version, replace the access keys below in the code.  

- ACCESS_KEY = '12345'
- SECREST_ACCESS_KEY = 'ABCDE'

 