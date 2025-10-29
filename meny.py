import streamlit as st
from menydata import MENYVALG

def vis_meny():
    st.markdown("""
    <style>
    .meny-rad {
        display: flex;
        overflow-x: auto;
        gap: 0.5rem;
        padding: 0.5rem 0;
        margin-bottom: 1rem;
        border-bottom: 1px solid #ddd;
        background-color: #f8f9fa;
    }
    .meny-rad::-webkit-scrollbar {
        height: 6px;
    }
    .meny-rad::-webkit-scrollbar-thumb {
        background-color: #ccc;
        border-radius: 3px;
    }
    .meny-knapp {
        font-size: 20px !important;
        padding: 0.4rem 0.6rem;
        border-radius: 6px;
        background-color: #f0f0f0;
        border: 2px solid transparent;
        white-space: nowrap;
    }
    .meny-knapp:hover {
        background-color: #e0e0e0;
    }
    .meny-knapp.aktiv {
        border-color: #003049;
        background-color: #dbe9f4;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="meny-rad">', unsafe_allow_html=True)

    for meny in MENYVALG:
        navn = meny["navn"]
        ikon = meny.get("ikon", "❓")
        aktiv = st.session_state.get("sidevalg") == navn
        knapp_style = "meny-knapp aktiv" if aktiv else "meny-knapp"

        # Bruk ekte Streamlit-knapp
        if st.button(f"{ikon}", key=navn):
            st.session_state.sidevalg = navn

    st.markdown('</div>', unsafe_allow_html=True)
