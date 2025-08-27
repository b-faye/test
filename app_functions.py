# app_functions.py
def add_task(tasks, task):
    if task.strip() == "":
        return False
    if any(t["task"] == task for t in tasks):
        return False
    tasks.append({"task": task, "done": False})
    return True

def mark_done(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        return True
    return False
