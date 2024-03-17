import math
import sys
import random

#Zadanie 1
# zdanie = input("Wpisz zdanie: ")
# słowa = zdanie.split(' ')
# print('Liczba słów w zdaniu: ' + str(len(słowa)))

#Zadanie 2
# sys.stdout.write("Podaj a, b i c: ")
# a = sys.stdin.readline()
# b = sys.stdin.readline()
# c = sys.stdin.readline()
# wynik = pow(int(a), int(b)) + int(c)
# sys.stdout.write(str(wynik))

#Zadanie 3
# napis = input("Wpisz napis: ")
# lista1 = list(napis)
# lista2 = list(napis)
# lista2.reverse()
#
# if lista1 == lista2:
#     print("Napis jest palindromem")
# else:
#     print("Napis nie jest palindromem")

#Zadanie 4
# a = int(input("Podaj liczbę: "))
# if a % 2 == 0 or a <= 1:
#     print("Liczba nie jest pierwsza")
# else:
#     for i in range(2, math.floor(math.sqrt(a)), 2):
#         if a % i == 0:
#             print("Liczba nie jest pierwsza")
#             break
#     else:
#         print("Liczba jest pierwsza")

#Zadanie 5
# liczby = []
# for a in range(2, 1001):
#     suma_dzielnikow = 0
#     for i in range(1, a):
#         if a % i == 0:
#             suma_dzielnikow += i
#     if suma_dzielnikow == a:
#         liczby.append(a)
# print("Liczby doskonałe to liczby: " + str(liczby) + ", a jest ich: " + str(len(liczby)))

#Zadanie 6
# lista = [2, 3, 4, 5.9, 9.9]
# for i in lista:
#     print(pow(i, 2))

#Zadanie 7
# licznik = 0
# lista = []
# while licznik < 10:
#     liczba = int(input("Podaj liczbę: "))
#     if liczba % 2 == 0:
#         lista.append(liczba)
#     licznik += 1
# print(lista)

#Zadanie 8
# lista = ['a', 'b0', 1, 2, 3, 4]
# slow = {}
# for item in lista:
#     slow[item] = lista.count(item)
# print(slow)
# for k in list(slow.keys()):
#     if type(k) == str:
#         slow.pop(k)
# print(slow)