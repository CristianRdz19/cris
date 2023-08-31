def funcion_inversa(cadena):
    return cadena [::-1]

cadena = input("Ingresa una palabra: ")
cadena_inversa = funcion_inversa(cadena)

print ("Cadena normal: ", cadena)
print ("Cadena inversa: ", cadena_inversa)

