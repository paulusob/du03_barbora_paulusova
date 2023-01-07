# Program pro výpočet vzdálenosti ke kontejnerům na tříděný odpad

# import funkcí a potřebných knihoven
from funkce import overeni_obsahu, wgs_to_jtsk, get_x, get_y, overeni_jtsk, valid_nact_json, overeni_exist_pristup
import json
from math import sqrt
from statistics import mean
import sys 

# otevření souborů s daty a jejich načtení do proměnných, ošetření nenalezení souboru a přístupových práv

overeni_exist_pristup ("adresy.geojson")
overeni_exist_pristup ("kontejnery.geojson")


with open ("adresy.geojson", encoding="utf-8") as a,\
    open ("kontejnery.geojson", encoding="utf-8") as k: 
        
    # ověření, zda některý ze souborů není prázdný 
    overeni_obsahu ("adresy.geojson")
    overeni_obsahu ("kontejnery.geojson")
        
    print ("Vstupní soubory byly načteny")
    # přepsání dat
    data_adresy = valid_nact_json ("adresy.geojson", a)
    data_kontejnery = valid_nact_json ("kontejnery.geojson", k)
        
    
# načtení dat do listů, ošetření neočekávaného formátu 
try: 
    adresy=list(data_adresy['features'])
    kontejnery=list(data_kontejnery['features'])

    # vytvoření slovníků pro vyhledávání a proměnných pro přiřazení maximální vzdálenosti a kumulativní vzdálenosti, ze které se bude nakonec počítat průměrná vzdálenost
    adresy_s_min_vzdal={}
    min_vzdalenosti=[]
    max_vzdalenost=-9999.0
    kumul_vzdalenost=0

    print ("Probíhá výpočet")

    # načtení každého adresního bodu a jeho vlastností
    for item in adresy:
        adresa=item ['properties']
        id_a=adresa['@id']
        ulice=adresa['addr:street']
        cislo=adresa['addr:housenumber']
        poloha_a=item['geometry']
        souradnice_a=poloha_a['coordinates']
        
        # převedení souřadnic z WGS do JTSK 
        jtsk_a=wgs_to_jtsk(souradnice_a)
        
        x1=get_x (jtsk_a)
        y1=get_y (jtsk_a)

        overeni_jtsk (x1,y1)

        vzdalenosti=[]
        min_vzdalenost=9999.0
        

        # výpočet vzdálenosti adresního bodu ke všem kontejnerům
        for item in kontejnery:
            vlastnosti=item ['properties']
            id_k=vlastnosti['ID']
            pristup=vlastnosti['PRISTUP']

            # ošetření volného přístupu kontejnerů 
            if "volně" in pristup:
                poloha_k=item['geometry']
                souradnice_k=poloha_k['coordinates']
                x2=get_x(souradnice_k)
                y2=get_y(souradnice_k)
                overeni_jtsk (x2, y2)
                vzdalenost=sqrt((((x2-x1))**2)+(((y2-y1))**2))
                if vzdalenost < min_vzdalenost:
                    min_vzdalenost=vzdalenost
            else:
                continue

        # vyhledání nejmenší vzdálenosti ke kontejneru
        adresa_domu=[ulice,cislo]
        

        # ověření, že nejbližší kontejner není dále než 10 km
        if min_vzdalenost > 10000:
            print (f"Chyba, pro adresu {str(' '.join(adresa_domu))} je nejbližší kontejner dál než 10 km, zkontrolujte vstupní soubory")
            sys.exit()
        
         
        # případné nové určení minimální vzdálenosti
        if min_vzdalenost>max_vzdalenost:
            max_vzdalenost=min_vzdalenost
        
        # přičtení minimální vzdálenosti do kumulativní vzdálenosti, ze které bude počítána průměrná minimální vzdálenost
        kumul_vzdalenost+=min_vzdalenost

        # přiřazení adresního bodu a nejmenší vzdálenosti do slovníku
        adresy_s_min_vzdal[min_vzdalenost]=[adresa_domu]
        
except KeyError:
    print ('Vstupní soubory neobsahují předpokládaná data nebo nejsou v požadovaném formátu, zkontrolujte soubory')
    sys.exit()


# výpočet průměrné minimální vzdálenosti vypočítaný z kumulativní minimální vzdálenosti vyděleným počtem adresních bodů
prum_min_vzdal="{:.0f}".format(kumul_vzdalenost/len(adresy))

# vyhledání příslušné adresy s maximální vzdáleností ke kontejneru
max_adresa_l=(adresy_s_min_vzdal[max_vzdalenost])
max_vzdalenost="{:.0f}".format(max_vzdalenost) 

print(f"Průměrná minimální vzdálenost ke kontejneru na tříděný odpad je pro danou čtvrť {prum_min_vzdal} metrů")
print(f"Nejdále je to k nejbližším kontejnerům tříděného odpadu z adresy {str(' '.join(max_adresa_l[0]))}, a to {max_vzdalenost} metrů")






