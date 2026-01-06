# Parte 1 - Reutiliza / adapta código previo
# 1 Reutiliza estas piezas (puedes copiarlas del Ejercicio 31):
#   - Excepciones:
#       - DatosUsuarioInvalidosError
#       - UsuarioDuplicadoErro
#   - Y añade una nueva:
#       - UsuarioNoEncontradoError
#       - Docstring:"Se lanza cuando no existe un usaurio con ese nombre"
#   - Clases/funciones:
#       - Usaurio con to_dict
#       - usuario_desde_dict
#       - UsuarioRepository (debe tener agregar y añade buscar_por_nombre)
#       - UsuarioService(debe tener crear_usuario y añade obtener_usaurio(self, nombre))
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

# Parte 2 - Repo:buscar por nombre
# 2 Implementa en UsuarioRepository el método
#   - buscar_por_nombre(self, nombre):
#       - Recorre la lista con for
#       - Si encuentra el usuario lo devuelve
#       - Si no, lanza UsuarioNoEncontradoError()

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
        
# Parte 3 - Service: obtener usuario
# 3 Implementa en UsuarioService el método:
#   - obtener_usuario(self, nombre):
#       - Llama a repo.buscar_por_nombre(nombre)
#       - Devuelve usuario.to_dict()
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
    
# Parte 4 - Endpoint GET simulado
# 4 Crea una función obtenida_usuario_endpoint(service, nombre) que devuelva:
# Si existe:
# {"status_code": 200, "data": <dict_usuario>}
# Si no existe (UsuarioNoEncontradoError)
# {"status_code": 404, "error": "Usuario no encontrado"}

def obtener_usuario_endpoint(service, nombre):
    try:
        usuario = service.obtener_usuario(nombre)
        return {"status_code": 200, "data": usuario}
    except UsuarioNoEncontradoError:
        return {"status_code": 404, "error": "Usuario no encontrado"}
    
# Parte 5 - Pruebas
# 5 Inicializa repo + service
# Crea 2 usuarios con el endpoint de crear (puedes copiar crear_usuario_endpoint del ejericio 30 o crear usuarios desde el service, como prefieras)
# Llamar a: 
#   - obtener_usuario_endpoint(service, "<nombre_existente>") -> imprime respuesta
#   - obtener_usuario_endpoint(service, "<nombre_inexistente>") -> imprime respuesta

usuarioRepository = UsuarioRepository()
usuarioService = UsuarioService(usuarioRepository)

def crear_usuario_endpoint(service, data):
    try:
        resultado = service.crear_usuario(data)
        return {"status_code": 201, "data": resultado}
    except DatosUsuarioInvalidosError:
        return {"status_code": 400, "error":"Datos de usuario inválidos"}
    except UsuarioDuplicadoError:
        return {"status_code": 409, "error": "Usuario duplicado"}
    
data1 = {"nombre": "Victor", "edad": 20, "activo": True}
data2 = {"nombre": "Lorena", "edad": 20, "activo": True}

crear_usuario_endpoint(usuarioService, data1)
crear_usuario_endpoint(usuarioService, data2)
respuesta1 = obtener_usuario_endpoint(usuarioService, "Victor")
respuesta2 = obtener_usuario_endpoint(usuarioService, "Juan")

print(respuesta1)
print(respuesta2)