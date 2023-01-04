# Program pro výpočet vzdálenosti ke kontejnerům na tříděný odpad

# import funkcí a potřebných knihoven
from funkce import *


# otevření souborů s daty a jejich načtení do proměnných, ošetření nenalezení souboru a přístupových práv
try:
    with open ("adresy.geojson", encoding="utf-8") as a,\
        open ("kontejnery.geojson", encoding="utf-8") as k: 
        
        # ověření, zda některý ze souborů není prázdný 
        overeni_obsahu ("adresy.geojson")
        overeni_obsahu ("kontejnery.geojson")

        # přepsání dat
        data_adresy=json.load(a)
        data_kontejnery=json.load(k)
        
except FileNotFoundError:
    print ('Vstupní soubor nebyl nalezen, zkontrolujte název a umístění souboru')
    sys.exit()
except PermissionError:
    print ('K otevření souboru nejsou přístupová práva')
    sys.exit()
    
# načtení dat do listů, ošetření neočekávaného formátu 
try: 
    adresy=list(data_adresy['features'])
    kontejnery=list(data_kontejnery['features'])

    # vytvoření slovníků pro vyhledávání 
    adresy_s_min_vzdal={}
    min_vzdalenosti=[]

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
                vzdalenost=sqrt(((abs(x2-x1))**2)+((abs(y2-y1))**2))
                vzdalenosti.append (vzdalenost)
            else:
                continue

        # vyhledání nejmenší vzdálenosti ke kontejneru
        min_vzdalenost=min(vzdalenosti)
        min_vzdalenosti.append (min_vzdalenost)  
        adresa_domu=[ulice,cislo]

        # přiřazení adresního bodu a nejmenší vzdálenosti do slovníku
        adresy_s_min_vzdal[min_vzdalenost]=[adresa_domu]
        
except KeyError:
    print ('Vstupní soubory neobsahují předpokládaná data nebo nejsou v požadovaném formátu, zkontrolujte soubory')
    sys.exit()


prum_min_vzdal="{:.0f}".format(mean(min_vzdalenosti))
max_min_vzdal=max(min_vzdalenosti)

max_adresa_l=(adresy_s_min_vzdal[max_min_vzdal])
max_min_vzdal="{:.0f}".format(max_min_vzdal) 

print(f"Průměrná minimální vzdálenost je pro danou čtvrť {prum_min_vzdal} metrů")
print(f"Nejdále je to k nejbližším kontejnerům tříděného odpadu z adresy {str(' '.join(max_adresa_l[0]))}, a to {max_min_vzdal} metrů")






