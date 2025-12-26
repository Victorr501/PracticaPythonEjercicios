# Parte 1 - Define el atributo de clase
# 1 Usa la clase Usuario
# 2 Añade un atributo de clase llamado tipo con el valor "usuairo"
# Parte 2 - Crear instancias
# 3 Crea dos objetos de clase Usuario con datos distintos
# Parte 3 - Acceder al atributo de clase
# 4 Muestra por pantalla: 
#   - El atributo tipo accedido desde la clase
#   - El atributo tipo accedido desde cada objeto

class Usuario:
    tipo = "usuario"
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
usuario_1 = Usuario("Victor", 20)
usuario_2 = Usuario("Terra", 30)

print(usuario_1.tipo)
print(usuario_2.tipo)
print(Usuario.tipo)
