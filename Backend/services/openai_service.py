from openai import OpenAI
from regex import match
from models.exercise_models import Exercise
import json
import re

import os
 

def generate_exercises(level: str, exercise_type: str) -> list[Exercise]:
    if exercise_type == "reading_and_use_of_language1":
            prompt = f"""
    You are an English teacher creating exercises for students at level {level} (C1).
    Generate ONE 'reading_and_use_of_language1' exercise in JSON format.

    Requirements:
    - The text must have 8 gaps, each marked as [1], [2], ..., [8].
    - For each gap, provide a question with 4 options (one correct), and indicate the correct answer.
    - Use clear, exam-like phrasing.

    Use this structure:
    {{
    "type": "reading_and_use_of_language1",
    "instructions": "Fill each gap with the correct word. Choose from the four options.",
    "text": "... [1] ... [2] ...",
    "questions": [
        {{
        "question": "1",
        "options": [{{"text": "catch"}}, {{"text": "win"}}, {{"text": "achieve"}}, {{"text": "receive"}}],
        "answer": "win",
        "answer_type": "multiple_choice"
        }},
        // ...repeat for each gap...
    ],
    "hints": []
    }}

    Rules:
    - Only fill the fields that make sense for this type.
    - Leave irrelevant fields as empty lists or empty strings.
    - Return ONLY valid JSON, no markdown or explanations.
    """
    elif exercise_type == "reading_and_use_of_language2":
        prompt = f"""You are an English teacher creating exercises for students at level {level} (C1).
    Generate ONE 'reading_and_use_of_language2' exercise in JSON format.

    Requirements:
    - The text must have 8 gaps, each marked as [1], [2], ..., [8].
    - For each gap, provide the answer, the answer must be 1 word.
    - Use clear, exam-like phrasing.
    Don't use this, is to show what we expect:
            The truth is nobody really knows how language first began. Did we all start talking at around the same time 9 of the manner in which our brains had begun to develop?
            Although there is a lack of clear evidence, people have come up with various theories about the origins of language. One recent theory is that human beings have evolved in 10 a way that we are programmed for language from the moment of birth.
            In 11 words, language came about as a result of an evolutionary change in our brains at some stage.
            Language 12 may well be programmed into the brain but, 13 this, people still need stimulus from others around them. From studies, we know that 14 children are isolated from human contact and have not learnt to construct sentences before they are ten, it is doubtful they will ever do so. This research shows, if 15 else, that language is a social activity, not something invented 16 isolation.


    Use this structure:
    {{
    "type": "reading_and_use_of_language2",
    "instructions": "Fill each gap with the correct word.",
    "text": "... [1] ... [2] ...",
    "questions": [
        {{
        "question": "1",
        "answer": "a word",
        "answer_type": "fill_in_the_blank"
        }},
        // ...repeat for each gap...
    ],
    "hints": []
    }}

    Rules:
    - Only fill the fields that make sense for this type.
    - Leave irrelevant fields as empty lists or empty strings.
    - Return ONLY valid JSON, no markdown or explanations.
    """
    elif exercise_type == "reading_and_use_of_language3":
        prompt = f"""You are an English teacher creating exercises for students at level {level} (C1).
        Generate ONE 'reading_and_use_of_language3' exercise in JSON format.
        Requirements:
        - The text must have 8 gaps, each marked as [1], [2], ..., [8].
        - For each gap provide:
        - "question": the gap number as string (e.g. "17")
        - "keyword": a single word in CAPITALS that the student must use to form the correct answer
        - "answer": the correct word that fits the gap (one word or hyphenated as needed)
        - "answer_type": "short_answer"
        - Provide a "Keyword List" (but include the keywords also inside each question object).
        - Use clear, exam-like phrasing (like Cambridge-style word-formation).
        Don't use this, is to show what we expect:
        What are the abilities that a professional sports person needs? To guarantee that opponents can be 17 , speed, stamina and agility are essential, not to mention outstanding natural talent. Both a rigorous and comprehensive 18 regime and a highly nutritious diet are vital for top-level performance. It is carbohydrates, rather than proteins and fat, that provide athletes with the 19 they need to compete. This means that pasta is more 20 than eggs or meat. Such a diet enables them to move very energetically when required. Failure to follow a sensible diet can result in the 21 to maintain stamina.
        Regular training to increase muscular 22 is also a vital part of a professional’s regime, and this is 23 done by exercising with weights. Sports people are prone to injury but a quality training regime can ensure that the 24 of these can be minimised.
        Flag question 17
        Keyword List
        17. COME
        18. FIT
        19. ENDURE
        20. BENEFIT
        21. ABLE
        22. STRONG
        23. TYPE
        24. SEVERE
        Use this structure:
            {{
            "type": "reading_and_use_of_language3",
            "instructions": "For each question, use the word in CAPITALS on the right to form a word that fits in the gap.",
            "text": "... [1] ... [2] ...",
            "questions": [
                {{
                "question": "17",
                "keyword": "COME",
                "answer": "something",
                "answer_type": "short_answer"
                }},
                ...
            ],
            "hints": []
            }}

            Rules:
            - Return ONLY valid JSON, no markdown or explanations.
            - Only fill the fields that make sense for this type.
            """
    elif exercise_type == "reading_and_use_of_language4":
        prompt = f"""
            You are an English teacher creating C1 sentence-transformation exercises.
            Generate ONE 'reading_and_use_of_language4' exercise in JSON format.
            Requirements:
            - Create 6 questions numbered 25 to 30.
            - For each item provide an ORIGINAL sentence and a SECOND sentence with a gap to complete.
            - Provide the GIVEN WORD in CAPITALS that must appear in the student's answer.
            - Provide the CORRECT ANSWER (3-6 words including the given word) and set answer_type to \"short_answer\".
            Don't use this, is to show what we expect:
                For each question, complete the second sentence so that it means the same as the first. Do not change the word given. You must use between three and six words, including the word given.
                My brother now earns far less money than he did when he was younger.
                NEARLY
                My brother earns nearly as much now as he did when he was younger.

            Return exactly this structure (JSON only):
            {{
              "type": "reading_and_use_of_language4",
              "instructions": "For each question, complete the second sentence so that it means the same as the first. Do not change the word given. Use between three and six words, including the given word.",
              "text": "",
              "questions": [
                {{ "question": "25", "original": "My brother now earns far less money than he did when he was younger.", "second": "My brother ____ much now as he did when he was younger.", "given": "NEARLY", "answer": "earns nearly as much", "answer_type": "short_answer" }},
                ... (repeat for 26-30)
              ],
              "hints": []
            }}
            "Rules:- Return ONLY valid JSON, no markdown or explanations.- Use concise, exam-style language."
        """
    elif exercise_type == "reading_and_use_of_language5":
        prompt = f"""
            You are an English teacher creating C1 multiple-choice reading comprehension exercises.
            Generate ONE 'reading_and_use_of_language5' exercise in JSON format based on the provided stimulus.
            Requirements:
            - Provide a short stimulus / passage in the \"text\" field (this will be shown above questions).
            - Create 6 questions numbered 31 to 36.
            - Generate a decent text for a c1 level reading comprehension exercise. (minimum 300 words)
            - For each question include:
              - "question": the question number as a string, e.g. "31"
              - "stem": the question text (the question as the student sees it)
              - "options": an array of four objects: {{"text":"..."}}
              - "answer": the correct option letter (A, B, C or D) or the exact option text
              - "answer_type": "multiple_choice"

            Don't use this, is to show what we expect:
                Read the introduction below to a book about the history of colour. For each question, choose the correct answer.
                Stimulus for Questions 31–36
                Introduction to a book about the history of colour
                This book examines how the ever-changing role of colour in society has been reflected in manuscripts, stained glass, clothing, painting and popular culture. Colour is a natural phenomenon, of course, but it is also a complex cultural construct that resists generalization and, indeed, analysis itself. No doubt this is why serious works devoted to colour are rare, and rarer still are those that aim to study it in historical context. Many authors search for the universal or archetypal truths they imagine reside in colour, but for the historian, such truths do not exist. Colour is first and foremost a social phenomenon. There is no transcultural truth to colour perception, despite what many books based on poorly grasped neurobiology or – even worse – on pseudoesoteric pop psychology would have us believe. Such books unfortunately clutter the bibliography on the subject, and even do it harm.
                The silence of historians on the subject of colour, or more particularly their difficulty in conceiving colour as a subject separate from other historical phenomena, is the result of three different sets of problems. The first concerns documentation and preservation. We see the colours transmitted to us by the past as time has altered them and not as they were originally. Moreover, we see them under light conditions that often are entirely different from those known by past societies. And finally, over the decades we have developed the habit of looking at objects from the past in black-and-white photographs and, despite the current diffusion of colour photography, our ways of thinking about and reacting to these objects seem to have remained more or less black and white.
                The second set of problems concerns methodology. As soon as the historian seeks to study colour, he must grapple with a host of factors all at once: physics, chemistry, materials, and techniques of production, as well as iconography, ideology, and the symbolic meanings that colours convey. How to make sense of all of these elements? How can one establish an analytical model facilitating the study of images and coloured objects? No researcher, no method, has yet been able to resolve these problems, because among the numerous facts pertaining to colour, a researcher tends to select those facts that support his study and to conveniently forget those that contradict it. This is clearly a poor way to conduct research. And it is made worse by the temptation to apply to the objects and images of a given historical period information found in texts of that period. The proper method – at least in the first phase of analysis – is to proceed as do palaeontologists (who must study cave paintings without the aid of texts): by extrapolating from the images and the objects themselves a logic and a system based on various concrete factors such as the rate of occurrence of particular objects and motifs, their distribution and disposition. In short, one undertakes the internal structural analysis with which any study of an image or coloured object should begin.
                The third set of problems is philosophical: it is wrong to project our own conceptions and definitions of colour onto the images, objects and monuments of past centuries. Our judgements and values are not those of previous societies (and no doubt they will change again in the future). For the writer-historian looking at the definitions and taxonomy of colour, the danger of anachronism is very real. For example, the spectrum with its natural order of colours was unknown before the seventeenth century, while the notion of primary and secondary colours did not become common until the nineteenth century. These are not eternal notions but stages in the ever-changing history of knowledge.
                I have reflected on such issues at greater length in my previous work, so while the present book does address certain of them, for the most part it is devoted to other topics. Nor is it concerned only with the history of colour in images and artworks – in any case that area still has many gaps to be filled. Rather, the aim of this book is to examine all kinds of objects in order to consider the different facets of the history of colour and to show how far beyond the artistic sphere this history reaches. The history of painting is one thing; that of colour is another, much larger, question. Most studies devoted to the history of colour err in considering only the pictorial, artistic or scientific realms. But the lessons to be learned from colour and its real interest lie elsewhere.
                Questions 31–36
                31
                What problem regarding colour does the writer explain in the first paragraph?
                Our view of colour is strongly affected by changing fashion.
                Analysis is complicated by the bewildering number of natural colours.
                Colours can have different associations in different parts of the world.
                Certain popular books have dismissed colour as insignificant.
                Flag question 31
                32
                What is the first reason the writer gives for the lack of academic work on the history of colour?
                There are problems of reliability associated with the artefacts available.
                Historians have seen colour as being outside their field of expertise.
                Colour has been rather looked down upon as a fit subject for academic study.
                Very little documentation exists for historians to use.
                Flag question 32
                33
                The writer suggests that the priority when conducting historical research on colour is to
                ignore the interpretations of other modern day historians.
                focus one’s interest as far back as the prehistoric era.
                find some way of organising the mass of available data.
                relate pictures to information from other sources.
                Flag question 33
                34
                In the fourth paragraph, the writer says that the historian writing about colour should be careful
                not to analyse in an old-fashioned way.
                when making basic distinctions between key ideas.
                not to make unwise predictions.
                when using certain terms and concepts.
                Flag question 34
                35
                In the fifth paragraph, the writer says there needs to be further research done on
                the history of colour in relation to objects in the world around us.
                the concerns he has raised in an earlier publication.
                the many ways in which artists have used colour over the years.
                the relationship between artistic works and the history of colour.
                Flag question 35
                36
                An idea recurring in the text is that people who have studied colour have
                failed to keep up with scientific developments.
                not understood its global significance.
                found it difficult to be fully objective.
                been muddled about their basic aims
              
            Use this structure exactly (return ONLY valid JSON):
            {{
              "type": "reading_and_use_of_language5",
              "instructions": "Read the text and choose the correct answer for each question.",
              "text": "...",
              "questions": [
                {{ "question":"31", "stem":"...", "options":[{{"text":" ..."}},{{"text":" ..."}},{{"text":" ..."}},{{"text":" ..."}}], "answer":" ", "answer_type":"multiple_choice" }},
                ... repeat for 32-36 ...
              ]
            }},
            "hints": []

          Rules:
          - Return ONLY valid JSON, no markdown or explanations.
          - Use clear, exam-style language and plausible distractors."
        """
    elif exercise_type == "reading_and_use_of_language6":
        prompt = f"""
            You are an English teacher creating C1 multiple-choice exercises based on four short reviews (labelled A, B, C and D).
            Generate ONE 'reading_and_use_of_language6' exercise in JSON format.
            Requirements:
            - Put the four short reviews (labelled "A", "B", "C", "D") in the "text" field.\n'
            - Create 4 questions numbered 37 to 40.
            - For each question include: 
            - Each text must be at least 100 words long.
              "question" (e.g. "37"), "stem" (the question text),
              "options": [{{"text":"Reviewer A"}}, {{"text":"Reviewer B"}}, {{"text":"Reviewer C"}}, {{"text":"Reviewer D"}}],
              "answer": "A" (or full option text), "answer_type": "multiple_choice".

            Use this structure exactly and RETURN ONLY valid JSON (no markdown/explanations):\n"
            {{
              "type": "reading_and_use_of_language6",
              "instructions": "Read the four reviews A–D. For each question choose the reviewer that matches the statement.",
              "text": "A) ...\nB) ...\nC) ...\nD) ...",
              "questions": [
                {{ "question":"37", "stem":"...", "options":[{{"text":"Reviewer A"}},{{"text":"Reviewer B"}},{{"text":"Reviewer C"}},{{"text":"Reviewer D"}}], "answer":" ", "answer_type":"multiple_choice" }},
                ... repeat for 38-40 ...
              ]
            }},
            "hints": []
        """
    elif exercise_type == "reading_and_use_of_language7":
        prompt = f"""
            You are an English teacher creating C1 paragraph-matching (gapped text) exercises.
            Generate ONE 'reading_and_use_of_language7' exercise in VALID JSON only.
            Requirements:
            - Provide a text with six gaps, marked [41] ... [46].
            - Provide six short paragraphs as options labelled A–F in the field 'options' as objects {{"label":"A","text":"..."}}
            - Provide 'questions' array with six items like {{"question":"41","answer":"A","answer_type":"multiple_choice"}} (answers are letters A-F).
            - The text and paragraphs should be about a coherent topic and suitable for C1 level and each text needs to be 100 words minimum and the answers need to have 50 words minimum.
            Use this exact structure:
            {{
              "type": "reading_and_use_of_language7",
              "instructions": "Read the extract and choose the paragraph (A–F) which best fits each gap.",
              "text": "... [41] ... [42] ... [43] ... [44] ... [45] ... [46] ...",
              "options": [
                {{"label":"A","text":"..."}},
                {{"label":"B","text":"..."}},
                {{"label":"C","text":"..."}},
                {{"label":"D","text":"..."}},
                {{"label":"E","text":"..."}},
                {{"label":"F","text":"..."}}
              ],
              "questions": [
                {{"question":"41","answer":"A","answer_type":"multiple_choice"}},
                {{"question":"42","answer":"B","answer_type":"multiple_choice"}},
                {{"question":"43","answer":"C","answer_type":"multiple_choice"}},
                {{"question":"44","answer":"D","answer_type":"multiple_choice"}},
                {{"question":"45","answer":"E","answer_type":"multiple_choice"}},
                {{"question":"46","answer":"F","answer_type":"multiple_choice"}}
              ],
              "hints": []
            }}

            "Rules:- Return ONLY valid JSON, no markdown or explanations.- Use exam-style language; paragraphs A–F should be plausible distractors with one extra paragraph unused."
        """
    elif exercise_type == "reading_and_use_of_language8":
        # Career consultants multiple-choice (questions 47-56)
        prompt = f"""
            You are an English teacher creating C1 multiple-choice exercises based on five short 
            consultant comments (labelled A, B, C, D and E).
            Generate ONE 'reading_and_use_of_language8' exercise in JSON format.

            Requirements:
            - Put the five consultant texts (labelled \"A\", \"B\", \"C\", \"D\", \"E\") in the \"text\" field.
            - Create 10 questions numbered 47 to 56.
            - Every consultant text must be at least 100 words long.
            - For each question include:
              - "question": the question number as a string (e.g. "47")
              - "stem": the question text (short)
              - "options": an array of five objects: {{"text":"Consultant A"}}, {{"text":"Consultant B"}}, ...
              - "answer": the correct option letter ("A"-"E") or the exact option text
              - "answer_type": "multiple_choice"
            Use this structure exactly and RETURN ONLY valid JSON (no markdown/explanations):
            {{
              "type": "reading_and_use_of_language8",
              "instructions": "Read the five consultants. For each question choose the consultant that matches the statement.",
              "text": "A) ...\\n\\nB) ...\\n\\nC) ...\\n\\nD) ...\\n\\nE) ...",
              "questions": [
                {{ "question":"47", "stem":"...", "options":[{{"text":"Consultant A"}}, {{"text":"Consultant B"}}, {{"text":"Consultant C"}}, {{"text":"Consultant D"}}, {{"text":"Consultant E"}}], "answer":"D", "answer_type":"multiple_choice" }},
                ... repeat for 48-56 ...
              ],
              "hints": []
            }}
            "Rules:- Return ONLY valid JSON, no markdown or explanations.- Use concise, exam-style language and plausible distractors."
        """
    else:
        prompt = f"""You are an English teacher creating exercises for students at level {level} (C1).
        Generate ONE exercise of type "{exercise_type}" in JSON format.

    Use this global structure:
    {{
    "type": "{exercise_type}",
    "title": "...",
    "instructions": "...",
    "text": "...",
    "questions": [],
    "blanks": [],
    "audio_url": "",
    "expected_output": "",
    "hints": []
    }}

    Rules:
    - Only fill the fields that make sense for the given type.
    - Leave irrelevant fields as empty lists or empty strings.
    - Use clear, exam-like phrasing.
    - Return ONLY valid JSON, no markdown or explanations."""
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )
    
    content = response.choices[0].message.content
    print(content)
    # Extraer el bloque JSON (ya sea lista o dict)
    match = re.search(r"(\{.*\}|\[.*\])", content, re.DOTALL)
    if not match:
        raise ValueError("No JSON found in content")

    json_str = match.group(1)

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        print("❌ Error parsing JSON:", e)
        print("Raw content:", content)
        raise

    # Si el resultado es un solo objeto, conviértelo en lista
    if isinstance(data, dict):
        data = [data]

    
    # Limpieza y validación
    cleaned = []
    for ex in data:
        ex.setdefault("instructions", "")
        ex.setdefault("text", "")
        ex.setdefault("questions", [])
        ex.setdefault("hints", [])
        if ex.get("type","").endswith("language7"):
            opts = ex.get("options", [])
            normalized = []
            for i, opt in enumerate(opts):
                if isinstance(opt, str):
                    label = chr(65 + i) if i < 26 else str(i+1)
                    normalized.append({"label": label, "text": opt})
                elif isinstance(opt, dict):
                    label = opt.get("label") or (chr(65 + i) if i < 26 else str(i+1))
                    text = opt.get("text") or ""
                    normalized.append({"label": label, "text": text})
                else:
                    # fallback to string conversion
                    label = chr(65 + i) if i < 26 else str(i+1)
                    normalized.append({"label": label, "text": str(opt)})
            ex["options"] = normalized
        # normalize exercise_id (existing code) ...
        # existing normalization loop...
        for q in ex.get("questions", []):
            if "question" not in q:
                q["question"] = str(q.get("id", ""))

            # ensure stem for MCQ types 5,6,8
            if ex.get("type", "").endswith("language5") or ex.get("type", "").endswith("language6") or ex.get("type", "").endswith("language8"):
                q.setdefault("stem", (q.get("stem") or q.get("text") or q.get("question_text") or ""))

            # map possible "given" field to keyword (used by other types)
            if "given" in q and isinstance(q["given"], str):
                q["keyword"] = q["given"].strip().upper()
            else:
                q["keyword"] = (q.get("keyword") or "").strip().upper()

            # normalize answer_type
            atype = (q.get("answer_type") or "").lower()
            if atype == "fill_in_the_blank":
                q["answer_type"] = "short_answer"
            elif atype not in ["short_answer", "essay", "multiple_choice"]:
                q["answer_type"] = "short_answer"

        cleaned.append(ex)
    
    print(cleaned)
    for ex in cleaned:
        for q in ex.get("questions", []):
            if "options" in q and all(isinstance(opt, str) for opt in q["options"]):
                q["options"] = [{"text": opt} for opt in q["options"]]

    return [Exercise(**ex) for ex in cleaned]



