# Parte 1 - Reutiliza / adapta código previo
# 1. Reutiliza del Ejercicio 32:
#   - Excepciones:
#       - DatosUsuarioInvalidosError
#       - UsuarioDuplicadoError
#       - UsuarioNoEncontradoError
#   - Usuario, usuario_desde_dict
#   - UsuarioRepository con:
#       - agregar
#       - obtener_usuario
#       - y añade eliminar_por_nombre
#   - UsuarioService con:
#       - crear_usuario
#       - obtener_usuario
#       - y añade eliminar_usuario(self, nombre)
#   - crear_usuario_endpoint (para preparar datos)

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
    
class Usuario:
    def __init__(self, nombre, edad, activo):
        self.nombre = nombre
        self.edad = edad
        self.activo = activo
        
    def to_dict(self):
        return {"nombre": self.nombre, "edad": self.edad, "activo": self.activo}
    
    
def usuario_desde_dict(data):
    if not isinstance(data, dict):
        raise DatosUsuarioInvalidosError()
    if not all (clave in data for clave in ("nombre", "edad", "activo") ):
        raise DatosUsuarioInvalidosError()
    if not isinstance(data["nombre"], str):
        raise DatosUsuarioInvalidosError()
    if not isinstance(data["edad"], int):
        raise DatosUsuarioInvalidosError()
    if not isinstance(data["activo"], bool):
        raise DatosUsuarioInvalidosError()
    return Usuario(data["nombre"], data["edad"], data["activo"])

def crear_usuario_endpoint(service, data):
    try:
        resultado = service.crear_usuario(data)
        return {"status_code": 201, "data": resultado}
    except DatosUsuarioInvalidosError:
        return {"status_code": 400, "error":"Datos de usuario inválidos"}
    except UsuarioDuplicadoError:
        return {"status_code": 409, "error": "Usuario duplicado"}
    
    
# Parte 2 - Repo: eliminar por nombre
# 2 Implementa UsuarioRepository.eliminar_por_nombre(self, nombre):
#   - Recoge self._usuarios con for
#   - Si encuentra el usuario con ese nombre:
#       - lo elimina
#       - hace return
#   - Si no lo encuentra:
#       -lanza UsuarioNoEncontradoError()
