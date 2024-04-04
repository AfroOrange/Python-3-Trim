# Método para buscar usuarios a través del DNI
def buscar_usuario(dni):
    with open('usuarios.txt', 'r') as filePath:
        for line in filePath:
            if dni in line:
                print(line)

dni = str(input("Introducir DNI: "))
buscar_usuario(dni)
