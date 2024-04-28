""" Úkol 1
Tvým úkolem bude vytvořit 4 třídy, které budou dohromady tvořit zoologickou zahradu. 
Doporučovala bych postupovat v pořadí ve kterém jsou třídy napsaný níže, bude to dávat největší smysl. 
Dodrzuj správnou strukturu souboru, tedy definice tříd děj nahoru pod sebe, samotné vytváření objektu a případné asserty na konec. 
Typování je dobrovolné. 

Třída Zvire 🦁 🐼 🐍
Tato třída bude obsahovat atributy jmeno:str, druh:str a vaha:int. Všechny parametry jsou povinné a budou se nastavovat v metodě __init__()

Dále přidej třídě Zvire:

metodu __str__(), formát výpisu je na tobě
metodu export_to_dict(), která vratí reprezentaci zvířete jako slovník, například takto:
pavouk = Zvire('Adolf', 'Tarantule Velká', 0.1)
pavouk_export = pavouk.export_to_dict()
assert pavouk_export['jmeno'] == 'Adolf'
assert pavouk_export['druh'] == 'Tarantule Velká'
assert pavouk_export['vaha'] == 0.1
Vytvoř objekty typu Zvire z následujícího seznamu slovníků. Použij for cyklus, můžeš (ale nemusíš) to napsat jako funkci. Výsledkem bude list obsahující 4 objekty typu Zvire.

zvirata_dict = [
    {'jmeno': 'Růženka', 'druh': 'Panda Velká', 'vaha': 150},
    {'jmeno': 'Vilda', 'druh': 'Vydra Mořská', 'vaha': 20},
    {'jmeno': 'Matýsek', 'druh': 'Tygr Sumaterský', 'vaha': 300},
    {'jmeno': 'Karlík', 'druh': 'Lední medvěd', 'vaha': 700},

]
Třída Zamestnanec 🧑‍🤝‍🧑
Tato třída bude obsahovat atributy cele_jmeno:str, rocni_plat:int a pozice:str. Všechny parametry jsou povinné a budou se nastavovat v metodě __init__()

Zaměstnanci dále přidej:

metodu __str__(), formát výpisu je na tobě
metodu ziskej_inicialy(), která bude vracet výstup ve formátu A.W., uvažuj pouze změstnance se dvěma jmény.
Vytvoř objekty typu Zamestnanec z následujícího seznamu slovníků. Použij for cyklus, můžeš (ale nemusíš) to napsat jako funkci. Výsledkem bude list obsahující 3 objekty typu Zamestnanec.

zamestnanci_dict = [
    {'cele_jmeno': 'Tereza Vysoka', 'rocni_plat': 700_000, 'pozice': 'Cvičitelka tygrů'},
    {'cele_jmeno': 'Anet Krasna', 'rocni_plat': 600_000, 'pozice': 'Cvičitelka vyder'},
    {'cele_jmeno': 'Martin Veliky', 'rocni_plat': 650_000, 'pozice': 'Cvičitel ledních medvědů'},
]
Třída Reditel 🧑‍💼
Tato třída bude dědit od třídy Zamestnanec, jediné co bude mít navíc je parametr oblibene_zvire: Zvire, parametr bude typu Zvire (třída kterou jsi už vytvořil/a). Parametr pozice rovnou nastav na 'Reditel'.

# Priklad vytvoreni objektu (klidne zkopiruj)
zvire = Zvire()
reditel = Reditel(jmeno='Karel', rocni_plat=800_000, oblibene_zvire=zvire)
assert reditel.pozice == 'Reditel'
assert isinstance(reditel.oblibene_zvire, Zvire)
Třída Zoo 🏡
Třída Zoo bude mít 5 atributů:

jmeno:str
adresa:str
reditel: Reditel - objekt typu Reditel
zamestnanci: List[Zamestnanec] - list objektů typu Zamestnanec (naši vytvoření zaměstnanci)
zvirata: List[Zvire] - list objektů typu Zvire (naše vytvořená zvířata)
a dvě metody:

*vaha_vsech_zvirat_v_zoo() - vrací číslo reprezentující součet váhy všech zvířat v zoologické zahradě *mesicni_naklady_na_zamestnance() - vrací číslo reprezentující měsíční náklady na zaměstnance zoologické zahrady (Nezapomeň na ředitele!)

Příklad použití třídy:

zoo = Zoo('ZOO Praha', 'U Trojského zámku 3/120', reditel, zamestnanci, zvirata)

print(zoo.reditel)
print('Celková váha zvířat v ZOO:', zoo.vaha_vsech_zvirat_v_zoo())
print('Měsíční náklady na zaměstnance:', zoo.mesicni_naklady_na_zamestnance())

"""

