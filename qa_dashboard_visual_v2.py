import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set dark theme and page config
st.set_page_config(page_title="Sensormatic Digital Dashboard", layout="wide")

# Add logo/banner image (replace with actual image path if available)
st.markdown(
    """
    <div style='text-align: center; padding: 10px;'>
        <h1 style='color: #00AEEF;'>📊 Sensormatic Digital Dashboard</h1>
        <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Sensormatic_logo.svg/2560px-Sensormatic_logo.svg.png' width='300'/>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar navigation
section = st.sidebar.radio("Select Dashboard Section", [
    "Functional Coverage Metrics",
    "Automation Metrics",
    "Error & Defect Metrics",
    "Performance & Uptime",
    "User Experience & Sentiment",
    "Release & Deployment Metrics"
])

# Mock data generators
def generate_country_coverage():
    return pd.DataFrame({
        'Country': ['US', 'UK', 'IN', 'DE', 'FR'],
        '% Pages Tested': [95, 90, 85, 80, 75]
    })

def generate_form_coverage():
    return pd.DataFrame({
        'Form Type': ['Contact', 'Demo', 'Newsletter'],
        '% Forms Tested': [98, 92, 88]
    })

def generate_coveo_coverage():
    return pd.DataFrame({
        'Metric': ['Queries Tested', 'Filters Tested', 'Relevance Score'],
        'Coverage %': [90, 85, 80]
    })

def generate_automation_metrics():
    return pd.DataFrame({
        'Suite': ['Smoke', 'Regression', 'E2E'],
        'Test Cases': [50, 120, 80],
        'Pass Rate %': [98, 92, 95],
        'Execution Time (min)': [5, 20, 15]
    })

def generate_browser_matrix():
    return pd.DataFrame({
        'Browser': ['Chrome', 'Firefox', 'Safari', 'Edge'],
        'Languages Covered': [5, 4, 3, 2]
    })

def generate_error_metrics():
    return pd.DataFrame({
        'Error Type': ['Broken Links', '404 Errors', '500 Errors', 'SEO Issues', 'Form Failures', 'Coveo Anomalies'],
        'Count': [12, 5, 2, 20, 8, 3]
    })

def generate_performance_metrics():
    return pd.DataFrame({
        'Country': ['US', 'UK', 'IN', 'DE', 'FR'],
        'Page Load Time (s)': [1.2, 1.5, 2.0, 1.8, 1.6],
        'Uptime %': [99.9, 99.8, 99.7, 99.6, 99.5]
    })

def generate_lighthouse_scores():
    return pd.DataFrame({
        'Metric': ['Accessibility', 'Performance', 'SEO'],
        'Score': [90, 85, 88]
    })

def generate_sentiment_data():
    return pd.DataFrame({
        'Sentiment': ['Positive', 'Neutral', 'Negative'],
        'Count': [120, 30, 10]
    })

def generate_lead_segmentation():
    return pd.DataFrame({
        'Lead Type': ['Sales', 'Support'],
        'Count': [80, 40]
    })

def generate_release_metrics():
    return pd.DataFrame({
        'Month': ['Jul', 'Aug', 'Sep'],
        'Deployments': [5, 6, 4],
        'Post-Deployment Issues': [2, 1, 3],
        'Time to Resolve (hrs)': [12, 8, 10],
        'QA Sign-off Time (hrs)': [4, 3, 5]
    })

# Section rendering
if section == "Functional Coverage Metrics":
    st.subheader("📍 Pages Tested by Country")
    df = generate_country_coverage()
    st.dataframe(df)
    st.plotly_chart(px.bar(df, x='Country', y='% Pages Tested', title='Pages Tested by Country'))

    st.subheader("📨 Forms Tested")
    df = generate_form_coverage()
    st.dataframe(df)
    st.plotly_chart(px.bar(df, x='Form Type', y='% Forms Tested', title='Forms Tested'))

    st.subheader("🔍 Coveo Search Coverage")
    df = generate_coveo_coverage()
    st.dataframe(df)
    st.plotly_chart(px.bar(df, x='Metric', y='Coverage %', title='Coveo Coverage'))

elif section == "Automation Metrics":
    st.subheader("🤖 Test Automation Summary")
    df = generate_automation_metrics()
    st.dataframe(df)
    st.plotly_chart(px.bar(df, x='Suite', y='Pass Rate %', title='Pass Rate by Suite'))

    st.subheader("🌐 Browser/Language Coverage")
    df = generate_browser_matrix()
    st.dataframe(df)
    st.plotly_chart(px.bar(df, x='Browser', y='Languages Covered', title='Browser Language Coverage'))

elif section == "Error & Defect Metrics":
    st.subheader("🚨 Error Summary")
    df = generate_error_metrics()
    st.dataframe(df)
    st.plotly_chart(px.pie(df, names='Error Type', values='Count', title='Error Type Distribution'))

elif section == "Performance & Uptime":
    st.subheader("📶 Site Performance by Country")
    df = generate_performance_metrics()
    st.dataframe(df)
    st.plotly_chart(px.line(df, x='Country', y='Page Load Time (s)', title='Page Load Time by Country'))

    st.subheader("📈 Lighthouse Scores")
    df = generate_lighthouse_scores()
    st.dataframe(df)
    st.plotly_chart(px.bar(df, x='Metric', y='Score', title='Lighthouse Scores'))

elif section == "User Experience & Sentiment":
    st.subheader("🧠 NLP Sentiment Analysis")
    df = generate_sentiment_data()
    st.dataframe(df)
    st.plotly_chart(px.pie(df, names='Sentiment', values='Count', title='User Sentiment Distribution'))

    st.subheader("📊 Lead Segmentation")
    df = generate_lead_segmentation()
    st.dataframe(df)
    st.plotly_chart(px.bar(df, x='Lead Type', y='Count', title='Lead Segmentation'))

elif section == "Release & Deployment Metrics":
    st.subheader("🚀 Deployment Summary")
    df = generate_release_metrics()
    st.dataframe(df)
    st.plotly_chart(px.line(df, x='Month', y=['Deployments', 'Post-Deployment Issues', 'QA Sign-off Time (hrs)'],
                            title='Month-wise QA Metrics Trends'))

st.markdown("---")
st.caption("Sensormatic Digital Dashboard | Built with Streamlit | © Harsha")
