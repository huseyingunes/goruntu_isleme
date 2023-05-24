import openai
import requests
from PIL import Image

openai.api_key = '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'

def generate(text):
  res = openai.Image.create(
    # text describing the generated image
    prompt=text,
    # number of images to generate
    n=1,
    # size of each generated image
    size="1024x1024",
  )
  # returning the URL of one image as
  # we are generating only one image
  return res["data"][0]["url"]

text = "cat walking on articial neural network"
url1 = generate(text)
response = requests.get(url1)

with open("img3.png", "wb") as f:
  f.write(response.content)
# opening the saved image and converting it into "RGBA" format
# converted image is saved in result
result = Image.open('img3.png').convert('RGBA')
# saving the new image in PNG format
result.save('img_rgba3.png','PNG')

Image.open(response.raw)
