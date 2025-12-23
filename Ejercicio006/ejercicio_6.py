# 1 Crea un conjunto con al menos 3 permisos (cadenas de texto)
# 2 Muestra por pantalla:
#   - El conjunto completo
#   - El número total de permisos
# 3 Añade un nuevo permiso al conjunto
# 4 Elimina un permiso existente del conjunto
# 5 Crea un segundo conjunto con otros permisos
# 6 Muestra por pantalla
#   - La unión de ambos conjuntos
#   - La intersección de ambos conjutos

set_permiso = {"Administrador", "Usuario", "Supervisor"}
print("Mostrar por pantalla los permisos de este conjunto")
print(set_permiso)
print(len(set_permiso))

print("------------------------")
set_permiso.add("Vip")
set_permiso.remove("Usuario")

set_permiso_segundo = {"Administrador", "Usuario", "Supervisor"}
print(set_permiso.union(set_permiso_segundo))
print(set_permiso.intersection(set_permiso_segundo))