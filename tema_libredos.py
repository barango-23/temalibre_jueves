# Función lambda para elevar al cuadrado los elementos de una secuencia
cuadrado = lambda secuencia: [x ** 2 for x in secuencia]

# Función lambda para duplicar todos los elementos de una secuencia
duplicar = lambda secuencia: tuple(x * 2 for x in secuencia)

# Función lambda para calcular el cuadrado de todos los valores en un diccionario
cuadrado_valores = lambda diccionario: {clave: valor ** 2 for clave, valor in diccionario.items()}

if __name__ == "__main__":
    # Ejemplo de uso de las funciones lambda
    lista_numeros = [1, 2, 3, 4, 5]
    tupla_valores = (10, 20, 30, 40, 50)
    diccionario_valores = {"a": 5, "b": 10, "c": 15, "d": 20}

    resultado_cuadrado_lista = cuadrado(lista_numeros)
    resultado_duplicar_tupla = duplicar(tupla_valores)
    resultado_cuadrado_diccionario = cuadrado_valores(diccionario_valores)

    print("Lista original:", lista_numeros)
    print("Lista con cuadrados:", resultado_cuadrado_lista)
    print("Tupla original:", tupla_valores)
    print("Tupla duplicada:", resultado_duplicar_tupla)
    print("Diccionario original:", diccionario_valores)
    print("Diccionario con valores al cuadrado:", resultado_cuadrado_diccionario)
