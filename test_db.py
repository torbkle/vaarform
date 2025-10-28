from db import lagre_treningsøkt

# Testdata
aktivitet = "Testøkt"
varighet = 45
distanse = 5.2
kommentar = "Dette er en test"
bruker = "Torbjørn"

# Kjør test
response = lagre_treningsøkt(bruker, aktivitet, varighet, distanse, kommentar)

# Skriv ut resultat
print("Respons fra Supabase:", response)
