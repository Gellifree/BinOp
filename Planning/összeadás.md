# Összeadás újragondolása

- Első lépés
  - Vegyük az összedandó számok listáját: ['10111001', '101100', '111', '1000'] (185, 44, 7, 8)
  - Egészítsük ki őket nullával, aleghoszabb alapján: ['10111001', '00101100', '00000111', '00001000']
  - Hozzunk létre két listát: m[] mint maradék, és e[] mint eredmény.
  - Fontos, hogy m[] kilegyen nullázva, a várható eredmény hosszáig
  - Jobbról balra (<-) vegyük az adott indexű elemet (1 + 0 + 1 + 0), és adjuk össze
  - az eredmény 2 (10) -> ['1', '0'], ahol a második elem az eredményünkhöz adódik, az első a maradékokhoz eggyel arébb
  - Ismételjük a folyamatot addig, amíg nem érünk a műveletek végére (Nem a kiinduló hosszúságig! Amennyiben a maradék tömb hoszabb, annak a végéig kell menni. -> indexelési probléma amennyiben hoszabb!)
  - A folyamat végén, sikeresen megvan az eredményünk, ami a segéd adatszerkezet álltal könnyedén vizualizálható
