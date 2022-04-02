#Ejercicio 2
def exchange_house():
    dolar_value = 3.8
    euro_value = 4.2
    print("Estas en el mejor lugar para cambiar dinero - La casa de cambio de Gabriel")
    print("Tenemos el mejor tipo de cambio DOLAR: " + str(dolar_value))
    print("Tenemos el mejor tipo de cambio EURO: " + str(euro_value))
    soles = float(input("Introduce el monto de soles a convertir: "))
    converted_value_dolar = soles // dolar_value
    converted_value_euro = soles // euro_value
    print("Te corresponderia " + str(converted_value_dolar) + " dolares")
    print("Te corresponderia " + str(converted_value_euro) + " euros")

#Ejercicio 3
def when_100():
    name = input("Introduce tu nombre: ")
    actual_age = int(input("Introduce la edad que cumpliste o cumplirás este año: "))
    age_100 = 100 - actual_age
    year_100 = 2022 + age_100
    print(str(name) + " en el año " + str(year_100) + " tendrás 100 años.")

#Ejercicio 4
def minutes_to_seconds():
    minutes = float(input("Introduce la cantidad de minutos a convertir: "))
    seconds = minutes * 60
    print(str(minutes) + " minutos equivale a " + str(seconds) + " segundos")

#Ejercicio 5
def minutes_with_seconds():
    seconds = int(input("Introduce la cantidad de segundos a convertir: "))
    minutes = seconds // 60
    seconds_residue = seconds % 60
    print("Equivale a " + str(minutes) + " minutos con " + str(seconds_residue) + " segundos")
