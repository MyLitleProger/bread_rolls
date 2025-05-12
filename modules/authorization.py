import streamlit as st

from utils.hash_pass import hash_password
from utils.user_file import load_users, save_users

from utils.i18n import _


def login():
    """
    The page login in.
    :return:
    """
    st.subheader(_("Войти"))
    username = st.text_input(_("Логин"))
    password = st.text_input(_("Пароль"), type="password")

    if st.form_submit_button(_("Войти")):
        users = load_users()
        if users is not None:
            if username in users and users[username]["password"] == hash_password(password):
                st.success(_("Вы вошли!"))
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.session_state["settings"] = users[username]["settings"]
            else:
                st.error(_("Неверный логин или пароль"))
        else:
            st.error(_("This user doesn't exist!"))


def register():
    """
    The page register.
    :return:
    """
    st.subheader(_("Зарегистрироваться"))
    new_user = st.text_input(_("Login"), placeholder=_("JohnJordan"))
    first_name = st.text_input(_("First name"), placeholder=_("John"))
    last_name = st.text_input(_("Last name"), placeholder=_("Jordan"))
    email = st.text_input(_("Email"), placeholder=_("JohnJordan@mail.com"))
    new_password = st.text_input(_("Password"), type="password")
    check_password = st.text_input(_("Repeat the password"), type="password")
    # country = st.selectbox("Country", )

    if new_password != check_password:
        st.warning(_("Passwords don't match"))

    if st.form_submit_button(_("Зарегистрироваться")) and new_password == check_password:
        users = load_users()
        if new_user in users:
            st.warning(_("Этот логин уже занят"))
        else:
            users[new_user] = {
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                # "country": country,
                "password": hash_password(new_password),
                "settings": {
                    "language": "en",
                    "theme": "dark"
                }
            }
            save_users(users)
            st.success(_("Аккаунт создан!"))

