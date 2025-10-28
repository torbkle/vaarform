import streamlit as st
import json
import os

SETTINGS_FIL = "data/settings.json"

def init_settings():
    if not os.path.exists(SETTINGS_FIL):
        default = {
            "torbjorn": {"mål": "Gå ned 5 kg og forbedre 5 km-tid", "navn": "Torbjørn"},
            "partner": {"mål": "Øke utholdenhet og styrke", "navn": "Ursula"}
        }
        with open(SETTINGS_FIL, "w", encoding="utf-8") as f:
            json.dump(default, f, indent=2)

def vis_mål():
    with open(SETTINGS_FIL, "r", encoding="utf-8") as f:
        data = json.load(f)
    st.sidebar.header("🎯 Våre mål")
    for bruker in data:
        st.sidebar.markdown(f"**{data[bruker]['navn']}**: {data[bruker]['mål']}")
