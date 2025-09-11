import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Sensormatic Digital Dashboard", layout="wide")
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

# Month selector
month = st.sidebar.selectbox("Select Month", ["July", "August", "September"])

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
        'Month': ['July', 'August', 'September'],
        'Deployments': [5, 6, 4],
        'Post-Deployment Issues': [2, 1, 3],
        'Time to Resolve (hrs)': [12, 8, 10],
        'QA Sign-off Time (hrs)': [4, 3, 5]
    })

# Section rendering
if section == "Functional Coverage Metrics":
    st.subheader("📍 Pages Tested by Country")
    df = generate_country_coverage()
    st.plotly_chart(px.bar(df, x='Country', y='% Pages Tested', color='Country', title="Pages Tested by Country"))

    st.subheader("📨 Forms Tested")
    st.plotly_chart(px.bar(generate_form_coverage(), x='Form Type', y='% Forms Tested', color='Form Type'))

    st.subheader("🔍 Coveo Search Coverage")
    st.plotly_chart(px.bar(generate_coveo_coverage(), x='Metric', y='Coverage %', color='Metric'))

    st.subheader("📈 Country Coverage Bubble Chart")
    bubble = px.scatter(df, x='Country', y='% Pages Tested', size='% Pages Tested', color='Country',
                        title="Stock-Market Style Country Distribution", size_max=60)
    st.plotly_chart(bubble)

elif section == "Automation Metrics":
    st.subheader("🤖 Test Automation Summary")
    auto_df = generate_automation_metrics()
    st.dataframe(auto_df)

    st.subheader("📊 Pass Rate Gauge")
    for i, row in auto_df.iterrows():
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=row['Pass Rate %'],
            title={'text': f"{row['Suite']} Pass Rate"},
            gauge={'axis': {'range': [0, 100]}}
        ))
        st.plotly_chart(fig)

    st.subheader("🌐 Browser/Language Coverage")
    st.plotly_chart(px.bar(generate_browser_matrix(), x='Browser', y='Languages Covered', color='Browser'))

elif section == "Error & Defect Metrics":
    st.subheader("🚨 Error Summary")
    err_df = generate_error_metrics()
    st.plotly_chart(px.pie(err_df, names='Error Type', values='Count', title="Error Type Distribution"))

elif section == "Performance & Uptime":
    st.subheader("📶 Site Performance by Country")
    perf_df = generate_performance_metrics()
    st.plotly_chart(px.line(perf_df, x='Country', y='Page Load Time (s)', markers=True, title="Page Load Time"))

    st.subheader("📊 Uptime Gauge")
    for i, row in perf_df.iterrows():
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=row['Uptime %'],
            title={'text': f"{row['Country']} Uptime"},
            gauge={'axis': {'range': [95, 100]}}
        ))
        st.plotly_chart(fig)

    st.subheader("📊 Lighthouse Scores")
    st.plotly_chart(px.bar(generate_lighthouse_scores(), x='Metric', y='Score', color='Metric'))

elif section == "User Experience & Sentiment":
    st.subheader("💬 Hotjar Feedback Trends")
    st.metric("Positive Feedback %", "85%")

    st.subheader("🧠 NLP Sentiment Analysis")
    st.plotly_chart(px.pie(generate_sentiment_data(), names='Sentiment', values='Count', title="User Sentiment"))

    st.subheader("📊 Lead Segmentation")
    st.plotly_chart(px.bar(generate_lead_segmentation(), x='Lead Type', y='Count', color='Lead Type'))

elif section == "Release & Deployment Metrics":
    st.subheader("🚀 Deployment Summary")
    release_df = generate_release_metrics()
    st.dataframe(release_df)

    st.subheader("📈 Month-wise QA Trends")
    st.plotly_chart(px.line(release_df, x='Month', y=['Deployments', 'Post-Deployment Issues', 'QA Sign-off Time (hrs)'],
                            markers=True, title="Monthly QA Metrics"))

st.markdown("---")
st.caption("Sensormatic Digital Dashboard | © Harsha")



# 📊 Lighthouse Deep Dive Section
def generate_lighthouse_deep_dive():
    return pd.DataFrame({
        'Metric': [
            'First Contentful Paint (FCP)',
            'Speed Index',
            'Time to Interactive (TTI)',
            'Total Blocking Time (TBT)',
            'Largest Contentful Paint (LCP)',
            'Cumulative Layout Shift (CLS)'
        ],
        'Value': [1.2, 3.5, 2.8, 150, 2.5, 0.1]
    })

if section == "Performance & Uptime":
    st.subheader("📊 Lighthouse Deep Dive")
    deep_dive_df = generate_lighthouse_deep_dive()
    st.dataframe(deep_dive_df)
    st.plotly_chart(px.bar(deep_dive_df, x='Metric', y='Value', color='Metric', title="Detailed Lighthouse Metrics"))
