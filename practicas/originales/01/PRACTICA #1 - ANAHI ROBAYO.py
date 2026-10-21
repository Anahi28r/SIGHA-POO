# Práctica #1
# ROBAYO TUAREZ ANAHI CAROLINA 

#Datos Primitivos
numero = 1
print(numero)

texto = "Hola Mundo"
print(texto)

decimal = 5.5
print(decimal)

verdadero = True
print(verdadero)

falso = False
print(falso)

#Entrada de Datos por teclado
nombre = input("Ingrese su nombre:")
print("Nombre:", nombre)

edad = int(input("Ingrese su edad:"))
print("Edad:",edad)

#listas
nombre = ["Carolina", "Thiago", "Alejandra", "Jose"]
print(nombre[0])
print(nombre[1])
print(nombre[2])
print(nombre[3])

#Matrices(Listas de listas)
matriz = [
    [10, 2, 1],
    [9, 8, 4],
    [4, 5, 2]
]

for fila in matriz:
    print(fila)

#Arrays (con NumPy) 
import numpy as np

arr1 = np.array([25, 15, 32])
arr2 = np.array([[5, 10,], [8, 6]])
print(arr1)
print(arr2)

#Funciones con Arrays
def mostrar_array(array):
    print(array)

arr = np.array([5, 10, 15, 20])

mostrar_array(arr + 2)

#Ejercicios con funciones
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)

print("Resultado:", resultado)

#Bucle for
for i in range(1, 6):
  print(i)

#Bucle While
x = 8

while x > 2:
    print(x)
    x = x - 1

#Switch (Case)
numero = int(input("Ingrese un número del 1 al 3: "))

if numero == 1:
    print("Elegiste UNO")
elif numero == 2:
    print("Elegiste DOS")
elif numero == 3:
    print("Elegiste TRES")
else:
    print("Número inválido")


#Ejercicios de aplicacion de los Bucles
numero = 2
contador = 1

while contador <= 3:
    print("Tabla del", numero)

    for i in range(1, 6):
        print(numero, "x", i, "=", numero * i)

    numero = numero + 1
    contador = contador + 1


#Ejercicio final: Crear un programa en Python que le solicite al usuario un numero del 1 al 7, y que muestre el dia 
#de la semana correspondiente a ese numero utilizando; un Switch (Case) simulado, entrada de datos por teclado y un bucle For.
numero = int(input("Ingrese un número del 1 al 7: "))

for i in range(1, 8):

    if numero == i:
        if i == 1:
            print("El día correspondiente es: Lunes")
        elif i == 2:
            print("El día correspondiente es: Martes")
        elif i == 3:
            print("El día correspondiente es: Miércoles")
        elif i == 4:
            print("El día correspondiente es: Jueves")
        elif i == 5:
            print("El día correspondiente es: Viernes")
        elif i == 6:
            print("El día correspondiente es: Sábado")
        elif i == 7:
            print("El día correspondiente es: Domingo")

if numero < 1 or numero > 7:
    print("El número debe ser entre 1 y 7.")