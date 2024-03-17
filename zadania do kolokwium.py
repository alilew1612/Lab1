import math, random

#Zadanie 1
# a = math.pow(math.exp(4) - math.log2(34), 1/3)
# a = round(a, 2)
# b = math.pow(math.log(20) + math.cos(45) + math.e, 1/3)
# b = round(b, 2)
# c = math.pow(math.log(20, 3) + math.sin(45) * (5/8), 1/4)
# c = round(c, 2)
# d = math.log(23, 3) + math.pow(math.sin(34) + 5, 1/3)
# d = round(d, 2)
# e = math.pow(math.log(32, 2) + math.pi + math.sin(56), 1/4)
# e = round(e, 2)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

#Zadanie 2
# def wieza(n):
#     if n > 10 or n < 1:
#         print("Zła wartość n")
#     else:
#         for i in range(1, n+1):
#             for j in range(0, i):
#                 print("A", end = "")
#             print()
# wieza(6)

#Zadanie 3
# def piramida(n):
#     if n > 10 or n < 1:
#         print("Zła wartość n")
#     else:
#         a = 2*n
#         for i in range(n):
#             for j in range(a):
#                 if j == a/2:
#                     print("A", end="")
#                 elif (j >= a/2 - i and j < a/2):
#                     print("A", end="")
#                 elif (j > a/2 and j <= a/2 + i):
#                     print("A", end="")
#                 else:
#                     print(" ", end="")
#             print("")
# piramida(10)

#Zadanie 5
# def wektor_nxn(n):
#     wektor = []
#     for i in range(0, n):
#         lista = [random.randint(0, 20) for k in range(n)]
#         wektor.append(lista)
#     print(wektor)
#     for j in wektor:
#         print(j, sum(j))
#
# wektor_nxn(5)