"""The adaptive engine — the part that makes DocQuiz feel like a tutor.

Pure logic, no database, no web, no AI calls. It gets two plain inputs and
returns one question. That separation is deliberate: you can reason about
(and test) this file on its own.
"""

DIFFICULTY_ORDER = ["easy", "medium", "hard"]


def pick_next_question(unanswered: list[dict], topic_stats: dict[str, dict]) -> dict | None:
    """Pick the next question to ask, favouring weak topics.

    unanswered:  questions not yet answered (each has topic + difficulty).
    topic_stats: {topic: {"correct": n, "total": n}} from answered so far.

    Strategy:
    1. No questions left -> None (quiz over).
    2. Find the topic you're weakest in (lowest accuracy). A topic you
       haven't been asked about yet counts as 0.5 — neither strong nor weak.
    3. Within that topic, pick difficulty based on your accuracy there:
       below 50% -> easy, below 80% -> medium, otherwise -> hard.
    4. If no question of that exact difficulty is left in the topic, fall
       back through easy -> medium -> hard.
    """
    # TODO 8: implement the strategy above. Suggested shape:
    #   - if not unanswered: return None
    #   - write a small helper accuracy(topic) that returns 0.5 when the
    #     topic has no stats yet, else correct / total
    #   - weakest question = min(unanswered, key=lambda q: accuracy(q["topic"]))
    #   - candidates = every unanswered question in that weakest topic
    #   - desired difficulty from accuracy: <0.5 easy, <0.8 medium, else hard
    #   - loop [desired] + DIFFICULTY_ORDER, return first candidate that
    #     matches; final fallback: candidates[0]
    raise NotImplementedError
