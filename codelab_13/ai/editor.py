from PIL import Image
from google import genai
from google.genai import types
from io import BytesIO
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

client = genai.Client(api_key=os.getenv("NANO_BANANA_API_KEY"))

OUTPUT_FOLDER = "static/generated"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)



def edit_image(image_path):

  prompt = """
    Create a photo-style line drawing/ink sketch of the faces identical to the uploaded reference photo — keep every facial feature, proportion, and expression exactly the same. Use black and white ink tones with intricate, fine line detailing, drawn on a notebook-page style
  """
  output_image_name = f"{OUTPUT_FOLDER}/{image_path.split('/')[-1].split('.')[0]}_edited.png"
  input_prompt_image=Image.open(image_path)

  response = client.models.generate_content(
      model="gemini-2.5-flash-image",
      contents=[input_prompt_image, prompt],
  )

  for part in response.candidates[0].content.parts:
    if part.text is not None:
      print(part.text)
    elif part.inline_data is not None:
      image = Image.open(BytesIO(part.inline_data.data))
      image.save(output_image_name)

  return output_image_name




