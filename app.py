import streamlit as st
import json
from datetime import datetime

# === Last inn treningsplan ===
with open("data/treningsplan.json", "r", encoding="utf-8") as f:
    plan = json.load(f)

# === Last inn motivasjon ===
with open("assets/motivasjon.txt", "r", encoding="utf-8") as f:
    motivasjon = f.readlines()

# === Dagens dato og ukedag ===
dag = datetime.now().strftime("%A").lower()

st.title("🏃‍♀️ VårForm – Treningsapp for to")
st.subheader(f"Dagens plan ({dag.capitalize()})")

# === Vis treningsplan ===
if dag in plan:
    st.markdown(f"**Trening:** {plan[dag]['trening']}")
    st.markdown(f"**Kostholdstips:** {plan[dag]['kosthold']}")
else:
    st.info("Ingen plan for i dag – kanskje en hviledag?")

# === Motivasjon ===
st.markdown("---")
st.markdown("💬 **Motivasjon:**")
st.success(motivasjon[datetime.now().day % len(motivasjon)].strip())

# === Fullført-knapp ===
if st.button("✅ Jeg har fullført dagens økt!"):
    st.balloons()
    st.write("Bra jobbet! Husk å drikke vann og smile til deg selv.")
