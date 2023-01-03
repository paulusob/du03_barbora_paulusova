import sys 
import os
import json
from pyproj import Transformer
from math import sqrt
from statistics import mean

wgs2jtsk=Transformer.from_crs(4326,5514, always_xy=True)

def overeni_obsahu (vstupni_soubor):
    if os.stat(vstupni_soubor).st_size>0:
        print (f"Soubor {vstupni_soubor} načten")
    else:
        print (f"Vstupní soubor {vstupni_soubor} je prázdný")
        sys.exit()

def wgs_to_jtsk (souradnice):
    jtsk=[]
    jtsk=wgs2jtsk.transform(souradnice[0],souradnice[1])
    return jtsk

def get_x (souradnice):
    x=abs(souradnice[0])
    return x 

def get_y (souradnice):
    y=abs(souradnice[1])
    return y 


    
