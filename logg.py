import streamlit as st
import pandas as pd
from datetime import datetime
import os

LOGG_FIL = "data/logg.csv"

def init_logg():
    if not os.path.exists(LOGG_FIL):
        df = pd.DataFrame(columns=["Dato", "Vekt (kg)", "Puls (snitt)", "Kommentar"])
        df.to_csv(LOGG_FIL, index=False)

def skriv_logg():
    st.subheader("📋 Logg dagens økt")
    vekt = st.number_input("Vekt (kg)", min_value=40.0, max_value=150.0, step=0.1)
    puls = st.number_input("Gjennomsnittspuls", min_value=60, max_value=200, step=1)
    kommentar = st.text_input("Kommentar (valgfritt)")
    if st.button("Lagre logg"):
        ny_rad = pd.DataFrame([[datetime.now().date(), vekt, puls, kommentar]],
                              columns=["Dato", "Vekt (kg)", "Puls (snitt)", "Kommentar"])
        ny_rad.to_csv(LOGG_FIL, mode='a', header=False, index=False)
        st.success("Logg lagret!")

def vis_logg():
    st.subheader("📈 Fremgang")
    df = pd.read_csv(LOGG_FIL)
    st.line_chart(df.set_index("Dato")[["Vekt (kg)", "Puls (snitt)"]])
    st.dataframe(df[::-1])  # Vis siste først

def vis_parlogg():
    st.subheader("👥 Parvisning – fremgang side om side")

    col1, col2 = st.columns(2)

    try:
        df = pd.read_csv(LOGG_FIL)
        df_torbjorn = df[df["Kommentar"].str.contains("Torbjørn", case=False, na=False)]
        df_ursula = df[df["Kommentar"].str.contains("Ursula", case=False, na=False)]

        with col1:
            st.markdown("### Torbjørn")
            st.line_chart(df_torbjorn.set_index("Dato")[["Vekt (kg)", "Puls (snitt)"]])
            st.dataframe(df_torbjorn[::-1])

        with col2:
            st.markdown("### Ursula")
            st.line_chart(df_ursula.set_index("Dato")[["Vekt (kg)", "Puls (snitt)"]])
            st.dataframe(df_ursula[::-1])

    except:
        st.warning("Ingen parlogg funnet – husk å skrive 'Torbjørn' eller 'Ursula' i kommentarfeltet.")
