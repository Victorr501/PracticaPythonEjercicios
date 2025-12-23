# 1 Crea una tupla con 3 roles (cadenas de texto)
# 2 Muestra por pantalla:
#   - La tupla completa
#   - El tipo de la estructura usando type()
#   - El primer rol
#   - El último rol usando indexación negativa
# 3 Intenta modificar uno de los roles de la tupal

tupla_roles = ("administrado", "desarrolador", "usuario")
print("Mostrar la tupla")
print(tupla_roles)
print(type(tupla_roles))
print(tupla_roles[0])
print(tupla_roles[-1])

print("------------------")
print("Intentar modificar la tupal")
tupla_roles[0] = "Hola mundo"
print(tupla_roles[0]) #Esta linea no se muestra porque al saltar error en la linea superior, este no se ejecuta, teniendo en cuenta que python se ejecuta de arriba hacia abajo