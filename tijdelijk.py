# vraag 1 t/m 4
mijn_dictonary = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5
}
prijsaardbei = mijn_dictonary["aardbei"]
aanbieding = str(prijsaardbei * 0.8)
reclame_tekst = "Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €"
reclame_tekst2 = reclame_tekst + aanbieding
print(reclame_tekst2)