""" Úkol 2 🐱 🐈
Tvojou úlohou bude napísať program, ktorý získa pomocou API 10 náhodných faktov 
o mačkách a uloží ich do súboru vo formáte JSON. """

# Spravne reseni!
# Par podnetu k zamysleni:
#   - Ktere hodnoty v kodu by bylo vhodne definovat jako konstanty?
#   - Seznam prochazime dvakrat (1. vytazeni 'text', 2. ocislovani); dalo by se zaridit, aby byl pruchod seznamem jen jeden?
#   - Ukladat vsechny mezistavy do souboru bylo urcite vyhodne pro ladeni programu, ale pro zadani to neni nutne.
#     Co kdybychom chteli u kazdeho zapisu take osetrovat pripadne vyjimky (napr. nedostatecna prava pro zapis)?
#     Mozna by bylo lepsi program strukturovat tak, aby byly jednotlive kroky oddelene:
#       1. Ziskani dat z endpointu vcetne osetreni vyjimek (v pripade vyjimky program ukoncit)
#       2. Transformace dat do tvaru pro zapis
#       3. Zapis vysledneho souboru
#     Pro jednotlive kroky (ne nutne vsechny) by se pak nabizelo pouziti funkci.

import requests
import json

# Získáváme 10 náhodných informací o kočkách z internetu a zapisujeme do souboru. 
# V případě příliš krátkého času na odezvu vrátí hlášku, aby byl zvýšen časový limit.
try:
    response = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=10', timeout=5)
    data = response.json()
    with open("fakta_kocky.json", mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    # (Kvuli citelnosti byva zvykem odsazovat komentare stejne jako okolni kod.)
    # Ze souboru získáme pouze požadovaná fakta - hodnoty pro klíč "text" a zapíšeme je do seznamu.
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

# Program upozorní, pokud čas pro odezvu serveru je příliš krátký.
except requests.exceptions.RequestException:
    print("Jste příliš nedočkaví! Zkuste zvýšit časový limit.")
