# Parte 1 - Clase abstacta
# 1 Crea una clase abstracta llamada UsuarioBase
# 2 Debe heredar de ABC.
# 3 Debe tener:
#   - Un método abstracto llamado presentarse que no tenga implementación
# Parte 2 - Clase concreta
# 4 Crea una clase Usuario que herede de UsuarioBase
# 5 La clase Usuario debe:
#   - Tener un atributo de instancia nombre
#   - Implementar el método presentarse devolviendo: "Soy un usuario llamado <nombre>"
# Parte 3 - Probar el comportamiento
# 6 Crea un objeto Usuario
# 7 Muestra por pantalla el resultado de presentarse()
from abc import ABC, abstractmethod

class UsuarioBase(ABC):
    @abstractmethod
    def presentarse(self):
        pass

class Usuario(UsuarioBase):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def presentarse(self):
        return f"Soy un usuario llamado {self.nombre}"
    
usuario = Usuario("Victor")

resultado = usuario.presentarse()

print(resultado)