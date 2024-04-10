class Videojuegos:
    idVideojuego = 1
    estados_validos = ["En venta", "Agotado", "Obsoleto"]  # Lista para agregar los estados de los juegos
    nombres_validos = ["PlayStation", "PS4", "PS5", "XBOX", "XBOX ONE", "Nintendo", "Switch", "PC", "Todas"]  # Lista para agregar consolas

    def __init__(self, nombre, consola, estado):
        if consola not in Videojuegos.nombres_validos:
            raise ValueError(f"Los nombres válidos son: {', '.join(Videojuegos.nombres_validos)}")

        if estado not in Videojuegos.estados_validos:
            raise ValueError(f"Los valores válidos son: {', '.join(Videojuegos.estados_validos)}")

        self.nombre = nombre
        self.consola = consola
        self.estado = estado

    # Método para añadir videojuegos nuevos 
    def añadir_videojuego(self):
        # Guarda los números de serie de los juegos
        numeros_seriales = set()

        # Lee el archivo para comprobar si existen números de serie iguales
        with open('juegos.txt', 'r') as juegosPath:
            for line in juegosPath:
                serial = line.split("| Nº de serie -->")[-1].strip()
                numeros_seriales.add(int(serial))
        
        # Establece el siguiente número de serie disponible
        while Videojuegos.idVideojuego in numeros_seriales:
            Videojuegos.idVideojuego += 1

        self.serial = Videojuegos.idVideojuego

        # Finalmente añade una entrada nueva a juegos.txt con el videojuego
        with open('juegos.txt', 'a+') as juegosPath:
            juegosPath.write(f"| {self.nombre} | {self.consola} | {self.estado} | Nº de serie --> {self.serial}\n")
