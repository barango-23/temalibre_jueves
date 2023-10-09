# Diccionario de empleados con información (nombre, salario, departamento)
empleados = {}

# Función lambda para calcular el salario promedio de todos los empleados
calcular_promedio_salario = lambda empleados: sum(empleado["salario"] for empleado in empleados.values()) / len(empleados) if len(empleados) > 0 else 0

# Función lambda para encontrar a los empleados en un departamento específico
buscar_empleados_por_departamento = lambda empleados, departamento: [empleado for empleado in empleados.values() if empleado["departamento"] == departamento]

# Función lambda para encontrar al empleado con el salario más alto
encontrar_empleado_con_salario_mas_alto = lambda empleados: max(empleados.values(), key=lambda x: x["salario"]) if empleados else None

# Función lambda para calcular el total de salarios por departamento
calcular_total_salarios_por_departamento = lambda empleados: {
    departamento: sum(empleado["salario"] for empleado in empleados.values() if empleado["departamento"] == departamento)
    for departamento in set(empleado["departamento"] for empleado in empleados.values())
}

# Menú interactivo
while True:
    print("\nSeleccione una opción:")
    print("1. Agregar un empleado")
    print("2. Calcular salario promedio")
    print("3. Buscar empleados por departamento")
    print("4. Encontrar empleado con salario más alto")
    print("5. Calcular total de salarios por departamento")
    print("6. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Nombre del empleado: ")
        salario = float(input("Salario: "))
        departamento = input("Departamento: ")
        empleados[nombre] = {"salario": salario, "departamento": departamento}
        print(f"{nombre} ha sido agregado como empleado.")
    elif opcion == "2":
        promedio_salario = calcular_promedio_salario(empleados)
        print(f"Salario promedio de todos los empleados: ${promedio_salario:.2f}")
    elif opcion == "3":
        departamento_buscar = input("Departamento a buscar: ")
        empleados_encontrados = buscar_empleados_por_departamento(empleados, departamento_buscar)
        if empleados_encontrados:
            print(f"Empleados en el departamento de {departamento_buscar}:")
            for empleado in empleados_encontrados:
                print(empleado["nombre"])
        else:
            print(f"No se encontraron empleados en el departamento de {departamento_buscar}.")
    elif opcion == "4":
        empleado_salario_mas_alto = encontrar_empleado_con_salario_mas_alto(empleados)
        if empleado_salario_mas_alto:
            print(f"Empleado con el salario más alto: {empleado_salario_mas_alto['nombre']} (${empleado_salario_mas_alto['salario']})")
        else:
            print("No hay empleados en la lista.")
    elif opcion == "5":
        total_salarios_por_departamento = calcular_total_salarios_por_departamento(empleados)
        if total_salarios_por_departamento:
            print("Total de salarios por departamento:")
            for departamento, total_salario in total_salarios_por_departamento.items():
                print(f"{departamento}: ${total_salario}")
        else:
            print("No hay empleados en la lista.")
    elif opcion == "6":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
