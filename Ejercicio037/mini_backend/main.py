from app.service import UsuarioService
from app.repository import UsuarioRepository
from app.dispatcher import dispatch_request

usuarioRepository = UsuarioRepository()
usuarioService = UsuarioService(usuarioRepository)


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


