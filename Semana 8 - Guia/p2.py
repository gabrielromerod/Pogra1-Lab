def generar_hasteriscos():
    numero_caracteres = n
    for a in range(numero_caracteres):
        print("#" * numero_caracteres + str(numero_caracteres))
        numero_caracteres -= 1

while True:
    n = int(input("ingresar numero: "))
    if n >= 1 and n <= 15:
        break

generar_hasteriscos()