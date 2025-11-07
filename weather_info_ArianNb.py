import os
import requests
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
location_latitude = st.text_input("Enter Latitude:")
location_longitude = st.text_input("Enter Longitude:")
api_key = os.getenv("API_KEY")
with st.sidebar:
    st.write("get your guess city's weather information!")
    # st.image("51ZgFK-FbwL._h1_.png")
btn = st.button("get weather info!")
if btn:
    api = f"https://api.weatherbit.io/v2.0/current?lat={location_latitude}&lon={location_longitude}&key={api_key}&include=minutely"
    response = requests.get(api)
    print(response.status_code)
    api_data = response.json()
    print(api_data)
    city_name = api_data['data'][0]['city_name']
    weather_description = api_data['data'][0]['weather']['description']
    st.write('city', city_name)
    st.write('weather', weather_description)
# tehran latitude and longitude
# 35.7219
# 51.3347
