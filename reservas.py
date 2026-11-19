
# Importamos las clases necesarias para gestionar reservas.
from clientes import Cliente
from servicios import Servicio

# Importamos las excepciones personalizadas.
from excepciones import ErrorReserva


class Reserva:
    """
    Representa una reserva realizada por un cliente
    para utilizar uno de los servicios de Software FJ.
    """

    # Estados posibles de una reserva.
    PENDIENTE = "Pendiente"
    CONFIRMADA = "Confirmada"
    CANCELADA = "Cancelada"
    PROCESADA = "Procesada"

    def __init__(self, identificador, cliente, servicio, duracion):
        """
        Inicializa una reserva con su cliente, servicio
        y duracion correspondiente.
        """

        # Validamos el identificador.
        if identificador is None or str(identificador).strip() == "":
            raise ErrorReserva("La reserva necesita un identificador.")

        # Comprobamos que exista un cliente valido.
        if not isinstance(cliente, Cliente):
            raise ErrorReserva("Debe asignarse un cliente valido.")

        # Comprobamos que el servicio sea correcto.
        if not isinstance(servicio, Servicio):
            raise ErrorReserva("Debe asignarse un servicio valido.")

        # Comprobamos la duracion mediante el servicio.
        try:
            servicio.validar_parametros(duracion)
        except Exception as error:
            raise ErrorReserva(
                "No fue posible validar la duracion de la reserva."
            ) from error

        # Almacenamos los datos de la reserva.
        self._identificador = str(identificador).strip()
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion

        # Toda reserva comienza en estado pendiente.
        self._estado = self.PENDIENTE

        # El resultado economico se calcula al procesar.
        self._costo_final = None

    @property
    def identificador(self):
        return self._identificador

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def duracion(self):
        return self._duracion

    @property
    def estado(self):
        return self._estado

    @property
    def costo_final(self):
        return self._costo_final

    def confirmar(self):
        """
        Confirma una reserva que se encuentra pendiente.
        """

        if self._estado != self.PENDIENTE:
            raise ErrorReserva(
                "Solo se pueden confirmar reservas pendientes."
            )

        self._estado = self.CONFIRMADA

        return "La reserva ha sido confirmada correctamente."

    def cancelar(self):
        """
        Cancela una reserva pendiente o confirmada.
        """

        if self._estado not in (self.PENDIENTE, self.CONFIRMADA):
            raise ErrorReserva(
                "No se puede cancelar una reserva procesada o cancelada."
            )

        self._estado = self.CANCELADA

        return "La reserva ha sido cancelada correctamente."

    def procesar(self, descuento=0, impuesto=0):
        """
        Procesa una reserva confirmada y calcula su costo.

        Utiliza el metodo calcular_costo del servicio,
        aplicando el polimorfismo.
        """

        if self._estado != self.CONFIRMADA:
            raise ErrorReserva(
                "La reserva debe estar confirmada antes de procesarse."
            )

        try:
            # El servicio determina su propio calculo.
            costo = self._servicio.calcular_costo(
                self._duracion,
                descuento,
                impuesto
            )

            # Verificamos que el resultado sea numerico y positivo.
            if isinstance(costo, bool) or not isinstance(costo, (int, float)):
                raise ValueError("El costo calculado no es numerico.")

            if costo <= 0:
                raise ValueError("El costo calculado debe ser positivo.")

        except Exception as error:
            # Encadenamos el error original para conservar su causa.
            raise ErrorReserva(
                "Ocurrio un problema al procesar el costo de la reserva."
            ) from error

        # Guardamos el resultado y actualizamos el estado.
        self._costo_final = costo
        self._estado = self.PROCESADA

        return costo

    def mostrar_informacion(self):
        """
        Presenta la informacion completa de la reserva.
        """

        costo = (
            f"${self._costo_final:,.2f}"
            if self._costo_final is not None
            else "Pendiente de calcular"
        )

        return (
            f"Reserva: {self._identificador}\n"
            f"Cliente: {self._cliente.nombre}\n"
            f"Servicio: {self._servicio.nombre}\n"
            f"Duracion: {self._duracion}\n"
            f"Estado: {self._estado}\n"
            f"Costo final: {costo}"
        )

    def __str__(self):
        """Representacion sencilla de la reserva."""

        return (
            f"Reserva {self._identificador} - "
            f"{self._cliente.nombre} - {self._estado}"
        )
