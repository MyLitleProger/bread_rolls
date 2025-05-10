import streamlit as st

from modules.authorization import login, register
from modules.user_settings import settings_page

from utils.i18n import _


def main_app():
    """
    The page with general menu.
    :return:
    """
    st.title(_("Добро пожаловать в Bread Rolls!"))
    st.write(_("Вы вошли как:"), st.session_state["username"])
    st.write(_("Настройки:"), st.session_state["settings"])
    if st.form_submit_button(_("Выйти")):
        st.session_state.clear()


def main():
    """
    The parent page with callbacks, where check session state.
    :return:
    """
    with st.form(key="general"):
        if "logged_in" not in st.session_state:
            st.session_state["logged_in"] = False

        if not st.session_state["logged_in"]:
            option = st.sidebar.selectbox(_("Вход / Регистрация"), [_("Войти"), _("Зарегистрироваться")])
            if option == _("Войти"):
                login()
            else:
                register()
        else:
            st.sidebar.write(_("Привет,"), st.session_state["username"])
            page = st.sidebar.radio(_("Перейти"), [_("Главная"), _("Настройки"), _("Выйти")])

            if page == _("Главная"):
                main_app()
            elif page == _("Настройки"):
                settings_page()
            elif page == _("Выйти"):
                st.session_state.clear()

if __name__ == '__main__':
    main()