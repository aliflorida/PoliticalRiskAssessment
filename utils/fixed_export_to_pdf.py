from fpdf import FPDF
import unicodedata

def export_to_pdf(path, narrative_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in narrative_text.split("\n"):
        # Normalize to remove any non-latin1 characters
        clean_line = unicodedata.normalize('NFKD', line).encode('latin-1', 'ignore').decode('latin-1')
        pdf.multi_cell(0, 10, clean_line)
    pdf.output(path)