# Ejercicio 5: (Lectura con centinela)
def ejercicio_5():
    suma = 0
    rep = 0
    while True:
        n = int(input("Ingrese su número: "))
        if n != 0:
            suma += n
            rep += 1
        else:
            break
    print(suma/rep)

#Ejercicio 6: (Lectura con centinela)
def ejercicio_6():
    i = 0
    par = 0
    impar = 0
    while True:
        n = int(input("Ingrese su número: "))
        if n == 0:
            break
        i = i + 1
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
    print("Cantidad de números leidos: " + str(i))
    print("Cantidad de números pares: " + str(par))
    print("Cantidad de números impares: " + str(impar))

#Ejercicio 7: Realice un programa, que permita leer un número entero mayor que uno y determine si el número es un número perfecto o no.
def ejercicio_7():
    while True:
        n = int(input("Ingrese su número: "))
        if n > 1:
            break
    suma = 0
    i=1
    while i < n:
        if n%i == 0:
            suma = suma + i
            i = i + 1
    if suma == n:
        print("El número es perfecto")
    else:
        print("El número no es perfecto")

