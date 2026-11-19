
# Importamos las herramientas para manejar registros.
import logging
import os

# Importamos las clases del proyecto.
from clientes import Cliente
from servicios import Servicio
from reservas import Reserva

# Importamos las excepciones personalizadas.
from excepciones import (
    ErrorCliente,
    ErrorServicio,
    ErrorReserva,
    ErrorOperacion
)


class SistemaGestion:
    """
    Clase principal encargada de administrar las operaciones
    del sistema Software FJ.

    La informacion se almacena en listas internas,
    sin utilizar bases de datos.
    """

    def __init__(self):
        # Creamos las listas donde se almacenaran los objetos.
        self._clientes = []
        self._servicios = []
        self._reservas = []

        # Configuramos el sistema de registros de eventos.
        self._configurar_logs()

    def _configurar_logs(self):
        """
        Configura el archivo donde se guardan los errores
        y los eventos importantes del sistema.
        """

        # Creamos la carpeta logs si todavia no existe.
        os.makedirs("logs", exist_ok=True)

        # Configuramos el registro de eventos.
        self.logger = logging.getLogger("SoftwareFJ")

        # Evitamos agregar varios manejadores al mismo registro.
        if not self.logger.handlers:
            self.logger.setLevel(logging.INFO)

            manejador = logging.FileHandler(
                "logs/sistema.log",
                encoding="utf-8"
            )

            formato = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )

            manejador.setFormatter(formato)
            self.logger.addHandler(manejador)

    def registrar_cliente(self, cliente):
        """
        Registra un cliente despues de comprobar sus datos
        y verificar que no exista otro con el mismo identificador.
        """

        try:
            if not isinstance(cliente, Cliente):
                raise ErrorCliente("El objeto recibido no es un cliente valido.")

            cliente.validar()

            # Comprobamos que no exista el identificador.
            if any(
                c.identificador == cliente.identificador
                for c in self._clientes
            ):
                raise ErrorCliente("Ya existe un cliente con ese identificador.")

            self._clientes.append(cliente)

            self.logger.info(
                "Cliente registrado: %s", cliente.identificador
            )

            return "Cliente registrado correctamente."

        except Exception as error:
            self.logger.exception("Error al registrar cliente.")
            raise

    def registrar_servicio(self, servicio):
        """
        Registra un servicio y comprueba que su identificador
        no se encuentre repetido.
        """

        try:
            if not isinstance(servicio, Servicio):
                raise ErrorServicio("El objeto recibido no es un servicio valido.")

            servicio.validar()

            if any(
                s.identificador == servicio.identificador
                for s in self._servicios
            ):
                raise ErrorServicio("Ya existe un servicio con ese identificador.")

            self._servicios.append(servicio)

            self.logger.info(
                "Servicio registrado: %s", servicio.identificador
            )

            return "Servicio registrado correctamente."

        except Exception:
            self.logger.exception("Error al registrar servicio.")
            raise

    def buscar_cliente(self, identificador):
        """Busca un cliente por su identificador."""

        for cliente in self._clientes:
            if cliente.identificador == str(identificador):
                return cliente

        raise ErrorCliente("No se encontro el cliente solicitado.")

    def buscar_servicio(self, identificador):
        """Busca un servicio por su identificador."""

        for servicio in self._servicios:
            if servicio.identificador == str(identificador):
                return servicio

        raise ErrorServicio("No se encontro el servicio solicitado.")

    def crear_reserva(self, identificador, id_cliente,
                      id_servicio, duracion):
        """
        Crea una reserva utilizando un cliente y un servicio
        previamente registrados.
        """

        try:
            # Comprobamos que el identificador no este repetido.
            if any(
                r.identificador == str(identificador)
                for r in self._reservas
            ):
                raise ErrorReserva("Ya existe una reserva con ese identificador.")

            # Recuperamos los objetos registrados.
            cliente = self.buscar_cliente(id_cliente)
            servicio = self.buscar_servicio(id_servicio)

            # Creamos el objeto Reserva.
            reserva = Reserva(
                identificador,
                cliente,
                servicio,
                duracion
            )

            # Guardamos la reserva en la lista interna.
            self._reservas.append(reserva)

            self.logger.info(
                "Reserva creada: %s", reserva.identificador
            )

            return reserva

        except Exception:
            self.logger.exception("Error al crear reserva.")
            raise

    def buscar_reserva(self, identificador):
        """Busca una reserva por su identificador."""

        for reserva in self._reservas:
            if reserva.identificador == str(identificador):
                return reserva

        raise ErrorReserva("No se encontro la reserva solicitada.")

    def confirmar_reserva(self, identificador):
        """Confirma una reserva pendiente."""

        try:
            reserva = self.buscar_reserva(identificador)
            resultado = reserva.confirmar()

            self.logger.info(
                "Reserva confirmada: %s", identificador
            )

            return resultado

        except Exception:
            self.logger.exception("Error al confirmar reserva.")
            raise

    def cancelar_reserva(self, identificador):
        """Cancela una reserva pendiente o confirmada."""

        try:
            reserva = self.buscar_reserva(identificador)
            resultado = reserva.cancelar()

            self.logger.info(
                "Reserva cancelada: %s", identificador
            )

            return resultado

        except Exception:
            self.logger.exception("Error al cancelar reserva.")
            raise

    def procesar_reserva(self, identificador,
                         descuento=0, impuesto=0):
        """Procesa una reserva y calcula su costo final."""

        try:
            reserva = self.buscar_reserva(identificador)

            costo = reserva.procesar(
                descuento,
                impuesto
            )

            self.logger.info(
                "Reserva procesada: %s. Costo: %.2f",
                identificador,
                costo
            )

            return costo

        except Exception:
            self.logger.exception("Error al procesar reserva.")
            raise

    def listar_clientes(self):
        """Devuelve la lista de clientes registrados."""

        return list(self._clientes)

    def listar_servicios(self):
        """Devuelve la lista de servicios registrados."""

        return list(self._servicios)

    def listar_reservas(self):
        """Devuelve la lista de reservas registradas."""

        return list(self._reservas)

    def resumen_general(self):
        """
        Presenta un resumen de los registros del sistema.
        """

        return (
            "RESUMEN GENERAL SOFTWARE FJ\n"
            "---------------------------\n"
            f"Clientes registrados: {len(self._clientes)}\n"
            f"Servicios registrados: {len(self._servicios)}\n"
            f"Reservas registradas: {len(self._reservas)}"
        )

    def cerrar(self):
        """
        Registra el cierre de la sesion del sistema.
        """

        self.logger.info("Sesion del sistema finalizada.")
        return "Sistema finalizado correctamente."
