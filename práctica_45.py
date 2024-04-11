# Método para mostrar todos los datos del archivo 
def mostrar_usuarios(file):
    for line in file:
        print(line)

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
def eliminar_usuario(dni):
        # La variable datos será un array donde guardaremos todas las líneas del documento
    datos = []

        # Una vez encuentre el DNI introducido, borrará el documento
    with open('usuarios.txt', 'r') as filePath:
        for line in filePath:
            if dni not in line:
                datos.append(line)

        # Luego lo reescribirá con los datos guardados
    with open('usuarios.txt', 'w') as filePath:
        for line in datos:
            filePath.write(line) 

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

archivo = open("usuarios.txt")

## "Menú"
print("--------- Inicio de Sesión ---------")
print("| 1 --> Ver la lista de usuarios  |  2 --> Buscar un usuario por DNI  |  3 --> Agregar un nuevo usuario  |  4 --> Eliminar un usuario  |")
respuesta = int(input("Seleccione la opción que sea hacer:" ))

# Acciones según la respuesta del usuario
while respuesta < 5:
    if respuesta == 1:
        mostrar_usuarios(archivo)
    if respuesta == 2:
        buscar_usuario(str(input("Introducir DNI:" )))
    if respuesta == 3:
        agregar_usuarios(str(input("DNI:" )), str(input("Nombre:" )), str(input("Apellidos:" )), str(input("Correo electrónico:" )))
    if respuesta == 4:
        pass

    print("\n")
    finalizar = str(input("¿Quiere hacer otra opción? --- | S / N |"))
    if finalizar == "S":
        pass
