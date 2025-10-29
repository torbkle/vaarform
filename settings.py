import streamlit as st
import json
import os

SETTINGS_FIL = "data/settings.json"

# Standardinnstillinger
default_settings = {
    "brukere": {
        "torbjorn": {
            "navn": "Torbjørn",
            "mål": "Gå ned 8 kg og øke utholdenhet og styrke"
        },
        "ursula": {
            "navn": "Ursula",
            "mål": "Gå ned 4 kg og øke utholdenhet og styrke"
        }
    },
    "visning": {
        "primærfarge": "#4CAF50",
        "ikonstørrelse": 50,
        "bruk_emoji": True
    }
}

def init_settings():
    """Oppretter settings.json hvis den ikke finnes"""
    if not os.path.exists(SETTINGS_FIL):
        os.makedirs(os.path.dirname(SETTINGS_FIL), exist_ok=True)
        with open(SETTINGS_FIL, "w", encoding="utf-8") as f:
            json.dump(default_settings, f, indent=2)

def hent_innstillinger():
    """Laster inn innstillinger fra fil"""
    if not os.path.exists(SETTINGS_FIL):
        init_settings()
    with open(SETTINGS_FIL, "r", encoding="utf-8") as f:
        return json.load(f)

def vis_mål():
    """Viser mål i hovedområdet (ikke sidebar)"""
    data = hent_innstillinger()
    brukere = data.get("brukere", {})
    if not brukere:
        st.warning("Ingen mål funnet – sjekk settings.json")
        return

    with st.expander("🎯 Våre mål", expanded=True):
        for bruker in brukere:
            navn = brukere[bruker].get("navn", bruker)
            mål = brukere[bruker].get("mål", "Ingen mål definert")
            st.markdown(f"**{navn}**: {mål}")
