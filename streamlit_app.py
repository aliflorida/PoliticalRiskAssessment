import streamlit as st
from models.prince_model import run_prince_model
from models.icrg_model import run_icrg_model
from models.wgi_model import run_wgi_model
from utils.model_selector import select_models
from utils.narrative import generate_full_narrative
from utils.export_utils import export_to_docx
from utils.benchmark_utils import compare_benchmark
import os

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
    benchmark_country = st.text_input("Benchmark Against Another Country (optional)")
    export_format = st.selectbox("Export Report As", ["DOCX"])
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

    if benchmark_country:
        st.subheader("Benchmark Comparison")
        for model in models:
            if model == "PRINCE":
                benchmark_outputs.append(run_prince_model(benchmark_country, industry, long_term))
            elif model == "ICRG":
                benchmark_outputs.append(run_icrg_model(benchmark_country, industry, long_term))
            elif model == "WGI":
                benchmark_outputs.append(run_wgi_model(benchmark_country, industry, long_term))

        comparison = compare_benchmark(base_outputs, benchmark_outputs)
        for item in comparison:
            st.write(f"{item['model']}: Base Score = {item['base_score']} vs Benchmark Score = {item['benchmark_score']} → {item['risk_higher']} higher risk")

    for result in base_outputs:
        st.subheader(f"{result['model']} Model")
        st.write(f"**Score**: {result['score']} / 100")
        st.write("**Macro Risk**:", result["macro"])
        st.write("**Micro Risk**:", result["micro"])
        st.write("**Sovereign Risk**:", result["sovereign"])
        st.write("**Recommendations:**")
        st.markdown(result["recommendations"])

    if export_format == "DOCX":
        export_path = os.path.join("exports", "political_risk_report.docx")
        export_to_docx(export_path, narrative, base_outputs)
        with open(export_path, "rb") as file:
            st.download_button("📥 Download DOCX Report", file, file_name="Political_Risk_Assessment.docx")