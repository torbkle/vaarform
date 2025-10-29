import streamlit as st

MENYVALG = [
    {"navn": "Velkommen", "ikon": "🏠"},
    {"navn": "Dagens plan", "ikon": "📅"},
    {"navn": "Logg", "ikon": "📓"},
    {"navn": "Fremgang", "ikon": "📈"},
    {"navn": "Parvisning", "ikon": "🧑‍🤝‍🧑"},
    {"navn": "Ukesmål", "ikon": "🎯"},
    {"navn": "Ukentlig oppsummering", "ikon": "🗓️"},
    {"navn": "Rediger mål", "ikon": "🛠️"},
    {"navn": "Planlegger", "ikon": "🧠"}
]

def vis_sidebar_meny():
    st.sidebar.title("Navigasjon")
    for meny in MENYVALG:
        navn = meny["navn"]
        ikon = meny["ikon"]
        if st.sidebar.button(f"{ikon} {navn}", key=navn):
            st.session_state.sidevalg = navn
