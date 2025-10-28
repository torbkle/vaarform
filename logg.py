import streamlit as st
import pandas as pd
import json
from datetime import datetime, timedelta
import os

LOGG_FIL = "data/logg.csv"
MÅL_FIL = "data/ukemaal.json"
SETTINGS_FIL = "data/settings.json"

# === Init-funksjoner ===
def init_logg():
    if not os.path.exists(LOGG_FIL):
        df = pd.DataFrame(columns=["Dato", "Vekt (kg)", "Puls (snitt)", "Distanse (km)", "Kommentar"])
        df.to_csv(LOGG_FIL, index=False)
        print("Opprettet ny logg.csv med kolonner.")

def init_settings():
    if not os.path.exists(SETTINGS_FIL):
        default_settings = {
            "torbjorn": {
                "navn": "Torbjørn",
                "mål": "Gå ned 8 kg og øke utholdenhet og styrke 💪"
            },
            "ursula": {
                "navn": "Ursula",
                "mål": "Gå ned 4 kg og øke utholdenhet og styrke 🌟"
            }
        }
        with open(SETTINGS_FIL, "w", encoding="utf-8") as f:
            json.dump(default_settings, f, indent=2, ensure_ascii=False)
        print("Opprettet settings.json med standardmål.")

# === Intensitet vurdering ===
def vurder_intensitet(rad):
    puls = rad["Puls (snitt)"]
    km = rad["Distanse (km)"] if "Distanse (km)" in rad else 0
    if puls > 165 and km > 8:
        return "🔥"
    elif puls > 150 or km > 6:
        return "🏃"
    elif puls >= 120 or km >= 3:
        return "🚶"
    else:
        return "🧘"



# === Ukesoppdatering ===
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
            km = person_df["Distanse (km)"].sum() if "Distanse (km)" in person_df.columns else 0
            person_df["Intensitet"] = person_df.apply(vurder_intensitet, axis=1)
            flammer = (person_df["Intensitet"] == "🔥").sum()

            vekt_diff = round(person_df["Vekt (kg)"].iloc[-1] - person_df["Vekt (kg)"].iloc[0], 1) if økter >= 2 else 0
            puls_diff = round(person_df["Puls (snitt)"].iloc[-1] - person_df["Puls (snitt)"].iloc[0], 1) if økter >= 2 else 0

            st.markdown(f"### {navn}")
            st.write(f"Antall økter: **{økter}**")
            st.write(f"Total distanse: **{km:.1f} km**")
            st.write(f"🔥 Intense økter: **{flammer}**")
            st.write(f"Vektendring: **{vekt_diff:+} kg**")
            st.write(f"Pulsendring: **{puls_diff:+} bpm**")

            if økter >= 3 and flammer >= 2:
                st.success("🏆 Ukens innsats: Sterk og intens! Fantastisk!")
            elif økter >= 3:
                st.info("💪 God treningsuke – jevn og solid innsats!")
            elif økter > 0:
                st.warning("🙂 Litt aktivitet – men du har mer inne!")
            else:
                st.error("😴 Ingen registrerte økter denne uka.")

        oppsummering("Torbjørn")
        oppsummering("Ursula")

        # Fellesøkter
        felles = uke_df[uke_df["Kommentar"].str.contains("Torbjørn", case=False, na=False) &
                        uke_df["Kommentar"].str.contains("Ursula", case=False, na=False)]
        if len(felles) > 0:
            st.markdown("### 👣 Fellesøkter")
            st.success(f"{len(felles)} økter sammen denne uka – sterkere sammen! 💞")

    except Exception as e:
        st.error(f"Feil ved ukesoppsummering: {e}")


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

            person_df["Intensitet"] = person_df.apply(vurder_intensitet, axis=1)
            antall_flammende = (person_df["Intensitet"] == "🔥").sum()

            st.markdown(f"### {navn}")
            st.progress(min(økter / øktmål, 1.0), text=f"Økter: {økter}/{øktmål}")
            st.progress(min(km_logget / km_mål, 1.0), text=f"Km: {km_logget:.1f}/{km_mål}")

            if økter >= øktmål and km_logget >= km_mål:
                st.success(f"{navn} har nådd ukemålet! Fantastisk innsats! 🎉")
                st.balloons()
                if antall_flammende >= 2:
                    st.info(f"🔥 {antall_flammende} intense økter denne uka – du gir alt!")

    except Exception as e:
        st.error(f"Feil ved visning av ukemål: {e}")

# === 3. Fremgang ===
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

# === 4. Parvisning ===
def vis_parlogg():
    st.subheader("👥 Parvisning – fremgang side om side")
    col1, col2 = st.columns(2)
    try:
        df = pd.read_csv(LOGG_FIL)
        df["Dato"] = pd.to_datetime(df["Dato"])
        df_torbjorn = df[df["Kommentar"].str.contains("Torbjørn", case=False, na=False)]
        df_ursula = df[df["Kommentar"].str.contains("Ursula", case=False, na=False)]

        for person_df in [df_torbjorn, df_ursula]:
            person_df["Intensitet"] = person_df.apply(vurder_intensitet, axis=1)
            person_df["Kort kommentar"] = person_df["Kommentar"].apply(
                lambda x: x[:40] + "..." if isinstance(x, str) and len(x) > 40 else x
            )

        visningskolonner = ["Dato", "Distanse (km)", "Intensitet", "Kort kommentar"]

        for navn, person_df, col in [("Torbjørn", df_torbjorn, col1), ("Ursula", df_ursula, col2)]:
            with col:
                st.markdown(f"### {navn}")
                st.line_chart(person_df.set_index("Dato")[["Vekt (kg)", "Puls (snitt)"]])
                if "Distanse (km)" in person_df.columns:
                    st.line_chart(person_df.set_index("Dato")[["Distanse (km)"]])
                with st.expander("📋 Se loggdetaljer"):
                    st.dataframe(person_df[visningskolonner][::-1], use_container_width=True)

    except Exception as e:
        st.warning(f"Feil ved visning av parlogg: {e}")

# === 5. Rediger mål ===
def rediger_maal():
    st.subheader("🛠️ Rediger treningsmål")
    try:
        with open(SETTINGS_FIL, "r", encoding="utf-8") as f:
            settings = json.load(f)

        for bruker in settings:
            navn = settings[bruker]["navn"]
            st.markdown(f"### {navn}")
            nytt_mål = st.text_input(f"Mål for {navn}", value=settings[bruker]["mål"], key=bruker)

            if st.button(f"Lagre nytt mål for {navn}", key=f"lagre_{bruker}"):
                settings[bruker]["mål"] = nytt_mål
                with open(SETTINGS_FIL, "w", encoding="utf-8") as f:
                    json.dump(settings, f, indent=2, ensure_ascii=False)
                st.success(f"Mål oppdatert for {navn}!")

    except Exception as e:
        st.error(f"Kunne ikke laste eller oppdatere settings.json: {e}")
