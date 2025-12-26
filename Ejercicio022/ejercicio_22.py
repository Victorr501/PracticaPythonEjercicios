# Parte 1 - Clase base
# 1 Usa la clase Usuario
# 2 La clase debe tener:
#   - Atributos de isntancia: nombre, edad
#   - Atributos de clase: tipo = "usuario"
# Parte 2 - Método estático
# 3 Añade un método estático llamado es_edad_valida que:
#   - Use el decorador @staticmethod
#   - Reciba un parámetro edad
#   - Devuelva True si la edad es mayor o igual a 0
#   - Devuelva False si la edad es negativo
# Parte 3 - Probar el método
# 4 Llama al método es_edad_valida:
#   - Una vez con una edad valida
#   - Una vez con una edad inválida
# 5 Muestra por pantalla el resultado de ambas llamadas

class Usuario:
    tipo = "usuario"
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    @staticmethod
    def es_edad_valida(edad):
        if edad >= 0:
            return True
        return False
    
prueba_1 = Usuario.es_edad_valida(10)
prueba_2 = Usuario.es_edad_valida(-5)

print(prueba_1)
print(prueba_2)