import streamlit as st

from utils.hash_pass import hash_password
from utils.user_file import load_users, save_users


# --- Логика входа ---
def login():
    """
    The page login in.
    :return:
    """
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
    """
    The page register.
    :return:
    """
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
