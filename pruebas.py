
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
            sistema.crear_reserva("R001", "1001", "S001", 2)
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
            sistema.crear_reserva("R002", "1002", "S002", 3)
            sistema.cancelar_reserva("R002")
            operaciones += 1
            print("PRUEBA 10: Reserva creada y cancelada.")

        except Exception as error:
            print(f"PRUEBA 10 FALLIDA: {error}")

        # PRUEBA ADICIONAL: Intento de crear una reserva fallida.
        try:
            sistema.crear_reserva("R003", "9999", "S001", 2)
            print("No se detecto el cliente inexistente.")

        except Exception as error:
            operaciones += 1
            print(
                "PRUEBA ADICIONAL: Reserva fallida controlada: "
                f"{error}"
            )

        # PRUEBA 12: Intento de crear una reserva con duracion negativa.
        try:
            sistema.crear_reserva("R004", "1001", "S001", -2)
            print("PRUEBA 12: No se detecto la duracion negativa.")

        except Exception as error:
            operaciones += 1
            print(f"PRUEBA 12: Duracion negativa controlada: {error}")

        # PRUEBA 13: Intento de utilizar un servicio inexistente.
        try:
            sistema.crear_reserva("R005", "1001", "S999", 2)
            print("PRUEBA 13: No se detecto el servicio inexistente.")

        except Exception as error:
            operaciones += 1
            print(f"PRUEBA 13: Servicio inexistente controlado: {error}")

        # PRUEBA 14: Intento de crear una reserva sin identificador.
        try:
            sistema.crear_reserva("", "1001", "S001", 2)
            print("PRUEBA 14: No se detecto el identificador vacio.")

        except Exception as error:
            operaciones += 1
            print(f"PRUEBA 14: Identificador incorrecto controlado: {error}")

        # PRUEBA 15: Crear una reserva para probar estados incorrectos.
        try:
            sistema.crear_reserva("R006", "1001", "S001", 2)
            operaciones += 1
            print("PRUEBA 15: Reserva creada para pruebas de estado.")

        except Exception as error:
            print(f"PRUEBA 15 FALLIDA: {error}")

        # PRUEBA 16: Intentar procesar una reserva sin confirmarla.
        try:
            sistema.procesar_reserva("R006", 0, 19)
            print("PRUEBA 16: No se detecto la reserva sin confirmar.")

        except Exception as error:
            operaciones += 1
            print(f"PRUEBA 16: Procesamiento sin confirmar controlado: {error}")

        # PRUEBA 17: Confirmar la reserva R006.
        try:
            sistema.confirmar_reserva("R006")
            operaciones += 1
            print("PRUEBA 17: Reserva confirmada correctamente.")

        except Exception as error:
            print(f"PRUEBA 17 FALLIDA: {error}")

        # PRUEBA 18: Intentar aplicar un descuento superior al 100%.
        try:
            sistema.procesar_reserva("R006", 150, 19)
            print("PRUEBA 18: No se detecto el descuento fuera de rango.")

        except Exception as error:
            operaciones += 1
            print(f"PRUEBA 18: Descuento fuera de rango controlado: {error}")

        # PRUEBA 19: Procesar correctamente la reserva R006.
        try:
            total_r006 = sistema.procesar_reserva("R006", 10, 19)
            operaciones += 1
            print("PRUEBA 19: Reserva procesada correctamente.")
            print(f"Total calculado: ${total_r006:,.2f}")

        except Exception as error:
            print(f"PRUEBA 19 FALLIDA: {error}")

        # PRUEBA 20: Intentar procesar nuevamente una reserva procesada.
        try:
            sistema.procesar_reserva("R006", 0, 19)
            print("PRUEBA 20: No se detecto el procesamiento duplicado.")

        except Exception as error:
            operaciones += 1
            print(f"PRUEBA 20: Procesamiento duplicado controlado: {error}")

        # PRUEBA 21: Intentar cancelar una reserva procesada.
        try:
            sistema.cancelar_reserva("R006")
            print("PRUEBA 21: No se detecto la cancelacion de una reserva procesada.")

        except Exception as error:
            operaciones += 1
            print(f"PRUEBA 21: Cancelacion no permitida controlada: {error}")

        # PRUEBA 22: Intentar cancelar una reserva inexistente.
        try:
            sistema.cancelar_reserva("R999")
            print("PRUEBA 22: No se detecto la reserva inexistente.")

        except Exception as error:
            operaciones += 1
            print(f"PRUEBA 22: Cancelacion inexistente controlada: {error}")

        # PRUEBA 23: Intentar crear una reserva con parametros faltantes.
        try:
            sistema.crear_reserva("R007", "1001", "S001")
            print("PRUEBA 23: No se detectaron los parametros faltantes.")

        except Exception as error:
            operaciones += 1
            print(f"PRUEBA 23: Parametros faltantes controlados: {error}")

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
