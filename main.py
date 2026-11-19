
from sistema import SistemaGestion
from clientes import Cliente
from servicios import ServicioSala, ServicioEquipo, ServicioAsesoria
from reservas import Reserva


def mostrar_menu():
    """Muestra las opciones principales del sistema."""
    print("\n========================================")
    print("       SISTEMA DE GESTION SOFTWARE FJ")
    print("========================================")
    print("1. Registrar cliente")
    print("2. Registrar servicio")
    print("3. Crear reserva")
    print("4. Confirmar reserva")
    print("5. Cancelar reserva")
    print("6. Procesar reserva")
    print("7. Listar clientes")
    print("8. Listar servicios")
    print("9. Listar reservas")
    print("10. Mostrar resumen general")
    print("0. Salir")
    print("========================================")


def ejecutar_sistema():
    """Controla el funcionamiento general del programa."""

    sistema = SistemaGestion()

    try:
        while True:
            mostrar_menu()

            try:
                opcion = input("Seleccione una opcion: ").strip()

                if opcion == "1":
                    identificador = input("Identificacion: ")
                    nombre = input("Nombre: ")
                    correo = input("Correo: ")
                    telefono = input("Telefono: ")

                    cliente = Cliente(
                        identificador, nombre, correo, telefono
                    )

                    sistema.registrar_cliente(cliente)
                    print("Cliente registrado correctamente.")

                elif opcion == "2":
                    print("\nTipos de servicio:")
                    print("1. Sala")
                    print("2. Equipo")
                    print("3. Asesoria")

                    tipo = input("Seleccione el tipo: ").strip()
                    identificador = input("Codigo del servicio: ")
                    nombre = input("Nombre: ")
                    descripcion = input("Descripcion: ")
                    tarifa = float(input("Tarifa base: "))

                    if tipo == "1":
                        capacidad = int(input("Capacidad de la sala: "))
                        servicio = ServicioSala(
                            identificador, nombre, descripcion,
                            tarifa, capacidad
                        )

                    elif tipo == "2":
                        equipo = input("Tipo de equipo: ")
                        servicio = ServicioEquipo(
                            identificador, nombre, descripcion,
                            tarifa, equipo
                        )

                    elif tipo == "3":
                        especialidad = input("Especialidad: ")
                        servicio = ServicioAsesoria(
                            identificador, nombre, descripcion,
                            tarifa, especialidad
                        )

                    else:
                        raise ValueError("Tipo de servicio no valido.")

                    sistema.registrar_servicio(servicio)
                    print("Servicio registrado correctamente.")

                elif opcion == "3":
                    identificador = input("Codigo de reserva: ")
                    id_cliente = input("Identificacion del cliente: ")
                    id_servicio = input("Codigo del servicio: ")
                    duracion = float(input("Duracion: "))

                    cliente = sistema.buscar_cliente(id_cliente)
                    servicio = sistema.buscar_servicio(id_servicio)

                    reserva = Reserva(
                        identificador, cliente, servicio, duracion
                    )

                    sistema.crear_reserva(reserva)
                    print("Reserva creada correctamente.")

                elif opcion == "4":
                    identificador = input("Codigo de reserva: ")
                    sistema.confirmar_reserva(identificador)
                    print("Reserva confirmada.")

                elif opcion == "5":
                    identificador = input("Codigo de reserva: ")
                    sistema.cancelar_reserva(identificador)
                    print("Reserva cancelada.")

                elif opcion == "6":
                    identificador = input("Codigo de reserva: ")
                    descuento = float(input("Descuento (%): "))
                    impuesto = float(input("Impuesto (%): "))

                    total = sistema.procesar_reserva(
                        identificador, descuento, impuesto
                    )

                    print(f"Reserva procesada. Total: ${total:,.2f}")

                elif opcion == "7":
                    for cliente in sistema.listar_clientes():
                        print(cliente.mostrar_informacion())

                elif opcion == "8":
                    for servicio in sistema.listar_servicios():
                        print(servicio.describir())

                elif opcion == "9":
                    for reserva in sistema.listar_reservas():
                        print(reserva.mostrar_informacion())

                elif opcion == "10":
                    print(sistema.resumen_general())

                elif opcion == "0":
                    print("Cerrando el sistema...")
                    break

                else:
                    print("Opcion no valida. Intente nuevamente.")

            except (ValueError, TypeError) as error:
                print(f"Error en los datos ingresados: {error}")

            except Exception as error:
                print(f"No fue posible completar la operacion: {error}")

            else:
                # Se ejecuta cuando la operacion termina sin excepciones.
                pass

    except KeyboardInterrupt:
        print("\nEjecucion interrumpida por el usuario.")

    finally:
        # Se ejecuta siempre, incluso si ocurre un error.
        sistema.cerrar()
        print("Sistema finalizado.")


if __name__ == "__main__":
    ejecutar_sistema()
