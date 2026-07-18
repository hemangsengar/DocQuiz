import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def _select_content(chunks: list[str], budget: int = 12000) -> str:
    """Pick content spread evenly across all chunks so multi-topic notes
    aren't reduced to just their opening section."""
    # TODO: if the combined chunks fit in `budget`, join them all with "\n\n".
    # Otherwise, give each chunk an equal share of the budget (budget // len(chunks))
    # and join the truncated pieces with "\n\n".
    raise NotImplementedError


def generate_questions(chunks: list[str], num_questions: int = 5) -> list[dict]:
    """Generate multiple-choice questions covering all topics in the notes via Groq."""
    # TODO: bump num_questions up to at least len(chunks) so every section gets
    # at least one question, build the prompt (mention notes may cover multiple
    # topics/sections), call client.chat.completions.create(...), parse the
    # JSON response into a list of dicts
    raise NotImplementedError
