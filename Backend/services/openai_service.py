from openai import OpenAI
from regex import match
from models.exercise_models import Exercise
import json
import re

import os

client =  OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_exercises(level: str, n: int = 2) -> list[Exercise]:
    prompt = f"Generate {n} C1-level English exercises in JSON format. Each exercise must include: exercise_id (integer), type, level, instructions, and questions (each question must include question, answer_type: 'short_answer', 'essay' or 'multiple_choice'). No extra text."
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )
    
    content = response.choices[0].message.content
    print(content)
    match = re.search(r"\[.*\]", content, re.DOTALL)
    if match:
        json_str = match.group(0)
        data = json.loads(json_str)
    else:
        raise ValueError("No JSON found in content")
    
    # Limpieza y validación
    cleaned = []
    for ex in data:
        # Convertir exercise_id a entero si es posible
        if isinstance(ex.get("exercise_id"), str) and ex["exercise_id"].isdigit():
            ex["exercise_id"] = int(ex["exercise_id"])
        elif isinstance(ex.get("exercise_id"), str):
            # Extraer número de string tipo "c1_exercise_001"
            num = ''.join(filter(str.isdigit, ex["exercise_id"]))
            ex["exercise_id"] = int(num) if num else None

        # Validar preguntas
        for q in ex.get("questions", []):
            # Si falta 'question', intenta usar otro campo
            if "question" not in q:
                if "sentence" in q:
                    q["question"] = q["sentence"]
                elif "original" in q:
                    q["question"] = q["original"]
                else:
                    q["question"] = "No question text"
            # Validar answer_type
            if q.get("answer_type") not in ["short_answer", "essay", "multiple_choice"]:
                q["answer_type"] = "short_answer"  # Valor por defecto

        cleaned.append(ex)
    
    print(cleaned)
    return [Exercise(**ex) for ex in cleaned]
