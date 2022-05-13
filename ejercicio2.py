while True:
    n = int(input("Filas : "))
    if n >= 1 and n <= 10:
        print("")
        break

total_lineas = n
lineas_hechas = 1
caracteres_hechos = n
caracteres_hechos_impresos = 1
while lineas_hechas != total_lineas:
    for i in range(n, 0, -1):
        print("0" * caracteres_hechos, end="" + str(caracteres_hechos_impresos) )
        
    caracteres_hechos_impresos += 1
    lineas_hechas += 1