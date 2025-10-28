from db import lagre_treningsøkt

def test_supabase():
    response = lagre_treningsøkt(
        bruker="Torbjørn",
        aktivitet="Testøkt",
        varighet=30,
        distanse=5.0,
        kommentar="Test fra Streamlit"
    )
    st.write("Respons:", response)
