from fastapi import FastAPI, Response
from services.openai_service import generate_exercises
from exercise_generators.reading_and_use_of_english_generator import generate_reading_and_use_of_language

app = FastAPI(title="English C1 Exercise Generator")

@app.get("/generate_pdf/")
def generate_pdf(level: str = "C1", exercise_type: str = "reading_and_use_of_language8"):
    exercises = generate_exercises(level, exercise_type)
    pdf_path = generate_reading_and_use_of_language(exercises)
    with open(pdf_path, "rb") as f:
        pdf_data = f.read()
    filename = f"exercise_{exercise_type}_{level}.pdf"
    headers = {"Content-Disposition": f"attachment; filename={filename}"}

    return Response(content=pdf_data, media_type="application/pdf", headers=headers)
