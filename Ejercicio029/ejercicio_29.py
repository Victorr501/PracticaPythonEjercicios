# Parte 1 - Excepción de validación
# 1 Crea una excepción personalizada DatosUsuarioInvalidosError que herede de Exception
# 2 Docstring: "Se lanza cuando el dict de entrada no tiene datos válidos"

class DatosUsuarioInvalidosError(Exception):
    """
    Se lanza cuando el dict de entrada no tiene datos válidos
    """
    pass

# Parte 2 - Entidad Usuario
# 3 Crea una clase Usuario con:
#   - __init__(self, nombre, edad, activo)
#   - Método to_dict(self) que devuelva un diccionario con claves:
#       - "Nombre"
#       - "Edad"
#       - "Activo"

class Usuario:
    def __init__(self, nombre, edad, activo):
        self.nombre = nombre
        self.edad = edad
        self.activo = activo
        
    def to_dict(self):
        return {"nombre": self.nombre, "edad": self.edad, "activo": self.activo} 
    
# Parte 3 - Función de fábrica desde disct
# 4 Crea una función fuera de la clase llamada usuario_desde_dict(data) que:
#   - Recibe data(debe ser un dict)
#   - Valide:
#       - Que data sea dict, si no lanzar DatosUsuarioInvalidosError
#       - Que existan las claves "nombre", "edad", "activo", si falta alguna lanzar DatosUsuarioInvalidosError
#       - Que "nombre" sea str
#       - Que "edad" sea int
#       - Que "activo" sea bool
#   - Si todo es válido, duevuelva un objeto Usuario creado con estos datos

def usuario_desde_dict(data):
    if not isinstance(data, dict):
        raise DatosUsuarioInvalidosError()
    if not all(clave in data for clave in ("nombre", "edad", "activo")):
        raise DatosUsuarioInvalidosError()
    if not isinstance(data["nombre"], str):
        raise DatosUsuarioInvalidosError()
    if not isinstance(data["edad"], int):
        raise DatosUsuarioInvalidosError()
    if not isinstance(data["activo"], bool):
        raise DatosUsuarioInvalidosError()
    return Usuario(data["nombre"], data["edad"], data["activo"])


# Parte 4 - Pruebas
# 5 Crea dos diccionarios:
#   - data_ok con datos correctos
#   - data_bad con al menos un dato incorrecto
# 6 Prueba:
#   - Convierte data_ok a Usuario y luego imprimir usuario.to_dict()
#   - Intenta convertir data_bad, capturar DatosUsuarioInvalidosError y mostrar un mensaje claro

data_ok = {"nombre": "victor", "edad": 20, "activo": True}
data_bad = {"nombre": "lorena", "edad": 22, "activ": False}

usuario_ok = usuario_desde_dict(data_ok)
print(usuario_ok.to_dict())

try:
    usuario_bad = usuario_desde_dict(data_bad)
    print(usuario_bad.to_dict())
except DatosUsuarioInvalidosError:
    print("Datos introducidos mal")
