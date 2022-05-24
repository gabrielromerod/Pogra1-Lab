

while True:
    n = int(input("ingresar el numero: "))
    if n >= 2:
        break

def factorializador(pa = 0):
    contador = n - pa
    while contador > 0:
        factorial = 1
        for i in range(contador, 1, -1):
            factorial = factorial* i
        print("el factorial de " + str(contador) + " es: " + str(factorial))
        contador -= 2

if n % 2 == 0:
    factorializador()
if n % 2 != 0:
    factorializador(1)