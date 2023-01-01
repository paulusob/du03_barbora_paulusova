import json

with open ("adresy.geojson", encoding="utf-8") as f: 
    data_a=json.load(f)

adresy=data_a['features']
adresy_l=list(adresy)
#for y in adresy_l:
    #print(y)
#ulice=data['addr:street']
#print (adresy)
#print (adresy_l)

adresy_sez={}

for item in adresy_l:
    adresa=item ['properties']
    id_a=adresa['@id']
    ulice=adresa['addr:street']
    cislo=adresa['addr:housenumber']
    poloha_a=item['geometry']
    souradnice_a=poloha_a['coordinates']
    seznam=[ulice, cislo, souradnice_a]
    adresy_sez[id_a]=seznam
    
    
print (adresy_sez)



with open ("kontejnery.geojson", encoding="utf-8") as f: 
    data_k=json.load(f)

kontejnery=data_k['features']
kontejnery_sez=[]
for item in kontejnery:
    poloha_k=item['geometry']
    souradnice_k=poloha_k['coordinates']
    kontejnery_sez.append(souradnice_k)
#print(kontejnery_sez)


