import streamlit as st
from menydata import MENYVALG

def vis_meny():
    st.markdown("""
    <style>
    .ikon-knapp button {
        font-size: 20px !important;
        padding: 0.4rem 0.6rem;
        border-radius: 6px;
        background-color: #f0f0f0;
        border: 2px solid transparent;
    }
    .ikon-knapp button:hover {
        background-color: #e0e0e0;
    }
    .ikon-knapp button.aktiv {
        border-color: #003049;
        background-color: #dbe9f4;
    }
    </style>
    """, unsafe_allow_html=True)

    kolonner = st.columns(len(MENYVALG))

    for i, meny in enumerate(MENYVALG):
        navn = meny["navn"]
        ikon = meny.get("ikon", "❓")
        aktiv = st.session_state.get("sidevalg") == navn

        with kolonner[i]:
            with st.container():
                st.markdown('<div class="ikon-knapp">', unsafe_allow_html=True)
                if st.button(f"{ikon}", key=navn, help=navn):
                    st.session_state.sidevalg = navn
                st.markdown('</div>', unsafe_allow_html=True)
