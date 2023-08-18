#Actividad Nº 1
#Consigna
#Realizar una función llamada año_bisiesto:
# ✓ Recibirá un año por parámetro
# ✓ Imprimirá “El año año es bisiesto” si el año es bisiesto
# ✓ Imprimirá “El año año no es bisiesto” si el año no es bisiesto
# ✓ Si se ingresa algo que no sea número, debe indicar que se ingrese un número.
#Información a tener en cuenta:
# Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. 
# Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.


# Este bloque de código define una función llamada anio_bisiesto. Toma un parámetro anio y utiliza múltiples condicionales 
# para determinar si el año es bisiesto o no. Devuelve una cadena de texto correspondiente al resultado.
def anio_bisiesto(anio):
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        respuesta = "Es bisiesto"
        return respuesta
    else:
        respuesta = "No es bisiesto" 
        return respuesta
   
# Estas líneas de código solicitan al usuario que ingrese su nombre y luego muestran un mensaje de bienvenida 
# junto con una breve descripción del programa.
nombre = input("Ingrese su nombre: ")
print(f"Bienvenid@ {nombre}, este programa le dirá si el año ingresado es bisiesto o no")

# Este bucle while se ejecuta continuamente hasta que se alcance una condición de salida. 
# Solicita al usuario que ingrese un año o la palabra "fin" para salir del programa.
while True:
    anio = input("Ingrese un año (o escriba 'fin' para salir): ") 

  # Dentro del bucle, se verifica si el valor ingresado para el año es la palabra "fin" (en minúsculas). 
  # Si es así, se muestra un mensaje de despedida y se rompe el bucle con break, finalizando el programa.
    if anio.lower() == "fin": 
        print(f"Gracias {nombre} por usar nuestro programa")
        break

  # En esta parte, se verifica si el valor ingresado para el año es un número utilizando el método isdigit().
  # Si es un número, se convierte a entero y se llama a la función anio_bisiesto para determinar si es bisiesto o no. 
  # El resultado se imprime en pantalla. Si no es un número, se muestra un mensaje de error. 
  # El bucle continúa solicitando un año válido hasta que se ingrese "fin" como palabra clave de salida.
    if anio.isdigit(): 
        anio = int(anio)  
        respuesta = anio_bisiesto(anio) 
        print(f"El año {anio} {respuesta}") 
    else: 
        print("Por favor ingrese el año en formato númerico.")
