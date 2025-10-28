from supabase import create_client
import datetime

SUPABASE_URL = "https://zewmjurylmyjweyqotpw.supabase.co"  # ← bytt ut med din faktiske URL
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inpld21qdXJ5bG15andleXFvdHB3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk0MDAwOTYsImV4cCI6MjA3NDk3NjA5Nn0.4awJMuo5KHQM1-i0EaIZC0Gf8q9hQYwqRqZc10IWc2o"  # ← bytt ut med din faktiske nøkkel

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

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
