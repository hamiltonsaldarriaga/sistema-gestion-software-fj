
# Excepciones personalizadas del sistema Software FJ.
# Todas heredan de una clase base general del sistema.


# Clase base para los errores propios del sistema.
class ErrorSistema(Exception):
    """Clase base para las excepciones de Software FJ."""
    pass


# Error relacionado con los datos de los clientes.
class ErrorCliente(ErrorSistema):
    """Se genera cuando los datos de un cliente no son validos."""
    pass


# Error relacionado con los servicios ofrecidos.
class ErrorServicio(ErrorSistema):
    """Se genera cuando un servicio presenta alguna inconsistencia."""
    pass


# Error relacionado con las reservas.
class ErrorReserva(ErrorSistema):
    """Se genera cuando una reserva no puede realizarse."""
    pass


# Error para operaciones que no estan permitidas.
class ErrorOperacion(ErrorSistema):
    """Se genera cuando se intenta realizar una operacion no permitida."""
    pass

