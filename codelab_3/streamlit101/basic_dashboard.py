# basic_dashboard.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the page configuration
st.set_page_config(page_title="Basic Streamlit Dashboard", layout="centered")

# Title and description
st.title("📊 Basic Streamlit Dashboard")
st.write("A simple dashboard showcasing Streamlit's basic features.")

# --- Sample Data Generation ---
@st.cache_data
def generate_data(rows=100):
    """Generates a sample DataFrame with random data."""
    np.random.seed(42)  # For reproducibility
    data = {
        'Category': np.random.choice(['A', 'B', 'C'], size=rows),
        'Value': np.random.randint(1, 100, size=rows),
        'Score': np.random.randn(rows) * 15 + 50
    }
    return pd.DataFrame(data)

# Load data
df = generate_data()

# --- Sidebar Widgets ---
st.sidebar.header("Filters")
category_filter = st.sidebar.multiselect("Select Category:", options=df['Category'].unique(), default=df['Category'].unique())
value_filter = st.sidebar.slider("Minimum Value:", min_value=0, max_value=100, value=0)

# Apply filters
filtered_df = df[(df['Category'].isin(category_filter)) & (df['Value'] >= value_filter)]

# --- Main Display ---
st.write("### Filtered DataFrame")
st.dataframe(filtered_df)

# --- Visualization ---
st.write("### Category Distribution")

# Matplotlib Bar Chart
fig, ax = plt.subplots()
filtered_df['Category'].value_counts().plot(kind='bar', color=['#4CAF50', '#FFC107', '#2196F3'], ax=ax)
ax.set_xlabel('Category')
ax.set_ylabel('Count')
ax.set_title('Distribution of Categories')
st.pyplot(fig)

# Line Chart Visualization
st.write("### Score Trends Over Entries")
st.line_chart(filtered_df[['Score']])

# --- Metrics Display ---
st.write("### Summary Metrics")
st.metric(label="Total Entries", value=len(filtered_df))
st.metric(label="Average Score", value=f"{filtered_df['Score'].mean():.2f}")
st.metric(label="Max Value", value=filtered_df['Value'].max())