class Zvire:
    def __init__ (self, jmeno:str, druh:str, vaha:int):
        self.jmeno = jmeno
        self.druh = druh
        self.vaha = vaha

    def __str__(self):
        return f"Jméno zvířete je {self.jmeno}, jedná se o druh {self.druh} a jeho váha je {self.vaha} kg."
    
# Vrací reprezentaci zvířete jako slovník.
    def export_to_dict(self):
        return {"jmeno":self.jmeno,
               "druh":self.druh,
               "vaha":self.vaha}
        
class Zamestnanec:
    def __init__ (self, cele_jmeno:str, rocni_plat:int, pozice:str):
        self.cele_jmeno = cele_jmeno
        self.rocni_plat = rocni_plat
        self.pozice = pozice
    def __str__(self):
        return f"Jméno zaměstnance je {self.cele_jmeno}, jeho pozice je {self.pozice} a jeho roční plat je {self.rocni_plat} Kč."
    
# Vrací inciály ve rofmě A.W. Pokud zaměstnanec nemá 2 jména, vrátí to komentář.
    def ziskej_inicialy(self):
        rozdelene_jmeno = self.cele_jmeno.split()
        if len(rozdelene_jmeno) == 2:
            krestni_jmeno, prijmeni = rozdelene_jmeno
            return f"{krestni_jmeno[0]}.{prijmeni[0]}."
        else:
            return"Jméno musí být dvouslovné (křestní jméno a příjmení)."

# Tato třída bude dědit od třídy Zamestnanec, jediné co bude mít navíc je parametr oblibene_zvire: Zvire, 
# parametr bude typu Zvire (třída kterou jsi už vytvořil/a). Parametr pozice rovnou nastav na 'Reditel' 
class Reditel (Zamestnanec):
    def __init__ (self, cele_jmeno, rocni_plat, oblibene_zvire:Zvire, pozice="Reditel"):
        super().__init__(cele_jmeno, rocni_plat, pozice)
        self.oblibene_zvire = oblibene_zvire

class Zoo:
    def __init__ (self, jmeno:str, adresa:str, reditel: Reditel, zamestnanci: list[Zamestnanec], zvirata: list[Zvire]):
        self.jmeno = jmeno
        self.adresa = adresa
        self.reditel = reditel
        self.zamestnanci = zamestnanci
        self.zvirata = zvirata

# U celkové váhy mi to háže chybu. Nevím proč? Přitom když jsem jen spustila příkaz pro součet váhy, tak mi vypadlo, že 150, tak tomu nerozumím.

    def vaha_vsech_zvirat_v_zoo(self):
        celkova_vaha = sum(z.vaha for z in self.zvirata)
        print(f"Celková váha všech zvířat je {celkova_vaha} kg.")

    def mesicni_naklady_na_zamestnance(self):
        mesicni_naklady_zamestnanci = sum(zam.rocni_plat / 12 for zam in self.zamestnanci)
        mesicni_naklady_reditel = self.reditel.rocni_plat / 12
        mesicni_naklady = mesicni_naklady_zamestnanci + mesicni_naklady_reditel
        return mesicni_naklady

# Úkoly pro část Zvíře.

""" Vytvoř objekty typu Zvire z následujícího seznamu slovníků. 
Použij for cyklus, můžeš (ale nemusíš) to napsat jako funkci. 
Výsledkem bude list obsahující 4 objekty typu Zvire. """

# Vytvoření objektů typu Zvire z daného seznamu slovníků
# Seznam slovníků s informacemi o zvířatech
zvirata_dict = [
    {'jmeno': 'Růženka', 'druh': 'Panda Velká', 'vaha': 150},
    {'jmeno': 'Vilda', 'druh': 'Vydra Mořská', 'vaha': 20},
    {'jmeno': 'Matýsek', 'druh': 'Tygr Sumaterský', 'vaha': 300},
    {'jmeno': 'Karlík', 'druh': 'Lední medvěd', 'vaha': 700},
]

# Vytvoření objektů zypu Zvire z informací ve slovnících
zvirata = []
for zvire_info in zvirata_dict:
    zvire_nove = Zvire(zvire_info['jmeno'], zvire_info['druh'], zvire_info['vaha'])
    zvirata.append(zvire_nove)

