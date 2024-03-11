import requests, json
import streamlit as st
from googletrans import Translator
from PIL import Image

translator = Translator()

# 날씨 아이콘 이미지 파일 경로
icon_mapping = {
    'Clear': 'clear.png',
    'Clouds': 'clouds.png',
    'Rain': 'rain.png',
    'Drizzle': 'drizzle.png',
    'Thunderstorm': 'thunderstorm.png',
    'Snow': 'snow.png',
    'Mist': 'mist.png',
    'Smoke': 'smoke.png',
    'Haze': 'haze.png',
    'Dust': 'dust.png',
    'Fog': 'fog.png',
    'Sand': 'sand.png',
    'Ash': 'ash.png',
    'Squall': 'squall.png',
    'Tornado': 'tornado.png'
}

st.title('날씨 출력')
city = st.text_input('원하시는 도시를 입력해주세요: ')

def get_weather_data(city):
    apikey = '03615dbd56a96fdc1191bebfd48e352c'
    lang = 'kr'
    units = 'metric'
    translated_city_name = translator.translate(city, dest='en').text
    api = f'http://api.openweathermap.org/data/2.5/weather?q={translated_city_name}&appid={apikey}&lang={lang}&units={units}'

    results = requests.get(api)
    data = json.loads(results.text)
    return data

if city:
    data = get_weather_data(city)
    if 'name' in data:
        st.write(data['name'], '의 날씨입니다.')

        weather_icon = data['weather'][0]['main']
        weather_description = data['weather'][0]['description']
        icon_path = icon_mapping.get(weather_icon.lower())
        if icon_path:
            icon = Image.open(icon_path)
            st.image(icon, caption=weather_description, width=100)

        st.write('현재 기상 상태는', weather_description, '입니다.')
        st.write('현재 온도는', data['main']['temp'], '입니다.')
        st.write('현재 체감 온도는', data['main']['feels_like'], '입니다.')
        st.write('현재 최저 기온은', data['main']['temp_min'], '입니다.')
        st.write('현재 최고 기온은', data['main']['temp_max'], '입니다.')
        st.write('현재 습도는', data['main']['humidity'], '입니다.')
        st.write('현재 기압은', data['main']['pressure'], '입니다.')
        st.write('현재 풍속은', data['wind']['deg'], '입니다.')
        st.write('현재 풍속은', data['wind']['speed'], '입니다.')

    else:
        st.write('날씨 정보를 가져올 수 없습니다. 다시 입력해주세요.')
