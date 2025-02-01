"""2. Feladat
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza, ha a paraméterként átvett listaelemek (egész számok) között van páros, ellenkező esetben a visszatérési érték False! A program tartalmazza a függvény hívását is!"""

def paros_e(szamok):
    for szam in szamok:
        if szam % 2 == 0:
            return True
    return False

print(paros_e([1, 7, 3, 23, 5]))