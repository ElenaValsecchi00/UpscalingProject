import requests
from dotenv import load_dotenv
import os

load_dotenv("../.env")

# Load the environment variables
BACKEND_URL = os.getenv('BACKEND_URL')
UPSCALER_URL = os.getenv('UPSCALER_URL')

def request_upscale():
    response = requests.post(f'{UPSCALER_URL}/api/upscale', json={
        "image":"baboon.png_180cbebb-e883-4a69-bb58-2cd116e28c25"
    })
    print(response.content)

if __name__ == '__main__':
    request_upscale()
