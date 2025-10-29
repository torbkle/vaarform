def vis_dagens_plan():
    st.image("assets/bilde_dagens_plan.png", use_container_width=True)

    bruker = APP["standard_bruker"]
    idag = date.today().isoformat()

    response = supabase.table("treningsplan").select("*").eq("bruker", bruker).eq("dato", idag).execute()
    økter = response.data

    if not økter:
        st.info("Ingen planlagt økt i dag.")
        return

    økt = økter[0]
    aktivitet = økt["aktivitet"].lower()
    ikon_fil = f"{IKONER['mappe']}{aktivitet}.png"

    if os.path.exists(ikon_fil):
        st.image(ikon_fil, width=IKONER["størrelse"])
    else:
        fallback = f"{IKONER['mappe']}{IKONER['standard']}"
        if os.path.exists(fallback):
            st.image(fallback, width=IKONER["størrelse"])
        else:
            st.error("Standardikon mangler også. Sjekk assets/icons/.")

    st.markdown(f"**Aktivitet:** {økt['aktivitet']}")
    st.markdown(f"**Økt:** {økt['beskrivelse']}")

    # ✅ Enkel knapp for å registrere økten
    if st.button("✅ Fullført"):
        st.success("Økten er registrert. God innsats!")
