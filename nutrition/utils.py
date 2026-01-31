from google import genai
from google.genai import types
import json
import re


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


def analysis_photo(image_path):
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    image = types.Part.from_bytes(
        data=image_bytes, mime_type="image/jpeg"
    )

    client = genai.Client(api_key='AIzaSyBFLQj7ZF7RzGAfSHE0GmtnZWQeamuaXvA')

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[prompt, image],
    )

    return parse_ai_json(response.text)


def parse_ai_json(ai_text):
    cleaned = re.sub(r"```(?:json)?|```", "", ai_text).strip()

    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError:
        raise ValueError("Gemini вернул невалидный JSON")
    return data


# with open('/home/nikto/Pictures/images/F1mVIz17019294837018_l.jpg', "rb") as f:
#     image_bytes = f.read()
#
# image = types.Part.from_bytes(
#     data=image_bytes, mime_type="image/jpeg"
# )
#
# client = genai.Client(api_key='AIzaSyAoW-rEn29ag8TTJo18nYCFz6agAgx1L4s')
#
# response = client.models.generate_content(
#     model="gemini-3-flash-preview",
#     contents=[prompt, image],
# )
#
# print(response.text)

# client = genai.Client(api_key='AIzaSyDmQypBTL1D0-Nds7qzUyywIKl1mP9n2IE')
#
# response = client.models.generate_content(
#     model="gemini-3-flash-preview",
#     contents="How does AI work?"
# )
# print(response.text)