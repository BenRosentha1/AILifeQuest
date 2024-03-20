from openai import OpenAI
from getAPI import getAPI
from PIL import Image
import base64
from io import BytesIO

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=getAPI())

def makePic(prompt):
    # Generate the image using DALL·E API
    image_response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024",
        response_format="b64_json"
    )

    # Get the base64-encoded image from the API response
    image_b64_json = image_response.data[0].b64_json

    # Decode the base64 JSON data and extract the image bytes
    image_bytes = base64.b64decode(image_b64_json)

    # Open the image using PIL
    image = Image.open(BytesIO(image_bytes))

    # Display the image
    image.show()
