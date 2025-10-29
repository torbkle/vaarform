import streamlit as st
from menydata import MENYVALG

def vis_meny():
    st.markdown("""
    <style>
    .venstremeny {
        position: fixed;
        top: 0;
        left: 0;
        height: 100%;
        width: 80px;
        background-color: #f8f9fa;
        border-right: 1px solid #ddd;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-top: 1rem;
        z-index: 100;
    }
    .menyknapp {
        font-size: 20px;
        padding: 0.6rem;
        margin-bottom: 0.5rem;
        border-radius: 6px;
        background-color: #f0f0f0;
        border: 2px solid transparent;
        cursor: pointer;
        width: 48px;
        height: 48px;
        text-align: center;
    }
    .menyknapp:hover {
        background-color: #e0e0e0;
    }
    .menyknapp.aktiv {
        border-color: #003049;
        background-color: #dbe9f4;
    }
    .innhold {
        margin-left: 90px;
        padding: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="venstremeny">', unsafe_allow_html=True)

    for meny in MENYVALG:
        navn = meny["navn"]
        ikon = meny.get("ikon", "❓")
        aktiv = st.session_state.get("sidevalg") == navn
        knappklasse = "menyknapp aktiv" if aktiv else "menyknapp"
        knapp_html = f"""
        <form action="" method="post">
            <button class="{knappklasse}" name="valg" value="{navn}" title="{navn}">{ikon}</button>
        </form>
        """
        st.markdown(knapp_html, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Håndter klikk
    if "valg" in st.session_state:
        st.session_state.sidevalg = st.session_state.valg
        del st.session_state.valg

    # Start innholdsområde
    st.markdown('<div class="innhold">', unsafe_allow_html=True)
