import streamlit as st

def vis_meny():
    st.sidebar.title("🧭 Navigasjon")
    valg = st.sidebar.radio("Velg visning:", [
        "Velkommen",
        "Dagens plan",
        "Logg",
        "Fremgang",
        "Parvisning",
        "Ukesmål",
        "Ukentlig oppsummering",
        "Rediger mål",
        "Planlegger"
    ])
    return valg
