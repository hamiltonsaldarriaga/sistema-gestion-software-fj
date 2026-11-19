
# Excepciones personalizadas del sistema Software FJ, Este archivo permite controlar errores específicos, que pueden presentarse durante la ejecución.

# Error relacionado con los datos de los clientes.
class ErrorCliente(Exception):
    """Se genera cuando los datos de un cliente no son válidos."""
    pass


# Error relacionado con los servicios ofrecidos.
class ErrorServicio(Exception):
    """Se genera cuando un servicio presenta alguna inconsistencia."""
    pass


# Error relacionado con las reservas.
class ErrorReserva(Exception):
    """Se genera cuando una reserva no puede realizarse."""
    pass


# Error para operaciones que no están permitidas.
class ErrorOperacion(Exception):
    """Se genera cuando se intenta realizar una operación no permitida."""
    pass
  
