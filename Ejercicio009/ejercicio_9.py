# Debes realizar dos recorridos distintos usando for.
# Parte 1 - Recorrido de una lista
# 1 Crea una lista con al menos 3  nombres de usuarios
# 2 Recorre la lista con un for y muesrta cada nombre por pantalla, uno por línea
# Parte 2 - Uso de range()
# 3 Usa un bucle for con range () para mostrar los números del 1 al 5 (ambos incluidos)

lista_1 = ["Correr", "Andar", "Nadar"]

for deporte in lista_1:
    print(deporte)
    
print("-------------------")

for number in range(1,6): # Se puede poner el inicio y el final en el rango
    print(number)