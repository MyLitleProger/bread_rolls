import streamlit as st

from modules.authorization import login, register, settings_page


# --- Главная страница ---
def main_app():
    st.title("Добро пожаловать в Bread Rolls!")
    st.write("Вы вошли как:", st.session_state["username"])
    st.write("Настройки:", st.session_state["settings"])
    if st.form_submit_button("Выйти"):
        st.session_state.clear()

# --- Точка входа ---
def main():
    with st.form(key="general"):
        if "logged_in" not in st.session_state:
            st.session_state["logged_in"] = False

        if not st.session_state["logged_in"]:
            option = st.sidebar.selectbox("Вход / Регистрация", ["Войти", "Зарегистрироваться"])
            if option == "Войти":
                login()
            else:
                register()
        else:
            st.sidebar.write("Привет,", st.session_state["username"])
            page = st.sidebar.radio("Перейти", ["Главная", "Настройки", "Выйти"])

            if page == "Главная":
                main_app()
            elif page == "Настройки":
                settings_page()
            elif page == "Выйти":
                st.session_state.clear()

if __name__ == "__main__":
    main()