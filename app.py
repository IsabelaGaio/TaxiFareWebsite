import streamlit as st

import numpy as np
import pandas as pd

import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
# Taxi Fare Model
## Input the details of your trip
''')

# input Date
date_time = st.text_input("Date and time", "2022-03-15 13:20:00")
pickup_longitude = st.number_input('Insert pickup longitude')
pickup_latitude = st.number_input('Insert pickup latitude')
dropoff_longitude = st.number_input('Insert dropoff longitude')
dropoff_latitude = st.number_input('Insert dropoff latitude')
passenger_count = st.number_input('Number of passengers')

params = {"date and time" : date_time,
    "pickup longitude": pickup_longitude,
    "pickup latitude": pickup_latitude,
    "dropoff longitude": dropoff_longitude,
    "dropoff latitude": dropoff_latitude,
    "passenger count": passenger_count}


url = 'https://taxifare.lewagon.ai/predict'
r = requests.get(url,params = params)

#if url == 'https://taxifare.lewagon.ai/predict':

st.markdown(f"${round(r.json()['fare'],2)}")
