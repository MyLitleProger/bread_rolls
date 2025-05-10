import streamlit as st

from utils.hash_pass import hash_password
from utils.user_file import load_users, save_users

# --- Логика входа ---
def login():
    st.subheader("Войти")
    username = st.text_input("Логин")
    password = st.text_input("Пароль", type="password")

    if st.form_submit_button("Войти"):
        users = load_users()
        if username in users and users[username]["password"] == hash_password(password):
            st.success("Вы вошли!")
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["settings"] = users[username]["settings"]
        else:
            st.error("Неверный логин или пароль")

# --- Регистрация ---
def register():
    st.subheader("Зарегистрироваться")
    new_user = st.text_input("Новый логин")
    new_password = st.text_input("Новый пароль", type="password")

    if st.form_submit_button("Зарегистрироваться"):
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
    st.title("Настройки")

    lang = st.selectbox("Выберите язык", ["Русский", "English"])
    theme = st.selectbox("Тема интерфейса", ["light", "dark"])

    if st.form_submit_button("Сохранить настройки"):
        users = load_users()
        user = st.session_state["username"]
        users[user]["settings"] = {
            "language": "ru" if lang == "Русский" else "en",
            "theme": theme
        }
        save_users(users)
        st.session_state["settings"] = users[user]["settings"]
        st.success("Настройки сохранены!")
