
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Set page config
st.set_page_config(page_title="Sensormatic Digital Dashboard", layout="wide")

# Title
st.title("📊 Sensormatic Digital Dashboard")

# Sidebar navigation
section = st.sidebar.radio("Select Dashboard Section", [
    "Birds-Eye View",
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

# Birds-Eye View Section
if section == "Birds-Eye View":
    st.subheader("📈 Birds-Eye View of QA Metrics")

    # Gauge for Pass Rate
    auto_df = generate_automation_metrics()
    avg_pass_rate = int(auto_df['Pass Rate %'].mean())
    fig_gauge_pass = go.Figure(go.Indicator(
        mode="gauge+number",
        value=avg_pass_rate,
        title={'text': "Avg Pass Rate %"},
        gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "green"}}
    ))

    # Gauge for Uptime
    perf_df = generate_performance_metrics()
    avg_uptime = round(perf_df['Uptime %'].mean(), 2)
    fig_gauge_uptime = go.Figure(go.Indicator(
        mode="gauge+number",
        value=avg_uptime,
        title={'text': "Avg Uptime %"},
        gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "blue"}}
    ))

    # Gauge for QA Sign-off Time
    rel_df = generate_release_metrics()
    avg_signoff = int(rel_df['QA Sign-off Time (hrs)'].mean())
    fig_gauge_signoff = go.Figure(go.Indicator(
        mode="gauge+number",
        value=avg_signoff,
        title={'text': "Avg QA Sign-off Time (hrs)"},
        gauge={'axis': {'range': [0, 10]}, 'bar': {'color': "orange"}}
    ))

    col1, col2, col3 = st.columns(3)
    col1.plotly_chart(fig_gauge_pass, use_container_width=True)
    col2.plotly_chart(fig_gauge_uptime, use_container_width=True)
    col3.plotly_chart(fig_gauge_signoff, use_container_width=True)

    # Bubble chart for country coverage
    country_df = generate_country_coverage()
    fig_bubble = px.scatter(country_df, x='Country', y='% Pages Tested',
                            size='% Pages Tested', color='Country',
                            title="Country-wise Page Coverage",
                            size_max=60)
    st.plotly_chart(fig_bubble, use_container_width=True)

    # Line chart for month-wise deployments
    fig_line = px.line(rel_df, x='Month',
                       y=['Deployments', 'Post-Deployment Issues', 'QA Sign-off Time (hrs)'],
                       markers=True,
                       title="Month-wise QA Trends")
    st.plotly_chart(fig_line, use_container_width=True)

# Footer
st.markdown("---")
st.caption("Sensormatic QA Dashboard | Built with Streamlit | © Harsha")
