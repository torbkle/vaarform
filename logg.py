import streamlit as st
import pandas as pd
import json
from datetime import datetime, timedelta
import os

def init_logg():
    if not os.path.exists(LOGG_FIL):
        df = pd.DataFrame(columns=["Dato", "Vekt (kg)", "Puls (snitt)", "Distanse (km)", "Kommentar"])
        df.to_csv(LOGG_FIL, index=False)
        print("Opprettet ny logg.csv med kolonner.")

LOGG_FIL = "data/logg.csv"
MÅL_FIL = "data/ukemaal.json"

def init_settings():
    filsti = "data/settings.json"
    if not os.path.exists(filsti):
        default_settings = {
            "torbjorn": {
                "navn": "Torbjørn",
                "mål": "Gå ned 8 kg og øke utholdenhet og styrke 💪"
            },
            "ursula": {
                "navn": "Ursula",
                "mål": "Holde energien oppe og trene jevnlig 🌟"
            }
        }
        with open(filsti, "w", encoding="utf-8") as f:
            json.dump(default_settings, f, indent=2, ensure_ascii=False)
        print("Opprettet settings.json med standardmål.")


# === 1. Logg treningsøkt manuelt ===
def skriv_logg():
    st.subheader("📋 Logg treningsøkt manuelt")

    dato = st.date_input("Dato for økten", value=datetime.now().date())
    vekt = st.number_input("Vekt (kg)", min_value=40.0, max_value=150.0, step=0.1)
    puls = st.number_input("Gjennomsnittspuls", min_value=60, max_value=200, step=1)
    distanse = st.number_input("Distanse (km)", min_value=0.0, max_value=50.0, step=0.1)
    kommentar = st.text_area("Beskrivelse av økten og hvem som trente")

    if st.button("Lagre logg"):
        ny_rad = pd.DataFrame([[dato, vekt, puls, distanse, kommentar]],
                              columns=["Dato", "Vekt (kg)", "Puls (snitt)", "Distanse (km)", "Kommentar"])
        ny_rad.to_csv(LOGG_FIL, mode='a', header=False, index=False)
        st.success(f"Logg lagret for {dato}!")

# === 2. Ukemål og fremdrift ===
def vis_ukemaal():
    st.subheader("📅 Ukemål og fremdrift")

    try:
        with open(MÅL_FIL, "r", encoding="utf-8") as f:
            mål = json.load(f)

        df = pd.read_csv(LOGG_FIL)
        df["Dato"] = pd.to_datetime(df["Dato"]).dt.date
        start_uke = datetime.now().date() - timedelta(days=datetime.now().weekday())
        uke_df = df[df["Dato"] >= start_uke]

        for bruker in mål:
            navn = mål[bruker]["navn"]
            øktmål = mål[bruker]["mål_økter"]
            km_mål = mål[bruker]["mål_km"]

            person_df = uke_df[uke_df["Kommentar"].str.contains(navn, case=False, na=False)]
            økter = len(person_df)
            km_logget = person_df["Distanse (km)"].sum() if "Distanse (km)" in person_df.columns else 0

            st.markdown(f"### {navn}")
            st.progress(min(økter / øktmål, 1.0), text=f"Økter: {økter}/{øktmål}")
            st.progress(min(km_logget / km_mål, 1.0), text=f"Km: {km_logget:.1f}/{km_mål}")

            if økter >= øktmål and km_logget >= km_mål:
                st.success(f"{navn} har nådd ukemålet! Fantastisk innsats! 🎉")
                st.balloons()

    except Exception as e:
        st.error(f"Feil ved visning av ukemål: {e}")

# ===Fremgang ===
def vis_fremgang():
    st.subheader("📈 Din fremgang")

    try:
        df = pd.read_csv(LOGG_FIL)
        df["Dato"] = pd.to_datetime(df["Dato"])
        df_torbjorn = df[df["Kommentar"].str.contains("Torbjørn", case=False, na=False)]

        st.line_chart(df_torbjorn.set_index("Dato")[["Vekt (kg)", "Puls (snitt)", "Distanse (km)"]])
        st.dataframe(df_torbjorn[::-1])

    except Exception as e:
        st.warning(f"Feil ved visning av fremgang: {e}")



# === 3. Parvisning med distanse ===
def vis_parlogg():
    st.subheader("👥 Parvisning – fremgang side om side")
    col1, col2 = st.columns(2)

    try:
        df = pd.read_csv(LOGG_FIL)
        df["Dato"] = pd.to_datetime(df["Dato"])

        df_torbjorn = df[df["Kommentar"].str.contains("Torbjørn", case=False, na=False)]
        df_ursula = df[df["Kommentar"].str.contains("Ursula", case=False, na=False)]

        for navn, person_df, col in [("Torbjørn", df_torbjorn, col1), ("Ursula", df_ursula, col2)]:
            with col:
                st.markdown(f"### {navn}")
                st.line_chart(person_df.set_index("Dato")[["Vekt (kg)", "Puls (snitt)"]])
                if "Distanse (km)" in person_df.columns:
                    st.line_chart(person_df.set_index("Dato")[["Distanse (km)"]])
                st.dataframe(person_df[::-1])

    except Exception as e:
        st.warning(f"Feil ved visning av parlogg: {e}")

# === 4. Ukentlig oppsummering ===
def vis_ukesoppsummering():
    st.subheader("📊 Ukentlig oppsummering")

    try:
        df = pd.read_csv(LOGG_FIL)
        df["Dato"] = pd.to_datetime(df["Dato"]).dt.date
        start_uke = datetime.now().date() - timedelta(days=datetime.now().weekday())
        slutt_uke = start_uke + timedelta(days=6)
        uke_df = df[(df["Dato"] >= start_uke) & (df["Dato"] <= slutt_uke)]

        def oppsummering(navn):
            person_df = uke_df[uke_df["Kommentar"].str.contains(navn, case=False, na=False)]
            økter = len(person_df)
            vekt_diff = round(person_df["Vekt (kg)"].iloc[-1] - person_df["Vekt (kg)"].iloc[0], 1) if økter >= 2 else 0
            puls_diff = round(person_df["Puls (snitt)"].iloc[-1] - person_df["Puls (snitt)"].iloc[0], 1) if økter >= 2 else 0
            km_sum = person_df["Distanse (km)"].sum() if "Distanse (km)" in person_df.columns else 0

            st.markdown(f"### {navn}")
            st.write(f"- Økter logget: **{økter}**")
            st.write(f"- Vektendring: **{vekt_diff} kg**")
            st.write(f"- Pulsendring: **{puls_diff} bpm**")
            st.write(f"- Total distanse: **{km_sum:.1f} km**")

            if økter >= 3:
                st.success(f"Flott uke, {navn}! Du er på vei 💪")
            elif økter == 0:
                st.warning(f"Ingen logg denne uka – kanskje en ny start neste uke, {navn}?")

        oppsummering("Torbjørn")
        oppsummering("Ursula")

    except Exception as e:
        st.error(f"Kunne ikke generere ukesoppsummering: {e}")