# Vypsání informací o zvířatech
for zvire_nove in zvirata:
    print (f"Jméno zvířete je {zvire_nove.jmeno}, jedná se o druh {zvire_nove.druh} a jeho váha je {zvire_nove.vaha} kg.")

print(zvire_nove)

# Úkoly pro část Zaměstnanec.

# Vytvoření objektů typu Zamestnanec z informací ve slovnících
zamestnanci_dict = [
    {'cele_jmeno': 'Tereza Vysoka', 'rocni_plat': 700_000, 'pozice': 'Cvičitelka tygrů'},
    {'cele_jmeno': 'Anet Krasna', 'rocni_plat': 600_000, 'pozice': 'Cvičitelka vyder'},
    {'cele_jmeno': 'Martin Veliky', 'rocni_plat': 650_000, 'pozice': 'Cvičitel ledních medvědů'},
]

zamestnanci = []
for zamestnanci_info in zamestnanci_dict:
    zamestnanec_nove = Zamestnanec(zamestnanci_info['cele_jmeno'], zamestnanci_info['rocni_plat'], zamestnanci_info['pozice'])
    zamestnanci.append(zamestnanec_nove)

# Vypsání informací o zaměstnancích.
for zamestnanec_nove in zamestnanci:
    print (f"Jméno zaměstnance je {zamestnanec_nove.cele_jmeno}, jeho pozice je {zamestnanec_nove.pozice} a jeho roční plat je {zamestnanec_nove.rocni_plat} Kč.")

print(zamestnanec_nove)

zamestnanec_nove.ziskej_inicialy()

# Část Ředitel

zvire = Zvire('Adolf', 'Tarantule Velká', 0.1)
reditel = Reditel(cele_jmeno='Karel', rocni_plat=800_000, oblibene_zvire=zvire)
assert reditel.pozice == 'Reditel'
assert isinstance(reditel.oblibene_zvire, Zvire)

# Část Zoo

zoo = Zoo('ZOO Praha', 'U Trojského zámku 3/120', reditel, zamestnanci, zvirata)

print(zoo.reditel)
print('Celková váha zvířat v ZOO:', zoo.vaha_vsech_zvirat_v_zoo())
print('Měsíční náklady na zaměstnance:', zoo.mesicni_naklady_na_zamestnance())


# Asserty

# Zvire class
zvire = Zvire('Láďa', 'Koala', 15)
assert hasattr(zvire, 'jmeno')
assert hasattr(zvire, 'druh')
assert hasattr(zvire, 'vaha')
assert isinstance(zvire.jmeno, str)
assert isinstance(zvire.druh, str)
assert isinstance(zvire.vaha, int)
assert zvire.export_to_dict() == {'jmeno': 'Láďa', 'druh': 'Koala', 'vaha': 15}

# Zamestnanec class
zamestnanec = Zamestnanec('Petr Novak', 50000, 'Programator')
assert hasattr(zamestnanec, 'cele_jmeno')
assert hasattr(zamestnanec, 'rocni_plat')
assert hasattr(zamestnanec, 'pozice')
assert isinstance(zamestnanec.cele_jmeno, str)
assert isinstance(zamestnanec.rocni_plat, int)
assert isinstance(zamestnanec.pozice, str)
assert zamestnanec.ziskej_inicialy() == 'P.N.'

# Reditel class
zvire = Zvire('Lev', 'Lvice', 150)
reditel = Reditel('Jan Novotny', 80000, zvire)
assert isinstance(reditel.oblibene_zvire, Zvire)

# Zoo class
zoo = Zoo('Zoo Praha', 'Praha', reditel, [zamestnanec], [zvire])
assert hasattr(zoo, 'jmeno')
assert hasattr(zoo, 'adresa')
assert hasattr(zoo, 'reditel')
assert hasattr(zoo, 'zamestnanci')
assert hasattr(zoo, 'zvirata')
assert isinstance(zoo.jmeno, str)
assert isinstance(zoo.adresa, str)
assert isinstance(zoo.reditel, Reditel)
assert isinstance(zoo.zamestnanci, list)
assert isinstance(zoo.zvirata, list)
# zoo.vaha_vsech_zvirat_v_zoo() -> Celková váha všech zvířat je 150 kg.
assert zoo.vaha_vsech_zvirat_v_zoo() == 150
assert zoo.mesicni_naklady_na_zamestnance() == (zamestnanec.rocni_plat + reditel.rocni_plat) / 12