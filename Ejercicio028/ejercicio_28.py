# Parte 1 - Excepciones
# 1 Crea dos excepciones personalizadas:
#   - UsuarioNoEncontradoError (igual que antes)
#   - UsuarioDuplicadoError (docstring: "Se lanza si ya existe un usuario con ese nombre")

class UsuarioNoEncontradoError(Exception):
    """
    Se lanza cuando no existe un usuario con ese nombre
    """
    pass

class UsuarioDuplicadoError(Exception):
    """
    Se lanza si ya existe un usuario con ese nombre
    """
    pass

# Parte 2 - Entidad Usuario
# 2 Crea la clase Usuario con:
#   - __init__(self, nombre, edad)
#   - Método es_mayor_de_edad(self)(igual que antes)

class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        return False
    
# Parte 3 - Repositorio UsaurioRespository
# 3 Crea una clase UsuarioRespository con:
#   - __init__(self) que inicialice una lista vacía interna (por ejemplo self._usaurios)
#   - agregar(self, usuario) que:
#       - Lanza UsuarioDuplicadoError si ya existe un usuario con el mismo nombre
#       - Si no existe, lo añada a la lista
#   - buscar_por _nombre(self, nombre) que:
#       - Devuelva el usuario si existe
#       - Si no existe, lanza UsuarioNoEncontradoError
#   - elimina_por_nombre(self, nombre) que:
#       - Elimine el usuario si existe
#       - Si no existe, lanza UsuarioNoEncontradoError

class UsuarioRepository:
    def __init__(self):
        self._usuarios = list()
        
    def agregar(self, usuario):
        for usuario_buscar in self._usuarios:
            if usuario_buscar.nombre == usuario.nombre:
                raise UsuarioDuplicadoError()
        self._usuarios.append(usuario)
        
        
    def buscar_por_nombre(self, nombre):
        for usuario in self._usuarios:
            if usuario.nombre == nombre:
                return usuario
        raise UsuarioNoEncontradoError()
    
    def eliminar_por_nombre(self, nombre):
        for usuario in self._usuarios:
            if usuario.nombre == nombre:
              self._usuarios.remove(usuario)
              return  
        raise UsuarioNoEncontradoError()
        
        
        
# Parte 4 - Servicio UsuarioService
# 4 Crea  una clase UsuarioService con:
#   - __init__(self, repo) donde repo es un UsuarioRepository
#   - registar_usaurio(self, nombre, edad) que:
#       - Crea un objeto Usuario 
#       - Lo agrega al repo (usando repo.agregar)
#       - Devuelva el usuario creado

class UsuarioService:
    def __init__(self, repo):
        self.repo = repo
    
    def registrar_usuario(self, nombre, edad):
        usuario = Usuario(nombre, edad)
        self.repo.agregar(usuario)
        return usuario
    
# Parte 5 - Pruebas
# 5 Debes probar:
#   - Registrar 2 usuarios distintos (mostrar sus nombres)
#   - Intenta registrar un usuario duplicado y capturar UsaurioDuplicadoError
#   - Buscar un usuario existente y mostrar si es mayor de edad
#   - Eliminar un usuario existente
#   - Intenta eliminar el mismo usuario otra vez y captura UsuarioNoEncotradoError

usuario_repository = UsuarioRepository()
usuario_service = UsuarioService(usuario_repository)

usuario_1 = usuario_service.registrar_usuario("Victor", 20)
usuario_2 = usuario_service.registrar_usuario("Lorena", 22)

print(usuario_1.nombre)
print(usuario_2.nombre)

try:
    usuario_3 = usuario_service.registrar_usuario("Victor", 20)
except UsuarioDuplicadoError:
    print("Este usuario ya esta registrado")
    
usuario_existente = usuario_repository.buscar_por_nombre("Lorena")
resultado_es_mayor_usuario_existente = usuario_existente.es_mayor_de_edad()
print(resultado_es_mayor_usuario_existente)

usuario_repository.eliminar_por_nombre("Victor")

try:
    usuario_repository.eliminar_por_nombre("Victor")
except UsuarioNoEncontradoError:
    print("Usuario no encontrado")