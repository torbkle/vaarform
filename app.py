import streamlit as st
from datetime import datetime

# === Importer moduler ===
from meny import vis_meny
from settings import init_settings, vis_mål
from config import FARGER, IKONER, APP
from logg import (
    init_logg,
    skriv_logg,
    vis_treningslogg,
    vis_dagens_plan,
    vis_fremgang,
    vis_parlogg,
    vis_ukesoppsummering,
    vis_ukemaal,
    rediger_maal,
    lag_detaljert_plan
)

# === Initier app ===
init_settings()
init_logg()

# === Sidebar ===
valg = vis_meny()
vis_mål()

# === Hovedvisning ===
st.markdown(
    f"<style>body {{ background-color: {FARGER['bakgrunn']}; }}</style>",
    unsafe_allow_html=True
)

if valg == "Velkommen":
    st.title("🏃‍♀️ VårForm – Treningsapp for to")
    st.markdown(f"""
    <div style='color:{FARGER['tekst']}'>
    Velkommen til VårForm – en personlig treningsapp for deg og din partner. Her får dere:
    - Daglige treningsplaner
    - Kostholdsråd tilpasset øktene
    - Motivasjon og fremgangslogg
    - Mulighet for Garmin-integrasjon
    </div>
    """, unsafe_allow_html=True)

elif valg == "Dagens plan":
    vis_dagens_plan()

elif valg == "Logg":
    skriv_logg()
    st.markdown("---")
    vis_treningslogg()

elif valg == "Fremgang":
    vis_fremgang()

elif valg == "Parvisning" and APP["vis_parvisning"]:
    vis_parlogg()
    st.markdown("---")
    st.subheader("💌 Send en oppmuntring")
    if st.button("Heia Ursula! 💪"):
        st.success("Melding sendt: Du er rå, Ursula! Fortsett å løpe med hjertet!")
    if st.button("Heia Torbjørn! 🚀"):
        st.success("Melding sendt: Du bygger deg selv – én økt av gangen!")

elif valg == "Ukesmål":
    vis_ukemaal()

elif valg == "Ukentlig oppsummering":
    vis_ukesoppsummering()

# === Automatisk ukesoppsummering på søndager ===
if datetime.now().weekday() == 6 and valg != "Ukentlig oppsummering":
    st.markdown("---")
    vis_ukesoppsummering()
