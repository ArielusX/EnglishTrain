from pydantic import BaseModel, Field
from typing import List, Union, Optional, Literal

class Option(BaseModel):
    label: Optional[str] = None
    text: str

class Question(BaseModel):
    question: str
    options: Optional[List[Union[str, Option]]] = Field(default_factory=list)
    answer: Optional[str] = None
    answer_type: Literal["short_answer", "essay", "multiple_choice"] = "short_answer"
    keyword: Optional[str] = None  # añadido para reading_and_use_of_language3
    original: Optional[str] = None   # <-- para reading_and_use_of_language4
    second: Optional[str] = None     # <-- la segona frase amb el buit
    given: Optional[str] = None      # <-- la paraula donada (NEARLY, IN, etc.)
    stem: Optional[str] = None       # <-- text/stem for multiple-choice questions (ex5)

class Exercise(BaseModel):
    exercise_id: Optional[int] = None
    type: str
    level: Optional[str] = None
    instructions: str = ""  # default vacío para evitar validación fallida
    text: Optional[str] = None
    # <-- afegit per mostrar opcions A–F, A–D, etc. al generator
    options: List[Option] = Field(default_factory=list)
    questions: List[Question] = Field(default_factory=list)
    blanks: List[str] = Field(default_factory=list)
    audio_url: Optional[str] = None
    expected_output: Optional[str] = None
    hints: List[str] = Field(default_factory=list)
    passage: Optional[str] = None
    prompt: Optional[str] = None

