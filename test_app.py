# test_app.py
from app_functions import add_task, mark_done

def test_add_task():
    tasks = []
    assert add_task(tasks, "Acheter pain") == True
    assert tasks[0]["task"] == "Acheter pain"

def test_add_empty_task():
    tasks = []
    assert add_task(tasks, "") == False

def test_mark_done():
    tasks = [{"task": "Acheter pain", "done": False}]
    assert mark_done(tasks, 0) == True
    assert tasks[0]["done"] == True

print("Tous les tests unitaires sont OK ✅")
