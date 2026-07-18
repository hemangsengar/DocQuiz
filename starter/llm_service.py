import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_questions(text: str, num_questions: int = 5) -> list[dict]:
    """Generate multiple-choice questions from study notes via Groq."""
    # TODO: build the prompt, call client.chat.completions.create(...),
    # parse the JSON response into a list of dicts
    raise NotImplementedError
