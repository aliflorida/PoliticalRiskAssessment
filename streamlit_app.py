import streamlit as st
import os
from models.prince_model import run_prince_model
from models.icrg_model import run_icrg_model
from models.wgi_model import run_wgi_model
from utils.model_selector import select_models

st.set_page_config(page_title="Political Risk Analyst", layout="wide")
st.title("🌍 Political Risk Assessment Tool")

with st.sidebar:
    st.header("Project Setup")
    target_country = st.text_input("📍 Target Country")
    home_country = st.text_input("🏢 Home Country of the Company")
    company_name = st.text_input("📛 Company Name (optional)")
    investment_type = st.selectbox("💼 Type of Investment", ["Market Entry", "Joint Venture", "Acquisition", "Infrastructure"])
    industry = st.text_input("🏭 Industry Sector")

    st.markdown("### ⏳ Time Horizons")
    start_date = st.text_input("1️⃣ Project Start Date")
    mid_term = st.text_input("2️⃣ Mid-Term Forecast Horizon")
    long_term = st.text_input("3️⃣ Long-Term Forecast Horizon")

    broad_risk = st.text_area("⚠️ General Political Risk Concerns")
    future_concerns = st.text_area("🔮 Specific Future Concerns for Forecasting")
    forecast_checks = st.text_area("🔎 Forecast Checks (e.g., coup, leadership change)")

    custom_vars = st.text_area("🛠️ Custom Variables (optional)")
    audiences = st.multiselect("👥 Report Audience", ["Data Analysis Team", "Political Risk Team", "Client", "Executive Leadership"])
    recommendation_type = st.selectbox("📌 Desired Recommendation Type", ["Go / No Go Decision", "Investment Timing Advice", "Mitigation Strategy Suggestions"])

if st.button("Run Risk Assessment"):
    st.header("📘 Definition of Political Risk")
    st.markdown("Political risk refers to the probability that political decisions, events, or conditions will affect the business environment in a way that may impact investments. Understanding political risk is essential for anticipating disruptions, designing mitigation strategies, and safeguarding long-term outcomes.")

    selected_models = select_models(investment_type, industry, long_term)
    st.success(f"Selected Models: {', '.join(selected_models)}")

    for model in selected_models:
        if model == "PRINCE":
            result = run_prince_model(target_country, industry, long_term, broad_risk, future_concerns, recommendation_type)
        elif model == "ICRG":
            result = run_icrg_model(target_country, industry, long_term, broad_risk, future_concerns, recommendation_type)
        elif model == "WGI":
            result = run_wgi_model(target_country, industry, long_term, broad_risk, future_concerns, recommendation_type)

        st.subheader(f"{result['model']} Model Results")
        st.markdown(f"**Risk Level**: {result['risk_level']}")
        st.markdown(f"**Score**: {result['score']} / 100")
        st.markdown("**Key Risks:**")
        st.write(result["key_risks"])
        st.markdown("**Summary:**")
        st.write(result["summary"])

    st.markdown("### ✅ Report Audience")
    st.write(f"This assessment was generated for the following audiences: {', '.join(audiences)}")