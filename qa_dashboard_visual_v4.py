
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="QA Automation Dashboard", layout="wide")

st.title("📊 Sensormatic Digital Dashboard")

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
        'Month': ['Jan', 'Feb', 'Mar'],
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
    st.subheader("🔁 Akamai Redirect Rules Validated")
    st.metric("Redirect Rules Validated", "150")
    st.subheader("🍪 Cookie Compliance Checks")
    st.metric("Compliance Passed", "98%")

elif section == "Automation Metrics":
    st.subheader("🤖 Test Automation Summary")
    st.dataframe(generate_automation_metrics())
    st.subheader("🌐 Browser/Language Coverage")
    st.dataframe(generate_browser_matrix())
    st.subheader("⏱️ Cron Job Success Rate")
    st.metric("Success Rate", "99.5%")

elif section == "Error & Defect Metrics":
    st.subheader("🚨 Error Summary")
    st.dataframe(generate_error_metrics())

elif section == "Performance & Uptime":
    st.subheader("📶 Site Performance by Country")
    perf_df = generate_performance_metrics()
    st.dataframe(perf_df)
    st.subheader("📈 Lighthouse Scores")
    st.dataframe(generate_lighthouse_scores())
    st.subheader("⚡ Akamai Rule Latency")
    st.metric("Avg Latency", "120ms")

elif section == "User Experience & Sentiment":
    st.subheader("💬 Hotjar Feedback Trends")
    st.metric("Positive Feedback %", "85%")
    st.subheader("🧠 NLP Sentiment Analysis")
    st.dataframe(generate_sentiment_data())
    st.subheader("📊 Lead Segmentation")
    st.dataframe(generate_lead_segmentation())

elif section == "Release & Deployment Metrics":
    st.subheader("🚀 Deployment Summary")
    st.dataframe(generate_release_metrics())

st.markdown("---")
st.caption("Mock QA Dashboard built with Streamlit | © Harsha")
