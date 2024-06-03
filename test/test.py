import requests
from dotenv import load_dotenv
import os

load_dotenv(".env")

# Load the environment variables
BACKEND_URL = os.getenv('BACKEND_URL')
UPSCALER_URL = os.getenv('UPSCALER_URL')

def request_upscale():
    response = requests.post(f'http://a4cfae2ac7d5145bb8059cd48496b358-1308506135.us-east-1.elb.amazonaws.com/api/edit', json={
        "image":"baboon.png",
        "upscale": True,
        "harmonize": True,
        "filters": []
    })
    print(response.content)

if __name__ == '__main__':
    request_upscale()
