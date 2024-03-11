import requests
headers = {}
response = requests.get('https://api.github.com', headers=headers)
print(response.request.headers)  # 요청에 사용된 헤더 출력