
from sistema import SistemaGestion
from clientes import Cliente
from servicios import ServicioSala, ServicioEquipo, ServicioAsesoria
from reservas import Reserva


def ejecutar_pruebas():
    """Ejecuta pruebas de funcionamiento y manejo de errores."""

    sistema = SistemaGestion()
    operaciones = 0

    print("\n========================================")
    print("       PRUEBAS DEL SISTEMA SOFTWARE FJ")
    print("========================================")

    try:
        # PRUEBA 1: Registro de un cliente valido.
        try:
            cliente1 = Cliente(
                "1001",
                "Carlos Ramirez",
                "carlos@gmail.com",
                "3001234567"
            )
            sistema.registrar_cliente(cliente1)
            operaciones += 1
            print("PRUEBA 1: Cliente registrado correctamente.")

        except Exception as error:
            print(f"PRUEBA 1 FALLIDA: {error}")

        # PRUEBA 2: Registro de un segundo cliente.
        try:
            cliente2 = Cliente(
                "1002",
                "Maria Torres",
                "maria@gmail.com",
                "3101234567"
            )
            sistema.registrar_cliente(cliente2)
            operaciones += 1
            print("PRUEBA 2: Segundo cliente registrado.")

        except Exception as error:
            print(f"PRUEBA 2 FALLIDA: {error}")

        # PRUEBA 3: Intento de registrar un cliente invalido.
        try:
            cliente_invalido = Cliente(
                "1003",
                "Pedro Lopez",
                "correo_incorrecto",
                "3001234567"
            )
            sistema.registrar_cliente(cliente_invalido)
            print("PRUEBA 3: No se detecto el correo incorrecto.")

        except Exception as error:
            operaciones += 1
            print(f"PRUEBA 3: Error controlado correctamente: {error}")

        # PRUEBA 4: Creacion de un servicio de sala.
        try:
            sala = ServicioSala(
                "S001",
                "Sala de reuniones",
                "Sala para reuniones empresariales",
                80000,
                20
            )
            sistema.registrar_servicio(sala)
            operaciones += 1
            print("PRUEBA 4: Servicio de sala creado.")

        except Exception as error:
            print(f"PRUEBA 4 FALLIDA: {error}")

        # PRUEBA 5: Creacion de un servicio de equipos.
        try:
            equipo = ServicioEquipo(
                "S002",
                "Computador portatil",
                "Alquiler de computador",
                50000,
                "Portatil"
            )
            sistema.registrar_servicio(equipo)
            operaciones += 1
            print("PRUEBA 5: Servicio de equipo creado.")

        except Exception as error:
            print(f"PRUEBA 5 FALLIDA: {error}")

        # PRUEBA 6: Creacion de un servicio de asesoria.
        try:
            asesoria = ServicioAsesoria(
                "S003",
                "Asesoria tecnica",
                "Asesoria especializada",
                100000,
                "Sistemas"
            )
            sistema.registrar_servicio(asesoria)
            operaciones += 1
            print("PRUEBA 6: Servicio de asesoria creado.")

        except Exception as error:
            print(f"PRUEBA 6 FALLIDA: {error}")

        # PRUEBA 7: Intento de crear un servicio con tarifa invalida.
        try:
            servicio_invalido = ServicioSala(
                "S004",
                "Sala invalida",
                "Servicio con tarifa incorrecta",
                -50000,
                10
            )
            sistema.registrar_servicio(servicio_invalido)
            print("PRUEBA 7: No se detecto la tarifa incorrecta.")

        except Exception as error:
            operaciones += 1
            print(f"PRUEBA 7: Error controlado correctamente: {error}")

        # PRUEBA 8: Creacion de una reserva valida.
        try:
            reserva1 = Reserva(
                "R001",
                sistema.buscar_cliente("1001"),
                sistema.buscar_servicio("S001"),
                2
            )
            sistema.crear_reserva(reserva1)
            operaciones += 1
            print("PRUEBA 8: Reserva creada correctamente.")

        except Exception as error:
            print(f"PRUEBA 8 FALLIDA: {error}")

        # PRUEBA 9: Confirmacion y procesamiento de reserva.
        try:
            sistema.confirmar_reserva("R001")
            total = sistema.procesar_reserva("R001", 10, 19)
            operaciones += 1
            print("PRUEBA 9: Reserva confirmada y procesada.")
            print(f"Total calculado: ${total:,.2f}")

        except Exception as error:
            print(f"PRUEBA 9 FALLIDA: {error}")

        # PRUEBA 10: Creacion y cancelacion de otra reserva.
        try:
            reserva2 = Reserva(
                "R002",
                sistema.buscar_cliente("1002"),
                sistema.buscar_servicio("S002"),
                3
            )
            sistema.crear_reserva(reserva2)
            sistema.cancelar_reserva("R002")
            operaciones += 1
            print("PRUEBA 10: Reserva creada y cancelada.")

        except Exception as error:
            print(f"PRUEBA 10 FALLIDA: {error}")

        # PRUEBA ADICIONAL: Intento de reserva con cliente inexistente.
        try:
            cliente_inexistente = sistema.buscar_cliente("9999")
            print(cliente_inexistente)

        except Exception as error:
            operaciones += 1
            print(
                "PRUEBA ADICIONAL: Error por cliente inexistente "
                f"controlado: {error}"
            )

        # Mostrar resultados finales.
        print("\n========================================")
        print("          RESUMEN DE LAS PRUEBAS")
        print("========================================")
        print(f"Operaciones ejecutadas: {operaciones}")
        print("\nClientes registrados:")
        for cliente in sistema.listar_clientes():
            print(cliente.mostrar_informacion())

        print("\nServicios registrados:")
        for servicio in sistema.listar_servicios():
            print(servicio.describir())

        print("\nReservas registradas:")
        for reserva in sistema.listar_reservas():
            print(reserva.mostrar_informacion())

    except Exception as error:
        print(f"Error general durante las pruebas: {error}")

    finally:
        sistema.cerrar()
        print("\nPruebas finalizadas.")


if __name__ == "__main__":
    ejecutar_pruebas()
