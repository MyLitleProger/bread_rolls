import streamlit as st
import json
import hashlib


# --- Утилиты ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

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

# --- Логика входа ---
def login():
    with st.form(key="login"):
        st.subheader("Войти")
        username = st.text_input("Логин")
        password = st.text_input("Пароль", type="password")

        if st.button("Войти"):
            users = load_users()
            if username in users and users[username]["password"] == hash_password(password):
                st.success("Вы вошли!")
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.session_state["settings"] = users[username]["settings"]
                st.rerun()
            else:
                st.error("Неверный логин или пароль")

# --- Регистрация ---
def register():
    with st.form(key="register"):
        st.subheader("Зарегистрироваться")
        new_user = st.text_input("Новый логин")
        new_password = st.text_input("Новый пароль", type="password")

        if st.button("Зарегистрироваться"):
            users = load_users()
            if new_user in users:
                st.warning("Этот логин уже занят")
            else:
                users[new_user] = {
                    "password": hash_password(new_password),
                    "settings": {
                        "language": "ru",
                        "theme": "dark"
                    }
                }
                save_users(users)
                st.success("Аккаунт создан!")

# --- Настройки пользователя ---
def settings_page():
    with st.form(key="settings"):
        st.title("Настройки")

        lang = st.selectbox("Выберите язык", ["Русский", "English"])
        theme = st.selectbox("Тема интерфейса", ["light", "dark"])

        if st.button("Сохранить настройки"):
            users = load_users()
            user = st.session_state["username"]
            users[user]["settings"] = {
                "language": "ru" if lang == "Русский" else "en",
                "theme": theme
            }
            save_users(users)
            st.session_state["settings"] = users[user]["settings"]
            st.success("Настройки сохранены!")