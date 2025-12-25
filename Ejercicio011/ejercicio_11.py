# Debes trabajar con una lista de números enteros
# 1 Crea una lista con al menos 6 números
# 2 Recorre la lista con un for
# 3 Dentro del bucle:
#   - Si el números es negativo, usa continue para saltarlo
#   - Si el número es 0, usa break para detener el bucle
#   - En cualquier otro caso, muestra el número por pantalla

lista_numeros = [1, 3, -5, 4, 0, 5]

for numero in lista_numeros:
    if numero < 0:
        continue
    if numero == 0:
        break
    if numero > 0:
        print(numero)
        
