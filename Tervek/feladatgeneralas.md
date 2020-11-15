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
