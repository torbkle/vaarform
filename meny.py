import streamlit as st

def vis_bunnmeny():
    st.markdown("---")
    st.markdown("### Navigasjon")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(
            """
            <div style="text-align:center">
                <form action="" method="post">
                    <button type="submit" style="background:none;border:none;padding:0;" name="valg" value="Velkommen">
                        <img src="assets/icons/home.png" width="50" style="cursor:pointer;">
                    </button>
                </form>
            </div>
            """,
            unsafe_allow_html=True
        )

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

    # Håndter klikk fra HTML-form
    if "valg" in st.session_state:
        st.session_state.sidevalg = st.session_state.valg
        del st.session_state.valg
