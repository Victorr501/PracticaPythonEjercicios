class DatosUsuarioInvalidosError(Exception):
    """
    Se lanza cuando el dict de entrada no tiene datos válidos
    """
    pass

class UsuarioDuplicadoError(Exception):
    """
    Se lanza si ya existe un usuario con ese nombre
    """
    pass

class UsuarioNoEncontradoError(Exception):
    """
    Se lanza cuando no existe un usaurio con ese nombre
    """
    pass