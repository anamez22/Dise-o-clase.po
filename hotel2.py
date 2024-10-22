# Clase Habitaciones
class Habitaciones:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.reservada = False
        self.huesped = None

    def reservar(self, huesped):
        if not self.reservada:
            self.reservada = True
            self.huesped = huesped
            print(f"Habitación {self.numero} ha sido reservada por {huesped.nombre}.")
        else:
            print(f"Habitación {self.numero} ya está reservada.")

    def cancelar_reserva(self):
        if self.reservada:
            print(f"Reserva cancelada para la habitación {self.numero}, que estaba ocupada por {self.huesped.nombre}.")
            self.reservada = False
            self.huesped = None
        else:
            print(f"La habitación {self.numero} no tiene reservas.")

    def estado(self):
        if self.reservada:
            print(f"Habitación {self.numero} (tipo {self.tipo}) está reservada por {self.huesped.nombre}.")
        else:
            print(f"Habitación {self.numero} (tipo {self.tipo}) está disponible.")

# Clase Hotel
class Hotel:
    def __init__(self):
        self.habitaciones = []

    def agregar_habitacion(self, numero, tipo):
        habitacion = Habitaciones(numero, tipo)
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        for habitacion in self.habitaciones:
            habitacion.estado()

    def reservar_habitacion(self, numero, huesped):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                habitacion.reservar(huesped)
                return
        print(f"No se encontró la habitación con el número {numero}.")

    def cancelar_reserva(self, numero):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                habitacion.cancelar_reserva()
                return
        print(f"No se encontró la habitación con el número {numero}.")

# Clase Huesped
class Huesped:
    def __init__(self, nombre):
        self.nombre = nombre

    def reservar_habitacion(self, hotel, numero):
        for habitacion in hotel.habitaciones:
            if habitacion.numero == numero:
                habitacion.reservar(self)
                return
        print(f"No se encontró la habitación con el número {numero}.")

# Ejemplo de uso del sistema
hotel = Hotel()

# Agregar habitaciones al hotel
hotel.agregar_habitacion(107, "individual")
hotel.agregar_habitacion(112, "doble")
hotel.agregar_habitacion(120, "individual")

# Mostrar el estado de las habitaciones
hotel.mostrar_habitaciones()

# Crear huéspedes
huésped1 = Huesped("Camila López")
huésped2 = Huesped("Ana Amezquita")
huésped3 = Huesped("Julio Gómez")

# Reservar una habitación
huésped1.reservar_habitacion(hotel, 107)
huésped2.reservar_habitacion(hotel, 112)

# Intentar reservar una habitación ya ocupada
huésped3.reservar_habitacion(hotel, 107)

# Mostrar el estado de las habitaciones después de las reservas
hotel.mostrar_habitaciones()

# Cancelar una reserva
hotel.cancelar_reserva(107)

# Mostrar el estado de las habitaciones después de cancelar la reserva
hotel.mostrar_habitaciones()
