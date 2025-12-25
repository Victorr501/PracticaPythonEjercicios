# Debes de crear una función que valide si un usaurio es mayor de edad
# 1 Define una función llamada es_mayor_de_edad que:
#   - Reciba un parámetro edad (entero)
#   - Devuelva True si la edad es mayor o igual a 18
#   - Devuelve False en caso contrario
# 2 Llama a la función al menos dos veces con edades distintas
# 3 Muestra por pantalla el resultado de cada llamada

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    if edad < 18:
        return False
    
prueba_1 = es_mayor_de_edad(18)
prueba_2 = es_mayor_de_edad(10)

print(prueba_1)
print(prueba_2)