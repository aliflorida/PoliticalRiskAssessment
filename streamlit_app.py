import streamlit as st
from models.prince_model import run_prince_model
from models.icrg_model import run_icrg_model
from models.wgi_model import run_wgi_model
from utils.model_selector import select_models

st.title("🌍 Political Risk Assessment Tool")

with st.sidebar:
    st.header("Assessment Inputs")
    target_country = st.text_input("Target Country")
    home_country = st.text_input("Home Country")
    company_name = st.text_input("Company Name (optional)")
    investment_type = st.selectbox("Type of Investment", ["Market Entry", "Joint Venture", "Acquisition", "Infrastructure"])
    industry = st.text_input("Industry Sector")
    time_horizon = st.selectbox("Time Horizon", ["Near-term (0–1 year)", "Mid-term (2–3 years)", "Long-term (4+ years)"])
    risk_concerns = st.text_area("Particular Risk Concerns (optional)")
    audience = st.selectbox("Intended Audience", ["Executive", "Analyst", "Client", "Government"])
    custom_vars = st.text_area("Custom Variables (optional)")
    future_focus = st.text_area("Future Concerns or Focus Areas (optional)")
    forecast_validation = st.text_area("Forecast Validation Requests (optional)")

if st.button("Run Assessment"):
    selected_models = select_models(investment_type, industry, time_horizon)
    st.success(f"Selected models: {', '.join(selected_models)}")
    results = []

    if "PRINCE" in selected_models:
        st.subheader("PRINCE Model Results")
        results.append(run_prince_model(target_country, industry, time_horizon))
        st.write(results[-1])
    if "ICRG" in selected_models:
        st.subheader("ICRCG Model Results")
        results.append(run_icrg_model(target_country, industry, time_horizon))
        st.write(results[-1])
    if "WGI" in selected_models:
        st.subheader("WGI Model Results")
        results.append(run_wgi_model(target_country, industry, time_horizon))
        st.write(results[-1])