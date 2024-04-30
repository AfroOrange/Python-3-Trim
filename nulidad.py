class recuento:    

    def verPrecio(idempresa):
        total_precio = 0  
        with open('Nulidad.txt', 'r') as filePath:
            for line in filePath:
                if idempresa in line:
                    linea_dividida = line.split()
                    precio_str = linea_dividida[2].replace('.', '').replace(',', '.')  # modifica la línea para poder leer correctamente el número como float
                    pagos = float(precio_str)
                    total_precio += pagos  # acumula los pagos totales de la empresa
        print(total_precio)

    def mandar_email():
        with open("Modelo carta empresa 1.txt") as carta1:
            for line in carta1: 
                print(line)

recuento.mandar_email()
