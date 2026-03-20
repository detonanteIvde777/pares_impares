# programa para calcular pares e impares

# libreria
import math

# input

print("----------------------")
print("digite los numeros")
print("----------------------")

# processing and output

cantidad_pares = 0
cantidad_impares = 0
list_n="nuemros: "

for i in range(1, 21):
    n= int(input("digite el numero " + str(i) + ": "))
    m = n % 2
    if (m==0):
        cantidad_pares = cantidad_pares + 1
    else:
        cantidad_impares = cantidad_impares + 2

print("----------------------")
print("cantidad de pares:", cantidad_pares)
print("----------------------")
print("cantidad de impares:", cantidad_impares)
print("----------------------")
print("listado de numeros:", list_n)