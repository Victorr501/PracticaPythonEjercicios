# Debes crear una función que realice una división segura
# 1 Define una función llamada division_segura que:
#   - Reciba dos parámetros: a y b
#   - Devuelva el resultado de a / b
# 2 Usa un bucle try / except dentro de la función para:
#   - Capturar un error de división entre cero
#   - En ese caso devuelver el valor None
# 3 Llama a la función:
#   - Una vez cada valores válidos
#   - Una vez provocando una división entre cero
# 4 Muestra por pantalla el resultado de ambas llamadas.

def division_segura(a, b):
    try:
        resultado = a/b
        return resultado
    except ZeroDivisionError:
        return None


numero_1 = division_segura(4,2)
numero_2 = division_segura(2,0)

print(numero_1)
print(numero_2)
