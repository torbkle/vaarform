import streamlit as st
from datetime import datetime
from logg import init_logg, skriv_logg, vis_parlogg, vis_ukesoppsummering, vis_ukemaal, vis_fremgang, rediger_maal, vis_treningslogg
from settings import init_settings, vis_mål
import json
from logg import importer_garmin_mock, lag_detaljert_plan, vis_dagens_plan


# === Initier moduler ===
init_settings()
init_logg()

# === Sidebar med menyvalg ===
st.sidebar.title("🧭 Navigasjon")
valg = st.sidebar.radio("Velg visning:", ["Velkommen", "Dagens plan", "Logg", "Fremgang", "Parvisning", "Ukesmål", "Ukentlig oppsummering", "Rediger mål", "Planlegger"])

# === Vis personlige mål ===
vis_mål()

# === Velkommen ===
if valg == "Velkommen":
    st.title("🏃‍♀️ VårForm – Treningsapp for to")
    st.markdown("""
    Velkommen til VårForm – en personlig treningsapp for deg og din partner.
    
    Her får dere:
    - Daglige treningsplaner
    - Kostholdsråd tilpasset øktene
    - Motivasjon og fremgangslogg
    - Mulighet for Garmin-integrasjon
    
    Trykk i menyen til venstre for å komme i gang!
    """)

    # === Ukentlig oppsummering (kun søndag) ===
    if datetime.now().weekday() == 6:  # 6 = søndag
        st.markdown("---")
        vis_ukesoppsummering()


# === Dagens plan ===
elif valg == "Dagens plan":
    vis_dagens_plan()
      

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
    st.markdown("---")
    vis_treningslogg()

if st.button("📥 Importer Garmin-data (mock)"):
    importer_garmin_mock()
    st.success("Garmin-økter importert!")

# === Fremgang ===
elif valg == "Fremgang":
    vis_fremgang()

# === Parvisning ===
elif valg == "Parvisning":
    vis_parlogg()
    
    st.markdown("---")
    st.subheader("💌 Send en oppmuntring")
    if st.button("Heia Ursula! 💪"):
        st.success("Melding sendt: Du er rå, Ursula! Fortsett å løpe med hjertet!")
    if st.button("Heia Torbjørn! 🚀"):
        st.success("Melding sendt: Du bygger deg selv – én økt av gangen!")





# === Ukesmål ===
elif valg  == "Ukesmål":
    vis_ukemaal()
    
# === Ukentlig oppsummering ===
elif valg == "Ukentlig oppsummering":
    vis_ukesoppsummering()


# === Rediger mål ===
elif valg == "Rediger mål":
    rediger_maal()

# === Planlegger ===
elif valg == "Planlegger":
    lag_detaljert_plan()



