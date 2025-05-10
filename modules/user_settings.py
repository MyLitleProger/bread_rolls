import streamlit as st

from utils.user_file import load_users, save_users


# --- Настройки пользователя ---
def settings_page():
    """
    This file with user settings page.
    Edit and save user settings.
    :return:
    """
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
