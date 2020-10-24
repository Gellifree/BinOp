## Rendszerterv

### Rendszer céljai, és nem céljai

A rendszer célja, hogy képes legyen műveletvégzésre, bármilyen számrendszerben. Mivel erre a *Python* alapvetően képes, ezért a feladat fő célja, hogy erre, egy kényelmesebb felületet biztosítson. Ezenkívül különböző számrendszerekben generált feladatok előállítására is alkalmasnak kell lennie, így készítve teszteket, az eredményekkel együtt. Minden generált feladatsorhoz, tartozik egy eredményeket tartalmazó fájl is. A rendszernek nem feladata lehetőséget biztosítani egy már meglévő feladatsor módosítására, vagy visszaállítására adatvesztés esetén. A rendszernek nem célja bármilyen formában bekérni egy kitöltött tesztet, és az eredmények helyességét ellenőrizni.

### Projektterv

**Projekt szerepkörök**

*Scrum master*: Kovács Norbert

*Product owner*: Hives Ferenc

*Dev csapat*:
- Zsák József
- Hives Ferenc
- Nagy Levente
- Kovács Norbert

#### Ütemterv

| Funkció | Feladat | Prioritás | Becslés | Aktuális becslés | Eltelt idő | Hátralévő idő |
| --- | --- | --- | --- | --- | --- | --- |
| Követelmény specifikáció |  Dokumentáció elkészítése |  0  |  36  |  36  |  36  |  0  |
| Funkcionális specifikáció | Dokumentáció elkészítése |  0  |  36  |  36  |  36  |  0  |
| Rendszerterv | Dokumentáció elkészítése |  1  |  84  |  84  |  36  |  50  |
| Kódolás | Alapok elkészítése | 1 | 30 | 30 | 0 | 30 |
|     | Átváltás | 2 | 40 | 40 | 0 | 40 |
|     | Feladat generálás | 2 | 40 | 40 | 0 | 40 |
|     | Ellenőrzés | 1 | 40 | 40 | 0 | 40 |
|     | Felület és Megjelenítés | 1 | 18 | 18 | 0 | 18 |
| Tatralék idő |     |  3  |  12  |  12  |  0  |  12  |
| Tesztelés | Hibák javítása | 2 | 24 | 24 | 24 | 24 |
|     | Felület tesztelése | 1 | 24 | 24 | 0 | 24 |
|     | Végső teszt | 2 | 12 | 12 | 0 | 12 |
| Tatralék idő |     |  3  |  12  |  12  |  0  |  12  |
| Véglegesítés | Dokumentáció ellenőrzése | 2 | 24 | 24 | 0 | 24 |
|     | Dokumentáció összesítése | 2 | 24 | 24 | 0 | 24 |
|     |     |     |     |     |     |     |
| Órák:     |     |     | 456  | 456 |  111   |  350  |
| Napok:    |     |     |  57  | 57  |  13.875   | 43.75  |
|     |     |     |     |     |     |     |
| Napidíj: |     |     |     |     |     |  25 000 Ft.    |
|     |     |     |     |     |     |     |
| Árajánlat: |    |     |     |     |     |   1 425 000 Ft.  |


#### Mérföldkövek

A bemutatás megtörtént

### Üzleti folyamatok modellje

| Szereplő | Folyamat | Szereplő |
| --- |  --- | --- |
| Diák-> | Átváltás tízes számrendszerből | <-Tanár |
| Diák-> | Átváltás tízes számrendszerbe | <-Tanár |
| Diák-> | Feladatmegoldás | <-Tanár |
|  | Feladatsor generálás | <-Tanár |
|  | Tárolt feladatsorok megtekintése | <-Tanár |



### Követelmények

 Funkcionális követelmények:
	
	Számítások elvégzése.
	
	Feladatok generálás.
	
	Ellenőrzések elvégzése.
	
	
Nem funkcionális követelmények:

	Hibamentes működés.
	
	Felhasználóbarát környezet.
	
	
Törvényi előírások, szabványok:

	-


### Funkcionális terv

Szereplők:

	-Tanár.

	-Diák.

Rendszerhasználati esetek és lefutásaik:

Tanár:

	-Átváltás tízes számrendszerből.

	-Átváltás tízes számrendszerbe.

	-Feladatsor generálása.

-Tárolt feladatsorok megtekintése.

	-Segítség.

	-Kilépés.

Diák:


	-Átváltás tízes számrendszerből.

	-Átváltás tízes számrendszerbe.

	-Segítség.

-Kilépés.

Menü-hierarchiák:

	[0] Átváltás tízes számrendszerből.

	[1] Átváltás tízes számrendszerbe.

	[2] Feladatsor generálása.

	[3] Tárolt feladatsorok megtekintése.

	[4] Segítség.

	[Q] Kilépés.


### Fizikai környezet

Az alkalmazás Linux platformra készül.

Nem rendelkezünk megvásárolt komponensel.

Fejlesztői eszközök:

	- Notepad++
	- Python
	- PyCharm 

### Absztrakt domain modellje

???

### Architekturális terv

Backend:

Az alkalmazás Python használatával készül. A felhasználó egy egyszerű és átlátható konzollal találkozik, ahol a menüpont kiválasztása után a kért művelet elvégzésre kerül. 

### Tesztterv

A tesztelések célja az alkalmazás és komponensei funkcionalitásának teljes vizsgálata, ellenőrzése.

Tesztelési eljárások:

		1.,Unit teszt:
		Már a fejlesztési idő alatt is folyamatosan tesztelés történik, hogy a
		metódusok megfelelően működnek-e.
		Ametódusok akkor mondhatók késznek, ha a tesztesetek hiba nélkül lefutnak.

		2.,Alfa teszt:
		A teszt elsődleges célja: a már meglévő funkciók különböző
		adatbevitellel történő tesztelése. A tesztet a
		fejlesztők végzik.
		Az eljárás sikeres, ha különböző adatbevitel során a hibás adatokkal hibát hoz az alkalmazás a megfelelő adat bevitele után pedig a helyes értéket adja vissza. A teszt időtartama egy hét.


		3.,Beta teszt:
		Ezt a tesztet nem a fejlesztők végzik, hanem meghatározott számú a fejlesztők által kiválasztott tesztelő. 
		A teszt időtartama egy hét.
		A tesztelés alatt a tesztelő felhasználók visszajelzéseket küldhetnek a
		fejlesztőknek, probléma,hiba felmerülése vagy egyéb észrevétel esetén.
		Ha hiba lép fel, a fejlesztők kijavítják a lehető leghamarabb. A tesztelők észrevételeit, ha a fejlesztők érdemesnek találják, akkor integrálhatják azt, azokat. 


### Telepítési terv

Terminál "alkalmazás mappája" python "alkalmazás neve".py

### Karbantartási terv

Az alkalmazás rendszeres üzemeltetése és karbantartása, mely
magában foglalja a hibák elhárítását, a változó igények miatti
módosításokat, valamint a felhasználók által jelentett hibák kijavítása.