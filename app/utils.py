import requests


def get_question(number: int) -> dict:
    url = f"https://jservice.io/api/random?count={number}"
    res = requests.get(url).json()

    questions = [
        {
            "id": r["id"],
            "question": r["question"],
            "answer": r["answer"],
            "created_at": r["created_at"],
        }
        for r in res
    ]

    return questions
