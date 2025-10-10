from pydantic import BaseModel
from typing import List, Literal

class Question(BaseModel):
    question: str
    answer_type: Literal["short_answer", "essay", "multiple_choice"]

class Exercise(BaseModel):
    exercise_id: int
    type: str
    level: str
    instructions: str
    passage: str | None = None
    questions: List[Question] | None = None
    prompt: str | None = None
    word_limit: int | None = None
