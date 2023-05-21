import requests


def get_question(number: int) -> dict:
    url = f"https://jservice.io/api/random?count={number}"
    res = requests.get(url).json()[0]

    return {
        "id": res["id"],
        "question": res["question"],
        "answer": res["answer"],
        "created_at": res["created_at"],
    }
