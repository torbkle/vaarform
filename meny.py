import streamlit as st

def vis_meny():
    st.sidebar.markdown("## 🏋️ VårForm")
    st.sidebar.markdown("### Navigasjon")

    valg = st.sidebar.radio("Velg visning:", [
        "🏠 Velkommen",
        "📅 Dagens plan",
        "📓 Logg",
        "📈 Fremgang",
        "🧑‍🤝‍🧑 Parvisning",
        "🎯 Ukesmål",
        "🗓️ Ukentlig oppsummering",
        "🛠️ Rediger mål",
        "🧠 Planlegger"
    ])

    # Fjerner emoji og returnerer ren visningsnavn
    return valg.split(" ", 1)[1]

