def funcion_max_de_3(num1,num2,num3):
    maximo= max(num1,num2,num3)
    return maximo

num1= int(input("Escribe un numero: "))
num2= int(input("Escribe un numero: "))
num3= int(input("Escribe un numero: "))

resultado = funcion_max_de_3(num1, num2, num3)
print("El numero mayor es: ", resultado)
