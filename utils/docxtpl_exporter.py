from docxtpl import DocxTemplate

def export_to_docx(filename, template_path, context):
    doc = DocxTemplate(template_path)
    doc.render(context)
    doc.save(filename)
    return filename