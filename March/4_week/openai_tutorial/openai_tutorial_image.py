from dotenv import load_dotenv
import os
from PIL import Image
import requests
from openai import OpenAI

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')
MODEL = "dall-e-3"

client = OpenAI(api_key=openai_api_key)

response = client.images.generate(
    model = MODEL,
    prompt = "만년설이 뒤덮인 산맥을 배경으로 화려한 붉은 망토를 걸치고 화려한 왕관을 쓴 근엄한 모습의 독수리의 전신을 실사로 그려줘",
    size = '1024x1024',
    quality = 'standard',
    n = 1,
)

image_url = response.data[0].url

filename = 'image.jpg'
response = requests.get(image_url)
with open(filename,'wb') as f:
    f.write(response.content)
Image.open(filename)