import streamlit as st

def vis_meny():
    st.sidebar.title("🧭 Navigasjon")
    valg = st.sidebar.radio("Velg side:", ["Forside", "Dagens plan", "Logg", "Innstillinger"])
    st.session_state.sidevalg = valg

