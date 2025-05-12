import streamlit as st

from modules.authorization import login, register
from modules.user_settings import settings_page

from utils.i18n import _


def main_app():
    """
    The page with general menu.
    :return:
    """
    st.title(_("Wellcome at the Bread Rolls!"))
    st.write(_("You entered as: "), st.session_state["username"])
    st.write(_("Settings:"), st.session_state["settings"])
    if st.form_submit_button(_("Sign out")):
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
            option = st.sidebar.selectbox(_("Sign in / Sign up"), [_("Sign in"), _("Sign up")])
            if option == _("Sign in"):
                login()
            else:
                register()
        else:
            st.sidebar.write(_("Hello,"), st.session_state["username"])
            page = st.sidebar.radio(_("Menu"), [_("Home"), _("Settings"), _("Sing out")])

            if page == _("Home"):
                main_app()
            elif page == _("Settings"):
                settings_page()
            elif page == _("Sing out"):
                st.session_state.clear()

if __name__ == '__main__':
    main()