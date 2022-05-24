def promedio():
    nota_bruta = 0 
    n1 = float(input("ingresar primera nota: "))
    nota_bruta += n1
    n2 = float(input("ingresar segunda nota: "))
    nota_bruta += n2
    n3 = float(input("ingresar tercera nota: "))
    nota_bruta += n3
    if n1 >= 0 and n1 <= 20 and n2 >= 0 and n3 <= 20 and n3 >= 0 and n3 <= 20:
        promedio = nota_bruta/3
        if promedio >= 0 and promedio <= 10.5:
            print("la nota desaprobatoria es : " + str(promedio))
        if promedio > 10.5 and promedio <= 20:
            print("la nota aprobatoria es : " + str(promedio))
    else:
        print("no se puede calcular el promedio")

promedio()
