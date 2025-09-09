import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Set page config
st.set_page_config(page_title="Sensormatic Digital Dashboard", layout="wide")

# Display logo banner
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Sensormatic_logo.svg/2560px-Sensormatic_logo.svg.png", use_container_width=True)

# Sidebar month selector
available_months = ["July", "August", "September"]
selected_month = st.sidebar.selectbox("Select Month", available_months)

# Sidebar section selector
section = st.sidebar.radio("Select Dashboard Section", [
    "Functional Coverage Metrics",
    "Automation Metrics",
    "Error & Defect Metrics",
    "Performance & Uptime",
    "User Experience & Sentiment",
    "Release & Deployment Metrics"
])

# Sample data generators for each section
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
        'Month': ['July', 'August', 'September'],
        'Deployments': [5, 6, 4],
        'Post-Deployment Issues': [2, 1, 3],
        'Time to Resolve (hrs)': [12, 8, 10],
        'QA Sign-off Time (hrs)': [4, 3, 5]
    })

# Section rendering
if section == "Functional Coverage Metrics":
    st.subheader("📍 Pages Tested by Country")
    st.dataframe(generate_country_coverage())
    st.subheader("📨 Forms Tested")
    st.dataframe(generate_form_coverage())
    st.subheader("🔍 Coveo Search Coverage")
    st.dataframe(generate_coveo_coverage())

elif section == "Automation Metrics":
    st.subheader("🤖 Test Automation Summary")
    st.dataframe(generate_automation_metrics())
    st.subheader("🌐 Browser/Language Coverage")
    st.dataframe(generate_browser_matrix())

elif section == "Error & Defect Metrics":
    st.subheader("🚨 Error Summary")
    st.dataframe(generate_error_metrics())
    error_df = generate_error_metrics()
    fig = px.pie(error_df, names='Error Type', values='Count', title='Error Type Distribution')
    st.plotly_chart(fig)

elif section == "Performance & Uptime":
    st.subheader("📶 Site Performance by Country")
    perf_df = generate_performance_metrics()
    st.dataframe(perf_df)
    st.subheader("📈 Page Load Time")
    fig = px.line(perf_df, x='Country', y='Page Load Time (s)', title='Page Load Time by Country')
    st.plotly_chart(fig)
    st.subheader("📊 Lighthouse Scores")
    st.dataframe(generate_lighthouse_scores())

elif section == "User Experience & Sentiment":
    st.subheader("💬 Sentiment Analysis")
    sentiment_df = generate_sentiment_data()
    st.dataframe(sentiment_df)
    fig = px.pie(sentiment_df, names='Sentiment', values='Count', title='User Sentiment Distribution')
    st.plotly_chart(fig)
    st.subheader("📈 Lead Segmentation")
    st.dataframe(generate_lead_segmentation())

elif section == "Release & Deployment Metrics":
    st.subheader("🚀 Deployment Summary")
    release_df = generate_release_metrics()
    st.dataframe(release_df)
    st.subheader("📊 Month-wise QA Trends")
    filtered_df = release_df[release_df['Month'] == selected_month]
    st.dataframe(filtered_df)
    fig = px.line(release_df, x='Month', y=['Deployments', 'Post-Deployment Issues', 'QA Sign-off Time (hrs)'],
                  title='Month-wise QA Metrics Trends')
    st.plotly_chart(fig)

# Footer
st.markdown("---")
st.caption("Sensormatic Digital Dashboard built with Streamlit | © Harsha")
