import streamlit as st
import pandas as pd
import json
import os
from datetime import date, datetime, timedelta
from db import supabase, lagre_treningsøkt
from config import FARGER, IKONER, APP

LOGG_FIL = "data/logg.csv"
MÅL_FIL = "data/ukemaal.json"

def init_logg():
    if not os.path.exists(LOGG_FIL):
        df = pd.DataFrame(columns=["Dato", "Vekt (kg)", "Puls (snitt)", "Distanse (km)", "Kommentar"])
        df.to_csv(LOGG_FIL, index=False)

def vurder_intensitet(rad):
    puls = rad["Puls (snitt)"]
    km = rad.get("Distanse (km)", 0)
    if puls > 165 and km > 8:
        return "🔥"
    elif puls > 150 or km > 6:
        return "🏃"
    elif puls >= 120 or km >= 3:
        return "🚶"
    else:
        return "🧘"

import os

def vis_dagens_plan():
    # 📌 Kun ikon som header
    st.image("assets/bilde_dagens_plan.png", use_container_width=True)
    bruker = APP["standard_bruker"]
    idag = date.today().isoformat()

    response = supabase.table("treningsplan").select("*").eq("bruker", bruker).eq("dato", idag).execute()
    økter = response.data

    if not økter:
        st.info("Ingen planlagt økt i dag.")
        return

    økt = økter[0]
    aktivitet = økt["aktivitet"].lower()
    ikon_fil = f"{IKONER['mappe']}{aktivitet}.png"

    # 🔒 Sjekk om bildet finnes før visning
    if os.path.exists(ikon_fil):
        st.image(ikon_fil, width=IKONER["størrelse"])
    else:
        st.warning(f"Ingen ikon funnet for aktiviteten '{aktivitet}'. Viser standard.")
        fallback = f"{IKONER['mappe']}{IKONER['standard']}"
        if os.path.exists(fallback):
            st.image(fallback, width=IKONER["størrelse"])
        else:
            st.error("Standardikon mangler også. Sjekk assets/icons/.")

    st.markdown(f"**Aktivitet:** {økt['aktivitet']}")
    st.markdown(f"**Økt:** {økt['beskrivelse']}")

    if st.button("✅ Fullført"):
        st.success("Økten er registrert. God innsats!")


def skriv_logg():
    st.subheader("📋 Logg treningsøkt manuelt")
    dato = st.date_input("Dato", value=datetime.now().date())
    vekt = st.number_input("Vekt (kg)", 40.0, 150.0, step=0.1)
    puls = st.number_input("Gjennomsnittspuls", 60, 200, step=1)
    distanse = st.number_input("Distanse (km)", 0.0, 50.0, step=0.1)
    kommentar = st.text_area("Beskrivelse og hvem som trente")

    if st.button("Lagre logg"):
        ny_rad = pd.DataFrame([[dato, vekt, puls, distanse, kommentar]],
                              columns=["Dato", "Vekt (kg)", "Puls (snitt)", "Distanse (km)", "Kommentar"])
        ny_rad.to_csv(LOGG_FIL, mode='a', header=False, index=False)
        st.success(f"Logg lagret for {dato}!")

def vis_treningslogg():
    response = supabase.table("treningslogg").select("*").order("dato", desc=True).execute()
    data = response.data
    if not data:
        st.info("Ingen treningsøkter registrert ennå.")
        return

    df = pd.DataFrame(data)
    df["dato"] = pd.to_datetime(df["dato"])
    df = df.sort_values("dato", ascending=False)

    st.subheader("📘 Din treningslogg")
    st.dataframe(df[["dato", "aktivitet", "varighet", "distanse", "kommentar"]])

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
            flammer = (person_df["Intensitet"] == "🔥").sum()

            st.markdown(f"### {navn}")
            st.progress(min(økter / øktmål, 1.0), text=f"Økter: {økter}/{øktmål}")
            st.progress(min(km_logget / km_mål, 1.0), text=f"Km: {km_logget:.1f}/{km_mål}")

            if økter >= øktmål and km_logget >= km_mål:
                st.success(f"{navn} har nådd ukemålet! 🎉")
                st.balloons()
            elif flammer >= 2:
                st.info(f"🔥 {flammer} intense økter denne uka – du gir alt!")
    except Exception as e:
        st.error(f"Feil ved visning av ukemål: {e}")

def vis_ukesoppsummering():
    st.subheader("📊 Ukentlig oppsummering")
    try:
        df = pd.read_csv(LOGG_FIL)
        df["Dato"] = pd.to_datetime(df["Dato"]).dt.date
        start_uke = datetime.now().date() - timedelta(days=datetime.now().weekday())
        slutt_uke = start_uke + timedelta(days=6)
        uke_df = df[(df["Dato"] >= start_uke) & (df["Dato"] <= slutt_uke)]

        for navn in ["Torbjørn", "Ursula"]:
            person_df = uke_df[uke_df["Kommentar"].str.contains(navn, case=False, na=False)]
            økter = len(person_df)
            km = person_df["Distanse (km)"].sum() if "Distanse (km)" in person_df.columns else 0
            flammer = (person_df.apply(vurder_intensitet, axis=1) == "🔥").sum()

            st.markdown(f"### {navn}")
            st.write(f"Antall økter: **{økter}**")
            st.write(f"Total distanse: **{km:.1f} km**")
            st.write(f"🔥 Intense økter: **{flammer}**")

            if økter >= 3 and flammer >= 2:
                st.success("🏆 Ukens innsats: Sterk og intens!")
            elif økter >= 3:
                st.info("💪 God treningsuke – jevn og solid innsats!")
            else:
                st.warning("📉 Litt rolig uke – kanskje neste blir sterkere?")
    except Exception as e:
        st.error(f"Feil ved oppsummering: {e}")

def vis_parlogg():
    st.subheader("👥 Parvisning")
    st.info("Parvisning kommer snart! Her vil du se fremgang for deg og partneren din side ved side.")

def rediger_maal():
    pass
def lag_detaljert_plan():
    pass
