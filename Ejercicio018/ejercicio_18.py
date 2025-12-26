# Parte 1 - Define la clase
# 1 Crea una clase llamada usuario
# 2 La clase debe tener un método __init__ que reciba:
#   - nombre
#   - edad
# 3 Dentro del __init__, guarda esos valores como atributos del objeto usando self
# Parte 2 - Crear objetos
# 4 Crea dos objetos de la clase usuario con datos distintos
# 5 Muestra por pantalla:
#   - El nombre del primer usuario
#   - La edad del segundo usuario

class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
usuario_1 = Usuario("Victor", 20)
usuario_2 = Usuario("Vitoria", 90)

print(usuario_1.nombre)
print(usuario_2.edad)