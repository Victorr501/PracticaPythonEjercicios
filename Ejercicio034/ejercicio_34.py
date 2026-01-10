# Parte 1 - Reutiliza la anterior
# - Excepciones:
#   - DatosUsuarioInvalidosError
#   - UsuarioDuplicadoError
#   - UsuarioNoEncontradoError
# - Usuario con to_dict
# - usuario_desde_dict
# - UsuarioRepository con:
#   - agregar
#   - buscar_por_nombre
#   - eliminar_por_nombre
# - UsuarioService con:
#   - crear_usuario
#   - obtener_usuario
#   - eliminar_usuario
# - Endpoints:
#   - crar_usuario_enpoint
#   - obtener_usuario_endpoint
#   - eliminar_usuario_endpoint

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
    
def obtener_usuario_endpoint(service, nombre):
    try:
        usuario = service.obtener_usuario(nombre)
        return {"status_code": 200, "data": usuario}
    except UsuarioNoEncontradoError:
        return {"status_code": 404, "error": "Usuario no encontrado"}
    
def eliminar_usuario_endpoint(service, nombre):
    try:
        service.eliminar_usuario(nombre)
        return {"status_code": 204}
    except UsuarioNoEncontradoError:
        return {"status_code": 404, "error": "Usuario no encontrado"}
    
# Parte 2 - Validación de update
# 2 Crear una función fuera de clases llamada validar_update_usuario(data) que:
# - Reciba data y valide:
#   - data es dict(si no, raise DatosUsuarioInvalidosErro())
#   - Debe existir al menos una de estas claves "edad" o "activo"
#       - si no existe ninguna -> raise DatosUsuarioInvalidosErro()
#   - Si viene "edad":
#       - debe ser int
#   - Si viene "activo":
#       - debe ser bool
#   Si todo ok, la función no devuelve nada (None), solo valida

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

# Parte 3 - Repo: actualizar usuario
# 3 Añade en UsuarioRepository el método:
# actualizar_por_nombre(self, nombre, data) que:
# - Recorra la lista con for
# - Si encuentra el usuario por nombre:
#   - Si "edad" está en data, actualiza usuario.edad
#   - Si "activo" está en data, actualiza usuario.activo
#   - Devuelve el usuario actualizado
# - Si no lo encuentra:
#   - raise UsuarioNoEncontradoError()

class UsuarioRepository:
    def __init__(self):
        self._usuarios = []
        
    def agregar(self, usuario):
        for usuario_buscar in self._usuarios:
            if usuario.nombre == usuario_buscar.nombre:
                raise UsuarioDuplicadoError()
        self._usuarios.append(usuario)
        
    def buscar_por_nombre(self, nombre):
        for usuario_buscar in self._usuarios:
            if nombre == usuario_buscar.nombre:
                return usuario_buscar
        raise UsuarioNoEncontradoError()
    
    def eliminar_por_nombre(self, nombre):
        index = -1
        for usuario_buscar in self._usuarios:
            index += 1
            if nombre == usuario_buscar.nombre:
                return self._usuarios.pop(index)
        raise UsuarioNoEncontradoError()
    
    def actualizar_por_nombre(self, nombre, data):
        for usuario_buscar in self._usuarios:
            if nombre == usuario_buscar.nombre:
                if "edad" in data:
                    usuario_buscar.edad = data["edad"]
                if "activo" in data:
                    usuario_buscar.activo = data["activo"]
                return usuario_buscar
        raise UsuarioNoEncontradoError()
    
# Parte 4 - Service: actualizar usuario
# 4 Añade en UsuarioService el método:
# actualizar_usuario(self, nombre, data) que:
# 1. Llame a validar_update_usuario(data)
# 2. Llame a repo.actualizar_por_nombre(nombre, data)
# 3. Devuelva usuario.to_dict()

class UsuarioService:
    def __init__(self, repo):
        self.repo = repo
    
    def crear_usuario(self, data):
        usuario = usuario_desde_dict(data)
        self.repo.agregar(usuario)
        return usuario.to_dict()
    
    def obtener_usuario(self, nombre):
        usuario = self.repo.buscar_por_nombre(nombre)
        return usuario.to_dict()
    
    def eliminar_usuario(self, nombre):
        self.repo.eliminar_por_nombre( nombre)
        return None
    
    def actualizar_usuario(self, nombre, data):
        validar_update_usuario(data)
        usuario = self.repo.actualizar_por_nombre(nombre, data)
        return usuario.to_dict()
    
# Parte 5 - Endpoint UPDATE simulado
# 5 Crea una función:
# actualizar_usuario_endpoint(service, nombre, data) que devuelva:
# Si todo ok:
# {"status_code": 200, "data": <dic_usuario_actualizado>}
# Si datos inválidos:
# {"status_code": 400, "error": "Datos de usuario inválidos"}
# Si no existe:
# {"status_code": 404, "error": "Usuario no encontrado"}

def actualizar_usuario_endpoint(service, nombre, data):
    try:
        usuario = service.actualizar_usuario(nombre, data)
        return {"status_code": 200, "data": usuario}
    except DatosUsuarioInvalidosError:
        return {"status_code": 400, "error": "Datos de usuario inválidos"}
    except UsuarioNoEncontradoError:
        return {"status_code": 404, "error": "Usuario no encontrado"}
    
# Parte 6 - Pruebas
# 6 Inicializa repo + service y crea 2 usuarios
# 7 Prueba en este orden e imprime respuestas completas:
#   1 Actualizar un usuario existen (por ejemplo cambiar "edad")
#   2 Actualizar un usuario inexistene -> 404
#   3 Actualizar con data inválida (por ejemplo {} o "edad": "20") -> 400
#   4 Confirmar con GET que el usuario actualizado cambió

usuarioRepository = UsuarioRepository()
usuarioService = UsuarioService(usuarioRepository)

data1 = {"nombre": "Victor", "edad": 20, "activo": True}
data2 = {"nombre": "Lorena", "edad": 20, "activo": True}

crear_usuario_endpoint(usuarioService, data1)
crear_usuario_endpoint(usuarioService, data2)

data1_actualizar = {"edad": 22}
data1_actualizar_error = {"edadd": 22}

respuesta1 = actualizar_usuario_endpoint(usuarioService,"Victor", data1_actualizar)
respuesta2 = actualizar_usuario_endpoint(usuarioService,"Oscar", data1_actualizar)
respuesta3 = actualizar_usuario_endpoint(usuarioService,"Victor", data1_actualizar_error)
respuesta4 = obtener_usuario_endpoint(usuarioService, "Victor")

print(respuesta1)
print(respuesta2)
print(respuesta3)
print(respuesta4)

