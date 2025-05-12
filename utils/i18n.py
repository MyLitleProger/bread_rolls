import gettext
import os
from locale import getdefaultlocale
import streamlit as st

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
LOCALE_DIR = os.path.join(PROJECT_ROOT, 'locales')

# chache translate
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
        translation = gettext.translation("messages", LOCALE_DIR, languages=[lang])
        _translations[lang] = translation
        return translation
    except FileNotFoundError:
        print(f"Translation file not found for {lang}")
        return gettext.NullTranslations()


def _(key: str):
    lang = st.session_state.get("settings", {}).get("language", "en")

    if not lang:
        lang = "en"
        st.session_state["settings"]["language"] = lang

    translation = load_translations(lang)
    result = translation.gettext(key)

    if result == key:
        result = gettext.gettext(key)

    return result
