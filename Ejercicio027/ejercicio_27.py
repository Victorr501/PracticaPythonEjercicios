# Parte 1 - Excepción de dominio
# 1 Crea una excecpión presonalizada UsaurioNoEncontradaError que herede de Exception
# 2 Docstring: "Se lanza cuando no existe un usuario con ese nombre"

class UsuarioNoEncontradoError(Exception):
    """
    Se lanza cuando no existe un usuario con ese nombre
    """
    pass

# Parte 2 - Clase Usuario
# 3 Crea una clase Usuario con:
#   - __init__(self, nombre, edad)
#   - Un método es_mayor_de_edad(self) que devuelva True/False

class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        return False
        
# Parte 3 - Clase UsuarioService
# 4 Crea una clase UsuairioService con:
#   - __init__(self, usuarios) donde Usuarios es una lista de objetos Usuario
#   - Un método buscar_por_nombre(self, nombre) que:
#       - Recorra la lista con un for
#       - Si encuentra un usaurio con usuario.nombre == nombre, lo devuelve
#       - Si termina y no lo encuentra, lanza UsuarioNoEncontradoError

class UsuarioService:
    def __init__(self, usuarios=None):
        self.usuarios = usuarios
        if usuarios is None:
            self.usuarios = list()

    def buscar_por_nombre(self, nombre):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                return usuario
        raise UsuarioNoEncontradoError()

# Parte 4 - Prueba
# 5 Crea una lista con 3 usuarios (edades distintas)
# 6 Crea una instancia de UsuarioService con esta lista
# 7 Haz dos pruebas:
#   - Busca un nombre que exista y mostar por pantalla:
#       - El nombre encontrado
#       - Si es mayor de edad
#   - Busca un nombre que NO exista y captura UsuarioNoEncontradoErro mostando un mensaje claro

lista_usuarios = [Usuario("Victor", 12), Usuario("Lorena", 20), Usuario("Oscar", 19)]

usuario_service = UsuarioService(lista_usuarios)

prueba_1 = usuario_service.buscar_por_nombre("Victor")

nombre_pruba_1 = prueba_1.nombre
es_mayor_prueba_1 = prueba_1.es_mayor_de_edad()

print(nombre_pruba_1)
print(es_mayor_prueba_1)

try:
    prueba_2 = usuario_service.buscar_por_nombre("Jose")
except UsuarioNoEncontradoError:
    print("No se ha encontrado un usuario con este nombre")