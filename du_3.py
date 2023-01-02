import json
from pyproj import Transformer
from math import sqrt
from statistics import mean

wgs2jtsk=Transformer.from_crs(4326,5514, always_xy=True)

with open ("adresy.geojson", encoding="utf-8") as e,\
    open ("kontejnery.geojson", encoding="utf-8") as d: 
    data_e=json.load(e)
    #print (data_e)
    data_d=json.load(d)
    #print (data_f)

adresy=data_e['features']
adresy_l=list(adresy)

kontejnery=data_d['features']
kontejnery_l=list(kontejnery)

kontejnery_sez={}

for item in kontejnery_l:
    
    poloha_k=item['geometry']
    souradnice_k=poloha_k['coordinates']
    vlastnosti=item ['properties']
    id_k=vlastnosti['ID']
    pristup=vlastnosti['PRISTUP']
    seznam_k=[souradnice_k, pristup]
    if "volně" in pristup:
        kontejnery_sez[id_k]=souradnice_k
    else:
        continue

   
#print(kontejnery_sez)

adresy_sez={}
min_vzdalenosti=[]

for item in adresy_l:
    adresa=item ['properties']
    id_a=adresa['@id']
    ulice=adresa['addr:street']
    cislo=adresa['addr:housenumber']
    poloha_a=item['geometry']
    souradnice_a=poloha_a['coordinates']
    jtsk_a=[]
    jtsk_a=wgs2jtsk.transform(souradnice_a[0],souradnice_a[1])
    x1=abs(jtsk_a[0])
    y1=abs(jtsk_a[1])
    seznam_a=[ulice, cislo, jtsk_a]
    adresy_sez[id_a]=seznam_a
    vzdalenosti=[]
    for item in kontejnery_l:
        poloha_k=item['geometry']
        souradnice_k=poloha_k['coordinates']
        x2=abs(souradnice_k[0])
        y2=abs(souradnice_k[1])
        vzdalenost=sqrt(((abs(x2-x1))**2)+((abs(y2-y1))**2))
        vzdalenosti.append (vzdalenost)
    min_vzdalenost=min(vzdalenosti)
    min_vzdalenosti.append (min_vzdalenost)  
    #prumer_min_vzd=mean(min_vzdalenost)
    #print ("Pro adresu" ulice, cislo "je minimální vzdálenost ke kontejneru" min_vzdalenost)
    #print(f"Pro adresu {ulice} {cislo} je minimální vzdálenost ke kontejneru {min_vzdalenost} metrů") 

prum_min_vzdal=mean(min_vzdalenosti)
print(f"Průměrná minimální vzdálenost je pro danou čtvrť {prum_min_vzdal} metrů")

    
        


#print (adresy_sez)

#x1=abs(jtsk_a[0])
#y1=abs(jtsk_a[1])
#x2=abs(souradnice_k[0])
#y2=abs(souradnice_k[1])
#print(x,y,u,v)
#vzdalenost=sqrt(((abs(x2-x1))**2)+((abs(y2-y1))**2))
#print (vzdalenost)

