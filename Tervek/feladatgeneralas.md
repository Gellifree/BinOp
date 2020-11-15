# Feladatgenerálás megtervezése

**A tervek mappában lévő leírások, elképzelések elsősorban ötletek a fejlesztéshez, nem kötelezően megvalósítandóak. Új ötletek, ötletek módosítása, vagy törlése elfogadott.**

## Feladatgenerálás felépítése

A feladatgenerálás négy részre lesz osztva.

 - Átváltások (7 darab)
 - Összeadás (1 darab)
 - Kivonás (1 darab)
 - Szorzás (1 darab)

Összesen 10 feladat lesz generálva, a következő mintákat követve:

### Átváltások

Az átváltások két fő részre osztható.
 - Az első részben tízes alapú számokat kell átváltani, kettes, nyolcas, tizenhatos alapú számokká.
 - A második részében N alapú (2,8,16) számokat kell tízesre átalakítani
 - +1 feladat: binárisból, oktálisból vagy hexadecimálisból binárisba, oktálisba vagy hexadecimálisba való átváltás. (2->8, 8->16, 16->2 stb.)

### Összeadás

Két véletlenszerűen generált számot kettes számrendszerben kell összeadni. A számot tízes alapon kapja meg, tehát annak az átváltásról is gondoskodni kell.

### Kivonás

Két véletlenszerűen generált számot kettes számrendszerben kell kivonni. A számot tízes alapon kapja meg, tehát annak az átváltásról is gondoskodni kell.

### Szorzás

Két kettes számrendszerben kapott számot kell összeszorozni.

## Feladatgenerálás adatszerkezetei

A konkrét megoldáshoz, meg kell tervezni a szükséges adatszerkezeteket.

 - Legyen egy lista, ami tartalmazza a kérdéseket szöveg formában. ''' questions ''' néven.
 - Legyen egy lista, ami listákat tartalmaz, amiben a feladathoz rendelt számok sorozata lesz. ''' numbers ''' néven.
 - A megfelelő indexelés segítségével, így eltároltuk a feladatokhoz szükséges számsorozatokat, amik véletlenszerűen generálhatók.

Ezek megléte után, meg kell formázni a kiíratást, hogy az olvasható, és egyértelmű legyen.


## Számgenerálás megtervezése

A feladatok legenerálásának fő váza, a különböző számokat tartalmazó feladatsorok. A feladatok ugyan azok, azonban az azokban lévő értékek mind más és mások, így kialakul a feladat megoldásához szükséges lépések logikai felépítése a tanulóban, azonban nem megjegyezhetőek a részeredmények.

A beállítások menüben biztosítani akarunk különböző opciókat, az első ilyen opció a számgenerálás módja lesz.

### Egyszerűbb számgenerálás

#### Tízes alapú véletlen érték generálása

Tízes számrendszerben kifejezetten egyszerű dolgunk van véletlenszerű számot generálni. Akár intervallumban lévő egészet, vagy 0, és 1 közötti lebegőpontos számról van szó.

Azonban, szeretnék nagyobb kontrollt kapni a számok generálásánál. Ezért az első elképzelés, az egyszerűbb számgenerálási módszer a következő lenne:

 - Generáljunk egy egész számot, nulla és kétszáz között. Ez lesz a generált szám egész része.
 - Generáljunk egy egész számot, nulla és kétezer között. Ez lesz a szám tizedes tört része.
 - Ezeket **szöveggé** átalakítva, összefűzve egy tizedesponttal, majd ismét **float** típussá alakítva, megkaptuk a generált számunkat.

 Alapjában véve, egy viszonylag komplikált folyamat, viszont nagyon könnyedén módosíthatjuk a **paramétereket**, amik meghatározzák a generált szám értékét, ami a feladatok *nehézségének* meghatározásánál még fontos szerepet játszhatnak.

#### N alapú érték generálása

Könnyedén paraméterezhető számgenerálásunkra építve, és a konvertáló függvény segítségével, megvan az eszközünk, hogy bármilyen számrendszerben generáljunk véletlenszerű értékeket.

### Komplikáltabb számgenerálás

A komplikáltabb számgenerálás egyenlőre nem élvez prioritást.

## Feladatsor lementésének első tervezni

Olyan formában akarjuk lementeni a feladatsorokat, hogy azok a lehető legkisebb méretben, a lehető legtöbb információt tárolják, és algoritmikusan feldolgozhatóak legyenek. Így egy legenerált feladatsorra bármikor lekérhetjük a megoldást, anélkül, hogy azt le kellene mentenünk.

Egy egyszerű szöveges fájlban tároljuk a feladatokat. Egy feladathoz egy, vagy több szám tartozik, ahogyan egy részfeladat is állhat egy, vagy több generált számból. Hogy ezek a generált számok milyen alapon vannak, és mit kell tenni velük a következőképpen tároljuk:
 - A ``c`` karakter, a konvertálást jelöli
 - A ``s`` karakter a kivonást jelöli
 - A ``a`` karakter az összeadást jelöli
 - A ``t`` karakter a szorzást jelöli
 - A ``d`` a decimális számrendszert jelöli
 - A ``b`` a bináris, azaz kettes számrendszert jelöli
 - A ``o`` az oktális, azaz nyolcas számrendszert jelöli
 - Az ``x`` a Hexadecimális, azaz 1tizenhatos számrendszert jelöli
Konvertálás esetén, így nézne ki néhány feladat:
 - 100010.11011-cbd; Ez azt jelenti, hogy a **100010.11011** számot, konvertáljuk át kettes alapról, tízes alapra.
 - 337.67-cod; Ez azt jelenti, hogy a **337.67** számot, konvertáljuk át nyolcas alapról tízes alapra.
 - 12.71-cdb; Ez azt jelenti, hogy a 12.71-et váltsuk át kettes számrendszerbe.
 - 4.24|3.1-adb; Ez azt jelenti, hogy a 4.24-et, és a 3.1-et, ami tízes számrendszerben értelmezett (**d**), adjuk össze (*a*) kettes számrendszerben (*b*).
 - 10011.01|110-tbb; Ez azt jelenti, hogy szorozzuk össze (**t**), a két bináris számrendszerben lévő számot. (Az első b, azt jelenti hogy a számok kettes számrendszerben vannak, a második pedig hogy az eredményt is kettes számrendszerben kérjük.)

 A feladatok elválasztására, használhatnánk a ``&`` jelet. Ennek a tárolási módszernek a kivitelézését megpróbálom megtervezni, és javítom a dokumentumot, amint valami változna, a tervezés közben.
