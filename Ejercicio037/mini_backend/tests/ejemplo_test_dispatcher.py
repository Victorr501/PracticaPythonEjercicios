import unittest
from app.dispatcher import dispatch_request
from app.service import UsuarioService
from app.repository import UsuarioRepository

class TestDispatcher(unittest.TestCase):
    def test_crear_usuario(self):
        repo = UsuarioRepository()
        servi = UsuarioService(repo)
        respuesta = dispatch_request(servi, "POST", "/usuarios", {"nombre": "Victor", "edad": 20, "activo": True})
        self.assertEqual(respuesta["status_code"], 201)
        self.assertIn("data", respuesta)
        self.assertIn("nombre", respuesta["data"])
        self.assertEqual(respuesta["data"]["nombre"], "Victor")
        
        
    def test_crear_usuario_duplicado(self):
        repo = UsuarioRepository()
        servi = UsuarioService(repo)
        dispatch_request(servi, "POST", "/usuarios", {"nombre": "Victor", "edad": 20, "activo": True})
        respuesta = dispatch_request(servi, "POST", "/usuarios", {"nombre": "Victor", "edad": 20, "activo": True})
        self.assertEqual(respuesta["status_code"], 409)
        self.assertIn("error", respuesta)
        self.assertEqual(respuesta["error"], "Usuario duplicado")

        
    def test_obtener_usaurio_existente(self):
        repo = UsuarioRepository()
        servi = UsuarioService(repo)
        dispatch_request(servi, "POST", "/usuarios", {"nombre": "Victor", "edad": 20, "activo": True})
        
        respuesta = dispatch_request(servi, "GET", "/usuarios/Victor")
        self.assertEqual(respuesta["status_code"], 200)
        self.assertIn("data", respuesta)
        self.assertIn("nombre", respuesta["data"])
        self.assertEqual(respuesta["data"]["nombre"], "Victor")
        
    def test_actualizar_usuario_existente(self):
        repo = UsuarioRepository()
        servi = UsuarioService(repo)
        dispatch_request(servi, "POST", "/usuarios", {"nombre": "Victor", "edad": 20, "activo": True})
        
        respuesta_put = dispatch_request(servi, "PUT", "/usuarios/Victor", {"edad": 30})
        self.assertEqual(respuesta_put["status_code"], 200)
        self.assertIn("data", respuesta_put)
        
        respuesta_get = dispatch_request(servi, "GET", "/usuarios/Victor")
        self.assertEqual(respuesta_get["status_code"], 200)
        self.assertEqual(respuesta_get["data"]["edad"], 30)
        
        
    def test_eliminar_usuario(self):
        repo = UsuarioRepository()
        servi = UsuarioService(repo)
        dispatch_request(servi, "POST", "/usuarios", {"nombre": "Victor", "edad": 20, "activo": True})
        
        respuesta_delete = dispatch_request(servi, "DELETE", "/usuarios/Victor")
        self.assertEqual(respuesta_delete["status_code"], 204)
        
        respuesta_get = dispatch_request(servi, "GET", "/usuarios/Victor")
        self.assertEqual(respuesta_get["status_code"], 404)
        self.assertIn("error", respuesta_get)
        self.assertEqual(respuesta_get["error"], "Usuario no encontrado")
        
    def test_ruta_no_encontra(self):
        repo = UsuarioRepository()
        servi = UsuarioService(repo)
        respuesta = dispatch_request(servi, "GET", "/ruta_inventada")
        self.assertEqual(respuesta["status_code"], 404)
        self.assertIn("error", respuesta)
        self.assertEqual(respuesta["error"], "Ruta no encontrada")
        