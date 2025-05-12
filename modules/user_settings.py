import streamlit as st

from utils.user_file import load_users, save_users
from utils.languages import languages
from utils.theme import themes


# --- Настройки пользователя ---
def settings_page():
    """
    This file with user settings page.
    Edit and save user settings.
    :return:
    """
    st.title("Настройки")

    lang = st.selectbox("Select language", languages)
    theme = st.selectbox("Theme", themes)

    if st.form_submit_button("Сохранить настройки"):
        users = load_users()
        user = st.session_state["username"]
        users[user]["settings"] = {
            "language": "ru" if lang == "Русский" else "en",    # todo: temporary
            "theme": theme
        }
        save_users(users)
        st.session_state["settings"] = users[user]["settings"]
        st.success("Настройки сохранены!")
