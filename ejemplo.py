"""
    Ejemplo de estructura de condicional
    simple actualizado 
"""
# variable edad, asume el valor ingresado por teclado
edad = input("Ingrese la edad de la persona: ")

# la variable edad, asume un valor de tipo cadena
# por defecto con la función input
# Se debe hacer un cambio de tipo de dato para que
# sea considerado con entero, a través de int

edad = int(edad)

# desde aquí la variable edad es considerada con tipo 
# de dato entero

# Se realiza la comparación en el condional
# en función del valor ingresado por teclado

if edad >= 18:
    # si la condición verdadera, se ejecutan las líneas de
    # código que pertencen al if
    print("Usted es mayor de edad en Ecuador.")
else:
    # si la condición es falsa en el if, se ejecutan las líneas 
    # de código que pertenecen al else
    print("Usted es menor de edad en Ecuador.")


