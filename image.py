import requests
import streamlit as st

st.title("HI THERE ! IT'S MUGI HERE")

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": st.text_input("Enter What you Want"),
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))

if st.button("Your Answae"):
    st.image(image)