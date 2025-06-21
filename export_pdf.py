from fpdf import FPDF
from datetime import datetime

def export_to_pdf(text, filename="final_output.pdf", title="Final Chapter Version"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Encode title to latin-1 safely (replacing unsupported characters)
    safe_title = title.encode("latin-1", "replace").decode("latin-1")
    pdf.set_font("Arial", "B", 16)
    pdf.multi_cell(0, 10, safe_title, align="C")
    pdf.ln()

    pdf.set_font("Arial", "", 12)

    for line in text.split("\n"):
        safe_line = line.encode("latin-1", "replace").decode("latin-1")
        pdf.multi_cell(0, 10, safe_line)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"{filename.replace('.pdf', '')}_{timestamp}.pdf"
    pdf.output(output_path)
    print(f"✅ Exported final version to PDF: {output_path}")
