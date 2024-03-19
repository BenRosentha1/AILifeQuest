from openai import OpenAI
from getAPI import getAPI
from PIL import Image, ImageTk
import tkinter as tk
import requests
from io import BytesIO

# Use the API key in OpenAI client initialization
client = OpenAI(api_key=getAPI())

def makePic(prompt, imageTitle):
    image_response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )

    image_url = image_response.data[0].url

    # Download the image from the URL
    response = requests.get(image_url)
    image_bytes = BytesIO(response.content)

    # Display the image in a pop-up window
    root = tk.Tk()
    root.title("imageTitle")

    image = Image.open(image_bytes)
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(root, image=photo)
    label.pack()

    root.mainloop()

