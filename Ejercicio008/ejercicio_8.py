# Debes simular una validación avanzada de acceso
# 1 Declara las siguientes variables:
#   - edad (entero)
#   - activo (booleano)
#   - rol (cadena de texto)
# 2 La lógica de acceso debe ser:
#   - El acceso se permite si:
#       - El usuario es mayor o igual a 28
#       - Está activo
#       - Y su rol es "admin" o "supervisor"
#   - En cualquier otro caso, el aceso se denega
# 3 Muestra por pantalla
#   - "Acceso permitido" o "acceso denegado" según corresponda

edad = 18
activo = True
rol = "supervisor"

if edad >= 18 and activo and (rol.__eq__("admin") or rol.__eq__("supervisor") ):# usar el .__eq__ no se llama a mano, sino que usas  == directamente ya que este llama por si solo al metodo .__eq__ 
    print("Acceso permitido")
else:
    print("Acceso denegado")