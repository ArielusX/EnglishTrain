from fastapi import FastAPI, Response
from services.openai_service import generate_exercises
from services.pdf_service import create_exercise_pdf

app = FastAPI(title="English C1 Exercise Generator")

@app.get("/generate_pdf/")
def generate_pdf(level: str = "C1"):
    exercises = generate_exercises(level)
    pdf_path = create_exercise_pdf(exercises)
    with open(pdf_path, "rb") as f:
        pdf_data = f.read()
    return Response(content=pdf_data, media_type="application/pdf")
