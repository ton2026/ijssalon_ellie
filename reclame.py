from algemene_functies import mijn_functie_2
def aanbieding_1(smaak,prijs,korting):
    lager = prijs - prijs*korting
    text = f"Vandaag in de annbieding: emmertje ijs ( 1 liter) in de smaak {smaak} , van {prijs} euro voor {lager}0 euro"
    return text
print (aanbieding_1("aardbei",4,0.1))
# next
def inkomsten_totaal (a,b,c,d,e,f,g):
    inkomsten = a+b+c+d+e+f+g
    return inkomsten
print (inkomsten_totaal(220,430,125,160,205,90,345))
# next
def inkomsten_totaal (a,b,c,d,e,f,g):
    inkomsten = a+b+c+d+e+f+g
    btw_p = 0.09
    bedrag = inkomsten * btw_p
    text = f"Het totaal van all inkomsten van deze week is {inkomsten} euro, waarover {bedrag} euro btw betaald dient te worden."
    return text
print (inkomsten_totaal(220,430,125,160,205,90,345))
# next
def laag_en_hoog (a,b,c,d,e,f,g):
    max_val = max(a,b,c,d,e,f,g)
    min_val = min(a,b,c,d,e,f,g)
    text = f"De hoogste waarde is {max_val} en de laagste waard is {min_val}."
    return text
print (laag_en_hoog(220,430,125,160,205,90,345))
# next
def gemiddelde (a,b,c,d,e,f,g):
    inkomsten = a+b+c+d+e+f+g
    gemiddelde = inkomsten/7
    text = f"De gemiddelde inkonsten deze week zijn {gemiddelde} euro."
    return text
print (gemiddelde(220,430,125,160,205,90,345))
# next
def meervoudig (a,b,c,d,e,f,g):
    return laag_en_hoog (a,b,c,d,e,f,g)
print (meervoudig(10,5,3,2,1,2,9))
#next
korte_lijst = []
def combinatie (invoer_lijst_2):
    global korte_lijst
    korte_lijst = [laag_en_hoog (invoer_lijst_2)]
    return
# volgende regel geeft error !!
# print (mijn_functie_2(combinatie (korte_lijst)))




