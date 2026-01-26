from google import genai
from google.genai import types
import requests
from django.conf import settings

# client = genai.Client(api_key='AIzaSyDmQypBTL1D0-Nds7qzUyywIKl1mP9n2IE')
#
# response = client.models.generate_content(
#     model="gemini-3-flash-preview",
#     contents="How does AI work?"
# )
# print(response.text)

prompt = '''
Определи блюдо по фото и верни ТОЛЬКО JSON:

{
  "name": "",
  "description": "",
  "cook_time": 0,
  "calories": 0,
  "ingredients": [
    {"name": "", "amount": ""}
  ]
}

Если что-то неясно — сделай разумную оценку.
Калории укажи для одной порции.
Никакого текста вне JSON.
'''

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(
  data=image_bytes, mime_type="image/jpeg"
)

client = genai.Client(api_key=settings.GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[prompt, image],
)

print(response.text)

