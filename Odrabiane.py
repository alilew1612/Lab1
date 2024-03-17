import math
import random

# try:
#     a = int(input())
#     b = int(input())
#     result = a/b
#     print(result)
# except ZeroDivisionError:
#     print("Error")
# except ValueError:
#     print("Brak liczby")

# a = [x**x for x in range(10)]
# print(a)
# l1 = [0,1,2,3,4,5,6,7,8,9]
# l2 = []
# for i in l1:
#     l2.append(i**2)
# print(l2)
# b = [3**y for y in range(6)]
# print(b)
# c = [x for x in a if x % 2 == 1]
# print(c)
# d = [(i,j) for i in l1 for j in l2]
# print(d)
#
# l3 = []
# for i in l1:
#     for j in l2:
#         l3.append((i,j))
# print(l3)
#
# s1 = {1:2, 2:3, 2:4}
# s2 = {v: k for k, v in s1.items()}
# print(s2)

# def rownanie_kwadratowe(a,b,c):
#     delta = b**2 - 4*a*c
#     if delta < 0:
#         print("brak pierwiastkow")
#         return 0
#     elif delta == 0:
#         x = -b/(2*a)
#         print("jeden pierwiastek")
#         return x
#     elif delta > 0:
#         x1 = (-b + math.sqrt(delta)) / (2*a)
#         x2 = (-b - math.sqrt(delta)) / (2*a)
#         print("dwa pierwiastki")
#         return x1, x2
#
#     print(rownanie_kwadratowe(6, 1, 3))
#     print(rownanie_kwadratowe(1, 2, 1))
#     print(rownanie_kwadratowe(1, 4, 1))

# def dlugosc_odcinka(x1=1, x2=2, y1=3, y2=4):
#     return math.sqrt((x2-x1)**2+(y2-y1)**2)
#
# print(dlugosc_odcinka())
# print(dlugosc_odcinka(2, 4, 5, 7))
# print(dlugosc_odcinka(x1=1,x2=5,y1=6,y2=7))
# print(dlugosc_odcinka(2,3, y2=7,y1=8))

# plik = open("nazwa pliku", 'a+')
# plik.seek(0)
# znaki = plik.read(10)
# plik.write('aaaa')
# plik.close()
# print(znaki)

# with open("plik_tekstowy", 'r') as plik:
#     znaki = plik.readlines()
#
# print(znaki)

#Zadania
#Zad1
# a = [1-x for x in range(1,10)]
# b = [4**i for i in range(8)]
# c = [x for x in b if x % 2 == 0]
# print(a)
# print(b)
# print(c)

#Zad2
# lista1 = []
# licznik = 0
# while licznik < 10:
#     a = random.randint(0, 100)
#     lista1.append(a)
#     licznik += 1
# print(lista1)
# nowa_lista = [x for x in lista1 if x % 2 == 0]
# print(nowa_lista)

#Zad3
# produkty = {"jajka": "sztuki", "mąka": "kg", "mleko": "litry", "jabłka": "sztuki"}
# lista = [key for key in produkty.keys() if produkty[key] == 'sztuki']
# print(lista)

#Zad4
# def trojkat(a,b,c):
#     dzialanie = a*a + b*b
#     if dzialanie == c * c:
#         print("Trojkat jest prostokątny")
#         return dzialanie, "=", c * c
#     else:
#         print("Trojkat nie jest prostokatny")
#         return dzialanie, "!=", c * c
# print(trojkat(1,2,3))
# print(trojkat(3,4,5))

#Zad5
# def trapez(a = 5, b = 10, h = 2):
#     return math.sqrt(((a+b)*h)/2)
# print(trapez())

#Zad6
# def iloczyn(a=1, b=4, ile=10):
#     licznik = 0
#     while licznik < ile:
#         a *= b
#         licznik += 1
#     return a
# print(iloczyn())


#Zad 7
# try:
#     a = int(input("Podaj liczbę: "))
#     result = math.sqrt(a)
#     print(result)
# except ValueError:
#     print("zła liczba")




