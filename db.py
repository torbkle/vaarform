import datetime
import streamlit as st
from supabase import create_client

# Opprett klient med verdier fra secrets.toml
supabase = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

def lagre_treningsøkt(bruker, aktivitet, varighet, distanse, kommentar):
    data = {
        "bruker": bruker,
        "dato": datetime.date.today().isoformat(),
        "aktivitet": aktivitet,
        "varighet": varighet,
        "distanse": distanse,
        "kommentar": kommentar
    }
    response = supabase.table("treningslogg").insert(data).execute()
    return response
