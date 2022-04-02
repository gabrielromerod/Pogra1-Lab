#Ejercicio 1
peso = int(input("ingresar peso en gramos: "))
altura = int(input("ingresar altura en cm: "))
bmi = (peso/1000)/((altura/100)**2)
print("el indice de masa corporal es: "+str(bmi))

#Ejercicio 2
import math
x2 = int(input("ingresa x2: "))
y2 = int(input("ingrsae y2: "))
x1 = int(input("ingresa x1: "))
y1 = int(input("ingrsae y1: "))
distancia = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
print("la distancia es: "+str(distancia))

#Ejercicio 3
num = input("Ingrese un número: ")
print("número invertido " + num[2] +  num[1]  + num[0])

#Ejercicio 4
segundos = int(input("Ingrese la cantidad de segundos: "))
seg = segundos % 60
min = segundos // 60
hor = min // 60
dia = hor // 24
print(seg)
print(min-(hor*60))
print(hor-(24*dia))
print(dia)
print("Equivale a: " + str(dia) + ":" + str(hor-(24*dia)) + ":" + str(min-(hor*60)) + ":" + str(seg))

#Ejercicio 5
from math import tan, pi
s = int(input("ingresa longitud de lados: "))
n = int(input("numero de lados: "))
area = (n*(s**2)) / (4*tan(pi/n))
print(area)

#Ejercicio 1 - S2
kW_consume = float(input("Introduce el consumo de kW: "))
if kW_consume > 100:
    kW_consume_extra = kW_consume - 100
    final_cost = (kW_consume_extra * 0.7) + 45.22
    print("El consumo de electricidad en soles es de: " + str(final_cost))
else:
    final_cost = kW_consume * 0.4522
    print("El consumo de electricidad en soles es de: " + str(final_cost))

#Ejercicio 1 - S2
