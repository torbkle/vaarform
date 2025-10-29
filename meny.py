import streamlit as st
from menydata import MENYVALG

def vis_meny():
    st.markdown("""
    <style>
    .ikonmeny {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 1rem;
        margin-bottom: 1.5rem;
    }
    .ikonknapp {
        font-size: 28px;
        background-color: #f0f0f0;
        border: 2px solid transparent;
        border-radius: 8px;
        padding: 0.5rem 0.75rem;
        cursor: pointer;
        text-align: center;
        transition: all 0.2s ease;
    }
    .ikonknapp:hover {
        background-color: #e0e0e0;
    }
    .ikonknapp.aktiv {
        border-color: #003049;
        background-color: #dbe9f4;
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
        st.markdown(f'<div class="ikonknapp {aktiv}">{ikon}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
