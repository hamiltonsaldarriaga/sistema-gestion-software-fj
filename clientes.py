
# Importamos la clase abstracta Entidad.
from entidades import Entidad

# Importamos la excepcion personalizada para clientes.
from excepciones import ErrorCliente

# Importamos re para validar el formato del correo electronico.
import re


class Cliente(Entidad):
    """
    Representa un cliente de la empresa Software FJ.

    Hereda de Entidad y aplica encapsulacion para proteger
    los datos personales del cliente.
    """

    def __init__(self, identificador, nombre, correo, telefono):
        """
        Inicializa los datos del cliente y verifica su validez.
        """

        # Inicializamos el identificador heredado de Entidad.
        super().__init__(identificador)

        # Guardamos los datos como atributos privados.
        self._nombre = nombre
        self._correo = correo
        self._telefono = telefono

        # Comprobamos que todos los datos sean correctos.
        self.validar()

    @property
    def nombre(self):
        """Permite consultar el nombre del cliente."""
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        """Permite modificar el nombre previa validacion."""
        self._validar_nombre(nuevo_nombre)
        self._nombre = nuevo_nombre.strip()

    @property
    def correo(self):
        """Permite consultar el correo electronico."""
        return self._correo

    @correo.setter
    def correo(self, nuevo_correo):
        """Permite modificar el correo previa validacion."""
        self._validar_correo(nuevo_correo)
        self._correo = nuevo_correo.strip().lower()

    @property
    def telefono(self):
        """Permite consultar el telefono del cliente."""
        return self._telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        """Permite modificar el telefono previa validacion."""
        self._validar_telefono(nuevo_telefono)
        self._telefono = str(nuevo_telefono).strip()

    @staticmethod
    def _validar_nombre(nombre):
        """
        Comprueba que el nombre no este vacio y contenga
        caracteres validos.
        """
        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorCliente("El nombre del cliente es obligatorio.")

        # Se permiten letras, espacios, guiones y apostrofes.
        nombre_limpio = nombre.strip()

        if not all(
            caracter.isalpha() or caracter in " -'"
            for caracter in nombre_limpio
        ):
            raise ErrorCliente("El nombre contiene caracteres no validos.")

    @staticmethod
    def _validar_correo(correo):
        """Comprueba que el correo tenga un formato valido."""

        if not isinstance(correo, str) or not correo.strip():
            raise ErrorCliente("El correo electronico es obligatorio.")

        patron = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"

        if not re.match(patron, correo.strip()):
            raise ErrorCliente("El formato del correo electronico no es valido.")

    @staticmethod
    def _validar_telefono(telefono):
        """
        Comprueba que el telefono contenga una cantidad
        adecuada de digitos.
        """

        if telefono is None:
            raise ErrorCliente("El telefono es obligatorio.")

        # Se eliminan espacios, guiones y el signo + para contar digitos.
        telefono_limpio = str(telefono).strip()
        digitos = "".join(
            caracter for caracter in telefono_limpio
            if caracter.isdigit()
        )

        if not digitos.isdigit() or not 7 <= len(digitos) <= 15:
            raise ErrorCliente("El telefono debe tener entre 7 y 15 digitos.")

    def validar(self):
        """
        Implementa el metodo abstracto heredado de Entidad.
        Verifica que todos los datos del cliente sean correctos.
        """

        self._validar_nombre(self._nombre)
        self._validar_correo(self._correo)
        self._validar_telefono(self._telefono)

        return True

    def mostrar_informacion(self):
        """
        Implementa el metodo abstracto heredado de Entidad.
        Devuelve la informacion general del cliente.
        """

        return (
            f"Identificacion: {self.identificador}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Telefono: {self.telefono}"
        )

    def __str__(self):
        """Permite representar el cliente como texto."""
        return f"{self.nombre} - {self.identificador}"
