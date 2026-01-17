import pytest
from fastapi.testclient import TestClient
from app.api import get_service
from app.repository import UsuarioRepository
from app.service import UsuarioService
from main import app

@pytest.fixture
def client():
    repo = UsuarioRepository()
    service = UsuarioService(repo)
    
    def overrider_get_service():
        return service
    
    app.dependency_overrides[get_service] = overrider_get_service
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()

@pytest.fixture
def body_valido():
    return {"nombre": "Victor", "edad": 20, "activo": True}
    
def test_post_usuario_ok(body_valido, client):
    r = client.post("/usuarios", json=body_valido)
    assert r.status_code == 201
    data = r.json()
    assert data["nombre"] == "Victor"
    
def test_post_usuario_duplicado(body_valido, client):
    client.post("/usuarios", json=body_valido)
    r = client.post("/usuarios", json=body_valido)

    assert r.status_code == 409

def test_get_usuario_existente(body_valido, client):
    client.post("/usuarios", json=body_valido)
    r = client.get("/usuarios/Victor")

    assert r.status_code == 200
    assert r.json()["nombre"] == "Victor"
    

def test_get_usaurio_inexistente(client):
    r = client.get("/usuarios/Victor")
    assert r.status_code == 404

def test_put_usuario_existente_cambia_edad(body_valido, client):
    client.post("/usuarios", json=body_valido)
    r = client.put("/usuarios/Victor", json={"edad": 30})
    assert r.status_code == 200
    assert r.json()["edad"] == 30
    
def test_put_usuario_body_invalido_vacio(body_valido, client):
    client.post("/usuarios",json=body_valido )
    r = client.put("/usuarios/Victor", json={})
    assert r.status_code == 400
    
def test_delete_usuario_existente(body_valido, client):
    client.post("/usuarios", json=body_valido)
    r = client.delete("/usuarios/Victor")
    assert r.status_code == 204
    assert r.text == "" 
    
def test_delete_usuario_inexistente(client):
    r = client.delete("/usuarios/NoExiste")
    assert r.status_code == 404