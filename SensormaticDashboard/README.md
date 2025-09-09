# Sensormatic Digital Dashboard

This repository contains a Streamlit-based QA dashboard with monthly metrics.

## 📁 Folder Structure

- `data/YYYY_MM/` — Monthly folders with CSV files for each dashboard section
- `qa_dashboard_visual.py` — Streamlit dashboard script
- `scripts/excel_to_csv_converter.py` — Script to convert Excel to CSV
- `requirements.txt` — Required Python packages

## 📊 Dashboard Sections

- Functional Coverage Metrics
- Automation Metrics
- Error & Defect Metrics
- Performance & Uptime
- User Experience & Sentiment
- Release & Deployment Metrics

## 🚀 How to Use

1. Upload monthly Excel file with sheets for each section
2. Run `excel_to_csv_converter.py` to generate CSVs
3. Launch dashboard with `streamlit run qa_dashboard_visual.py`
4. Use sidebar to select month and view metrics

