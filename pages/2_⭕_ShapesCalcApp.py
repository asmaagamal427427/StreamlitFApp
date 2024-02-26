#Importing Libs
from ast import increment_lineno
from random import randint
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import time

#Testing Streamlit
st.header("Shapes Calculations")

st.sidebar.title('Configurations')
with st.sidebar:
    shape = st.selectbox("Choose Shape: ", ['Circle', 'Rectangle'])

if shape == 'Circle':
    radius = st.number_input('Choose Radius: ', min_value=0, max_value=100, step=1)
    area = radius * radius * 3.14
    perimeter = 2 * 3.14 * radius

if shape == 'Rectangle':
    width = st.number_input('Choose Width: ', min_value=0, max_value=100, step=1)
    Height = st.number_input('Choose Height: ', min_value=0, max_value=100, step=1)
    area = width * Height
    perimeter = 2 * (width + Height)

compute_btn = st.button('Compute Area and Perimeter')
if compute_btn:
    with st.spinner('Computing...'):
        time.sleep(1)
        st.write('Area: ', area)
        st.write('Perimeter: ', perimeter)