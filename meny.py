import streamlit as st
from menydata import MENYVALG

def vis_meny():
    st.markdown("""
    <style>
    .ikonmeny-wrapper {
        overflow-x: auto;
        white-space: nowrap;
        margin-bottom: 1rem;
        padding: 0.5rem 0;
        background-color: #f8f9fa;
        border-bottom: 1px solid #ddd;
    }
    .ikonmeny {
        display: flex;
        flex-direction: row;
        gap: 0.5rem;
        justify-content: center;
        align-items: center;
        min-width: max-content;
    }
    .ikonknapp {
        font-size: 20px;
        padding: 0.4rem 0.6rem;
        border-radius: 6px;
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
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="ikonmeny-wrapper"><div class="ikonmeny">', unsafe_allow_html=True)

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

    st.markdown('</div></div>', unsafe_allow_html=True)

    # Håndter klikk
    if "valg" in st.session_state:
        st.session_state.sidevalg = st.session_state.valg
        del st.session_state.valg
