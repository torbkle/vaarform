import streamlit as st
from datetime import datetime

# === Importer moduler ===
from settings import init_settings, vis_mål
from garmin import hent_mock_økt
from config import FARGER, IKONER, APP
from menydata import MENYVALG
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

# === Sett opp appen ===
st.set_page_config(page_title="VårForm", page_icon="🏋️", layout="centered")
init_settings()
init_logg()

# === Initier menyvalg hvis det ikke finnes ===
if "sidevalg" not in st.session_state:
    st.session_state.sidevalg = "Velkommen"

# === Toppmeny ===
st.markdown("## Navigasjon")
kolonner = st.columns(len(MENYVALG))

for i, meny in enumerate(MENYVALG):
    navn = meny["navn"]
    bilde = meny.get("bilde", None)

    with kolonner[i]:
        if bilde and navn == "Velkommen":
            st.image(bilde, width=50)
            if st.button(" ", key="velkommen_bilde"):
                st.session_state.sidevalg = navn
        else:
            if st.button(navn):
                st.session_state.sidevalg = navn

# === Hovedvisning ===
valg = st.session_state.sidevalg

st.markdown(
    f"<style>body {{ background-color: {FARGER['bakgrunn']}; }}</style>",
    unsafe_allow_html=True
)

if valg == "Velkommen":
    st.image("assets/varform.png", use_container_width=True)
    st.markdown("""
    <div style='text-align: center; font-size: 20px; font-family: "Segoe UI", sans-serif; color: #003049;'>
      <strong>Tren sammen. Følg fremgangen. Del seieren.</strong><br>
      VårForm hjelper deg og partneren din å holde motivasjonen oppe – én økt av gangen.
    </div>
    """, unsafe_allow_html=True)

elif valg == "Dagens plan":
    vis_dagens_plan()
    økt = hent_mock_økt("Torbjørn")
    st.markdown("---")
    st.subheader("📡 Synkronisert Garmin-økt (mock)")
    st.write(f"**Aktivitet:** {økt['aktivitet']}")
    st.write(f"**Distanse:** {økt['distanse_km']} km")
    st.write(f"**Varighet:** {økt['varighet_min']} min")
    st.write(f"**Puls:** {økt['gjennomsnittspuls']} bpm")
    st.write(f"**Kalorier:** {økt['kalorier']} kcal")

elif valg == "Logg":
    skriv_logg()
    st.markdown("---")
    vis_treningslogg()

elif valg == "Fremgang":
    vis_fremgang()
    økt = hent_mock_økt("Torbjørn")
    st.markdown("---")
    st.subheader("📈 Fremgang basert på Garmin-data")
    emoji = "🔥" if økt["gjennomsnittspuls"] > 140 else "💧"
    st.write(f"{emoji} Du har gjennomført en {økt['aktivitet'].lower()} på {økt['distanse_km']} km med {økt['gjennomsnittspuls']} bpm i snittpuls.")

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

elif valg == "Rediger mål":
    rediger_maal()

elif valg == "Planlegger":
    lag_detaljert_plan()

# === Automatisk ukesoppsummering på søndager ===
if datetime.now().weekday() == 6 and valg != "Ukentlig oppsummering":
    st.markdown("---")
    vis_ukesoppsummering()

# === Våre mål i bunnen ===
st.markdown("---")
st.markdown("### Våre mål")
vis_mål()
