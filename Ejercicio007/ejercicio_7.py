# Debes simular una validación de acceso de un usuario
# 1 Declara las siguiente variable:
#   - edad (entero)
#   - activo (booleano)
# 2 Usa una estructura if / elif / else para:
#   - Si el usuario es mayor o igual a 18  y esta activo -> mostrar "Acceso permitido"
#   - Si el usuario es menor de 18 -> mostrar "Acceso denegado por edad"
#   - En cualquier otro caso -> mostrar "Acceso denegado"

edad = 17
activo = True

if edad >= 18 and activo:
    print("Acceso permitido")
elif edad < 18:
    print("Acceso denegado por edad")
else:
    print("Acceso denegado")