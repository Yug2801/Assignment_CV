import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

def generate_plots(data):
    numerical_cols = data.select_dtypes(include=['number']).columns
    categorical_cols = data.select_dtypes(exclude=['number']).columns
    
    # Plot histograms for numerical columns
    for col in numerical_cols:
        valid_data = data[col].dropna()  # Remove NaN values
        valid_data = valid_data[np.isfinite(valid_data)]  # Remove infinite values
        if not valid_data.empty:
            fig = px.histogram(valid_data, x=col, nbins=50, title=f'Histogram of {col}')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning(f"No valid data for column: {col}")
    
    # Plot count plots for categorical columns
    for col in categorical_cols:
        fig = px.histogram(data, x=col, title=f'Count Plot of {col}')
        st.plotly_chart(fig, use_container_width=True)

# Example usage:
# data = load_csv('data/sample.csv')
# encoded_data, _ = encode_data(data)
# generate_plots(encoded_data)
