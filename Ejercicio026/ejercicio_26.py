# Parte 1 - Excepción de dominio
# 1 Crea una excepción personalizada PermisoInvalidoError que herede de Exception
# 2 Añade un docstring breve indicando cuándo se lanza
# Parte 2 - Clase base Usuario
# 3 Crea una clase Usuario con:
#   - Atributo de clase: tipo = "usuario"
#   - __init_(self, nombre, edad, permisos)
#       - permisos debe ser un set de strings
#   - Un método tiene_permiso(self, permiso) que:
#       - Si permiso no es str, lance PermisoInvalidoErro
#       - Si el str, devuelva True si está en el set de permisos, si no False
# Parte 3 - Clase Admin(herencia)
# 4 Crea una clase Admin que herede de Usuario con:
#   - Atributo de clase: tipo = "admin"
#   - Override de tiene_permiso(self, permiso) para que:
#       - Use super().tiene_permiso(permiso) solo para validar el tipo
#       - Pero finalmente siempre True(un admin tiene todos los permisos)
# Parte 4 - Pruebas
# 5 Crea:
#   - Un Usuario con permisos: {"leer", "escribir"}
#   - Un Admin con permisos: {"leer"} (aunque no importará)
# 6 Muestra por pantalla:
#   - Tipo del usuario y del admin
#   - Resultado de tiene_permiso("escribir" en ambos)
# 7 Provoca el error llamado a tiene_permiso(123) en el usuario y maneja la excepción con try/except mostrando un mensaje claro

class PermisoInvalidoError(Exception):
    """
    Los permisos no son str
    """
    pass

class Usuario:
    tipo = "usuario"
    def __init__(self, nombre, edad, permisos=None):
        self.nombre = nombre
        self.edad = edad
        if not isinstance(permisos, set):
            self.permisos = set()
        elif isinstance(permisos, set):
            self.permisos = permisos
        
    def tiene_permiso(self, permiso):
        if not isinstance(permiso, str):
            raise PermisoInvalidoError()
        if permiso in self.permisos:
            return True
        return False
    
class Admin(Usuario):
    tipo = "admin"
    def __init__(self, nombre, edad, permisos=None):
        super().__init__(nombre, edad, permisos)

    def tiene_permiso(self, permiso):
        super().tiene_permiso(permiso)
        return True
    
usuario = Usuario("Victor", 20, {"leer", "escribir"})
admin = Admin("Lorena", 22, {"leer"})

tipo_usuario = usuario.tipo
tipo_admin = admin.tipo

print(tipo_usuario)
print(tipo_admin)

resultado_usuario = usuario.tiene_permiso("escribir")
resultado_admin = admin.tiene_permiso("escribir")

print(resultado_usuario)
print(resultado_admin)

try:
    usuario.tiene_permiso(123)
except PermisoInvalidoError:
    print("Tienes que introducir un string")
        