Program pro výpočet vzdálenosti ke kontejnerům na tříděný odpad
Program slouží k výpočtu průměrné nejmenší vzdálenosti a největší vzdálenosti ke kontejnerům na tříděný odpad
ve vybrané pražské čtvrti. 
Vstup 
Vstupním souborem je soubor adresních bodů vybrané pražské čtvrti (dostupný z https://overpass-turbo.eu/) 
uložený jako adresy.geojson a soubor obsahující polohu a vlastnosti kontejnerů na tříděný odpad v Praze 
(dostupný z https://www.geoportalpraha.cz/cs/data/otevrena-data/8726EF0E-0834-463B-9E5F-FE09E62D73FB)
uložený jako kontejnery.geojson. Oba soubory musí být ve formátu geojson. 
Program předpokládá, že soubor adresních bodů je v souřadnicovém systému WGS-84, zatímco soubor se souřadnicemi 
kontejnerů je v JTSK. 
Výstup
Prvním výstupem z programu je informace o průměrné minimální vzdálenosti ke kontejnerům na tříděný odpad
pro danou čtvrť, druhý výstup udává adresu, odkud je nejbližší kontejner na tříděný odpad 
vzdálený nejdále a taktéž samotnou vzdálenost k nejbližšímu kontejneru. 
