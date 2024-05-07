import requests
from dotenv import load_dotenv
import os

load_dotenv("../.env")

# Load the environment variables
BACKEND_URL = os.getenv('BACKEND_URL')

def request_upscale():
    response = requests.get(f'{BACKEND_URL}/api')
    print(response.content)

if __name__ == '__main__':
    request_upscale()
