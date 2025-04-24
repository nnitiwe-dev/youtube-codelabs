
import requests
import json
from fastapi import UploadFile

# Load API keys from a JSON configuration file
with open('../secrets/config.json', 'r') as keys:
    secret_keys = json.load(keys)

STABILITY_API_KEY = secret_keys["stability_ai_token"] 

# The function `remove_background` takes an image file and an output format as input, sends a request to the Stability AI API, and returns the processed image.
def remove_background(image: UploadFile, output_format: str = "webp") -> bytes:
    response = requests.post(
        url="https://api.stability.ai/v2beta/stable-image/edit/remove-background",
        headers={
            "authorization": f"Bearer {STABILITY_API_KEY}",
            "accept": "image/*"
        },
        files={
            "image": (image.filename, image.file, image.content_type)
        },
        data={
            "output_format": output_format
        },
    )

    if response.status_code == 200:
        return response.content
    else:
        raise Exception(str(response.json()))
