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
    if not os.path.exists(SETTINGS_FIL):
        os.makedirs(os.path.dirname(SETTINGS_FIL), exist_ok=True)
        with open(SETTINGS_FIL, "w", encoding="utf-8") as f:
            json.dump(default_settings, f, indent=2)

def hent_innstillinger():
    with open(SETTINGS_FIL, "r", encoding="utf-8") as f:
        return json.load(f)

def vis_mål():
    data = hent_innstillinger()
    st.sidebar.header("🎯 Våre mål")
    for bruker in data["brukere"]:
        navn = data["brukere"][bruker]["navn"]
        mål = data["brukere"][bruker]["mål"]
        st.sidebar.markdown(f"**{navn}**: {mål}")
