# Clase usuario para 
class Usuario:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre

        edad_valida = False
        while not edad_valida:
            try:
                edad = int(edad)
                if edad <= 0:
                    raise ValueError
                edad_valida = True
            except ValueError:
                print('La edad debe ser un número entero positivo')
                edad = input("Ingrese nuevamente la edad: ")
                
        self.edad = edad

        altura_valida = False
        while not altura_valida:
            try:
                altura = int(altura)
                if altura <= 0:
                    raise ValueError
                altura_valida = True
            except ValueError:
                print('La altura debe ser un número entero positivo')
                altura = input("Ingrese nuevamente la altura en centímetros: ")

        self.altura = altura

    def mostrar_datos(self):
        print('Nombre:', self.nombre)
        print('Edad  :', self.edad)
        print('Altura:', self.altura / 100, 'm')

print("---------- Inicio de Sesión ----------")

nombre = input("Inserte su nombre: ")
edad = input("Inserte la edad: ")
altura = input("Inserte la altura en centímetros: ")

persona = Usuario(nombre, edad, altura)
print("\n")
persona.mostrar_datos()
