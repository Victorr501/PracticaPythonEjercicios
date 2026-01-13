from app.errors import UsuarioNoEncontradoError, UsuarioDuplicadoError, DatosUsuarioInvalidosError

def crear_usuario_endpoint(service, data):
    try:
        resultado = service.crear_usuario(data)
        return {"status_code": 201, "data": resultado}
    except DatosUsuarioInvalidosError:
        return {"status_code": 400, "error":"Datos de usuario inválidos"}
    except UsuarioDuplicadoError:
        return {"status_code": 409, "error": "Usuario duplicado"}
    
def obtener_usuario_endpoint(service, nombre):
    try:
        usuario = service.obtener_usuario(nombre)
        return {"status_code": 200, "data": usuario}
    except UsuarioNoEncontradoError:
        return {"status_code": 404, "error": "Usuario no encontrado"}
    
def eliminar_usuario_endpoint(service, nombre):
    try:
        service.eliminar_usuario(nombre)
        return {"status_code": 204}
    except UsuarioNoEncontradoError:
        return {"status_code": 404, "error": "Usuario no encontrado"}
    
def actualizar_usuario_endpoint(service, nombre, data):
    try:
        usuario = service.actualizar_usuario(nombre, data)
        return {"status_code": 200, "data": usuario}
    except DatosUsuarioInvalidosError:
        return {"status_code": 400, "error": "Datos de usuario inválidos"}
    except UsuarioNoEncontradoError:
        return {"status_code": 404, "error": "Usuario no encontrado"}