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
    
def obtener_usuario_endpoint(service, nombre):
    try:
        usuario = service.obtener_usuario(nombre)
        return {"status_code": 200, "data": usuario}
    except UsuarioNoEncontradoError:
        return {"status_code": 404, "error": "Usuario no encontrado"}
    
    
# Parte 2 - Repo: eliminar por nombre
# 2 Implementa UsuarioRepository.eliminar_por_nombre(self, nombre):
#   - Recoge self._usuarios con for
#   - Si encuentra el usuario con ese nombre:
#       - lo elimina
#       - hace return
#   - Si no lo encuentra:
#       -lanza UsuarioNoEncontradoError()

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

# Parte 3 - Service: eliminar usuario
# 3 Implementa UsuarioService.eliminar_usuario(self, nombre):
# - Llama a repo.eliminar_por_nombre(nombre)
# - No devuelve nada(None)

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
        usuario = self.repo.eliminar_por_nombre( nombre)
        return None
    
# Parte 4 - Endpoint DELETE simulado
# 4. Crear una función eliminar_usuario_endpoint(service, nombre):
# Si se elimina correctamente:
# {"status_code": 204}
# Si no existe(UsuarioNoEncontradoError):
# {"status_code": 404, "error": "Usuario no encontrado"}

def eliminar_usuario_endpoint(service, nombre):
    try:
        service.eliminar_usuario(nombre)
        return {"status_code": 204}
    except UsuarioNoEncontradoError:
        return {"status_code": 404, "error": "Usuario no encontrado"}
    
# Parte 5 - Pruebas
# 5 Inicializa repo + service
# 6 Crea 2 usuarios con crear_usuario_endpoint
# 7 Prueba:
#   - Eliminar un usuario existen -> imprimir respuesta
#   - Intenar eliminar el mismo usuario otra vez -> imprimir repuesta (debe ser 404)
#   - confirmar que el otro usuario sigue existiendo usando obtener_usuario_endpoint

usuarioRepository = UsuarioRepository()
usuarioService = UsuarioService(usuarioRepository)

data1 = {"nombre": "Victor", "edad": 20, "activo": True}
data2 = {"nombre": "Lorena", "edad": 20, "activo": True}

crear_usuario_endpoint(usuarioService, data1)
crear_usuario_endpoint(usuarioService, data2)

respuesta1 = eliminar_usuario_endpoint(usuarioService, "Victor")
respuesta2 = eliminar_usuario_endpoint(usuarioService, "Victor")

print(respuesta1)
print(respuesta2)

respuesta3 = obtener_usuario_endpoint(usuarioService, "Lorena")
print(respuesta3)
                
            
