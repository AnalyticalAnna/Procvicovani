""" Úkol 2 🐱 🐈
Tvojou úlohou bude napísať program, ktorý získa pomocou API 10 náhodných faktov 
o mačkách a uloží ich do súboru vo formáte JSON. """

import requests
import json

# Získáváme 10 náhodných informací o kočkách z internetu a zapisujeme do souboru. 
# V případě příliš krátkého času na odezvu vrátí hlášku, aby byl zvýšen časový limit.
try:
    response = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=10', timeout=1)
    data = response.json()
    with open("fakta_kocky.json", mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
except requests.exceptions.RequestException:
    data = [{"text":"Data nebyla zapsána, byl příliš krátký čas pro odezvu."}]
    print("Jste příliš nedočkaví! Zkuste zvýšit časový limit.")

# Ze souboru získáme pouze požadivaná fakta - hodnoty pro klíč "text" a zapíšeme je do seznamu.
seznam_faktu = []
for slovnik in data:
    seznam_faktu.append(slovnik["text"])
with open("fakta_kocky_10.json", mode = "w", encoding = "utf-8") as file:
    json.dump(seznam_faktu, file, indent=4)

# Seznam očíslujeme.
ocislovany_seznam = [f"{i+1}. {text}" for i, text in enumerate(seznam_faktu)]

# Zapíšeme očíslovaný seznam do souboru
with open("kocici_fakta.json", mode = "w", encoding = "utf-8") as file:
    json.dump(ocislovany_seznam, file, indent=4)

print(ocislovany_seznam)