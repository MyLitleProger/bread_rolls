import gettext
import os
from locale import getdefaultlocale
import streamlit as st


LOCALE_DIR = os.path.join(os.path.dirname(__file__), 'locales')

#chache translate
_translations = {}

def load_translations(lang: str):
    """
    Load translate for using language.
    :param lang: using language [en, ru, ...]
    :return: translation
    """
    if lang in _translations:
        return _translations[lang]

    try:
        translation = gettext.translation("messages", LOCALE_DIR, languages=[lang], fallback=True)
        _translations[lang] = translation
        return translation
    except FileNotFoundError:
        return gettext.NullTranslations()

def _(key: str):
    lang = st.session_state.get("language")

    if not lang:
        system_lang = getdefaultlocale()[0][:2]
        lang = system_lang if system_lang in ["en", "ru"] else "en"
        st.session_state["language"] = lang

    translation = load_translations(lang)
    result = translation.gettext(key)

    if result == key:
        result = gettext.gettext(key)

    return result