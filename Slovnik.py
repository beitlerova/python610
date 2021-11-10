######## slovnik
muj_slovnik = {"jmeno": "Matous", "registrovany": True, "vek": 100}
print(muj_slovnik)
# zapis - {"klic1" : hodnota1, "klic2 : hodnota2}
# hodnota muze byt str, int, bool,...

# najiti hodnoty klice
print(muj_slovnik["jmeno"])  # odpoved: "Matous"

# prazdny slovnik
slovnik1 = {}

# pridani klice a hodnoty, prepis hodnoty
slovnik1["prace"] = "ajtak"  # vytvori se nova dvojice
print(slovnik1)
slovnik1["prace"] = "programator"  # prepise se puvodni hodnota
print(slovnik1)

# zapis hodnot - temer cokoliv, tuple, slovnik, bool, int
slovnik1["kontaktni_udaje"] = ("+420582582582", "matous@matous.cz")
print(slovnik1["kontaktni_udaje"])

# vnoreni, nestovani - do slovniku muzu jako hodnotu vlozit slovnik
kontakty = {"mobil" : 123456789, "email" : "a@b.cd"}
slovnik1["kontakt"] = kontakty
print(slovnik1["kontakt"]) # vypise cely vnoreny slovnik
print(slovnik1["kontakt"]["mobil"]) # vypise z vnoreneho slovniku jen hodnotu pozadovaneho klice

# metody slovniku
slovnik1["pozice"] = "manazer"
print(slovnik1)
print(slovnik1.items()) # .items - vypise list dvojic
print(slovnik1.get("prace")) # vypise hodnotu klice
print(slovnik1.pop("kontaktni_udaje")) # odstrani dvojici zadaneho klice a vypise hodnotu
print(slovnik1) #zde jiz odstraneno

######## sety, mnoziny
# je to datovy typ
# zapis: muj_set = {"zena", "ruze", "pisen", "kost"}
# slozene zavorky, jednotlive hodnoty, oddeleno carkami
# lze s nimi delat klasicke operce s mnozinami - prunik, hledat duplicity, hledat unikaty,...
# je mutable (menitelny)

# prazdny set
set1 = set()
# set s hodnotami
set2 = {"predseda", "soudce"}
print(set2)
#lze delat z jiz hotovych listu a tuplu
list1 = ["mesto", "more"]
tupl1 = ("kure", "staveni")
set3 = set(list1)
set4 = set(tupl1)
print(set3)
print(set4)

# metody setu
set_a = {"zena", "ruze", "kost", "pisen", "Lucie", "Matous"}
set_b = {"zena", "ruze", "kost", "pisen", "Lukas"}
print(set_a.union(set_b))  # sjednoceni
print(set_a.intersection(set_b))  # prunik
print(set_a.symmetric_difference(set_b))  # rozdil
print(set_a.difference(set_b))  # a - b

# pridavani a odebirani hodnot - metoda .add
set_a.add("Zuzana")
print(set_a)
set_a.add(["mesto","more"])
print(set_a)
set_a.add(tupl1)
print(set_a)




