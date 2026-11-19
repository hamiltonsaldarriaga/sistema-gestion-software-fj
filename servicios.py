
# Importamos la clase abstracta Entidad.
from entidades import Entidad

# Importamos la excepcion personalizada para servicios.
from excepciones import ErrorServicio

# Importamos herramientas para crear clases abstractas.
from abc import abstractmethod


class Servicio(Entidad):
    """
    Clase abstracta que representa los servicios ofrecidos
    por la empresa Software FJ.
    """

    def __init__(self, identificador, nombre, descripcion, tarifa_base):
        # Inicializamos el identificador heredado.
        super().__init__(identificador)

        # Almacenamos los datos generales del servicio.
        self._nombre = nombre
        self._descripcion = descripcion
        self._tarifa_base = tarifa_base

    @property
    def nombre(self):
        return self._nombre

    @property
    def tarifa_base(self):
        return self._tarifa_base

    def validar(self):
        """
        Comprueba los datos generales del servicio.
        """

        if not isinstance(self._nombre, str) or not self._nombre.strip():
            raise ErrorServicio("El nombre del servicio es obligatorio.")

        if not isinstance(self._descripcion, str) or not self._descripcion.strip():
            raise ErrorServicio("La descripcion del servicio es obligatoria.")

        if isinstance(self._tarifa_base, bool) or not isinstance(
            self._tarifa_base, (int, float)
        ):
            raise ErrorServicio("La tarifa debe ser un valor numerico.")

        if self._tarifa_base <= 0:
            raise ErrorServicio("La tarifa debe ser mayor que cero.")

        # Cada servicio comprueba sus propios parametros.
        self.validar_parametros(1)

        return True

    def mostrar_informacion(self):
        """Muestra la informacion general del servicio."""

        return (
            f"Codigo: {self.identificador}\n"
            f"Servicio: {self.nombre}\n"
            f"Descripcion: {self._descripcion}\n"
            f"Tarifa base: ${self.tarifa_base:,.2f}"
        )

    def _calcular_total(self, costo_base, descuento=0, impuesto=0):
        """
        Calcula el valor final aplicando descuento e impuesto.
        Los parametros opcionales permiten diferentes formas
        de calcular el costo.
        """

        if isinstance(descuento, bool) or not isinstance(descuento, (int, float)):
            raise ErrorServicio("El descuento debe ser numerico.")

        if isinstance(impuesto, bool) or not isinstance(impuesto, (int, float)):
            raise ErrorServicio("El impuesto debe ser numerico.")

        if not 0 <= descuento <= 100:
            raise ErrorServicio("El descuento debe estar entre 0 y 100.")

        if not 0 <= impuesto <= 100:
            raise ErrorServicio("El impuesto debe estar entre 0 y 100.")

        valor_descuento = costo_base * (descuento / 100)
        subtotal = costo_base - valor_descuento
        valor_impuesto = subtotal * (impuesto / 100)

        return round(subtotal + valor_impuesto, 2)

    @abstractmethod
    def calcular_costo(self, duracion=1, descuento=0, impuesto=0):
        """Cada servicio implementa su propio calculo de costos."""
        pass

    @abstractmethod
    def describir(self):
        """Cada servicio define su propia descripcion."""
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        """Cada servicio valida sus parametros especificos."""
        pass


# ============================================================
# SERVICIO 1: RESERVA DE SALAS
# ============================================================

class ServicioSala(Servicio):
    """
    Representa el servicio de reserva de salas por horas.
    """

    def __init__(self, identificador, nombre, descripcion,
                 tarifa_base, capacidad_maxima):

        super().__init__(identificador, nombre, descripcion, tarifa_base)

        self._capacidad_maxima = capacidad_maxima
        self.validar()

    def validar_parametros(self, duracion):
        """Valida la duracion y capacidad de la sala."""

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ErrorServicio("La duracion debe ser numerica.")

        if duracion <= 0:
            raise ErrorServicio("La duracion de la reserva debe ser positiva.")

        if isinstance(self._capacidad_maxima, bool) or not isinstance(
            self._capacidad_maxima, int
        ) or self._capacidad_maxima <= 0:
            raise ErrorServicio("La capacidad de la sala debe ser un entero positivo.")

        return True

    def calcular_costo(self, duracion=1, descuento=0, impuesto=0):
        """Calcula el costo de reservar una sala por horas."""

        self.validar_parametros(duracion)

        costo_base = self.tarifa_base * duracion

        return self._calcular_total(costo_base, descuento, impuesto)

    def describir(self):
        """Describe las caracteristicas del servicio de salas."""

        return (
            f"{self._nombre}: reserva de sala por horas. "
            f"Capacidad maxima: {self._capacidad_maxima} personas."
        )


# ============================================================
# SERVICIO 2: ALQUILER DE EQUIPOS
# ============================================================

class ServicioEquipo(Servicio):
    """
    Representa el alquiler de equipos por dias.
    """

    def __init__(self, identificador, nombre, descripcion,
                 tarifa_base, tipo_equipo):

        super().__init__(identificador, nombre, descripcion, tarifa_base)

        self._tipo_equipo = tipo_equipo
        self.validar()

    def validar_parametros(self, duracion):
        """Valida los dias de alquiler y el tipo de equipo."""

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ErrorServicio("La duracion del alquiler debe ser numerica.")

        if duracion <= 0:
            raise ErrorServicio("Los dias de alquiler deben ser positivos.")

        if not isinstance(self._tipo_equipo, str) or not self._tipo_equipo.strip():
            raise ErrorServicio("Debe especificarse el tipo de equipo.")

        return True

    def calcular_costo(self, duracion=1, descuento=0, impuesto=0):
        """Calcula el costo del alquiler de equipos por dias."""

        self.validar_parametros(duracion)

        costo_base = self.tarifa_base * duracion

        return self._calcular_total(costo_base, descuento, impuesto)

    def describir(self):
        """Describe las caracteristicas del alquiler de equipos."""

        return (
            f"{self._nombre}: alquiler de equipos tipo "
            f"{self._tipo_equipo}, cobrado por dias."
        )


# ============================================================
# SERVICIO 3: ASESORIAS ESPECIALIZADAS
# ============================================================

class ServicioAsesoria(Servicio):
    """
    Representa las asesorias especializadas por horas.
    """

    def __init__(self, identificador, nombre, descripcion,
                 tarifa_base, especialidad):

        super().__init__(identificador, nombre, descripcion, tarifa_base)

        self._especialidad = especialidad
        self.validar()

    def validar_parametros(self, duracion):
        """Valida la duracion y especialidad de la asesoria."""

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ErrorServicio("La duracion de la asesoria debe ser numerica.")

        if duracion <= 0:
            raise ErrorServicio("Las horas de asesoria deben ser positivas.")

        if not isinstance(self._especialidad, str) or not self._especialidad.strip():
            raise ErrorServicio("Debe especificarse una especialidad.")

        return True

    def calcular_costo(self, duracion=1, descuento=0, impuesto=0):
        """Calcula el costo de una asesoria segun las horas contratadas."""

        self.validar_parametros(duracion)

        costo_base = self.tarifa_base * duracion

        return self._calcular_total(costo_base, descuento, impuesto)

    def describir(self):
        """Describe las caracteristicas de la asesoria."""

        return (
            f"{self._nombre}: asesoria especializada en "
            f"{self._especialidad}, cobrada por horas."
        )
