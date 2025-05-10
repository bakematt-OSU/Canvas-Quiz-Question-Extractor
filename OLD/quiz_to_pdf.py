from fpdf import FPDF
from quiz_models import Quiz
import os

def export_quiz_to_pdf(quiz: Quiz, output_path: str):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.set_font("Arial", style='B', size=14)
    pdf.cell(200, 10, f"Quiz: {quiz.title}", ln=True, align='C')
    pdf.ln(10)

    for question in quiz.questions:
        pdf.set_font("Arial", style='B', size=12)
        pdf.multi_cell(0, 10, f"{question.number}: {question.text}")

        if question.images:
            for img_path in question.images:
                if os.path.exists(img_path):
                    pdf.image(img_path, w=100)

        pdf.set_font("Arial", size=12)
        for idx, option in enumerate(question.options):
            prefix = "[x]" if option.is_selected else "[ ]"
            pdf.multi_cell(0, 8, f"{prefix} {option.text}")
            if option.images:
                for img in option.images:
                    if os.path.exists(img):
                        pdf.image(img, w=90)

        pdf.ln(5)

    pdf.output(output_path)
    print(f"✅ PDF saved to {output_path}")
