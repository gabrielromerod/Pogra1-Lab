def generar_filas():
    numero_caracteres = n_filas + 1
    for a in range(numero_caracteres):
        print("{}".format(caracter) * numero_caracteres)
        numero_caracteres -= 1
    print("")

while True:
    caracter = input("Caracter: ")
    n_figuras = int(input("Numero de figuras: "))
    n_filas = int(input("Numero de figuras: "))
    if n_figuras >= 0 and n_filas >= 0:
        print("")
        break

for i in range(n_figuras):
    generar_filas()