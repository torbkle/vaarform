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
    # rediger_maal,
    # lag_detaljert_plan
)

# === Initier app ===
init_settings()
init_logg()

# === Sidebar ===
valg = vis_meny()
vis_mål()

# === Hovedvisning ===
st.markdown(f"<style>body {{ background-color: {FARGER['bakgrunn']}; }}</style>", unsafe_allow_html=True)

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
    st.markdown(f"<h3 style='color:{FARGER['primær']}'>📅 Dagens økt</h3>", unsafe_allow_html=True)
    vis_dagens_plan()

elif valg == "Logg":
    st.markdown(f"<h3 style='color:{FARGER['primær']}'>📝 Logg treningsøkt</h3>", unsafe_allow_html=True)
    skriv_logg()
    st.markdown("---")
    vis_treningslogg()

elif valg == "Fremgang":
    st.markdown(f"<h3 style='color:{FARGER['primær']}'>📈 Fremgang</h3>", unsafe_allow_html=True)
    vis_fremgang()

elif valg == "Parvisning" and APP["vis_parvisning"]:
    st.markdown(f"<h3 style='color:{FARGER['primær']}'>👥 Parvisning</h3>", unsafe_allow_html=True)
    vis_parlogg()
    st.markdown("---")
    st.subheader("💌 Send en oppmuntring")
    if st.button("Heia Ursula! 💪"):
        st.success("Melding sendt: Du er rå, Ursula! Fortsett å løpe med hjertet!")
    if st.button("Heia Torbjørn! 🚀"):
        st.success("Melding sendt: Du bygger deg selv – én økt av gangen!")

elif valg == "Ukesmål":
    st.markdown(f"<h3 style='color:{FARGER['primær']}'>🎯 Ukesmål</h3>", unsafe_allow_html=True)
    vis_ukemaal()

elif valg == "Ukentlig oppsummering":
    st.markdown(f"<h3 style='color:{FARGER['primær']}'>📊 Ukentlig oppsummering</h3>", unsafe_allow_html=True)
    vis_ukesoppsummering()

elif valg == "Rediger mål":
    st.markdown(f"<h3 style='color:{FARGER['primær']}'>✏️ Rediger mål</h3>", unsafe_allow_html=True)
    rediger_maal()

elif valg == "Planlegger":
    st.markdown(f"<h3 style='color:{FARGER['primær']}'>🗓 Lag treningsplan</h3>", unsafe_allow_html=True)
    lag_detaljert_plan()

# === Automatisk ukesoppsummering på søndager ===
if datetime.now().weekday() == 6 and valg != "Ukentlig oppsummering":
    st.markdown("---")
    vis_ukesoppsummering()
