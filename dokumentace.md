# Program pro výpočet vzdálenosti ke kontejnerům na tříděný odpad

Program slouží k výpočtu průměrné nejmenší vzdálenosti a rovněž největší vzdálenosti 
ke kontejnerům na tříděný odpad ve vybrané pražské čtvrti.

## Funkce
Všechny funkce a importované knihovny jsou zapsány v samostatném souboru *funkce.py*. 
Jednotlivé funkce budou popsány níže.

## Vstupní soubory
Vstupním souborem je soubor adresních bodů vybrané pražské čtvrti uložený jako *adresy.geojson* a soubor obsahující polohu a vlastnosti kontejnerů na tříděný odpad v Praze uložený jako *kontejnery.geojson*.

### adresy.geojson
Soubor adresních bodů pro libovolnou pražskou čtvrť lze stáhnout z [Overpass Turbo](https://overpass-turbo.eu/) v souřadnicovém systému WGS-84.
Soubor musí být ve formátu *json* a pod atributem *features* musí být uloženy jednotlivé adresy, přičemž pod atributem *properties* musí být uloženy dílčí atributy *@id* , *addr:housenumber* a *addr:street*, ze kterých je následně vytvořena adresa domu. Atribut *geometry* musí obsahovat *coordinates*, kde jsou uloženy souřadnice dané adresy. 

### kontejnery.geojson
Soubor s polohou kontejnerů v Praze lze stáhnout z [pražského Geoportálu](https://www.geoportalpraha.cz/cs/data/otevrena-data/8726EF0E-0834-463B-9E5F-FE09E62D73FB) v souřadnicovém systému JTSK. 
Soubor musí být ve formátu *json* a pod atributem *features* musí být uloženy jednotlivé kontejnery. Pod atributem *properties* musí být uloženo *ID*, které odlišuje jednotlivé kontejnery a atribut *geometry* musí obsahovat *coordinates*, kde jsou uloženy souřadnice daného kontejneru. 

## Zdrojový kód
Ve zdrojovém kódu je nejprve proveden import celého souboru *funkce*, který obsahuje definované funkce a 
importy dalších knihoven. Následně jsou otevřeny oba vstupní soubory a pomocí funkce *overeni_obsahu* 
je kontrolováno, zda nejsou soubory prázdné. Současně je ovšetřeno nenalezení 
souboru a přístupových práv k otevření souboru. Jednotlivé vstupní soubory jsou přepsány do proměnných 
*data_adresy* a *data_kontejnery*. 

Následně jsou vytvořeny listy, které obsahují již samotné údaje o adresních bodech *(adresy)* a kontejnerech *(kontejnery)*. 
Postupně je načítána poloha každého adresního bodu a jeho vlastnosti jsou extrahovány 
do jednotlivých proměnných. Souřadnice adresního bodu jsou převedeny pomocí funkce *wgs_to_jtsk*, která je 
definována v souboru funkce, přičemž je využíván model *PyProj*. Rovněž je pro získané souřadnice JTSK pomocí funkce *overeni_jtsk* ověřováno, zda leží na území ČR, tedy v oblasti, kde je souřadnicový systém definován. 
Následně je počítána vzdálenost kontejnerů od adresních bodů. Ze souboru jsou nejdřív vyextrahovány 
požadované vlastnosti jako *ID* a *přístup*. Pokud je přístup ke kontejnerům volný, získávají se pro daný
objekt souřadnice, které se také ověřují pomocí funkce *overeni_jtsk*. Pomocí pythagorovy věty je potom
počítána vzdálenost souřadnic adresního bodu a každého kontejneru s volným přístupem. Kontejnery přístupné pouze obyvatelům domu nejsou uvažovány. Při každém opakování se ukládá nejmenší hodnota v porovnání s předchozími vzdálenostmi.  

Když jsou takto analyzovány všechny kontejnery, nejmenší vzdálenost se pro danou adresu uloží do slovníku 
*adresy_s_min_vzdalenosti* a také se přičte ke kumulativní vzdálenosti. Pokud je minimání vzdálenost vyšší než předchozí hodnota, nahrazuje hodnotu v proměnné max_vzdalenost. Taktéž je ošetřeno, že vstupní soubory obsahují předpokládané klíče. 

Ze všech minimálních vzdáleností je vydělením kumulativní vzdálenosti počtem adres vypočítán průměr, který je vypsán do *terminalu*. 
Podle nejvyšší hodnoty je pak ze slovníku *adresy_s_min_vzdal* vyhledána i příslušná adresa s touto hodnotou. Tento výstup je taktéž vypsán do terminalu. 






