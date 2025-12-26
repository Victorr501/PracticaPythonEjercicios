# Parte 1 - Ampliar la clase
# 1 Usa la clase Usuario del ejercicio anterior
# 2 Añade un método de instancia llamado es_mayor_de_edad que:
#   - No reciba parámetros (solo self)
#   - Devuelva True si la edad del usuario es mayor o igual a 18
#   - Devuelva False en caso contrario
# Parte 2 - Probar el método
# 3 Crea dos usuarios:
#   - Uno mayor de edad
#   - Uno menor de edad
# 4 Llama al método es_mayor_de_edad en ambos objetos
# 5 Muestra por pantalla el resultado de cada llamada

class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        if self.edad < 18:
            return False

usuario_1 = Usuario("Victor", 20)
usuario_2 = Usuario("Lorena", 16)

prueba_1 = usuario_1.es_mayor_de_edad()
prueba_2 = usuario_2.es_mayor_de_edad()

print(prueba_1)
print(prueba_2)

