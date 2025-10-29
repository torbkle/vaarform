import streamlit as st
from meny import vis_meny
from forside import vis_forside
from dagens_plan import vis_dagens_plan
from logg import vis_logg
from innstillinger import vis_innstillinger

def main():
    st.set_page_config(page_title="VårForm", page_icon="🏋️", layout="centered")

    if "sidevalg" not in st.session_state:
        st.session_state.sidevalg = "Forside"

    vis_meny()

    if st.session_state.sidevalg == "Forside":
        vis_forside()
    elif st.session_state.sidevalg == "Dagens plan":
        vis_dagens_plan()
    elif st.session_state.sidevalg == "Logg":
        vis_logg()
    elif st.session_state.sidevalg == "Innstillinger":
        vis_innstillinger()

if __name__ == "__main__":
    main()

