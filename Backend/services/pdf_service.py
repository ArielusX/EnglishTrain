from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_exercise_pdf(exercises, output_path="exercises.pdf"):
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    content = []

    for ex in exercises:
        content.append(Paragraph(f"<b>Exercise {ex.exercise_id} - {ex.type}</b>", styles['Heading2']))
        content.append(Paragraph(ex.instructions, styles['Normal']))
        if ex.passage:
            content.append(Paragraph(f"<i>{ex.passage}</i>", styles['Normal']))
        if ex.questions:
            for q in ex.questions:
                content.append(Paragraph(f"• {q.question}", styles['Normal']))
        if ex.prompt:
            content.append(Paragraph(ex.prompt, styles['Normal']))
        content.append(Spacer(1, 20))

    doc.build(content)
    return output_path
