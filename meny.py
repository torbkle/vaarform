import streamlit as st

def vis_bunnmeny():
    st.markdown("""
    <style>
    .hamburger {
        font-size: 24px;
        cursor: pointer;
        background-color: transparent;
        border: none;
        margin: 0.5rem 0;
    }
    .menyvalg {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        justify-content: center;
        margin-bottom: 1rem;
    }
    @media (max-width: 768px) {
        .menyvalg {
            flex-direction: column;
            align-items: center;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # === Toggle menyvisning ===
    if "vis_meny" not in st.session_state:
        st.session_state.vis_meny = False

    if st.button("☰", key="hamburger", help="Meny"):
        st.session_state.vis_meny = not st.session_state.vis_meny

    # === Menyvalg ===
    if st.session_state.vis_meny:
        with st.container():
            st.markdown('<div class="menyvalg">', unsafe_allow_html=True)

            if st.button("Velkommen"):
                st.session_state.sidevalg = "Velkommen"
            if st.button("Dagens plan"):
                st.session_state.sidevalg = "Dagens plan"
            if st.button("Logg"):
                st.session_state.sidevalg = "Logg"
            if st.button("Fremgang"):
                st.session_state.sidevalg = "Fremgang"
            if st.button("Parvisning"):
                st.session_state.sidevalg = "Parvisning"
            if st.button("Ukesmål"):
                st.session_state.sidevalg = "Ukesmål"
            if st.button("Ukentlig oppsummering"):
                st.session_state.sidevalg = "Ukentlig oppsummering"
            if st.button("Rediger mål"):
                st.session_state.sidevalg = "Rediger mål"
            if st.button("Planlegger"):
                st.session_state.sidevalg = "Planlegger"

            st.markdown('</div>', unsafe_allow_html=True)
