import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

def generate_plot(data, column, plot):
    valid_data = data[column].dropna() 
#generating Histogram plots
    if plot == 'Histogram':
        if data[column].dtype in ['int64', 'float64']:
            fig = px.histogram(valid_data, x=column, nbins=50, title=f'Histogram of {column}')
        else:
            fig = px.histogram(data, x=column, title=f'Count Plot of {column}')

#generating line plots 
    elif plot == 'Line Plot':
        if data[column].dtype in ['int64', 'float64']:
            fig = px.line(valid_data, y=column, title=f'Line Plot of {column}')
        else:
            fig = px.line(valid_data, y=column, title=f'Line Plot of {column}')

# generating scatter plots       
    elif plot == 'Scatter Plot':
        if data[column].dtype in ['int64', 'float64']:
            fig = px.scatter(valid_data, y=column, title=f'Scatter Plot of {column}')
        else:
            fig = px.scatter(valid_data, y=column, title=f'Scatter Plot of {column}')

# generating Pie charts     
    elif plot == 'Pie Chart':
        if data[column].dtype == 'object' or data[column].dtype.name == 'category':
            fig = px.pie(data, names=column, title=f'Pie Chart of {column}')
        else:
            fig = px.pie(data, names=column, title=f'Pie Chart of {column}')
           


    st.plotly_chart(fig, use_container_width=True)
