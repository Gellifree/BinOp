## Funkcionális specifikáció

### Áttekintés
Egy olyan programot szeretnénk készíteni, ami megkönnyíti a hétköznapjait, azoknak az oktatóknak, akik *Bevezetés az informatikába* című tárgyat oktatják. Hogy megszüntessük a repetitív teszteket, amelyeket a diákok nagyobb erőfeszítés nélkül kijátszhatnak, változatos feladatgenerálás is a céljaink közé tartozik. Ezenkívül a gyakorlatok során, esetenként a vizsgaalkalom, vagy zárthelyi dolgozat során, az oktatónak előre kell készülnie a feladatsorokkal, vizsgán feltett gyakorlati kérdésekkel, és azok megoldásával. Ezt is segíti a program, hiszen egyszerű átváltásokat is képes lesz, részletesen lépésenként megjeleníteni a szoftver, ami gyorsítja ezeknek az előre elkészített feladatoknak a megtervezését. Ezen kívül, a rögtönzött feladatok megoldását is nagy mértékben gyorsítja, hiszen megadva az elvégezendő feladatot, annak eredményét, vagy igény szerint részeredményeit is azonnal megjeleníti, hiba arány nélkül. Így a táblánál elvégzett, levezetett feladatot, elég összehasonlítani a program által kijelzett eredménnyel, és azonnal észrevehetjük, ha a diák hibát vétett valahol, ami sok esetben idő, és energiaigényes feladat volna, manuálisan. Kifejezetten fontosnak tartjuk, hogy a felhasználói felületben gyorsan lehessen navigálni, arra alapozva, hogy a felhasználó alapvetően kiismeri magát, egy terminál alapú programban.

### Jelenlegi helyzet leírása
Jelenleg, amennyiben a gyakorlaton, egy diáknak el kell végeznie, akár egy egyszerű átváltást is, valamilyen számrendszerből, bármilyen számrendszerbe, annak az ellenőrzése, egy manuális folyamat. Attól eltekintve, hogy kiváló fejszámolási képességgel rendelkeznek az oktatók, bizonyos feladatok, és részfeladatok, igen komplikált mélységekbe is beleérhetnek, aminek kijavítása, esetleg hibakeresése, hosszas, időigényes feladat, ami az óra, értékes, másra fordítható időkeretéből vesz el. Előfordulhat olyan helyzet is, hogy a tárgyat oktató személy, nem rendelkezik elég idővel, hogy minden csoportnak, külön külön feladatsort készítsen el, változatos feladatokkal. Sok csoportnál, ez igen hosszas folyamat, és még jobban meghosszabbítja, a dolgozatok kijavításához szükséges időt. Ez egy gyenge pont a dolgozatok szempontjából, hiszen ha a diákok rendelkeznek egymás közötti kapcsolati hálóval, akkor könnyedén elvégezheti, egy kiváló tanuló a tesztet, ami aztán futótűzként terjedhet végig az illetékes diákokon. Akik immáron, ismerik a feladatok megoldásait, részeredményeit, és trükkjeit, ezáltal könnyedén megtörténhet, hogy a csalásra hajlamos hallgatók, így különösebb erőfeszítés nélkül megússzák a zárthelyi dolgozatot, jeles eredménnyel. Igen sok munka szükséges a tárgyat oktató személytől, hogy ezeket a gyenge pontokat kiküszöbölje, és ezzel a saját munkáját sokszorozza meg, a javítás során, amivel csökken a többi feladatára szánható értékes időkeret.

### Vágyálom rendszer
A cél, egy olyan szoftver elkészítése, ami ezeket a gyenge pontokat megszüntetni, a folyamatokat felgyorsítja, és elsősorban tehermentesíti a tárgyat oktató személyt. Egy könnyen, és gyorsan navigálható menürendszer segítségével, azonnal elérhető minden funkció, kivételes sebességgel. Bizonyos szituációkban, igen nagy prioritással rendelkezik egy feladat megoldásának sebessége, ezért sem rendelkezünk grafikus felülettel. Habár a mostani hardverek több mint képesek, kíméletlenül gyorsan megjeleníteni egyszerű grafikus felületeket, azonban egy terminálablak elindítása, és egy parancs begépelését, mindenekelőtt gyorsabbnak, és hatékonyabbnak gondoljuk. Főleg olyan felhasználók körében, akik Linux alapú operációs rendszerrel rendelkeznek, hiszen a legtöbb ilyen felhasználó nem idegenkedik egy terminálablaktól, legtöbb munkafolyamatát itt végzi, ezért ismerős a környezet számára. Szerencsére, jelenlegi helyzetünkben, a legtöbb oktató Linux alapú operációs rendszereket használ, így ideális megoldásnak tartjuk a grafikus felület hiányát. A feladatsorok legenerálására, egy olyan algoritmust szeretnénk, amely hasonló koncepció alapján készíti a feladatokat, ugyan abban a nehézségi szintben, azonban a feladatok alapértékei mások, így nem megoldható a megoldások továbbadása. Akik alapvetően a koncepciókkal tisztában vannak, azoknak a feladatok nem különböznek egymástól, így nem is érzékelnek mérhető különbséget. Ezenkívül kiváló lehetőséget nyújt ez a megoldás, egy próba zárthelyi dolgozat megírására is, a gyakorlaton résztvevő hallgatók között, akik látni fogják ugyan a dolgozat vázát, és koncepcióját, ugyanakkor a konkrét megoldások csak segítenek nekik a tanulás elmélyítésében. A feladatsor legenerálása során, generálunk egy megoldásokat tartalmazó fájlt is, amivel a javítás során, csak össze kell hasonlítani a dolgozatokat. Ezzel töredékére csökkentve, a feladatok elkészítéséhez szükséges időt, és azok javításához befektetett energiát.

