# Parte 1 - Excepciones
# 1 Crea estas excepciones personalizadas:
#   - DatosUsuarioInvalidosError
#   Docstring: "Se lanza cuando el dict de entrada no tiene datos válidos"
#   - UsuarioDuplicadoError
#   Docstring: "Se lanza si ya existe un usuario con ese nombre"

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

# Parte 2 - Entidad Usuario
# 2 Crea la clase Usuario con:
#   - __init__(self, nombre, edad, activo)
#   - to_dict(self) -> devuelve {"nombre": ....., "edad":....., "activo":.....}

class Usuario:
    def __init__(self, nombre, edad, activo):
        self.nombre = nombre
        self.edad = edad
        self.activo = activo
        
    def to_dict(self):
        return {"nombre": self.nombre, "edad": self.edad, "activo": self.activo}
    
# Parte 3 - Factory usuario_desde_dict
# 3 Crea una función usuario_desde_dict(data) que valide:
#   - data es dict
#   - tiene claves "nombre", "edad", "activo"
#   - "nombre" es str, "edad" es int, "activo" es bool
# Si algo falla -> raise DatoUsuarioInvalidosError()
# Si todo ok -> devuelve Usuario(...)

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

# Parte 4 - Repositorio en memoria
# 4 Crea UsuarioRepository con:
#   - __init__ crea self._usuarios = []
#   - agregar(self, usuario):
#       - Si ya existe un usuario con el mismo nombre -> raise UsuarioDuplicadoError()
#       - si no, lo añade

class UsuarioRepository:
    def __init__(self):
        self._usuarios = []
        
    def agregar(self, usuario):
        for usuario_buscar in self._usuarios:
            if usuario.nombre == usuario_buscar.nombre:
                raise UsuarioDuplicadoError()
        self._usuarios.append(usuario)
        
# Parte 5 - Servicio
# 5 Crea UsuarioService con:
#   - __init__(self, repo)
#   - crear_usuario(self, data) que:
#       - Cree un Usuario usando usuario_desde_dict(data)
#       - Lo agregue al repositorio
#       - Devuelva usuario.to_dict()

class UsuarioService:
    def __init__(self, repo):
        self.repo = repo
    
    def crear_usuario(self, data):
        usuario = usuario_desde_dict(data)
        self.repo.agregar(usuario)
        return usuario.to_dict()
    
# Parte 6 - Simulación de endpoint
# 6 Simula un "endpoint" haciendo:
#   - Un data_ok válido
#   - Un data_dup con el mismo nombre que data_ok
#   - Un data_bad inválido
# 7 Prueba (en este orden):
#   - Llamar service.crear_usuario(data_ok) y hacer print del dict devuelto
#   - Llamar service.crear_usuario(data_dup) y capturar UsuarioDuplicadoError mostrando mensaje claro
#   - Llamar service.crear_usaurio(data_bad) y capturar DatosUsuarioInvalidosError mostrando mensaje claro

data_ok = {"nombre": "Victor", "edad": 20, "activo": True}
data_dup = {"nombre": "Victor", "edad": 20, "activo" : True}
data_bad = {"nombre": "Juan", "eda": 20, "activo" : True}

usuario_repository = UsuarioRepository()
usuario_service = UsuarioService(usuario_repository)

resultado_ok = usuario_service.crear_usuario(data_ok) 
print(resultado_ok)

try:
    resultado_dup = usuario_service.crear_usuario(data_dup)
    print(resultado_dup)
except UsuarioDuplicadoError:
    print("Usuario con el nombre duplicado")
    
try:
    resultado_bad = usuario_service.crear_usuario(data_bad)
    print(resultado_bad)
except DatosUsuarioInvalidosError:
    print("Los datos mal introducidos")
        
