from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_reading_and_use_of_language(exercises, output_path="exercises.pdf"):
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    content = []

    for ex in exercises:
        content.append(Paragraph(f"<b>Exercise {ex.exercise_id} - {ex.type}</b>", styles['Heading2']))
        content.append(Paragraph(ex.instructions, styles['Normal']))
        content.append(Spacer(1,8))
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
        elif ex.type == "reading_and_use_of_language2":
            # Mostrar el text amb els buits
            if ex.text:
                content.append(Paragraph(ex.text, styles['Normal']))
            # Per cada buit mostrem una línia en blanc on l'alumne ha d'escriure la paraula
            if ex.questions:
                for q in ex.questions:
                    # Mostrar "Gap X: _________" sense revelar la resposta
                    blank_line = "_" * 30
                    content.append(Paragraph(f"Gap {q.question}: {blank_line}", styles['Normal']))
                    content.append(Spacer(1, 8))
            if ex.hints:
                content.append(Paragraph(f"Hints: {', '.join(ex.hints)}", styles['Normal']))

        # Fill in the blanks
        elif ex.type == "reading_and_use_of_language3":
            # text with gaps
            if ex.text:
                content.append(Paragraph(ex.text, styles['Normal']))
                content.append(Spacer(1, 8))

            # show blanks for students
            if ex.questions:
                for q in ex.questions:
                    # line for student to write the formed word
                    blank_line = "_" * 30
                    content.append(Paragraph(f"Gap {q.question}: {blank_line}", styles['Normal']))
                    content.append(Spacer(1, 6))

            # Keyword list (numbers + CAPITAL keywords)
            if ex.questions:
                content.append(Spacer(1, 8))
                content.append(Paragraph("Keyword List", styles['Heading3']))
                for q in ex.questions:
                    kw = getattr(q, "keyword", "") if hasattr(q, "keyword") else (q.get("keyword") if isinstance(q, dict) else "")
                    # safe fallback if kw is empty: show question number only
                    content.append(Paragraph(f"{q.question}. {kw}", styles['Normal']))
                content.append(Spacer(1, 10))

            if ex.hints:
                content.append(Paragraph(f"Hints: {', '.join(ex.hints)}", styles['Normal']))

        # Writing exercise
        elif ex.type == "reading_and_use_of_language4":
            # If there's a shared passage/text show it (optional)
            if ex.text:
                content.append(Paragraph(ex.text, styles['Normal']))
                content.append(Spacer(1, 8))

            # For each question show the original sentence, the second sentence with a gap, and the GIVEN word
            if ex.questions:
                for q in ex.questions:
                    qnum = getattr(q, "question", "")
                    original = getattr(q, "original", "") or getattr(q, "text", "")
                    second = getattr(q, "second", "") or getattr(q, "second_sentence", "")
                    given = (getattr(q, "given", None) or getattr(q, "keyword", None) or "").strip().upper()

                    # Question header
                    if qnum:
                        content.append(Paragraph(f"<b>Question {qnum}</b>", styles['Heading4']))

                    # Show original sentence
                    if original:
                        content.append(Paragraph(f"Original: {original}", styles['Normal']))

                    # Show second sentence with blank (if provided show as is, otherwise show placeholder)
                    if second:
                        content.append(Paragraph(f"Complete: {second}", styles['Normal']))
                    else:
                        content.append(Paragraph("Complete: ___________________________", styles['Normal']))

                    # Show GIVEN WORD
                    if given:
                        content.append(Paragraph(f"Word given: {given}", styles['Normal']))

                    # Blank for student answer
                    blank_line = "_" * 60
                    content.append(Paragraph(f"Answer: {blank_line}", styles['Normal']))
                    content.append(Spacer(1, 10))

            if ex.hints:
                content.append(Paragraph(f"Hints: {', '.join(ex.hints)}", styles['Normal']))
        elif ex.type == "reading_and_use_of_language5":
            # Show stimulus / passage
            if ex.text:
                content.append(Paragraph("<b>Stimulus</b>", styles['Heading3']))
                content.append(Paragraph(ex.text, styles['Normal']))
                content.append(Spacer(1, 10))

            # Render the 6 MCQs (31-36)
            if ex.questions:
                for q in ex.questions:
                    qnum = getattr(q, "question", "")
                    stem = getattr(q, "stem", "") or ""
                    # Header
                    if qnum:
                        content.append(Paragraph(f"<b>Question {qnum}</b>", styles['Heading4']))
                    # Question stem
                    if stem:
                        content.append(Paragraph(stem, styles['Normal']))
                    # Options (A-D)
                    if q.options:
                        opts_lines = []
                        for i, opt in enumerate(q.options):
                            text = opt.text if hasattr(opt, "text") else (opt.get("text") if isinstance(opt, dict) else str(opt))
                            label = chr(65 + i)
                            opts_lines.append(f"{label}) {text}")
                        content.append(Paragraph("\n".join(opts_lines), styles['Normal']))
                    # small gap
                    content.append(Spacer(1, 8))
            if ex.hints:
                content.append(Paragraph(f"Hints: {', '.join(ex.hints)}", styles['Normal']))
        elif ex.type == "reading_and_use_of_language6":
            # show the four reviews stimulus (A, B, C, D) as provided in ex.text
            if ex.text:
                content.append(Paragraph("<b>Reviews (A–D)</b>", styles['Heading3']))
                # ex.text expected to contain labels "A) ...", "B) ...", etc.
                content.append(Paragraph(ex.text, styles['Normal']))
                content.append(Spacer(1, 10))

            # Render the 4 MCQs (37-40)
            if ex.questions:
                for q in ex.questions:
                    qnum = getattr(q, "question", "")
                    stem = getattr(q, "stem", "") or ""

                    if qnum:
                        content.append(Paragraph(f"<b>Question {qnum}</b>", styles['Heading4']))
                    if stem:
                        content.append(Paragraph(stem, styles['Normal']))

                    # Options should be Reviewer A-D; display labels A) Reviewer A, etc.
                    if q.options:
                        opts_lines = []
                        for i, opt in enumerate(q.options):
                            # option may be an object with text or a string
                            if hasattr(opt, "text"):
                                opt_text = opt.text
                            elif isinstance(opt, dict):
                                opt_text = opt.get("text", "")
                            else:
                                opt_text = str(opt)
                            label = chr(65 + i)
                            # Keep option short: show reviewer label or the provided text
                            opts_lines.append(f"{label}) {opt_text}")
                        content.append(Paragraph("\n".join(opts_lines), styles['Normal']))

                    content.append(Spacer(1, 8))
            if ex.hints:
                content.append(Paragraph(f"Hints: {', '.join(ex.hints)}", styles['Normal']))
        elif ex.type == "reading_and_use_of_language7":
            # show text with gaps
            if ex.text:
                content.append(Paragraph(ex.text, styles['Normal']))
                content.append(Spacer(1, 12))

            # show option paragraphs labelled A-F
            if getattr(ex, "options", None):
                content.append(Paragraph("<b>Options</b>", styles['Heading3']))
                for opt in ex.options:
                    # opt may be dict or pydantic Option; handle both
                    label = getattr(opt, "label", None) or (opt.get("label") if isinstance(opt, dict) else "")
                    text = getattr(opt, "text", None) or (opt.get("text") if isinstance(opt, dict) else str(opt))
                    content.append(Paragraph(f"{label}) {text}", styles['Normal']))
                    content.append(Spacer(1, 6))
                content.append(Spacer(1, 10))

            # render questions 41-46: student writes letter
            if ex.questions:
                for q in ex.questions:
                    qnum = getattr(q, "question", None) or (q.get("question") if isinstance(q, dict) else "")
                    if qnum:
                        content.append(Paragraph(f"<b>Question {qnum}</b>", styles['Heading4']))
                        # space to write the letter
                        content.append(Paragraph("Answer: ____________________", styles['Normal']))
                        content.append(Spacer(1, 8))

            if ex.hints:
                content.append(Paragraph(f"Hints: {', '.join(ex.hints)}", styles['Normal']))
        if ex.type == "reading_and_use_of_language7":
            if ex.text:
                content.append(Paragraph(ex.text, styles['Normal']))
                content.append(Spacer(1, 12))
            if getattr(ex, "options", None):
                content.append(Paragraph("<b>Options</b>", styles['Heading3']))
                for opt in ex.options:
                    label = getattr(opt, "label", None) or (opt.get("label") if isinstance(opt, dict) else "")
                    text = getattr(opt, "text", None) or (opt.get("text") if isinstance(opt, dict) else str(opt))
                    content.append(Paragraph(f"{label}) {text}", styles['Normal']))
                    content.append(Spacer(1, 6))
                content.append(Spacer(1, 10))
            if ex.questions:
                for q in ex.questions:
                    qnum = getattr(q, "question", None) or (q.get("question") if isinstance(q, dict) else "")
                    if qnum:
                        content.append(Paragraph(f"<b>Question {qnum}</b>", styles['Heading4']))
                        content.append(Paragraph("Answer: ____________________", styles['Normal']))
                        content.append(Spacer(1, 8))

        # Consultants MCQ -> reading_and_use_of_language8
        elif ex.type == "reading_and_use_of_language8":
            # show stimulus with the five consultants labelled A–E
            if ex.text:
                content.append(Paragraph("<b>Stimulus: Consultants A–E</b>", styles['Heading3']))
                # keep formatting line breaks in ex.text
                content.append(Paragraph(ex.text.replace("\n\n", "<br/><br/>"), styles['Normal']))
                content.append(Spacer(1, 10))

            # Render the 10 MCQs (47-56)
            if ex.questions:
                for q in ex.questions:
                    qnum = getattr(q, "question", "") or (q.get("question") if isinstance(q, dict) else "")
                    stem = getattr(q, "stem", "") or (q.get("stem") if isinstance(q, dict) else "")
                    if qnum:
                        content.append(Paragraph(f"<b>Question {qnum}</b>", styles['Heading4']))
                    if stem:
                        content.append(Paragraph(stem, styles['Normal']))
                    # Options (Consultant A–E)
                    if ex.options:
                        opts_lines = []
                        for i, opt in enumerate(ex.options):
                            text = getattr(opt, "text", None) or (opt.get("text") if isinstance(opt, dict) else str(opt))
                            label = chr(65 + i)
                            opts_lines.append(f"{label}) {text}")
                        # use newline separation (ReportLab Paragraph accepts \n)
                        content.append(Paragraph("\n".join(opts_lines), styles['Normal']))
                    content.append(Spacer(1, 8))
        # Default fallback for other types
        else:
            if ex.text:
                content.append(Paragraph(ex.text, styles['Normal']))
                content.append(Spacer(1,8))
            if ex.questions:
                for q in ex.questions:
                    content.append(Paragraph(f"• {q.question}", styles['Normal']))
                    content.append(Spacer(1,6))
            if ex.prompt:
                content.append(Paragraph(ex.prompt, styles['Normal']))
            if ex.hints:
                content.append(Paragraph(f"Hints: {', '.join(ex.hints)}", styles['Normal']))

        content.append(Spacer(1, 20))

    doc.build(content)
    return output_path
