# Parte 1 - Crear una excepción prersonalizada
# 1 Crea una clase llamada EdadInvalidadErro que herede de Excecption
# 2 Ponle un docstring breve explicando cuándo se usa
# Parte 2 - Función con validación y raise
# 3 Define una función llamada validad_edad que:
#   - Reciba un parámetro edad
#   - Si edad es menor que 0, debe lanzar EdadInvalidaError
#   - Si no, debe devolver True
# Parte 3 - Probar el error
# 4 Llama a validar_edad dos veces:
#   - Una con una edad válida (por ejemplo 20)
#   - Otra con una edad inválida (por ejemplo -5)
# 5 Debes manejar el caso inválido con try / except para:
#   - Capturar EdadInvalidaError
#   - Mostrar por pantalla un mensaje claro indicando que la edad no es válida

class EdadInvalidaError(Exception):
    """
    Se lanza cuando la edad sea menor que 0
    """
    # El docstring debería explicar cuándo se lanza, no “qué verifica”.
    
def validar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError() # Se instancia asi con los parentesis 
    return True


try:
    prueba_1 = validar_edad(20)
    print(prueba_1) # No es error pero asi verifico el ejercicio antes de que lance el error
    prueba_2 = validar_edad(-5)
    print(prueba_2)
except EdadInvalidaError:
    print("La edad es menor que 0")
    
