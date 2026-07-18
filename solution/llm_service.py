import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_questions(text: str, num_questions: int = 5) -> list[dict]:
    """Generate multiple-choice questions from study notes via Groq."""
    prompt = f"""You are an expert teacher. Generate {num_questions} multiple-choice questions
from the following study notes.

For each question return: question, options (A, B, C, D), correct_answer (letter),
explanation, difficulty (easy/medium/hard), topic.

Return ONLY a JSON object with a "questions" array.

Notes:
{text[:12000]}
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        response_format={"type": "json_object"},
    )
    data = json.loads(response.choices[0].message.content)
    return data["questions"]
