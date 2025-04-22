import streamlit as st
import pandas as pd
import os
from models.prince_model import run_prince_model
from utils.narrative import generate_full_report

st.set_page_config(page_title="Political Risk Assessment", layout="wide")
st.title("📊 Political Risk Assessment Tool")

with st.sidebar:
    target_country = st.text_input("Target Country")
    home_country = st.text_input("Home Country")
    company_name = st.text_input("Company Name")
    investment_type = st.selectbox("Type of Investment", ["Market Entry", "Joint Venture", "Acquisition", "Infrastructure"])
    industry = st.text_input("Industry Sector")
    start_date = st.text_input("Start Date")
    mid_term = st.text_input("Mid-Term Forecast")
    long_term = st.text_input("Long-Term Forecast")
    broad_risk = st.text_area("Broad Political Risk Concerns (e.g. expropriation, FX instability)")
    future_concerns = st.text_area("Specific Forecast Concerns (e.g. elections, coups, military unrest)")
    recommendation_type = st.selectbox("Type of Recommendation", [
        "Go / No Go Decision", "Investment Timing Advice", "Mitigation Strategy Suggestions"
    ])
    export_format = st.selectbox("Export Report As", ["None", "DOCX", "PDF"])

if st.button("Generate Assessment"):
    model_data = []
    prince = run_prince_model(target_country, industry, long_term)
    model_data.append(prince)

    report_text = generate_full_report(
        target_country,
        company_name,
        investment_type,
        industry,
        broad_risk,
        future_concerns,
        recommendation_type,
        model_data
    )

    st.header("📘 Full Report")
    st.markdown(report_text)

    st.header("📊 Model Tables")
    for model in model_data:
        st.subheader(f"{model['model']} Model")
        df = pd.DataFrame({
            "Risk Type": ["Macro", "Micro", "Sovereign"],
            "Variables": [", ".join(model["macro"]), ", ".join(model["micro"]), ", ".join(model["sovereign"])],
            "Recommendation": [model["recommendations"]] * 3
        })
        st.table(df)