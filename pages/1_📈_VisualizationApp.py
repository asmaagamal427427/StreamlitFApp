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

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

#File Uploading
file = st.file_uploader('Upload Your CSV File', type='CSV')

if file is not None:
    df = load_data(file)


n_rows = st.slider('Choose number of rows to display',
                   min_value=5, max_value=len(df), step=1)
columns_to_show = st.multiselect('Select Columns to show', df.columns, default=df.columns.to_list())
numerical_columns = df.select_dtypes(include=np.number).columns.to_list()

st.write(df[:n_rows][columns_to_show])

tab1, tab2 = st.tabs(['Scatter Plot', 'Histogram'])

with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        x_column = st.selectbox('Select a column on the x axis', options=numerical_columns)
    with col2:
        y_column = st.selectbox('Select a column on the y axis', options=numerical_columns)
    with col3:
        color = st.selectbox('Select column to be the color', df.columns)

    fig_scatter = px.scatter(df, x=x_column, y=y_column, color=color)
    st.plotly_chart(fig_scatter)

with tab2:
    hist_feat = st.selectbox('Select feature for the histogram', options=numerical_columns)
    fig_hist = px.histogram(df, x=hist_feat)
    st.plotly_chart(fig_hist)