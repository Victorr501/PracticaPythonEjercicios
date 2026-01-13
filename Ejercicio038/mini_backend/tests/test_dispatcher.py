import pytest
from app.dispatcher import dispatch_request
from app.service import UsuarioService
from app.repository import UsuarioRepository

class TestDispatcher(pytest.TestCase):
    def service(self):
        userRepository = UsuarioRepository()
        userService = UsuarioService(userRepository)
        return userService
    
    def test_post_usuario_ok(self, service):
        body_valido = {"nombre": "Victor", "edad": 20, "activo": True}
        respuesta = dispatch_request(service, "POST", "/usuarios", body_valido)
    