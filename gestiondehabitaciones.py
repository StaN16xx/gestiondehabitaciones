habitaciones = []
reservas = []

def habitaciones_disponibles():
    print("habitaciones disponibles:")
    for habitacion in habitaciones:
        print(f"numero: {habitacion['numero']}, tipo: {habitacion['tipo']}, capacidad: {habitacion['capacidad']}, estado: {habitacion['estado']}")

def agregar_habitacion(numero, tipo, capacidad):
    habitaciones.append({
        'numero': numero,
        'tipo': tipo,
        'capacidad': capacidad,
        'estado': 'disponible'
    })

def mostrar_reservas():
    print("reservas realizadas:")
    for reserva in reservas:
        print(f"numero de habitación: {reserva['numero']}, nombre del cliente: {reserva['nombre_cliente']}, dias de reserva: {reserva['dias_reserva']}")

def reservas_habitacion(numero, nombre_cliente, dias_reserva, ocupantes):
    for habitacion in habitaciones:
        if habitacion['numero'] == numero:
            if habitacion['estado'] == 'disponible':
                if ocupantes <= habitacion['capacidad']:
                    reservas.append({
                        'numero': numero,
                        'nombre_cliente': nombre_cliente,
                        'dias_reserva': dias_reserva
                    })
                    habitacion['estado'] = 'reservada'
                    print("reserva realizada con éxito")
                else:
                    print("la cantidad de personas excede la capacidad de la habitación.")
            else:
                print("esta habitacion no está disponible.")
            return
    print("esa habitacion no existe")

def menu():
    while True:
        print(" ----BIENVENIDO A NUESTRO HOTEL-----")
        print(" | (1) agregar habitación          |")
        print(" | (2) habitaciones disponibles    |")
        print(" | (3) reservar habitación         |")
        print(" | (4) mostrar reservas            |")
        print(" | (5) salir                       |")
        print(" ----------------------------------- ")
        opcion = input("seleccione una opción: ")

        if opcion == '1':
            numero = input("ingrese el número de habitación: ")
            tipo = input("ingrese el tipo de habitación: individual/doble/suite ")
            capacidad = int(input("ingrese la capacidad máxima de ocupantes: "))
            agregar_habitacion(numero, tipo, capacidad)
        elif opcion == '2':
            habitaciones_disponibles()
        elif opcion == '3':
            numero = input("ingrese el número de habitación a reservar: ")
            nombre_cliente = input("ingrese su nombre: ")
            dias_reserva = int(input("ingrese los días reserva: "))
            ocupantes = int(input("ingrese la cantidad de personas: "))
            reservas_habitacion(numero, nombre_cliente, dias_reserva, ocupantes)
        elif opcion == '4':
            mostrar_reservas()
        elif opcion == '5':
            print("gracias por preferir nuestro servicio")
            break
        else:
            print("opción no válida elija otra")

menu()
