while True:
    frase = input("ingresar texto: ")
    if frase.islower():
        break

convertido = ""
for letra in frase: 
    if letra == " ":
        convertido += " "
    elif letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        convertido += letra.upper()
    else:
        convertido += letra
print(convertido)