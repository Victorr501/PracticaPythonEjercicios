# 1 Crea un diccionario con las siguientes claves:
#   -"nombre" -> cadena de texto
#   -"edad" -> número entero
#   -"activo" -> booleano
# 2 Muestra por pantalla:
#   -El diccionario completo
#   -El valor asociado a la clave "nombre"
#   -El valor asociado a la clave "edad"
# 3 Modifica:
#   -El valor de la clave "edad"
#   -El valor de la clave "activo"
# 4 Muestra de nuevo el diccionario completo tras las modificaciones

diccionario = {"nombre": "Victor", "edad" : 20, "activo": True}
print("Mostrar el dicionario")
print(diccionario)
print(diccionario["nombre"])
print(diccionario["edad"])

print("------------------")
print("Modificar el diccionario")
diccionario["edad"] = 21
diccionario["activo"] = False
print(diccionario)