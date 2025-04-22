import streamlit as st
import os
from models.prince_model import run_prince_model
from models.icrg_model import run_icrg_model
from models.wgi_model import run_wgi_model
from utils.model_selector import select_models
from utils.narrative import generate_full_narrative
from utils.docxtpl_exporter import export_to_docx
from utils.pdf_exporter import export_to_pdf
from utils.benchmark_utils import compare_benchmark

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
    benchmark_country = st.text_input("Benchmark Country (optional)")
    export_format = st.selectbox("Export Report As", ["DOCX", "PDF"])
    audiences = st.multiselect("Audience", ["Client", "Analyst Team", "Political Risk Group"])

if st.button("Generate Assessment"):
    narrative = generate_full_narrative(target_country, company_name, investment_type, industry, broad_risk, future_concerns, recommendation_type)
    st.header("Narrative Report")
    st.markdown(narrative)

    models = select_models(investment_type, industry, long_term)
    base_outputs, benchmark_outputs = [], []

    for model in models:
        if model == "PRINCE":
            base_outputs.append(run_prince_model(target_country, industry, long_term))
        elif model == "ICRG":
            base_outputs.append(run_icrg_model(target_country, industry, long_term))
        elif model == "WGI":
            base_outputs.append(run_wgi_model(target_country, industry, long_term))

    model_text = ""
    for result in base_outputs:
        model_text += f"\n{result['model']} Model\nScore: {result['score']}\n"
        model_text += f"Macro Risk: {', '.join(result['macro'])}\n"
        model_text += f"Micro Risk: {', '.join(result['micro'])}\n"
        model_text += f"Sovereign Risk: {', '.join(result['sovereign'])}\n"
        model_text += f"Recommendations: {result['recommendations']}\n"

    benchmark_text = ""
    if benchmark_country:
        for model in models:
            if model == "PRINCE":
                benchmark_outputs.append(run_prince_model(benchmark_country, industry, long_term))
            elif model == "ICRG":
                benchmark_outputs.append(run_icrg_model(benchmark_country, industry, long_term))
            elif model == "WGI":
                benchmark_outputs.append(run_wgi_model(benchmark_country, industry, long_term))
        comparison = compare_benchmark(base_outputs, benchmark_outputs)
        for cmp in comparison:
            benchmark_text += f"{cmp['model']} → {cmp['base_score']} (Base) vs {cmp['benchmark_score']} (Benchmark). Higher risk: {cmp['risk_higher']}\n"

    if export_format == "DOCX":
        ctx = {
            "title": "Political Risk Assessment Report",
            "narrative": narrative,
            "model_section": model_text,
            "benchmark_section": benchmark_text
        }
        docx_path = os.path.join("exports", "report.docx")
        template_path = os.path.join("templates", "report_template.docx")
        os.makedirs("exports", exist_ok=True)
        export_to_docx(docx_path, template_path, ctx)
        with open(docx_path, "rb") as f:
            st.download_button("📥 Download DOCX Report", f, file_name="Political_Risk_Report.docx")

    elif export_format == "PDF":
        pdf_path = os.path.join("exports", "report.pdf")
        os.makedirs("exports", exist_ok=True)
        export_to_pdf(pdf_path, narrative, model_text, benchmark_text)
        with open(pdf_path, "rb") as f:
            st.download_button("📥 Download PDF Report", f, file_name="Political_Risk_Report.pdf")