# Parte 1 - Clase base
# 1 Usa la clase Usuario como clase base, con:
#   - Atributos de instancia: nombre, edad
#   - Atributos de clase: tipo = "usaurio"
# Parte 2 - Clase hija
# 2 Crea una clase llamada Admin que herede de Usuario
# 3 La clase Admin debe:
#   - Tener un atributo de clase tipo = "admin"
#   - Tener un método es_admin que devuelva True
# Parte 3 - Inicialización correcta
# 4 El constructor (__init__) de admin debe:
#   - Recibir nombre y edad
#   - Llamar al constructor de la calse padre usando super()
# Parte 4 - Probar la herencia
# 5 Crea un objeto usuario y un objeto admin
# 6 Muestra por pantalla:
#   - Nombre del usuario
#   - El tipo del usuario
#   - El nombre del admin
#   - El tipo del admin
#   - El resultado del método es_admin

class Usuario:
    tipo = "usuario"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
class Admin(Usuario):
    tipo = "admin"
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        
    def es_admin(self):
        return True
    
usuario = Usuario("Victor", 20)
admin = Admin("Oscar", 20)

resultado_prueba = admin.es_admin()

print(usuario.nombre)
print(usuario.tipo)
print(admin.nombre)
print(admin.tipo)
print(resultado_prueba)