### Követelménylista
| Modul | ID | Név | Kifejtés |
| --- | --- | --- | --- |
| Funkció | K1 | Átváltás 10-ből | A felhasználó képes legyen bármilyen alapú számrendszerbe átváltani tízes alapú számrendszerből, egész, és tizedes értékeket egyaránt, és lehessen választani, a részeredmények megjelenítése, és csak a végeredmény megjelenítése között. |
| Funkció | K2 | Átváltás 10-be | A felhasználó, bármilyen alapú számrendszerből, képes legyen tízes alapú számrendszerbe átváltani, egész, és tizedes értékekkel egyaránt, és szintén lehessen választani, hogy a részeredményeket megkívánjuk-e tekinteni, vagy csak a végeredményre vagyunk kíváncsiak. |
| Funkció | K3 | Feladat generálás | A program rendelkezzen olyan funkcióval, ami képes X számú feladatot generálni, mindig hasonló tematikában, csupán változó értékekkel, hasonló nehézségi szinten. |
| Funkció | K4 | Ellenőrzés | Egy adott legenerált feladatsort, mentsen le, és ehhez készítse el, a részletes megoldási információkat is, egy külön fájlban, hogy azt majd a megírt tesztekkel, elég legyen csak összehasonlítani. |
| Megjelenés | K5 | Átlátható felület | A terminálablakban tisztán, és egyértelműen jelenleg meg a program, könnyedén navigálható menürendszerrel. Rendelkezzen egy segítő dokumentummal, ami leírja a program működését, és funkcióit, ez a dokumentum legyen elérhető a programon belülről, és a programnak paraméterként átadott *--help* jelzővel. |
| Megjelenés | K6 | Dinamikus megjelenítés | Amennyiben Linux alapú rendszeren fut a program, így kifejezetten könnyedén kérhetjük le a terminálablak fizikai paramétereit, és változtathatunk a színeken. Ezzel készítsünk el, egy olyan megjelenítési formát, ami vonzó a felhasználónak, és igény esetén, a megjelenítés alkalmazkodik a terminál méretéhez. (A program nevét a terminál közepére igazítja stb) |

### Fogalomszótár

-*HARDVER (HARDWARE)*
A számítástechnikában hardvernek nevezzük magát a számítógépet és minden megfogható tartozékát, a számítógép alkatrészeit (melyekből összeszerelték a számítógépet). 
-*SZOFTVER (SOFTWARE)*
Szoftvernek nevezzük a számítógépre írt programokat. A szoftvereket programozók készítik. Szellemi termékek, kézzel nem megfoghatóak A szoftver a számítógépen futó programok összefoglaló neve, valamint a hardver egységeket működtető-, és vezérlő programok összessége.
-*PROGRAM*
A program olyan egyszerű utasítások, műveletek logikus sorozata, amelyekkel a számítógépet irányítjuk. A program az utasításokat is és az adatokat is kettes számrendszerben leírt számokkal ábrázolja. 
-*LINUX*
A Linux egy operációs rendszer, a szabad szoftverek és a nyílt forráskódú programok egyik legismertebb példája.

### Használati esetek

A szoftvert bármely felhasználó tudja használni, egyenlő feltételek mellett. Az átváltásokat főleg inkább a tanulmányaikat végző diákok, míg a feladatgenerálást és az ellenőrzést az oktatók részesíthetik előnybe. 

### Használati esetek - követelmény megfeleltetés

A használati esetek a letisztultságnak és az egyszerűségnek köszönhetően teljesen lefedik a követelménylista elemeit.

### "Képernyő" tervek

Mivel egy terminálablakban futó alkalmazásról van szó, ezért a képernyőtervek, nem annyira beszédesek, azonban megpróbáljuk a lehető legjobban átadni a program funkcionalitását, és felépítését.

Amikor elindítjuk a programot, a következő menü fogadna bennünket: 

```
2020                                Számrendszer átváltó és feladatgeneráló

    [0] Átváltás tízes számrendszerből
    [1] Átváltás tízes számrendszerbe
    [2] Feladatsor generálása
    [3] Tárolt feladatsorok megtekintése
    [4] Segítség
    [Q] Kilépés

  >> _
```
Itt megadhatjuk a menüpontot reprezentáló számot, a '>>' jel után, ami *enter* leütésénél, kiválasztja az adott opciót. A program a 'Q' karakter leütésénél, megkérdezi, hogy biztosan ki szeretnénk-e lépni:

```
2020                                Számrendszer átváltó és feladatgeneráló

    [0] Átváltás tízes számrendszerből
    [1] Átváltás tízes számrendszerbe
    [2] Feladatsor generálása
    [3] Tárolt feladatsorok megtekintése
    [4] Segítség
    [Q] Kilépés

  >> Q

 Biztos vagy benne hogy kiszeretnél lépni? [I/n]
 >> _
```
### Funkció - követelmény megfeleltetés

- A *K1*, és *K2* követelmény, az általánosan megfogalmazható átváltáshoz szükséges algoritmusoknak köszönhetően teljesíthető. A képernyőterven a menü nulladik [0], és első [1] pontja fogja lefedni ezeket a funkciókat.
- A *K3* követelményért a képernyőképen a második [2] menüpont lesz felelős.
- A *K4* követelményért a képernyőképen a harmadik [3] menüpont lesz a felelős.
- A *K5* követelmény teljesítéséért a képernyőképen látható elrendezés, és a négyes [4] menüpont felelős.
- A *K6* követelményt Az algoritmuson belül kell lekezelnünk, hogy a program lekérje a megfelelő adatokat, és annak megfelelően jelenítse meg a programot, ezt szemléltei a képernyőkép (Középre igazított programnév).