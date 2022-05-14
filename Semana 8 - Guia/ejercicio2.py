while True:
    n = int(input("Filas : "))
    if n >= 1 and n <= 10:
        print("")
        break

total_lineas = n + 1
lineas_hechas = 1
caracteres_hechos = n - 1
caracteres_hechos_impresos = 1
while lineas_hechas < total_lineas:
    numeros = ""
    for ni in range(caracteres_hechos_impresos, 0, -1):
            numeros += str(ni)
    print("0" * caracteres_hechos, end="" + str(numeros) +"\n")
        
    caracteres_hechos_impresos += 1
    lineas_hechas += 1
    caracteres_hechos -= 1