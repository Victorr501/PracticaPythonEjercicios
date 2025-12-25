# Debes crear una función que calcule el precio final de un producto aplicando un impuesto
# 1 Define una función llamada calcular_precio_final que:
#   - Reciba un parámetro precio (float o int)
#   - Reciba un parámetro impuesto con valor por defecto 21
#   - Devuelva el precio final aplicando el impuesto
# 2 Llama a la función:
#   - Una vez sin indicar el impuesto (usar el valor por defecto)
#   - Una vez indicando un impuesto distinto
# 3 Muestra por pantalla el resultado de ambas llamadas

def calcular_precio_final (precio, impuesto = 21):
    precio_final = precio + (precio * (impuesto / 100))
    return precio_final

prueba_1 = calcular_precio_final(100)
prueba_2 = calcular_precio_final(100, 10)

print(prueba_1)
print(prueba_2)