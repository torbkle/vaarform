import streamlit as st
from menydata import MENYVALG

def vis_meny():
    st.markdown("""
    <style>
    .streamlit-button {
        font-size: 28px !important;
        padding: 0.4rem 0.6rem;
        border-radius: 8px;
        background-color: #f0f0f0;
        border: 2px solid transparent;
        transition: all 0.2s ease;
    }
    .streamlit-button:hover {
        background-color: #e0e0e0;
    }
    .streamlit-button.aktiv {
        border-color: #003049;
        background-color: #dbe9f4;
    }
    .ikonmeny {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 0.5rem;
        margin-bottom: 1rem;
    }
    @media (max-width: 768px) {
        .ikonmeny {
            flex-direction: column;
            align-items: center;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="ikonmeny">', unsafe_allow_html=True)

    for meny in MENYVALG:
        navn = meny["navn"]
        ikon = meny.get("ikon", "❓")
        aktiv = "aktiv" if st.session_state.get("sidevalg") == navn else ""
        if st.button(f"{ikon}", key=navn, help=navn):
            st.session_state.sidevalg = navn

    st.markdown('</div>', unsafe_allow_html=True)
