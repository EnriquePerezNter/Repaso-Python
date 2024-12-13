#Ejercicio de repaso 2

import csv


def cargar_datos_comentarios():
    with open('Ejercicio2\\comentarios.csv', 'r') as archivo_comentarios:
        lector_csv = csv.DictReader(archivo_comentarios)
        lista_comentarios= [fila for fila in lector_csv]
    
    return lista_comentarios 

def cargar_datos_publicaciones():
    with open('Ejercicio2\\publicaciones.csv', 'r') as archivo_publicaciones:
        lector_csv = csv.DictReader(archivo_publicaciones)
        lista_publicaciones= [fila for fila in lector_csv]

    return lista_publicaciones

def cargar_datos_usuarios():
    with open('Ejercicio2\\usuarios.csv', 'r') as archivo_usuarios:
        lector_csv = csv.DictReader(archivo_usuarios)
        lista_usuarios= [fila for fila in lector_csv]

    return lista_usuarios

#Clase publicacion
class Publicacion:
    def __init__(self,id,contenido):
        self.id= id
        self.contenido= contenido
        self.comentario= []

#Metodo para agregar un comentario

    def agregar_comentario (self):
        texto : str
        nombre_usuario = ''
        texto= input('Escribe el comentario:')

        comentario = {'nombre_usuario': nombre_usuario, 'texto': texto}
        pass

#Metodo para ver todos comentarios
    def ver_comentarios (self):
        pass
    
#Metodo para ver detalles de la publicacion junto con los comentarios de la misma
    def ver_detalles (self):
        pass

#Clase usuario
class Usuario: 
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.publicaciones = []

#Metodo para crear una publicación        
    def crear_publicacion (self):
        pass

#Metodo para ver todas las publicaciones de el usuario
    def ver_publicaciones (self):
        pass



#Clase red social (maneja las interacciones y operaciones dentro de la red social)
class RedSocial:
    def __init__ (self):
        self.usuarios= cargar_datos_usuarios()
        self.publicaciones = cargar_datos_publicaciones()
        self.comentarios = cargar_datos_comentarios()
        
    def registrar_usuarios(self):
        new_usuario= Usuario(id= input('Escribe el id del usuario: '), nombre = input ('Escribe el nombre del usuario: '), email= input('Escribe el email del usuario: '))

        self.usuarios.append(new_usuario)
        
        with open('Ejercicio2\\usuarios.csv', 'a') as archivo_usuarios:
            escritor_csv = csv.writer(archivo_usuarios)
            escritor_csv.writerow([new_usuario.id, new_usuario.nombre, new_usuario.email])

        print("Usuario registrado exitosamente.")

    def crear_publicacion(self):
        new_publicacion= Publicacion(id= input('Escribe el id de la publicacion: '), contenido = input ('Escribe el contenido de la publicacion: '))

        self.publicaciones.append(new_publicacion)
        
        with open('Ejercicio2\\publicaciones.csv', 'a') as archivo_publicaciones:
            escritor_csv = csv.writer(archivo_publicaciones)
            escritor_csv.writerow([new_publicacion.id, new_publicacion.contenido])

        print("Publicacion registrado exitosamente.")

    def listar_usuarios(self):
        self.usuarios = cargar_datos_usuarios()
        for usuario in self.usuarios:
            print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Email: {usuario['email']}")

    def listar_publicaciones(self):
        self.publicaciones = cargar_datos_publicaciones()
        for publicacion in self.publicaciones:
            print(f"ID: {publicacion['id']}, Contenido: {publicacion['contenido']}")
# Menú
def menu():
    cargar_datos_usuarios()
    cargar_datos_comentarios()
    cargar_datos_publicaciones()
    red_social= RedSocial()
    print('1. Crear Usuario  \n2. Crear publicacion   \n3. Agregar comentario a una publicacion  \n4. Ver los detalles de una publicacion  \n5. Listar todos los usuarios  \n6. Listar toda las publicaciones  \n7. Ver los comentarios de una publicacion  \n8. Salir')
    while True:
        try:
            opcion = int(input('Selecciona una opción válida (1-8): '))
            if opcion < 1 or opcion > 8:
                print('Selecciona una opción válida')
                continue
            
            if opcion == 1:
                red_social.registrar_usuarios()
            elif opcion == 2:
                red_social.crear_publicacion()
            elif opcion == 3:
                print('Funcion no implentada')
            elif opcion == 4:
                print('Funcion no implentada')
            elif opcion == 5:
                red_social.listar_usuarios()
            elif opcion == 6:
                red_social.listar_publicaciones()
            elif opcion == 7:
                print('Funcion no implentada')
            elif opcion == 8:
                print('Salida Completada')
                break 
        except ValueError:
            print('Por favor, ingresa un número entero.')

menu()