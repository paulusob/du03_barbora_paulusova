
import sys 
import os
from pyproj import Transformer
import json

def valid_nact_json (vstupni_soubor, parametr):
    try:
        data=json.load (parametr)
        return data
    except ValueError:
        print (f"Soubor {vstupni_soubor} není validní json")
        sys.exit()



def overeni_obsahu (vstupni_soubor):
    if os.stat(vstupni_soubor).st_size==0:
        print (f"Vstupní soubor {vstupni_soubor} je prázdný")
        sys.exit()

def wgs_to_jtsk (souradnice):
    wgs2jtsk=Transformer.from_crs(4326,5514, always_xy=True)
    jtsk=wgs2jtsk.transform(souradnice[0],souradnice[1])
    return jtsk

def get_x (souradnice):
    x=abs(souradnice[0])
    return x 

def get_y (souradnice):
    y=abs(souradnice[1])
    return y 

def overeni_jtsk (x,y):
    if x > 1000000 and x < 40000:
        print ("Souřadnice x jsou v rozmezí mimo ČR")
        sys.exit()
    if y > 1300000 and y < 900000:
        print ("Souřadnice y jsou v rozmezí mimo ČR")
        sys.exit()

