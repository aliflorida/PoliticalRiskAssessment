from fpdf import FPDF

def export_to_pdf(filename, narrative, model_text, benchmark_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, "Political Risk Assessment Report")
    pdf.ln()
    pdf.multi_cell(0, 10, narrative)
    pdf.ln()
    pdf.multi_cell(0, 10, model_text)
    pdf.ln()
    if benchmark_text:
        pdf.multi_cell(0, 10, benchmark_text)
    pdf.output(filename)
    return filename