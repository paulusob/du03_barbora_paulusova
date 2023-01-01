import json

with open ("adresy.geojson", encoding="utf-8") as f: 
    data_a=json.load(f)

adresy=data_a['features']
adresy_l=list(adresy)


adresy_sez={}

for item in adresy_l:
    adresa=item ['properties']
    id_a=adresa['@id']
    ulice=adresa['addr:street']
    cislo=adresa['addr:housenumber']
    poloha_a=item['geometry']
    souradnice_a=poloha_a['coordinates']
    seznam_a=[ulice, cislo, souradnice_a]
    adresy_sez[id_a]=seznam_a
    
    
print (adresy_sez)


with open ("kontejnery.geojson", encoding="utf-8") as f: 
    data_k=json.load(f)

kontejnery=data_k['features']
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
        kontejnery_sez[id_k]=seznam_k
    else:
        continue
    
print(kontejnery_sez)


