import streamlit as st
import os
import pandas as pd
import unicodedata
from utils.narrative import generate_full_report

# Placeholder model simulation
def run_prince_model():
    return {
        "model": "PRINCE",
        "score": 65,
        "macro": ["Regulatory burden", "Policy inconsistency"],
        "micro": ["Bureaucratic delays", "Elite capture"],
        "sovereign": ["Judicial inefficiency"],
        "recommendations": "Engage local advisors, negotiate arbitration fallback, monitor reform cycles."
    }

# PDF Export Function with Unicode Fix
def export_to_pdf(path, narrative_text):
    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in narrative_text.split("\n"):
        clean_line = unicodedata.normalize('NFKD', line).encode('latin-1', 'ignore').decode('latin-1')
        pdf.multi_cell(0, 10, clean_line)
    pdf.output(path)

# App Layout
st.set_page_config(page_title="Political Risk Assessment Tool", layout="wide")
st.title("📊 Political Risk Assessment Tool")

with st.sidebar:
    target_country = st.text_input("Target Country")
    home_country = st.text_input("Home Country")
    company_name = st.text_input("Company Name")
    investment_type = st.selectbox("Type of Investment", ["Market Entry", "Joint Venture", "Acquisition", "Infrastructure"])
    industry = st.text_input("Industry Sector")
    broad_risk = st.text_area("Broad Political Risk Concerns")
    future_concerns = st.text_area("Specific Forecast Risks")
    recommendation_type = st.selectbox("Recommendation Type", ["Go / No-Go", "Timing Advice", "Mitigation Plan"])

if st.button("Generate Report"):
    model_outputs = [run_prince_model()]
    full_report = generate_full_report(
        target_country,
        company_name,
        investment_type,
        industry,
        broad_risk,
        future_concerns,
        recommendation_type,
        model_outputs
    )

    st.header("📘 Political Risk Report")
    st.markdown(full_report)

    st.subheader("📊 Model Table: PRINCE")
    df = pd.DataFrame({
        "Category": ["Macro", "Micro", "Sovereign"],
        "Variables": [
            ", ".join(model_outputs[0]["macro"]),
            ", ".join(model_outputs[0]["micro"]),
            ", ".join(model_outputs[0]["sovereign"])
        ],
        "Recommendations": [model_outputs[0]["recommendations"]] * 3
    })
    st.table(df)

    # PDF Export
    pdf_path = os.path.join("exports", "political_risk_report.pdf")
    os.makedirs("exports", exist_ok=True)
    export_to_pdf(pdf_path, full_report)
    with open(pdf_path, "rb") as f:
        st.download_button("📥 Download Full Report (PDF)", f, file_name="Political_Risk_Report.pdf")