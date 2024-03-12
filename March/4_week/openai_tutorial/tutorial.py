from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

MODEL = "gpt-3.5-turbo"
client = OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
    model = MODEL,
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "너는 번역기야. 고객의 응답에 한국어로 답변해줘 You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": "나는 우주에 나가서 살고싶어"}
    ],
    temperature=0.1,
    top_p=0.1
)
print(response.choices[0].message.content)