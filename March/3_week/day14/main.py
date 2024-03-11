import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pages import *
# 상태 저장
if 'page' not in st.session_state:
    st.session_state['page'] = 'HOME'

@st.cache_data
def load_data():
    data = pd.read_csv("health_2017~2021.csv")
    return data
data = load_data()
data[:200]

menus = {'HOME':home,'시기별':period,'연령별':age,'지역별':state}

with st.sidebar:
    for menu in menus.keys():
        if st.button(menu,use_container_width=True, type='primary' if st.session_state['page'] == menu else 'secondary'):
            st.session_state['page'] = menu
            st.rerun()
    st.title('Like Lion')

st.sidebar.title('Kim junho')
for menu in menus.keys():
    if st.session_state['page'] == menu:
        menus[menu]()