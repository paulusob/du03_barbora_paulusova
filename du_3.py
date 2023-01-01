import json

with open ("adresy.geojson", encoding="utf-8") as f: 
    data_a=json.load(f)

adresy=data_a['features']
#ulice=data['addr:street']
#print (adresy)


adresy_sez=[]
for item in adresy:
    adresa=item ["properties"]
    ulice=adresa["addr:street"]
    cislo=adresa["addr:housenumber"]
    adresy_sez.append(ulice)
    adresy_sez.append(cislo)
    poloha_a=item["geometry"]
    souradnice_a=poloha_a["coordinates"]
    adresy_sez.append(souradnice_a)
print (adresy_sez)

with open ("kontejnery.geojson", encoding="utf-8") as f: 
    data_k=json.load(f)

kontejnery=data_k['features']
kontejnery_sez=[]
for item in kontejnery:
    poloha_k=item['geometry']
    souradnice_k=poloha_k['coordinates']
    kontejnery_sez.append(souradnice_k)
print(kontejnery_sez)


