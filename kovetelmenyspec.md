## Követelmény specifikáció

### Áttekintés
Számrendszerek közötti átváltások illetve azokkal való műveletek gyakorlására van szükség egy programra. Gyakorlófeladatok generálása, és azok ellenőrzése is szükségszerű. Az alkalmazás ideális megvalósítását **Python** nyelvel tudnánk elképzelni.

### Jelenlegi helyzet leírása
A tanórák nélkülözhetetlen eleme a számrendszerek közötti átváltás és annak ellenőrzése.
Számrendszerek közötti átváltások és azok ellenőrzésének egyszerűsítésének illetve meggyorsításának érdekében van szükség egy olyan alkalmazásra ami
ezt gyorsan és pontosan elvégzi, papír felhasználása és az oktató terhelése nélkül. *Bevezetés az informatikába* tantárgy oktatójának segítő alkalmazás jelenleg még nincs. Különböző csoportok számára változatos és egyben egyforma nehézségi szintnek megfelelő feladatsort időigényes összeállítani.

### Vágyálom rendszer leírása
Egy olyan alkalmazás, aminek használata igen kézenfekvő, intuitív, és lehetőséget biztosít arra, hogy mindenféle nehézség nélkül gyakoroljunk különböző számrendszerekkel való számítást és munkát. A program, egy egyszerű, kis rendszerigényű terminálban futó alkalmazás, ami képes feladatsorokat generálni a felhasználónak, és azokat kiértékelni, jelezve a feladatok lépésenkénti megoldását, ezenkívül egyéni átváltásokat is képes elvégezni, bármilyen számrendszerből bármilyen számrendszerbe. Attól függetlenül, hogy terminálablakban elérhető az alkalmazás, ideális volna, egy átlátható, könnyen olvasható, esetleg színekkel rendelkező megjelenés.

### Követelménylista

| Modul | ID  | Név | Kifejtés |
| ----- | --- | --- | -------- |
| Funkció	| K1	| Átváltás 10-ből		| A felhasználó 10-es számrendszerből képes legyen tetszőleges számrendszerbe átváltani			|
| Funkció	| K2	| Átváltás 10-be		| A felhasználó bármilyen alapú számrendszerből képes legyen 10-es számrendszerbe váltani		|
| Funkció	| K3	| Feladat generálás		| A program tudjon generálni, változatos feladatsorokat, számrendszerek közötti műveletek gyakorlására	|
| Funkció 	| K4	| Ellenőrzés			| Az elkészített eredmények elemzése, és az eredmények megjelenítése a felhasználó számára		|
| Megjelenés	| K5	| Átlátható felület		| Elvárás egy vonzó kinézetű menürendszer, és logikus, könnyen olvasható megjelenítés			|
| Megjelenés	| K6	| Dinamikus megjelenítés	| A program alkalmazkodjon a terminálablak méretéhez							|

### Fogalomszótár
* Számrendszer: A számábrázolási rendszer röviden; számrendszer meghatározza, hogyan ábrázolható egy adott szám. A számjegy egy szimbólum (vagy azok csoportja), ami egy számot ír le. A számjegyek éppen úgy különböznek az általuk leírt számtól, mint egy szó attól a dologtól, amit valójában jelent.
Az adott számrendszerben szerepeltethető számjegyek: 0 és 1.

Számrendszerek:

* I. Kettes számrendszer:
A kettes vagy más néven bináris számrendszerbeli számok a 0 és az 1 számjegyekből állnak. A számjegyek helyiértékeit az alábbi táblázatban foglaltuk össze.

* II. Tízes számrendszer:
A tízes számrendszer vagy decimális számrendszer a számok ábrázolásának legelterjedtebb módja. Helyiértékes számrendszer, számjegyei a 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, helyiértékei a tíz hatványai. A nem egész számok tizedestört formájában ábrázolhatóak benne.

* III. Nyolcas számrendszer:
 nyolcas számrendszer vagy oktális számrendszer a 8-as számon alapuló számrendszer. Nyolc számjegy: 0, 1, 2, 3, 4, 5, 6, 7 segítségével ábrázolja a számokat.

* IV. Tizenhatos számrendszer:
A tizenhatos vagy más néven hexadecimális számrendszerbeli számok 0 és 15 közötti helyiértékeket tartalmazhatnak, melyek a következők: 0 1 2 3 4 5 6 7 8 9 A B C D E F
Az egyes betűk a következő értékeket szimbolizálják:
A=10, B=11, C=12, D=13, E=14, F=15



A parancssoros felhasználói felület (angolul: Command Line Interface, elterjedt rövidítése: CLI) a felhasználói felületek egyik változata.
nnél a felhasználói felületnél a felhasználóval való kapcsolattartás parancsok segítségével történik. A felhasználó a billentyűzeten parancsokat gépel be, melyet a számítógép értelmez, végrehajt, és az eredményt (ha van) a képernyőn megjeleníti, esetleg hangjelzéssel jelzi a parancsvégrehajtás befejezését. A kimenet nem csak a monitor lehet, hanem tetszőleges fájl is.

Parancssori felhasználói felülettel szinte mindegyik operációs rendszer rendelkezik, mert sok olyan feladat is megoldható vele, amelyekre a grafikus felhasználói felület nem ad lehetőséget.
### Használati esetek