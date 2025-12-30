# Parte 1 - Reutiliza estas piezas (puedes copiarlas del Ejercicio 30)
# 1 Excepciones:
#   - DatosUsuarioInvalidosError
#   - UsuarioDuplicadoError
# 2 Clases/funciones:
#   - Usuario con to_dict
#   - usuario_desde_dict
#   - UsaurioRepository con agregar
#   - UsuarioService con crear_usuario

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

class UsuarioRepository:
    def __init__(self):
        self._usuarios = []
        
    def agregar(self, usuario):
        for usuario_buscar in self._usuarios:
            if usuario.nombre == usuario_buscar.nombre:
                raise UsuarioDuplicadoError()
        self._usuarios.append(usuario)

class UsuarioService:
    def __init__(self, repo):
        self.repo = repo
    
    def crear_usuario(self, data):
        usuario = usuario_desde_dict(data)
        self.repo.agregar(usuario)
        return usuario.to_dict()
    
# Parte 2 - Capa endpoint simulada
# 3 Crea una función llamada crear__usuario_endpoint(service, data) que:
# - Reciba service (UsuarioService)
# - Reciba data (dict)
# 4 Dentro de esta función:
# - Debe llamar a service.crear_usuario(data)
# - Debe devolver un diccionario de respuesta con esta estructura:
# Si todo va bien:
# {"status_code":201, "data":<dict_del_usuario>}
# Si falla por datos inválidos
# {"status_code": 400, "error" : "Datos de usuario inválidos"}
# Si falla por duplicado
# {"status_code": 409, "error" : "Usuario duplicado"}

def crear_usuario_endpoint(service, data):
    try:
        resultado = service.crear_usuario(data)
        return {"status_code": 201, "data": resultado}
    except DatosUsuarioInvalidosError:
        return {"status_code": 400, "error":"Datos de usuario inválidos"}
    except UsuarioDuplicadoError:
        return {"status_code": 409, "error": "Usuario duplicado"}
    
# Parte 3 - Pruebas
# 5 Crea:
#   - data_ok válido
#   - data_dup con mismo nombre
#   - data_bad inválido(por ejemplo falta una clave)
# 6 Inicializa repo + service
# 7 Llama a crear_usuario_endpoint(service, ...) con cada uno en este orden:
#   - data_ok -> Imprimir respuesta completa
#   - data_dup -> Imprimir respuesta completa
#   - data_bad -> Imprimir respuesta completa

data_ok = {"nombre": "Victor", "edad": 20, "activo": True}
data_dup = {"nombre": "Victor", "edad": 20, "activo" : True}
data_bad = {"nombre": "Juan", "eda": 20, "activo" : True}

usuario_respository = UsuarioRepository()
usuario_service = UsuarioService(usuario_respository)

resultado_ok = crear_usuario_endpoint(usuario_service, data_ok)
resultado_dup = crear_usuario_endpoint(usuario_service, data_dup)
resultado_bad = crear_usuario_endpoint(usuario_service, data_bad)

print(resultado_ok)
print(resultado_dup)
print(resultado_bad)