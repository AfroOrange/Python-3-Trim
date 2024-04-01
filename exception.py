class usuario:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre

        try:
            if edad <= 0:
                raise ValueError
        except (ValueError or TypeError):
            print('No se puede introducir edad menor que cero')
            while edad <= 0:
                edad = int(input("Ingrese nuevamente el dato: "))
        self.edad = edad

        try: 
            if altura % 2 == 0:
                raise ValueError
        except (ValueError, TypeError):
            print('No se puede transformar un string en un decimal')
            altura = float(input("Ingrese nuevamente el dato: "))
        self.altura = altura

    def mostrar_datos(self):
        print('Nombre:', self.nombre)
        print('Edad  :', self.edad)
        print('Altura:', self.altura)

print("Login")

persona = usuario(input("Inserte su nombre: "), int(input("Inserte la edad: ")), input("Inserte la altura: "))
print("\n")
persona.mostrar_datos()


