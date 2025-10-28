# test_logg_import.py

print("🔍 Tester import av funksjoner fra logg.py...")

try:
    from logg import (
        init_logg,
        skriv_logg,
        vis_parlogg,
        vis_ukesoppsummering,
        vis_ukemaal,
        vis_fremgang,
        rediger_maal
    )
    print("✅ Alle funksjoner importert uten feil.")
except ImportError as e:
    print("❌ ImportError:", e)
except SyntaxError as e:
    print("❌ SyntaxError:", e)
except Exception as e:
    print("❌ Annen feil:", e)
