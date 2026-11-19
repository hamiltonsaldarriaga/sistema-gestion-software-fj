

# ABC permite crear clases abstractas.
# abstractmethod permite definir metodos obligatorios.
from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta que representa una entidad general
    dentro del sistema Software FJ.

    Sirve como clase base para clientes y servicios.
    """

    def __init__(self, identificador):
        """
        Inicializa una entidad con un identificador unico.
        """

        # Se valida que el identificador no este vacio.
        if identificador is None or str(identificador).strip() == "":
            raise ValueError("El identificador no puede estar vacio.")

        # Se almacena el identificador como atributo protegido.
        self._identificador = str(identificador).strip()

    @property
    def identificador(self):
        """
        Permite consultar el identificador de la entidad.
        """
        return self._identificador

    @abstractmethod
    def validar(self):
        """
        Metodo abstracto que cada clase hija debe implementar.

        Su funcion es comprobar que los datos de la entidad
        sean correctos.
        """
        pass

    @abstractmethod
    def mostrar_informacion(self):
        """
        Metodo abstracto para mostrar los datos de la entidad.

        Cada clase derivada definira la informacion que necesita
        presentar.
        """
        pass
