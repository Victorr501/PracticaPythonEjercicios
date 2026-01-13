import pytest
from app.dispatcher import dispatch_request
from app.service import UsuarioService
from app.repository import UsuarioRepository


@pytest.fixture
def service():
    userRepository = UsuarioRepository()
    userService = UsuarioService(userRepository)
    return userService

@pytest.fixture
def body_valido():
    return {"nombre": "Victor", "edad": 20, "activo": True}
    
def test_post_usuario_ok(service, body_valido):
    respuesta = dispatch_request(service, "POST", "/usuarios", body_valido)
    assert respuesta["status_code"] == 201
    assert "data" in respuesta
    assert respuesta["data"]["nombre"] == "Victor"
    
def test_post_usuario_duplicado(service, body_valido):
    dispatch_request(service, "POST", "/usuarios", body_valido)
    respuesta = dispatch_request(service, "POST", "/usuarios", body_valido)
    assert respuesta["status_code"] == 409
    assert respuesta["error"] == "Usuario duplicado"

def test_get_usuario_existente(service, body_valido):
    dispatch_request(service, "POST", "/usuarios", body_valido)
    respuesta = dispatch_request(service, "GET", "/usuarios/Victor")
    assert respuesta["status_code"] == 200
    assert respuesta["data"]["nombre"] == "Victor"
    
def test_put_usuario_actualizar(service, body_valido):
    dispatch_request(service, "POST", "/usuarios", body_valido)
    respuesta_PUT = dispatch_request(service, "PUT", "/usuarios/Victor", {"edad": 30})
    respuesta_GET = dispatch_request(service, "GET", "/usuarios/Victor")
    assert respuesta_PUT["status_code"] == 200
    assert respuesta_GET["data"]["edad"] == 30
    
def test_delete_usaurio(service, body_valido):
    dispatch_request(service, "POST", "/usuarios", body_valido)
    respuesta_DELETE = dispatch_request(service, "DELETE", "/usuarios/Victor")
    respuesta_GET = dispatch_request(service, "GET", "/usuarios/Victor")
    assert respuesta_DELETE["status_code"] == 204
    assert respuesta_GET["status_code"] == 404
    assert respuesta_GET["error"] == "Usuario no encontrado"
   
def test_ruta_no_encontrada_simple(service):
    respuesta = dispatch_request(service, "PUT", "/ruta_inventada")
    assert respuesta["status_code"] == 404
    assert respuesta["error"] == "Ruta no encontrada"
     
@pytest.mark.parametrize("method, path", [
    ("GET", "/nope"),
    ("POST", "/nope"),
    ("PUT", "/usuarios"),
    ("DELETE", "/usuarios")
])   
def test_ruta_no_encontrada(service, method, path):
    respuesta = dispatch_request(service, method, path)
    assert respuesta["status_code"] == 404
    assert respuesta["error"] == "Ruta no encontrada"
    
