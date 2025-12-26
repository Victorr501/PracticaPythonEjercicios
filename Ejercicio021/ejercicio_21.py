# Parte 1 - Define la clase
# 1 Usa la clase Usuario
# 2 La casle debe tener:
#   - Atributos de instancia: nombre, edad
#   - Atributos de clase: tipo = "usuario"
# Parte 2 - Crear un método de clase
# 3 Añade un método de clase llamado crear_usuario_por_defecto que:
#   - Use el decorador @classmethod
#   - Reciba cls como parámetro
#   - Devuelva un nuevo objeto Usuario con:
#       - nombre "Invitado"
#       - edad 0
# Parte 3 - Probar el método
# 4 Usa el método crear_usuario_por_defecto para crear un usuario
# 5 Muestra por pantalla
#   - El nombre del usuario creado
#   - La edad del usuario creado
#   - El atributo de clase tipo

class Usuario:
    tipo = "usuario"
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 
    
    @classmethod
    def crear_usuario_por_defecto(cls):
        return Usuario("Invitado", 0)
    
usuario_defecto = Usuario.crear_usuario_por_defecto()

print(usuario_defecto.nombre)
print(usuario_defecto.edad)
print(usuario_defecto.tipo)



