import requests
import json
import streamlit as st
from googletrans import Translator
import folium
from streamlit_folium import folium_static


translator = Translator()  #  영어로 변환하기 위해

# 온도별 이미지
image_clear = open('clear.jpg', 'rb').read()
image_snow = open('snow.jpg', 'rb').read()
image_fall = open('fall.jpg', 'rb').read()

st.title("🏚️ :flag-kr: Today's Weather")
city = st.text_input('원하시는 도시를 한글로 입력해주세요: ')

def get_weather_data(city):
    apikey = '03615dbd56a96fdc1191bebfd48e352c'
    lang = 'kr'  # 한글로 표시하기 위해
    units = 'metric'  # 섭씨로 변환
    translated_city_name = translator.translate(city, dest='en').text
    api = f'http://api.openweathermap.org/data/2.5/weather?q={translated_city_name}&appid={apikey}&lang={lang}&units={units}'

    results = requests.get(api)
    data = json.loads(results.text)  # json 파일로 변환
    return data

if city:
    data = get_weather_data(city)
    if 'name' in data:
        st.write(data['name'], '의 날씨입니다.')

        weather_description = data['weather'][0]['description']

        st.write('현재 기상 상태는', weather_description, '입니다.')
        st.write('현재 온도는', data['main']['temp'], '입니다.')
        st.write('현재 체감 온도는', data['main']['feels_like'], '입니다.')
        st.write('현재 최저 기온은', data['main']['temp_min'], '입니다.')
        st.write('현재 최고 기온은', data['main']['temp_max'], '입니다.')
        st.write('현재 습도는', data['main']['humidity'], '입니다.')
        st.write('현재 기압은', data['main']['pressure'], '입니다.')
        st.write('현재 풍속은', data['wind']['deg'], '입니다.')
        st.write('현재 풍속은', data['wind']['speed'], '입니다.') 
        if data['main']['feels_like'] >= 28:  # 온도별 옷차림 참고 / 체감온도를 기준으로 함
            st.write('☀️🥵뜨거워요! 야외활동을 삼가해주세요!')
            st.image(image_clear, use_column_width=False, width=500)
        if 23 <= data['main']['feels_like'] <= 27:
            st.write('꽤 덥습니다 옷차림을 가볍게 해주세요')
            st.image(image_clear, use_column_width=False, width=500)
        if 20 <= data['main']['feels_like'] <= 22:
            st.write('포근한 봄 날씨입니다 ~ ')
            st.image(image_fall, use_column_width=False, width=500)
        if 17 <= data['main']['feels_like'] <= 19:
            st.write('쾌적한 날씨입니다 ~  ~ ')
            st.image(image_fall, use_column_width=False, width=500)
        if 12 <= data['main']['feels_like'] <= 16:
            st.write('선선한 날씨입니다. 가벼운 외투를 챙겨주세요')
            st.image(image_fall, use_column_width=False, width=500)
        if 9 <= data['main']['feels_like'] <= 11:
            st.write('쌀쌀한 날씨입니다. 외투를 챙겨주세요')
            st.image(image_fall, use_column_width=False, width=500)
        if 5 <= data['main']['feels_like'] <= 8:
            st.write('😰오늘은 춥습니다 옷차림을 따뜻하게 해주세요')
            st.image(image_snow, use_column_width=False, width=500)
        if data['main']['feels_like'] <= 4:
            st.write('☃️🥶너무 추워요 옷차림을 두껍게 해주세요! ~ ')
            st.image(image_snow, use_column_width=False, width=500)

        # Create map
        m = folium.Map(location=[data['coord']['lat'], data['coord']['lon']], zoom_start=10)
        folium.Marker([data['coord']['lat'], data['coord']['lon']], popup=city).add_to(m)
        folium_static(m)

    else:
        st.write('날씨 정보를 가져올 수 없습니다. 다시 입력해주세요.')