def generador_tablas(contador, n):
    contador_tabla = 1
    n += 1
    while n > contador:
        print(str(contador) + " X " + str(contador_tabla) + " = " + str(contador * contador_tabla))
        contador_tabla += 1
        if contador_tabla > 10:
            print("")
            contador_tabla -= 10
            contador += 2

while True:
    n = int(input("Numero desde 1 a 9 : "))
    if n >= 1 and n <= 10:
        print("")
        break

if n % 2 == 0:
    generador_tablas(2, n)
if n % 2 != 0:
    generador_tablas(1, n)