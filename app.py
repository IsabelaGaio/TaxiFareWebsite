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
pickup_longitude = st.text_input('Insert pickup longitude', "-73.95")
pickup_latitude = st.text_input('Insert pickup latitude', "40.8")
dropoff_longitude = st.text_input('Insert dropoff longitude', "-73.98")
dropoff_latitude = st.text_input('Insert dropoff latitude', "40.77")
passenger_count = st.text_input('Number of passengers',"1")

params = {"pickup_datetime" : date_time,
    "pickup_longitude" : float(pickup_longitude),
    "pickup_latitude" : float(pickup_latitude),
    "dropoff_longitude" : float(dropoff_longitude),
    "dropoff_latitude" : float(dropoff_latitude),
    "passenger_count" : int(passenger_count)}


url = 'https://taxifare.lewagon.ai/predict'
r = requests.get(url,params = params)

#if url == 'https://taxifare.lewagon.ai/predict':

st.markdown(f"${round(r.json()['fare'],2)}")
