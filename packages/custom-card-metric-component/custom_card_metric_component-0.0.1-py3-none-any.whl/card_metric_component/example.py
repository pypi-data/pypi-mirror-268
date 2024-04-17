import streamlit as st
from __init__ import card_metric

st.set_page_config(layout="wide")


data = [
    {
        "id":0,
        "metricTitle":"Minimum Total Damage",
        "heroName":"Hero",
        "heroUrl":"http://localhost:8501/app/static/heroes/Miya.png",
        "metric":300000
    },
     {
        "id":1,
        "metricTitle":"Minimum Total Damage",
        "heroName":"Hero",
        "heroUrl":"http://localhost:8501/app/static/heroes/Miya.png",
        "metric":300000
    }
]

card_metric(dataCards=data)