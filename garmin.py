# garmin.py
import datetime
import random

def hent_mock_økt(bruker="Torbjørn"):
    """Returnerer en simulert treningsøkt med Garmin-lignende data."""
    return {
        "bruker": bruker,
        "dato": datetime.date.today().isoformat(),
        "aktivitet": random.choice(["Løping", "Sykling", "Styrke"]),
        "varighet_min": random.randint(20, 60),
        "distanse_km": round(random.uniform(3.0, 10.0), 1),
        "gjennomsnittspuls": random.randint(110, 160),
        "kalorier": random.randint(200, 600),
    }

def synkroniser_økt(supabase_client, data):
    """Lagrer økten i Supabase-tabellen 'garmin_data'."""
    response = supabase_client.table("garmin_data").insert(data).execute()
    return response
