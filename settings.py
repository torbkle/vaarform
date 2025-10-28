import streamlit as st
import json
import os

SETTINGS_FIL = "data/settings.json"

def init_settings():
    if not os.path.exists(SETTINGS_FIL):
        default = {
            "torbjorn": {"mål": "Gå ned 8 kg og øke utholdenhet og styrke", "navn": "Torbjørn"},
            "ursula": {"mål": "Gå ned 4 kg og øke utholdenhet og styrke", "navn": "Ursula"}
        }
        with open(SETTINGS_FIL, "w", encoding="utf-8") as f:
            json.dump(default, f, indent=2)

def vis_mål():
    with open(SETTINGS_FIL, "r", encoding="utf-8") as f:
        data = json.load(f)
    st.sidebar.header("🎯 Våre mål")
    for bruker in data:
        st.sidebar.markdown(f"**{data[bruker]['navn']}**: {data[bruker]['mål']}")
