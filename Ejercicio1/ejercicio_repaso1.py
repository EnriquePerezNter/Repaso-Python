#Ejercicio Repaso

import json

lista_empleados = []

# Agregar Empleado
def agregar_empleado():
    print('Introduce los datos del empleado:')
    id = int(input('Id del Empleado:'))
    nombre = input('Nombre del empleado:')
    edad = int(input('Edad del Empleado:'))
    departamento = input('Departamento del Empleado:')
    salario = float(input('Salario del Empleado:'))  
    
    nuevo_empleado = {'id': id, 'nombre': nombre, 'edad': edad, 'departamento': departamento, 'salario': salario}    
    lista_empleados.append(nuevo_empleado)
    print('El empleado ha sido añadido correctamente')

# Buscar Empleado por id
def buscar_empleado_por_id():
    id = int(input('Introduce el Id del empleado que quieres buscar:'))
    encontrado = False  
    for empleado in lista_empleados:
        if empleado['id'] == id:
            print('Empleado encontrado')
            print(f"ID: {empleado['id']}, Nombre: {empleado['nombre']}, Edad: {empleado['edad']}, Departamento: {empleado['departamento']}, Salario: {empleado['salario']}")
            encontrado = True  
            break  
    if not encontrado:
        print(f'No se ha encontrado ningún empleado con el Id: {id}') 

# Eliminar empleados
def eliminar_empleado_por_id():
    id = int(input('Introduce el Id del empleado que quieres eliminar:'))
    encontrado = False  
    for empleado in lista_empleados:
        if empleado['id'] == id:
            print('Empleado eliminado')
            encontrado = True  
            lista_empleados.remove(empleado)
            break
    if not encontrado:
        print(f'No se ha encontrado ningún empleado con el Id: {id}') 

# Mostrar empleados
def mostrar_empleados():
    if lista_empleados:
        print('Estos son todos los empleados disponibles:')
        for empleado in lista_empleados:
            print(f"ID: {empleado['id']}, Nombre: {empleado['nombre']}, Edad: {empleado['edad']}, Departamento: {empleado['departamento']}, Salario: {empleado['salario']}")
    else:
        print('No hay ningún empleado registrado')

# Guardar empleados en un archivo JSON
def guardar_empleados_en_archivo():
    if lista_empleados:
        with open('empleados.json', 'w') as archivo_empleado:
            json.dump(lista_empleados, archivo_empleado, indent=4)
            print('Los empleados se han guardado correctamente')
    else:
        print('No hay ningún empleado registrado')

# Cargar empleados desde un archivo JSON
def cargar_empleados_desde_archivo():
    try:
        with open('empleados.json', 'r') as archivo_empleado:
            lista_empleados.extend(json.load(archivo_empleado))
            print("Empleados cargados desde el archivo.")
    except FileNotFoundError:
        print("El archivo 'empleados.json' no existe.")

# Menú
def seleccion_opcion():
    print('1. Agregar empleado  \n2. Buscar empleado por ID  \n3. Eliminar empleado por ID  \n4. Mostrar todos los empleados  \n5. Guardar empleados en un archivo  \n6. Cargar empleados desde un archivo  \n7. Salir')
    while True:
        try:
            opcion = int(input('Selecciona una opción válida (1-7): '))
            if opcion < 1 or opcion > 7:
                print('Selecciona una opción válida')
                continue
            
            if opcion == 1:
                agregar_empleado()
            elif opcion == 2:
                buscar_empleado_por_id()
            elif opcion == 3:
                eliminar_empleado_por_id()
            elif opcion == 4:
                mostrar_empleados()
            elif opcion == 5:
                guardar_empleados_en_archivo()
            elif opcion == 6:
                cargar_empleados_desde_archivo()
            elif opcion == 7:
                print('Salida Completada')
                break 
        except ValueError:
            print('Por favor, ingresa un número entero.')

seleccion_opcion()
