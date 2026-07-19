import tempfile
from pathlib import Path

from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

import db
from adaptive import pick_next_question
from pdf_service import extract_text_from_pdf, chunk_text
from llm_service import generate_questions

app = FastAPI(title="DocQuiz")
db.init_db()

STATIC_DIR = Path(__file__).parent / "static"


class AnswerIn(BaseModel):
    question_id: int
    selected: str  # "A" | "B" | "C" | "D"


@app.get("/")
def home():
    """Serve the frontend — one HTML file, no build step."""
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/upload")
async def upload_pdf(file: UploadFile):
    """PDF in → questions in the database. The whole Day-1 engine, behind
    one endpoint."""
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Please upload a PDF file")

    # UploadFile is bytes in memory; pdfplumber wants a file on disk.
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    # TODO 6: run the engine, store the result. Four steps:
    #   1. text = extract_text_from_pdf(tmp_path)
    #      (if text is empty: raise HTTPException(400, "No text found in PDF"))
    #   2. chunks = chunk_text(text)
    #   3. questions = generate_questions(chunks)
    #   4. db.clear_quiz(), then count = db.save_questions(questions)
    # Finally: return {"questions_saved": count}
    raise NotImplementedError


@app.get("/quiz/next")
def next_question():
    """Ask the adaptive engine what to serve. Note what we DON'T send the
    browser: correct_answer and explanation stay server-side — never trust
    the client."""
    question = pick_next_question(db.get_unanswered_questions(), db.get_topic_stats())
    if question is None:
        return {"done": True}
    return {
        "done": False,
        "id": question["id"],
        "question": question["question"],
        "options": question["options"],
        "difficulty": question["difficulty"],
        "topic": question["topic"],
    }


@app.post("/answer")
def submit_answer(answer: AnswerIn):
    """Check the answer server-side, record it, reveal the explanation."""
    # TODO 7: three steps:
    #   1. question = db.get_question(answer.question_id)
    #      (if None: raise HTTPException(status_code=404, detail="Question not found"))
    #   2. is_correct = answer.selected.upper() == question["correct_answer"].upper()
    #      then db.record_answer(answer.question_id, answer.selected.upper(), is_correct)
    #   3. return {"correct": is_correct,
    #              "correct_answer": question["correct_answer"],
    #              "explanation": question["explanation"]}
    raise NotImplementedError


@app.get("/progress")
def progress():
    """Per-topic accuracy plus overall counts — feeds the progress bar."""
    stats = db.get_topic_stats()
    total_questions = len(db.get_all_questions())
    answered = sum(s["total"] for s in stats.values())
    return {
        "total_questions": total_questions,
        "answered": answered,
        "topics": stats,
    }
