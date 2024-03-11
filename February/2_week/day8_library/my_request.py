import requests
response = requests.get('https://www.naver.com')
print(response.text)  # 응답 텍스트 출력

data = {"title":"python", "major":"backend"}
print(data)

response = requests.get('https://httpbin.org/get', params = data)
print(response)

print(response.url)
response = requests.post('https://httpbin.org/post', data=data)
print(response.text)

response_result = response.json()

print(type(response_result))

print(response_result)

headers = {"User-Agent Kimjunho":"My User Agent 1.0"}
response = requests.get('https://httpbin.org/get', headers=headers)

print(response.request.headers)

try:
    response = requests.get('https://httpbin.org/get', timeout=0.00001)
except requests.exceptions.Timeout:
    print('시간이 지연되니 다음단계로') 

with requests.Session() as session:
    session.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
    response = session.get('https://httpbin.org/cookies')

    