# UpscalingProject
A site in cloud where you can upload your photos and edit them

## API Endpoints (Backend)
### /upload
- **Method**: POST
- **Description**: Upload an image to the AWS S3 bucket
- **Request Body**: 
  - `image`: Image file
- **Response**:
    - `status`: Status of the request
    - `message`: Message of the request
    - `image_url`: URL of the uploaded image in the S3 bucket

### /edit
- **Method**: POST
- **Description**: Start the editing process
- **Request Body**: 
  - `image_url`: URL of the image to edit in the S3 bucket
  - `filters`: List of filters to apply
- **Response**:
    - `status`: Status of the request
    - `message`: Message of the request
    - `image_url`: URL of the edited image

### /upscale
- **Method**: POST
- **Description**: Start the upscaling process
- **Request Body**: 
  - `image_url`: URL of the image to upscale in the S3 bucket
- **Response**:
    - `status`: Status of the request
    - `message`: Message of the request
    - `image_url`: URL of the upscaled image

### /color-correction
- **Method**: POST
- **Description**: Color correct an image
- **Request Body**: 
  - `image_url`: URL of the image to color correct in the S3 bucket
- **Response**:
    - `status`: Status of the request
    - `message`: Message of the request
    - `image_url`: URL of the color corrected image

 ## API Endpoints (Upscaler)
### /api/v1/upscale
- **Method**: POST
- **Description**: Upscale an image and save it to the S3 bucket
- **Request Body**: 
  - `image_url`: URL of the image to upscale in the S3 bucket
- **Response**:
    - `status`: Status of the request
    - `message`: Message of the request
    - `image_url`: URL of the upscaled image

    
 ## API Endpoints (Filters)
### /api/v1/apply-filter
- **Method**: POST
- **Description**: Apply a filter to an image and save it to the S3 bucket
- **Request Body**: 
  - `image_url`: URL of the image to apply the filter to in the S3 bucket
  - `filter`: Filter to apply
- **Response**:
    - `status`: Status of the request
    - `message`: Message of the request
    - `image_url`: URL of the image with the filter applied

### /api/v1/color-correction
- **Method**: POST
- **Description**: Color correct an image and save it to the S3 bucket
- **Request Body**: 
  - `image_url`: URL of the image to color correct in the S3 bucket
- **Response**:
    - `status`: Status of the request
    - `message`: Message of the request
    - `image_url`: URL of the color corrected image