from app.errors import DatosUsuarioInvalidosError

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

def validar_update_usuario(data):
    if not isinstance(data, dict):
        raise DatosUsuarioInvalidosError()
    if "edad" not in data and "activo" not in data:
        raise DatosUsuarioInvalidosError()
    if "edad"in data and not isinstance(data["edad"], int):
        raise DatosUsuarioInvalidosError()
    if "activo" in data and not isinstance(data["activo"], bool):
        raise DatosUsuarioInvalidosError()
    return None