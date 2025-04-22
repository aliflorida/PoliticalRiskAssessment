import streamlit as st
import os
from models.prince_model import run_prince_model
from models.icrg_model import run_icrg_model
from models.wgi_model import run_wgi_model
from utils.model_selector import select_models
from utils.narrative import generate_full_narrative
from utils.docxtpl_exporter import export_to_docx

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
    broad_risk = st.text_area("Broad Political Risk Concerns")
    future_concerns = st.text_area("Specific Forecast Concerns")
    recommendation_type = st.selectbox("Type of Recommendation", [
        "Go / No Go Decision", "Investment Timing Advice", "Mitigation Strategy Suggestions"
    ])
    export_format = st.selectbox("Export Report As", ["DOCX"])
    audiences = st.multiselect("Audience", ["Client", "Analyst Team", "Political Risk Group"])

if st.button("Generate Assessment"):
    narrative = generate_full_narrative(target_country, company_name, investment_type, industry, broad_risk, future_concerns, recommendation_type)
    st.header("Narrative Report")
    st.markdown(narrative)

    models = select_models(investment_type, industry, long_term)
    outputs = []

    for model in models:
        if model == "PRINCE":
            outputs.append(run_prince_model(target_country, industry, long_term))
        elif model == "ICRG":
            outputs.append(run_icrg_model(target_country, industry, long_term))
        elif model == "WGI":
            outputs.append(run_wgi_model(target_country, industry, long_term))

    model_text = ""
    for result in outputs:
        model_text += f"\n\n{result['model']} Model:\nScore: {result['score']}\n"
        model_text += f"Macro: {', '.join(result['macro'])}\n"
        model_text += f"Micro: {', '.join(result['micro'])}\n"
        model_text += f"Sovereign: {', '.join(result['sovereign'])}\n"
        model_text += f"Recommendations: {result['recommendations']}\n"

    st.subheader("Model Results")
    st.text(model_text)

    if export_format == "DOCX":
        context = {
            "title": "Political Risk Assessment Report",
            "narrative": narrative,
            "model_section": model_text
        }
        export_path = os.path.join("exports", "political_risk_report.docx")
        template_path = os.path.join("templates", "report_template.docx")
        os.makedirs("exports", exist_ok=True)
        export_to_docx(export_path, template_path, context)
        with open(export_path, "rb") as file:
            st.download_button("📥 Download DOCX Report", file, file_name="Political_Risk_Assessment.docx")