"""5. Feladat
Írj egy programot, ami addig kér be egész pozitív számokat, amíg a felhasználó negtív számot nem ír! A megadott számokat tárolja a program egy listában, és ezt adja át paraméterként egy függvények, amely a lista legkisebb elemével tér vissza. A program írja ki, hogy melyik volt a megadott legkisebb szám!
"""

szamok = []
while True:
    szam = int(input("Adj meg egy egész pozitív számot: "))
    if szam < 0:
        break
    szamok.append(szam)

print(min(szamok))
