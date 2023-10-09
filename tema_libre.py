# Crear una lista de tuplas para el inventario de productos
inventario_lista = []

# Crear un diccionario para el inventario de productos
inventario_diccionario = {}

# Función para agregar un producto
def agregar_producto(nombre, precio, cantidad):
    if nombre in inventario_diccionario:
        print(f"{nombre} ya existe en el inventario.")
    else:
        producto = (nombre, precio, cantidad)
        inventario_lista.append(producto)
        inventario_diccionario[nombre] = {"precio": precio, "cantidad": cantidad}
        print(f"{nombre} ha sido agregado al inventario.")

# Función para eliminar un producto
def eliminar_producto(nombre):
    if nombre in inventario_diccionario:
        inventario_lista[:] = [producto for producto in inventario_lista if producto[0] != nombre]
        del inventario_diccionario[nombre]
        print(f"{nombre} ha sido eliminado del inventario.")
    else:
        print(f"{nombre} no existe en el inventario.")

# Función para realizar una venta
def realizar_venta(nombre, cantidad):
    producto = inventario_diccionario.get(nombre)
    if producto:
        if producto["cantidad"] >= cantidad:
            precio_total = cantidad * producto["precio"]
            producto["cantidad"] -= cantidad
            for i, (nombre, precio, cantidad_disponible) in enumerate(inventario_lista):
                if nombre == producto:
                    nueva_cantidad = cantidad_disponible - cantidad
                    inventario_lista[i] = (nombre, precio, nueva_cantidad)
            return precio_total
        else:
            print(f"No hay suficientes {nombre} en stock.")
    else:
        print(f"{nombre} no existe en el inventario.")
    return 0

# Función para mostrar el inventario
def mostrar_inventario():
    print("Inventario:")
    for nombre, producto in inventario_diccionario.items():
        print(f"{nombre}: Precio Unitario=${producto['precio']}, Cantidad Disponible={producto['cantidad']}")

# Menú para que el usuario interactúe
while True:
    print("\nSeleccione una opción:")
    print("1. Agregar un producto")
    print("2. Eliminar un producto")
    print("3. Realizar una venta")
    print("4. Mostrar inventario")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio unitario: "))
        cantidad = int(input("Cantidad disponible: "))
        agregar_producto(nombre, precio, cantidad)
    elif opcion == "2":
        nombre = input("Nombre del producto a eliminar: ")
        eliminar_producto(nombre)
    elif opcion == "3":
        nombre = input("Nombre del producto a vender: ")
        cantidad = int(input("Cantidad a vender: "))
        total_venta = realizar_venta(nombre, cantidad)
        if total_venta:
            print(f"Venta de {nombre}: ${total_venta}")
    elif opcion == "4":
        mostrar_inventario()
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
