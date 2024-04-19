import streamlit as st
from __init__ import card_metric

st.set_page_config(layout="wide")


data = [
    {
        "id":0,
        "metricTitle":"Maximum Total Damage",
        "heroName":"Miya",
        "heroUrl":"http://localhost:8501/app/static/heroes/Miya.png",
        "skillUrl":"http://localhost:8501/app/static/heroes/Miya.png",
        "skillUrlLabel":"Maximum total damage skill",
        "skillName":"skillName",
        "metric":300000,
    },
     {
        "id":1,
        "metricTitle":"Minimum Total Damage",
        "heroName":"Miya",
        "heroUrl":"http://localhost:8501/app/static/heroes/Miya.png",
        "skillUrl":"http://localhost:8501/app/static/heroes/Miya.png",
        "skillUrlLabel":"Minimum total damage skill",
        "skillName":"skillName",
        "metric":300000
    }
]

card_metric(dataCards=data)