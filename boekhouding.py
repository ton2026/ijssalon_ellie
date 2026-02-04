# boekhouding
import csv
from presentatie import presenteer
from helper import *
mijn_dictionary = {
    "Aardbeien-ijs-totaal": 1000,
    "Vanille-ijs-totaal": 2000,
    "Chocolade-ijs-totaal": 1500,
    "Waterijsjes-totaal": 750,
}
totaal_inkomsten=som(mijn_dictionary)
print (presenteer(mijn_dictionary,totaal_inkomsten))
# next
with open('boekhouding.csv', 'w',newline='') as csvfile:
    for key, value in mijn_dictionary.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value])