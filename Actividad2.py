#1) Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura. 
# Calcula el área de un rectángulo de 15 de base y 10 de altura
# Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.

def area_rectangulo(base, altura):
    area = base * altura
    return area 

print("Ejemplo de uso: ")
ejemplo = area_rectangulo(15,10)
print(f"El área del rectángulo de base 15 y altura 10 es de {ejemplo} ")
print("-------------------------------------------------------------------------------------------------------------")

while True:
    base = input("Ingrese la base de su rectángulo (fin para salir): ")
    if base.lower() == "fin":
        break
    altura = input("Ingrese la altura de su rectángulo (fin para salir): ")
    if altura.lower() == "fin":
        break
    
    if base.isdigit() and altura.isdigit():
        base = float(base)
        altura = float(altura)
        area_r = area_rectangulo(base, altura)
        print(f"El área del rectángulo de base {base} y altura {altura} es de {area_r} ")
        print("-------------------------------------------------------------------------------------------------------------")
    else:
        print("Por favor ingrese la base y altura en formato númerico.")

#2) Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. 
# Calcula el área de un círculo de 5 de radio
#Ayuda: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. 
# Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math.

import math
def area_circulo(radio):
    # Acceder al número pi
    pi = math.pi
    area = (radio**2) * pi 
    return area 

print("Ejemplo de uso: ")
ejemplo = area_circulo(5)
print(f"El área del círculo de radio 5 es de {ejemplo} ")
print("-------------------------------------------------------------------------------------------------------------")

while True:
    radio = input("Ingrese el radio de su círculo (fin para salir): ")
    if radio.lower() == "fin":
        break
    elif radio.isdigit():
        radio = float(radio)
        area_c = area_circulo(radio)
        print(f"El área del círculo de radio {radio} es de {area_c} ")
        print("-------------------------------------------------------------------------------------------------------------")
    else:
        print("Por favor ingrese el radio en formato númerico.")


#3) Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:
# ✓ Si el primer número es mayor que el segundo, debe devolver 1.
# ✓ Si el primer número es menor que el segundo, debe devolver -1.
# ✓ Si ambos números son iguales, debe devolver un 0.
#Comprueba la relación entre los números: 5 y 10, 10 y 5, 5 y 5.

def relacion(num1,num2):
    if num1 > num2:
        return 1, f"El {num1} es mayor que el {num2}"
    elif num1 < num2:
        return -1, f"El {num1} es menor que el {num2}"
    else:
        return 0, f"El {num1} es igual que el {num2}"
 
print("Ejemplos de uso")
ejemplo1, respuesta = relacion(5,10)
print(f"{respuesta} ----------> {ejemplo1}")

ejemplo2, respuesta = relacion(10,5)
print(f"{respuesta} ----------> {ejemplo2}")

ejemplo3, respuesta = relacion(5,5)
print(f"{respuesta} ----------> {ejemplo3}")
print("-------------------------------------------------------------------------------------------------------------")

while True: 
    num1 = input("Ingrese el primer número (fin para salir): ")
    if num1.lower() == "fin":
        break
    num2 = input("Ingrese el segundo número (fin para salir): ")
    if num2.lower() == "fin":
        break
    
    if num1.isdigit() and num2.isdigit():
        num1 = float(num1)
        num2 = float(num2)
        resultado, respuesta = relacion(num1,num2)
        print(f"{respuesta} ----------> {resultado}")
        print("-------------------------------------------------------------------------------------------------------------")
    else:
        print("Por favor ingrese los números en formato númerico.")
    
#4) Realiza una función llamada intermedio() que, a partir de dos números, devuelva su punto intermedio:
# Ayuda: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2
# Comprueba el punto intermedio entre -12 y 24

def intermedio(num1, num2):
    punto_intermedio = (num1 + num2) / 2
    return punto_intermedio

print("Ejemplos de uso")
ejemplo = intermedio(-12,24)
print(f"El punto intermedio entre el -12 y el 24 es {ejemplo} ")
print("-------------------------------------------------------------------------------------------------------------")

while True:
    num1 = input("Ingrese el primer número (fin para salir): ")
    if num1.lower() == "fin":
        break
    num2 = input("Ingrese el segundo número (fin para salir): ")
    if num2.lower() == "fin":
        break
    
    if num1.isdigit() and num2.isdigit():
        num1 = float(num1)
        num2 = float(num2)
        resultado = intermedio(num1,num2)
        print(f"El punto intermedio entre el {num1} y el {num2} es {resultado} ")
        print("-------------------------------------------------------------------------------------------------------------")
    else: 
        print("Por favor ingrese los números en formato númerico.")

#5) Realiza una función llamada recortar() que reciba tres parámetros. El primero es el número a recortar, 
# el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:
# ✓ Devolver el límite inferior si el número es menor que éste
# ✓ Devolver el límite superior si el número es mayor que éste.
# ✓ Devolver el número sin cambios si no se supera ningún límite.
# ✓ Comprueba el resultado de recortar 15 entre los límites 0 y 10

def recortar(num,limite_inferior,limite_superior):
    if num < limite_inferior:
        return limite_inferior
    elif num > limite_superior:
        return limite_superior
    else:
        return num
 
print("Ejemplos de uso") 
ejemplo = recortar(15,0,10)
print("El resultado de recortar el número 15 entre los límites 0 y 10 es:", ejemplo)
print("-----------------------------------------------------------------------------------------------------------------------------")

while True:
    num = input("Ingrese un número a recortar (fin para salir): ")
    if num.lower() == "fin":
        break
    limite_inferior = input("Ingrese un límite inferior (fin para salir): ")
    if limite_inferior.lower() == "fin":
        break
    limite_superior = input("Ingrese un límite superior (fin para salir): ")
    if limite_superior.lower() == "fin":
        break
    
    if num.isdigit() and limite_inferior.isdigit() and limite_superior.isdigit():
        num = int(num)
        limite_inferior = int(limite_inferior)
        limite_superior = int(limite_superior)
        resultado = recortar(num,limite_inferior,limite_superior)
        print(f"El resultado de recortar el número {num} entre los límites {limite_inferior} y {limite_superior} es {resultado}")
        print("-----------------------------------------------------------------------------------------------------------------------------")
    else:
        print("Por favor ingrese el número y los límites en formato númerico.")

#6) Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. 
# La primera con los números pares, y la segunda con los números impares:
# Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()

def separar(lista):
    pares = []
    impares = []

    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    pares.sort()
    impares.sort()
    return pares, impares

lista_numeros = []
while True:
    num = input("Ingrese los números que desee (fin para terminar): ")
    if num.lower() == "fin":
        break
    elif num.isdigit():
        lista_numeros.append(int(num))
    else:
        print("Por favor ingrese un número")

print(f"Lista = {lista_numeros}")
pares, impares = separar(lista_numeros)
print(f"Los Números Pares son {pares}")
print(f"Los Números Impares son {impares}")
