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
# print(reclame_tekst2)
# vraag5
# print(reclame_tekst2[:62])
# vraag6
# print(reclame_tekst3.upper())
# vraag7
reclame_tekst3 = (reclame_tekst2[:62])
aanbieding2= (reclame_tekst3[58:])
# print(aanbieding2)
reclame_tekst4 = ["Vandaag", "in", "de", "aanbieding", "vanille-ijs,", "1 liter -", "slechts €",(aanbieding2)]
# print(reclame_tekst4)
# vraag8/9
# for el in reclame_tekst4:
#    print (el.lower())
# vraag10
for el in reclame_tekst4:
    if len(el) < 5:
        print (el.lower())
    else:
        print (el.upper())

