import streamlit as st
from datetime import datetime
from logg import init_logg, skriv_logg, vis_logg
from settings import init_settings, vis_mål
import json

# === Initier moduler ===
init_settings()
init_logg()

# === Sidebar med menyvalg ===
st.sidebar.title("🧭 Navigasjon")
valg = st.sidebar.radio("Velg visning:", ["Velkommen", "Dagens plan", "Logg", "Fremgang", "Parvisning"])

# === Vis personlige mål ===
vis_mål()

# === Velkommen ===
if valg == "Velkommen":
    st.title("🏃‍♀️ VårForm – Treningsapp for to")
    st.markdown("""
    Velkommen til VårForm – en personlig treningsapp for deg og din kjæreste.
    
    Her får dere:
    - Daglige treningsplaner
    - Kostholdsråd tilpasset øktene
    - Motivasjon og fremgangslogg
    - Mulighet for Garmin-integrasjon
    
    Trykk i menyen til venstre for å komme i gang!
    """)

# === Dagens plan ===
elif valg == "Dagens plan":
    st.title("📅 Dagens treningsplan")
    dag = datetime.now().strftime("%A").lower()
    try:
        with open("data/treningsplan.json", "r", encoding="utf-8") as f:
            plan = json.load(f)
        if dag in plan:
            st.markdown(f"**Trening:** {plan[dag]['trening']}")
            st.markdown(f"**Kostholdstips:** {plan[dag]['kosthold']}")
        else:
            st.info("Ingen plan for i dag – kanskje en hviledag?")
    except:
        st.error("Fant ikke treningsplanfilen.")

    # Motivasjon
    try:
        with open("assets/motivasjon.txt", "r", encoding="utf-8") as f:
            motivasjon = f.readlines()
        st.success(motivasjon[datetime.now().day % len(motivasjon)].strip())
    except:
        st.warning("Fant ikke motivasjonsfilen.")

    if st.button("✅ Jeg har fullført dagens økt!"):
        st.balloons()
        st.write("Bra jobbet! Husk å drikke vann og smile til deg selv.")

# === Logg ===
elif valg == "Logg":
    skriv_logg()

# === Fremgang ===
elif valg == "Fremgang":
    vis_logg()

# === Parvisning ===
elif valg == "Parvisning":
    vis_parlogg()
