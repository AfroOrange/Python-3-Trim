# Método para buscar usuarios a través del DNI
def buscar_usuario(dni):
    with open('usuarios.txt', 'r') as filePath:
        for line in filePath:
            if dni in line:
                print(line)

# Método para agregar usuarios con los datos introducidos
def agregar_usuarios(dni, nombre, apellidos, correo):
    with open('usuarios.txt', 'a+') as filePath:
        filePath.write("\n"f"{dni}, {nombre}, {apellidos}, {correo} \n")
        print("Datos agregados:", dni, nombre, apellidos, correo)

# Mismo método para agregar, pero esta vez leerá los datos almacenados en una lista
def agregar_lista_datos(datos):
    with open('usuarios.txt', 'a+') as filePath:
        for valores in datos:
            filePath.write(valores + ', ')
        print("Datos agregados correctamente")

# Método para eliminar usuarios a través del DNI

# Datos de los usuarios para buscar
id = str(input("Insertar DNI: "))
buscar_usuario(id)

# Datos del usuario para introducir 
dni = '02103123d'
nombre = 'Manuel'
apellidos = 'López Ortega'
correo = 'manuelortega@correo.com'
agregar_usuarios(dni, nombre, apellidos, correo)

# Ejemplo con una lista de datos
datos = ['02103123d', 'Elena', 'Marrero Dávila', 'elenadav@correo.com']
agregar_lista_datos(datos)
