# 🌐 **Streamlit Starter Pack**

A hands-on introduction to **Streamlit**, covering the basics and moving towards a fully interactive data dashboard.

---

## 📌 **Contents**

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Hello World App](#hello-world-app)
4. [Basic Dashboard](#basic-dashboard)
5. [Running the Applications](#running-the-applications)
6. [Next Steps](#next-steps)

---

## 🎯 **Introduction**

Streamlit is a powerful and lightweight web framework that allows you to build data applications using just **Python**. With Streamlit, you can:

* Create interactive apps in minutes
* Visualize data without HTML, CSS, or JavaScript
* Share your work instantly with others

---

## 🚀 **Getting Started**

### **Prerequisites**

Ensure you have the following installed:

* Python 3.8+
* pip (Python package manager)

### **Installation**

First, clone the repository:

```bash
git clone https://github.com/your-username/streamlit-starter-pack.git
cd streamlit-starter-pack
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## 👋 **Hello World App**

The **Hello World** example introduces you to Streamlit's core features:

* Text display with `st.title`, `st.header`, and `st.write`
* Interactive widgets like buttons and sliders

### **hello\_world.py**

```python
import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Hello World App", layout="centered")

# Display the title
st.title("Hello, Streamlit World!")

# Add a header and some text
st.header("Welcome to Your First Streamlit App")
st.write("This example introduces you to Streamlit’s core features.")

# Interactive button
if st.button("Click Me"):
    st.success("Button clicked successfully!")

# User input
name = st.text_input("What’s your name?")
if name:
    st.write(f"Hello, {name}! Nice to meet you.")

# Slider for interactivity
age = st.slider("Select your age:", 1, 100)
st.write(f"You’re {age} years old.")
```

### **Key Features**

1. **Interactive Widgets:** Buttons, sliders, and text inputs.
2. **Real-Time Updates:** UI changes as users interact.
3. **Simple Python API:** No HTML, CSS, or JavaScript required.

---

## 📊 **Basic Dashboard**

Building on `hello_world.py`, this example introduces data visualization and filtering.

### **basic\_dashboard.py**

```python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="Basic Streamlit Dashboard", layout="centered")
st.title("Basic Streamlit Dashboard")
st.write("A straightforward dashboard to explore Streamlit’s capabilities.")

# Generate sample data
@st.cache_data
def generate_data(rows=100):
    np.random.seed(42)
    data = {
        'Category': np.random.choice(['A', 'B', 'C'], size=rows),
        'Value': np.random.randint(1, 100, size=rows),
        'Score': np.random.randn(rows) * 15 + 50
    }
    return pd.DataFrame(data)

df = generate_data()

# Sidebar filters
st.sidebar.header("Filters")
category_filter = st.sidebar.multiselect("Select Category:", options=df['Category'].unique(), default=df['Category'].unique())
value_filter = st.sidebar.slider("Minimum Value:", min_value=0, max_value=100, value=0)

# Apply filters
filtered_df = df[(df['Category'].isin(category_filter)) & (df['Value'] >= value_filter)]

# Display data
st.write("### Filtered Data")
st.dataframe(filtered_df)

# Visualizations
st.write("### Category Distribution")
fig, ax = plt.subplots()
filtered_df['Category'].value_counts().plot(kind='bar', color=['#4CAF50', '#FFC107', '#2196F3'], ax=ax)
ax.set_xlabel('Category')
ax.set_ylabel('Count')
ax.set_title('Distribution of Categories')
st.pyplot(fig)

st.write("### Score Trends")
st.line_chart(filtered_df[['Score']])
```

### **Key Features**

1. **DataFrame Display:** Interactive table view for filtered data.
2. **Sidebar Controls:** Real-time filtering of data with dropdowns and sliders.
3. **Data Visualization:** Bar charts and line charts for easy analysis.

---

## ▶️ **Running the Applications**

To run the applications, navigate to the project directory and use the following commands:

### **Hello World App**

```bash
streamlit run hello_world.py
```

Visit [http://localhost:8501](http://localhost:8501) to interact with the app.

---

### **Basic Dashboard**

```bash
streamlit run basic_dashboard.py
```

Visit [http://localhost:8501](http://localhost:8501) to view the dashboard.

---

## 🌐 **Next Steps**

Now that you have successfully run:

1. `hello_world.py` for basic interactivity.
2. `basic_dashboard.py` for data visualization.

### Consider exploring:

* **Music Streaming Analytics Dashboard:** A full-fledged real-time dashboard with Spotify and Apple Music data.
* **Deployment on Hugging Face or Streamlit Cloud** to make your apps public.

---

Would you like me to extend this README to include deployment steps for both **Hugging Face** and **Streamlit Community Cloud**? That would allow you to share your apps live with just a few commands.
