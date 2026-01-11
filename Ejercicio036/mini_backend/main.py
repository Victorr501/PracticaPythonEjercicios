# 1 Estructura de carpetas
# Crea esta estructura (los nombre importan):
# mini_backend/
#   app/
#       __init__.py
#       errors.py
#       models.py
#       repository.py
#       service.py
#       endpoints.py
#       dispatcher.py
#   main.py

# 2 Qué va en cada archivo
#   - errors.py
#       - DatosUsuarioInvalidosError
#       - UsuarioDuplicadoError
#       - UsuarioNoEncontradoError
#   - models.py
#       - Clase Usuario
#       - Función usuario_desde_dict(data)
#       - Función validar_update_usuario(data)
#   - repository.py
#       - Clase usuarioRepository con:
#           - agregar
#           - buscar_por_nombre
#           - eliminar_por_nombre
#           - actualizar_por_nombre
#   - service.py
#       - Clase UsuarioService con:
#           - crear_usuario
#           - obtener_usuario
#           - eliminar_usuario
#           - actualizar_usuario
#   - endpoints.py
#       - crear_usuario_endpoint
#       - obtener_usuario_endpoint
#       - actualizar_usaurio_endpoint
#       - eliminar_usuario_endpoint
#   - dispatcher.py
#       - dispatch_request(service, method, path, body=None)
#   - main.py
#       - Debe:
#           1. Instanciar usuarioRepository y UsuarioService
#           2. Ejecutar la misma secuenca de "requests" que en el Ejercicio 35
#           3. Hacer print() de cada respuesta

from app.service import UsuarioService
from app.repository import UsuarioRepository
from app.dispatcher import dispatch_request

usuarioRepository = UsuarioRepository()
usuarioService = UsuarioService(usuarioRepository)

# 3 Imports (muy importante)
#   - Debes usar imports propios entre módulos (según tu estructura)
#   - Permitido: imports absolutos tipo from app.service  import UsuarioService o relativos dentro del paquete (si sabes usarlos bien)
#   - Prohibido: copiar / pegar todo en main.py "para que funcione"
#   - Evita cirular imports (si te pasa, reoganiza dependecias)

# 4 Comportamiento esperado (tests manuales)
# Tu salida (los status_code) debe seguir esta lógica
# 1 POST /usuarios Victor válido -> 201
# 2 POST duplicado Victor -> 409
# 3 GET /usuarios/Victor -> 200
# 4 PUT /usuarios/Victor con {"edad":30} -> 200
# 5 GET /usuarios/Victor -> 200 (edad actualizada)
# 6 DELTE /usuarios/Victor -> 204
# 7 GET /usuarios/Victor -> 404
# 8 GET /ruta_inventada -> 404 con "Ruta no encontrada"

respuesta1 = dispatch_request(usuarioService, "POST", "/usuarios", {"nombre": "Victor", "edad": 20, "activo": True})
respuesta2 = dispatch_request(usuarioService, "POST", "/usuarios", {"nombre": "Victor", "edad": 20, "activo": True})
respuesta3 = dispatch_request(usuarioService, "GET", "/usuarios/Victor")
respuesta4 = dispatch_request(usuarioService, "PUT", "/usuarios/Victor", {"edad": 30})
respuesta5 = dispatch_request(usuarioService, "GET", "/usuarios/Victor")
respuesta6 = dispatch_request(usuarioService, "DELETE", "/usuarios/Victor")
respuesta7 = dispatch_request(usuarioService, "GET", "/usuarios/Victor")
respuesta8 = dispatch_request(usuarioService, "GET", "/ruta_inventada")

print(respuesta1)
print(respuesta2)
print(respuesta3)
print(respuesta4)
print(respuesta5)
print(respuesta6)
print(respuesta7)
print(respuesta8)



