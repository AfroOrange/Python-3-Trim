import re

class videojuegos:
    idVideojuego = 0

    def __init__(self, nombre, consola, estado, id_juego):
        videojuegos.idVideojuego += 1
        self.id = id_juego

        self.nombre = nombre 
        self.consola = consola
        self.estado = estado

    def añadir_videojuego(self):
            with open('juegos.txt', 'a+') as juegosPath:
                juegosPath.write(f"{self.nombre}, {self.consola}, {self.estado}, {self.id}")
        
    def buscar_videojuego(idvideojuego):
        with open('juegos.txt', 'r') as juegosPath:
            for line in juegosPath:
                if idvideojuego in line:
                    print(line)

    def marcar_obsoleto():
        pass


class usuarios:
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



zelda = videojuegos("Zelda", "Nintendo", "En venta", 1)
zelda.añadir_videojuego
