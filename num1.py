def ingresar_numero(numero):
    if len(str(numero)) == 5:
        return str(numero)[:2] + "k"
    if len(str(numero)) == 6:
        return str(numero)[:3] + "k"
    elif len(str(numero)) == 7:
        return str(numero)[0] + "M"
    elif len(str(numero)) == 8:
        return str(numero)[2] + "M"
    else:
        return str(numero)

numero = int(input("Ingresa un numero: "))
resultado = ingresar_numero(numero)
print(resultado)