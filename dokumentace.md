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

Následně jsou vytvořeny listy, které obsahují již samotné údaje o adresních bodech (adresy) a kontejnerech
(kontejnery). Ve for cyklu je načítána poloha každého adresního bodu a jeho vlastnosti jsou extrahovány 
do jednotlivých proměnných. Souřadnice adresního bodu jsou převedeny pomocí funkce wgs_to_jtsk, která je 
definována v souboru funkce, přičemž je využíván model PyProj. Rovněž je pro získané souřadnice JTSK pomocí funkce overeni_jtsk ověřováno, zda leží na území ČR, tedy v oblasti, kde je souřadnicový systém definován. 
Následně je počítána vzdálenost kontejnerů od adresních bodů. Ze souboru jsou nejdřív vyextrahovány 
požadované vlastnosti jako ID a přístup. Pokud je přístup ke kontejnerům volný, získávají se pro daný
objekt souřadnice, které se také ověřují pomocí funkce overeni_jtsk. Pomocí pythagorovy věty je potom
počítána vzdálenost souřadnic adresního bodu a každého kontejneru s volným přístupem. Vzdálenost je uložena do seznamu vzdalenost. 

Když jsou takto analyzovány všechny kontejnery, ze seznamu vzdalenost se vybere ten s nejnižší hodnotou.
Nejmenší vzdálenost se uloží do seznamu min_vzdalenosti a rovněž je s adresou přiřazen do slovníku 
adresy_s_min_vzdalenosti. V celém tomto bloku je ošetřeno, že vstupní soubory obsahují předpokládané klíče.

Ze všech minimálních vzdáleností je vypočítán průměr, který je vypsán do terminalu. 
Rovněž je vyhledána nejvyšší hodnota, podle které je pak ze slovníku vyhledána i příslušná adresa 
s touto hodnotou. Tento výstup je taktéž vypsán do terminalu. 






