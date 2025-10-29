import streamlit as st
from menydata import MENYVALG

def vis_meny():
    st.markdown("""
    <style>
    .ikonmeny {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 0.5rem;
        margin: 0.5rem 0 1rem 0;
        padding: 0.5rem 0;
        border-bottom: 1px solid #ddd;
        background-color: #f8f9fa;
        position: sticky;
        top: 0;
        z-index: 999;
    }
    .ikonknapp {
        font-size: 24px;
        padding: 0.4rem 0.6rem;
        border-radius: 8px;
        background-color: #f0f0f0;
        border: 2px solid transparent;
        cursor: pointer;
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
            flex-direction: row;
            overflow-x: auto;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="ikonmeny">', unsafe_allow_html=True)

    for meny in MENYVALG:
        navn = meny["navn"]
        ikon = meny.get("ikon", "❓")
        aktiv = "aktiv" if st.session_state.get("sidevalg") == navn else ""
        knapp_html = f"""
        <form action="" method="post">
            <button class="ikonknapp {aktiv}" name="valg" value="{navn}" title="{navn}">{ikon}</button>
        </form>
        """
        st.markdown(knapp_html, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Håndter klikk
    if "valg" in st.session_state:
        st.session_state.sidevalg = st.session_state.valg
        del st.session_state.valg
