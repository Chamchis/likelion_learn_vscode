import requests, json

city = input('원하시는 도시를 입력해주세요 : ')
apikey = '03615dbd56a96fdc1191bebfd48e352c'
lang = 'kr'
units = 'metric'
api = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units={units}'

results = requests.get(api)
# print(results.text)


data = json.loads(results.text)

# print(type(results.text))
# print(type(data))

print(data['name'],'의 날씨입니다.')
print('현재 기상 상태는',data['weather'][0]['description'],'입니다')
print('현재 온도는',data['main']['temp'],'입니다')
print('현재 체감 온도는',data['main']['feels_like'],'입니다')
print('현재 최저 기온은',data['main']['temp_min'],'입니다')
print('현재 최저 기온은',data['main']['temp_min'],'입니다')
print('현재 최고 기온은',data['main']['temp_max'],'입니다')
print('현재 습도는',data['main']['humidity'],'입니다')
print('현재 기압은',data['main']['pressure'],'입니다')
print('현재 풍속은',data['wind']['deg'],'입니다')
print('현재 풍속은',data['wind']['speed'],'입니다')

