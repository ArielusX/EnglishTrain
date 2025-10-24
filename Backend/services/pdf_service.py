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

        # Reading exercise
        if ex.type in ["reading_and_use_of_language", "reading_and_use_of_language1"]:
            if ex.text:
                content.append(Paragraph(ex.text, styles['Normal']))
            if ex.questions:
                for q in ex.questions:
                    opts = ""
                    if q.options:
                        opts = "\n".join([f"{chr(65+i)}) {opt.text}" for i, opt in enumerate(q.options)])
                    content.append(Paragraph(f"Gap {q.question}:\n{opts}", styles['Normal']))
                    content.append(Spacer(1, 10))  # <-- línia en blanc entre gaps
            if ex.hints:
                content.append(Paragraph(f"Hints: {', '.join(ex.hints)}", styles['Normal']))

        # Listening exercise
        elif ex.type == "listening":
            if ex.audio_url:
                content.append(Paragraph(f"Audio: {ex.audio_url}", styles['Normal']))
            if ex.questions:
                for q in ex.questions:
                    content.append(Paragraph(f"• {q.question}", styles['Normal']))
            if ex.hints:
                content.append(Paragraph(f"Hints: {', '.join(ex.hints)}", styles['Normal']))

        # Fill in the blanks
        elif ex.type == "fill_in_the_blanks":
            if ex.text:
                content.append(Paragraph(ex.text, styles['Normal']))
            if ex.blanks:
                content.append(Paragraph(f"Blanks: {', '.join(ex.blanks)}", styles['Normal']))
            if ex.hints:
                content.append(Paragraph(f"Hints: {', '.join(ex.hints)}", styles['Normal']))

        # Writing exercise
        elif ex.type == "writing":
            if ex.prompt:
                content.append(Paragraph(f"Prompt: {ex.prompt}", styles['Normal']))
            if ex.expected_output:
                content.append(Paragraph(f"Expected Output: {ex.expected_output}", styles['Normal']))
            if ex.hints:
                content.append(Paragraph(f"Hints: {', '.join(ex.hints)}", styles['Normal']))

        # Default fallback for other types
        else:
            if ex.text:
                content.append(Paragraph(ex.text, styles['Normal']))
            if ex.questions:
                for q in ex.questions:
                    content.append(Paragraph(f"• {q.question}", styles['Normal']))
            if ex.prompt:
                content.append(Paragraph(ex.prompt, styles['Normal']))
            if ex.hints:
                content.append(Paragraph(f"Hints: {', '.join(ex.hints)}", styles['Normal']))

        content.append(Spacer(1, 20))

    doc.build(content)
    return output_path
