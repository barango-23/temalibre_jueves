# Crear una lista de contactos que contiene diccionarios con la información de cada contacto
contactos = []

# Función para agregar un contacto a la lista
def agregar_contacto(nombre, telefono, correo):
    contacto = {"Nombre": nombre, "Teléfono": telefono, "Correo": correo}
    contactos.append(contacto)
    print(f"Contacto '{nombre}' ha sido agregado a la lista.")

# Función para buscar un contacto por nombre
def buscar_contacto(nombre):
    for contacto in contactos:
        if contacto["Nombre"] == nombre:
            print(f"Nombre: {contacto['Nombre']}")
            print(f"Teléfono: {contacto['Teléfono']}")
            print(f"Correo: {contacto['Correo']}")
            return
    print(f"Contacto '{nombre}' no se encuentra en la lista.")

# Función para mostrar la lista de contactos
def mostrar_contactos():
    print("Lista de contactos:")
    for i, contacto in enumerate(contactos, 1):
        print(f"{i}. {contacto['Nombre']} - {contacto['Teléfono']} - {contacto['Correo']}")

# Menú para que el usuario interactúe
while True:
    print("\nSeleccione una opción:")
    print("1. Agregar un contacto")
    print("2. Buscar un contacto")
    print("3. Mostrar la lista de contactos")
    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Nombre del contacto: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        agregar_contacto(nombre, telefono, correo)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        buscar_contacto(nombre)
    elif opcion == "3":
        mostrar_contactos()
    elif opcion == "4":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
