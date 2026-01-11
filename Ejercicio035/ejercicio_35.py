# Parte 1 - Reutiliza tu "mini backend"
# 1 Reutiliza del Ejercicio 34 
# - Excepciones
# - Usuario, usuario_desde_dict
# - UsuarioRepository, Usuarioservice
# - Endpoint
#   - crear_usuario_endpoint(service, data)
#   - obtener_usuario_endpoint(service, nombre)
#   - actualizar_usuario_endpoint(service, nombre, data)
#   - eliminar_usuario_endpoint(service, nombre)

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
    
def actualizar_usuario_endpoint(service, nombre, data):
    try:
        usuario = service.actualizar_usuario(nombre, data)
        return {"status_code": 200, "data": usuario}
    except DatosUsuarioInvalidosError:
        return {"status_code": 400, "error": "Datos de usuario inválidos"}
    except UsuarioNoEncontradoError:
        return {"status_code": 404, "error": "Usuario no encontrado"}
    
    
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
    
# Parte 2 - Dspatcher
# 2 Crea una función dispatch_request(service, method, path, body=None) que:
# Entrada
#   - Service: UsuarioService
#   - method: string "GET", "POST", "PUT", "DELETE"
#   - path: string como:
#       - "/usuarios"
#       - "/usuarios/Victor"
#   - body: dict (para POST/PUT) o None

# Logica que debe soportar
#   - Si method == "POST" y path == "/usuarios":
#       - Llama a crear_usuario_endpoint(service, body)
#   - Si method == "GET" y path empieza por "/usuarios/":
#       - Extrae  el nombre de la ruta y llama a obtener_usuario_endpoint(service, nombre)
#   - Si method == "PUT" y path empieza por "/usuarios/":
#       - Extrae el nombre y llama a actualizar_usuario_endpoint(service, nombre, body)
#   - Si method == "DELETE" y path empieza por "/usuarios/":
#       - Extrae el nombre y llama a eliminar_usuario_endpoint(service, nombre)

# Si la ruta o método no coincide
# Devuelve:
# {"status_code": 404, "error": "Ruta no encontrada"}

def dispatch_request(service, method, path, body=None):
    prefijo = "/usuarios/"
    if method == "POST" and path == "/usuarios":
        return crear_usuario_endpoint(service, body)
    if method == "GET" and path.startswith(prefijo):
        nombre = path[len(prefijo):]
        return obtener_usuario_endpoint(service, nombre)
    if method == "PUT" and path.startswith(prefijo):
        nombre = path[len(prefijo):]
        return actualizar_usuario_endpoint(service, nombre, body)
    if method == "DELETE" and path.startswith(prefijo):
        nombre = path[len(prefijo):]
        return eliminar_usuario_endpoint(service, nombre)
    return {"status_code": 404, "error": "Ruta no encontrada"}

# Parte 3 - Pruebas 
# 3 Inicializa repo + service
# 4 Crea una lista de "requests" y ejecútalas una a una (sin bucles while; for is esta permitido aqui):
# Ejecuta en este orden y haz print de cada respuesta:
# 1 POST /usuarios con body válido (crea Victor)
# 2 POST /usuarios con body duplicado (Victor de nuevo)
# 3 GET /usuarios/Victor (debe dar 200)
# 4 PUT /usuarios/Victor con body {"edad": 30}
# 5 GET /usuarios/Victor (confirmar edad actualizada)
# 6 DELETE /usuarios/Victor
# 7 GET /usuarios/victor (debe dar 404)
# 8 GET /ruta_inventada (debe dar 404 ruta no encotrada)

usuarioRepository = UsuarioRepository()
usuarioService = UsuarioService(usuarioRepository)

respuesta1 = dispatch_request(usuarioService, "POST", "/usuarios", {"nombre": "Victor", "edad": 20, "activo": True})
respuesta2 = dispatch_request(usuarioService, "POST", "/usuarios", {"nombre": "Victor", "edad": 20, "activo": True})
respuesta3 = dispatch_request(usuarioService, "GET", "/usuarios/Victor")
respuesta4 = dispatch_request(usuarioService, "PUT", "/usuarios/Victor", {"edad": 30})
respuesta5 = dispatch_request(usuarioService, "GET", "/usuarios/Victor")
respuesta6 = dispatch_request(usuarioService, "DELETE", "/usuarios/Victor")
respuesta7 = dispatch_request(usuarioService, "GET", "/usuarios/Victor")
respuesta8 = dispatch_request(usuarioService, "GET", "/ruta_inventada")

print(respuesta1)
print(respuesta2)
print(respuesta3)
print(respuesta4)
print(respuesta5)
print(respuesta6)
print(respuesta7)
print(respuesta8)