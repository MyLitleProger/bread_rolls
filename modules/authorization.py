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
        if users is not None:
            if username in users and users[username]["password"] == hash_password(password):
                st.success("Вы вошли!")
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.session_state["settings"] = users[username]["settings"]
            else:
                st.error("Неверный логин или пароль")
        else:
            st.error("This user doesn't exist!")


# --- Регистрация ---
def register():
    """
    The page register.
    :return:
    """
    st.subheader("Зарегистрироваться")
    new_user = st.text_input("Login")
    first_name = st.text_input("First name")
    last_name = st.text_input("Last name")
    email = st.text_input("Email")
    new_password = st.text_input("Password", type="password")
    check_password = st.text_input("Repeat the password", type="password")
    country = st.selectbox("Country", )

    if new_password != check_password:
        st.warning("Passwords don't match")

    if st.form_submit_button("Зарегистрироваться") and new_password == check_password:
        users = load_users()
        if new_user in users:
            st.warning("Этот логин уже занят")
        else:
            users[new_user] = {
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "country": country,
                "password": hash_password(new_password),
                "settings": {
                    "language": "en",
                    "theme": "dark"
                }
            }
            save_users(users)
            st.success("Аккаунт создан!")

