while True:
    n = int(input("Numero de gorinkis: "))
    if n > 3:
        print("")
        break

contador = 1
while contador < n:
    for i in range(1,6):
        sum = 0
        val = float(input("Presion sistlica " + str(i) + " : "))
        sum += val
    promedio = sum / 5
    if promedio > 130:
        print("Ud. es hipertenso , el promedio de su presion sistica es: " + str(promedio))
    else:
        print("Ud.No es hipertenso , el promedio de su presion sistlica es: " + str(promedio))