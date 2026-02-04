def decoreer(tekst=""):
    lengte = len(tekst)+4
    print()
    print(lengte*"*")
    print(f"* {tekst} *")
    print(lengte*"*")
    print()
# next
def fooi_pp(bedrag,personen):
    bedrag_pp = bedrag / personen
    return f"Het bedrag per persoon is {bedrag_pp} euro"
def onderstreep (tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "-")
    return uit
def som (input):
    totaal = 0
    for k, v in input.items():
        totaal = totaal + v
    return totaal
