# Parte 1 - Clase base 
# 1 Usa la clase Usuario
# 2 La clase Usuario debe tener
#   - Atributos de instancia: nombre, edad
#   - Atributos de clase: tipo = "usuario"
# 3 Añade un método de instancia llamado presentarse que:
#   - Devuelve una cadena de texto con el formato: "Soy un usuario llamado <nombre>"
# Parte 2 - Clase hija con override
# 4 Usa la clase Admin que herede de Usuario
# 5 La clase Admin debe:
#   - Tener tipo = "admin"
#   - Sobreescribir el método presentarse para que:
#       - Use super().presentarse()
#       - Añada al final: " y soy administrador"
# Parte 3 - Probar el comportamiento
# 6 Crear:
#   - Un objeto Usuario
#   - Un objeto Admin
# 7 Muestra por pantalla:
#   - El resultado de presentarse() del usurio
#   - El resultado de presentarse() del admin

class Usuario:
    tipo = "usuario"
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def presentarse(self):
        return f"Soy un usuario llamado {self.nombre}"
    
class Admin(Usuario):
    tipo = "admin"
    
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        
    def presentarse(self):
        return super().presentarse() + " y soy administrador"
    
usuario = Usuario("victor", 20)
admin = Admin("Juan", 23)

respuesta_1 = usuario.presentarse()
respuesta_2 = admin.presentarse()

print(respuesta_1)
print(respuesta_2)

