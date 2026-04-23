roster = [
    {"name": "Maria", "gwa": 1.50},
    {"name": "Juan",  "gwa": 2.25},
    {"name": "Ana",   "gwa": 1.75},
]

highest = min(roster, key = lambda score: score["gwa"])
lowest = max(roster, key = lambda score: score["gwa"])


sorted_gwa = sorted(roster, key = lambda score: score["gwa"])

print(sorted_gwa)
    

for s in sorted_gwa:
    print(f"{s["name"]} : {s["gwa"]}")
    
    
    
ranking = lambda s: "Summa" if s["gwa"] <= 1.25 else "Magna" if s["gwa"] <= 1.50 else "Good Standing"


#print(highest)
#print(lowest)
