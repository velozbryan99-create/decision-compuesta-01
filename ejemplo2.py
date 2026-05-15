"""
    Ejemplo de estructura de condicional
    simple actualizado
"""
# variable edad, asume el valor ingresado por teclado
edad = input("Ingrese la edad de la persona: ") # 27 cadena

# la variable edad, asume un valor de tipo cadena
# por defecto con la función input
# Se debe hacer un cambio de tipo de dato para que
# sea considerado con entero, a través de int

edad = int(edad) # 27entero

# desde aquí la variable edad es considerada con tipo 
# de dato entero

# Se realiza la comparación en el condional
# en función del valor ingresado por teclado

if edad >= 18 and edad <=25:
    # si la condición verdadera, se ejecutan las líneas de
    # código que pertencen al if
    print("Su edad es permitida para ingresar")
else:
    # si la condición es falsa en el if, se ejecutan las líneas 
    # de código que pertenecen al else
    print("Su edad esta fuera de rango")

print("finalizar programa")
