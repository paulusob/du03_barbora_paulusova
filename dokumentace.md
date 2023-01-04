Program pro výpočet vzdálenosti ke kontejnerům na tříděný odpad

Program slouží k výpočtu průměrné nejmenší vzdálenosti a rovněž největší vzdálenosti 
ke kontejnerům na tříděný odpad ve vybrané pražské čtvrti.

Funkce
Všechny funkce a importované knihovny jsou zapsány v samostatném souboru funkce.py. 
Jednotlivé funkce budou popsány níže.

Vstup
Vstupním souborem je soubor adresních bodů vybrané pražské čtvrti (dostupný z https://overpass-turbo.eu/)
uložený jako adresy.geojson a soubor obsahující polohu a vlastnosti kontejnerů na tříděný odpad v Praze 
(dostupný z https://www.geoportalpraha.cz/cs/data/otevrena-data/8726EF0E-0834-463B-9E5F-FE09E62D73FB) 
uložený jako kontejnery.geojson. Oba soubory musí být ve formátu geojson. 
Program předpokládá, že soubor adresních bodů je v souřadnicovém systému WGS-84, zatímco soubor 
se souřadnicemi kontejnerů je v JTSK.

Zdrojový kód
Ve zdrojovém kódu je nejprve proveden import celého souboru fuknce, který obsahuje definované funkce a 
importy dalších knihoven. Následně jsou otevřeny oba vstupní soubory a pomocí funkce overeni_obsahu 
je kontrolováno, zda nejsou soubory prázdné. Současně je pomocí bloku try a except ovšetřeno nenalezení 
souboru a přístupových práv k otevření souboru. Jednotlivé vstupní soubory jsou přepsány do proměnných 
data_adresy a data_kontejnery. 


