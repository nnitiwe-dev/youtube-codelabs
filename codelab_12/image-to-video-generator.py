from python-dotenv import load_dotenv, find_dotenv
import os
import requests
import base64


# Load environment variables
load_dotenv(find_dotenv())


url = "https://api.novita.ai/v3/async/seedance-v1-lite-i2v"

# Read and encode local image to base64
image_path = "input/nnitiwe_cartoon.PNG"  # Change to your actual image path
with open(image_path, "rb") as img_file:
    image_base64 = base64.b64encode(img_file.read()).decode("utf-8")

# Set API key from environment variable
api_key = os.getenv("NOVITA_API_KEY")

def generate_video(prompt,image=image_base64,resolution="720p",aspect_ratio="16:9",last_image="",camera_fixed=True,seed=123,duration=123):
    try:
        payload = {
            "prompt": prompt,
            "image": image,
            "resolution": resolution,
            "aspect_ratio": aspect_ratio,
            "last_image": last_image,
            "camera_fixed": camera_fixed,
            "seed": seed,
            "duration": duration
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        response = requests.post(url, json=payload, headers=headers)

        return response.json()

    except Exception as e:
        print(f"Error: {e}")
        return None