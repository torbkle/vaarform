import streamlit as st

def vis_bunnmeny():
    # === Sticky menystil ===
    st.markdown("""
    <style>
    .sticky-meny {
        position: sticky;
        top: 0;
        background-color: #f8f9fa;
        padding: 0.5rem 0;
        z-index: 999;
        border-bottom: 1px solid #ddd;
    }
    .sticky-meny .element-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 0.5rem;
    }
    @media (max-width: 768px) {
        .sticky-meny .element-container {
            flex-direction: column;
            align-items: center;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # === Sticky menyseksjon ===
    with st.container():
        st.markdown('<div class="sticky-meny">', unsafe_allow_html=True)

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.image("assets/icons/home.png", width=50)
            if st.button(" ", key="velkommen_knapp", help="Velkommen"):
                st.session_state.sidevalg = "Velkommen"

        with col2:
            if st.button("Dagens plan"):
                st.session_state.sidevalg = "Dagens plan"
        with col3:
            if st.button("Logg"):
                st.session_state.sidevalg = "Logg"
        with col4:
            if st.button("Fremgang"):
                st.session_state.sidevalg = "Fremgang"
        with col5:
            if st.button("Parvisning"):
                st.session_state.sidevalg = "Parvisning"

        col6, col7, col8, col9 = st.columns(4)

        with col6:
            if st.button("Ukesmål"):
                st.session_state.sidevalg = "Ukesmål"
        with col7:
            if st.button("Ukentlig oppsummering"):
                st.session_state.sidevalg = "Ukentlig oppsummering"
        with col8:
            if st.button("Rediger mål"):
                st.session_state.sidevalg = "Rediger mål"
        with col9:
            if st.button("Planlegger"):
                st.session_state.sidevalg = "Planlegger"

        st.markdown('</div>', unsafe_allow_html=True)
