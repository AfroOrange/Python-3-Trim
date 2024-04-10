import re

class Usuarios:
    def __init__(self, dni, nombre, apellidos, telefono, correo):
        self.dni = dni(re.sub(r'[0-9]{8}[A-Z]'))
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono 
        self.correo = correo

    def agregar_usuarios(dni, nombre, apellidos, telefono, correo):
        with open('usuarios.txt', 'a+') as filePath:
            filePath.write(f"{dni}, {nombre}, {apellidos}, {telefono}, {correo}")

    def buscar_usuario(dni):
        with open('usuarios.txt', 'r') as filePath:
            for line in filePath:
                if dni in line:
                    print(line)

    def eliminar_usuario():
        pass

