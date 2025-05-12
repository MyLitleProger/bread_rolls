import json


# --- Загрузка пользователей ---
def load_users():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


# --- Сохранение пользователей ---
def save_users(users_db):
    with open("users.json", "w") as f:
        json.dump(users_db, f, indent=4)
