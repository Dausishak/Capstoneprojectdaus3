import streamlit as st
import pandas as pd
import altair as alt
import numpy as np 
import streamlit as st
import os
import openpyxl


# Load data from the Excel file
@st.cache
def load_data():
    data = pd.read_excel("Copy of combined_data.xlsx")
    return data

data = load_data()

from PIL import Image
image = Image.open("ExamP.jpg")

st.image(image, caption='Exam Perfromance',width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

# Sidebar - Assessment Type Selection
st.sidebar.title("Dashboard Options")
assessment_types = data['assessment_type'].unique()
selected_assessment_type = st.sidebar.selectbox('Select Assessment Type:', assessment_types)

# Group by course and calculate the average performance
average_performance = data[data['assessment_type'] == selected_assessment_type].groupby('code_module')['score'].mean().reset_index()

# Create an Altair bar chart
chart = alt.Chart(average_performance).mark_bar().encode(
    x='code_module',
    y='score',
    color='code_module:N',
    tooltip=['code_module', 'score']
).properties(
    width=600,
    height=400,
    title='Average Course Performance in the University'
).configure_axis(
    labelAngle=45
)

# Display the Altair chart using Streamlit
st.title('Average Course Performance')
st.write(f'Selected Assessment Type: {selected_assessment_type}')
st.altair_chart(chart, use_container_width=True)

# Display an interactive table
st.subheader('Interactive Table - Average Performance')
st.dataframe(average_performance.style.format({'score': '{:.2f}'}), width=600)

# Optional: Display raw data table
st.subheader('Raw Data')
st.write(average_performance)
