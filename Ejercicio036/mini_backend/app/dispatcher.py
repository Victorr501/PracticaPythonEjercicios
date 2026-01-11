from app.endpoints import crear_usuario_endpoint, obtener_usuario_endpoint, actualizar_usuario_endpoint, eliminar_usuario_endpoint

def dispatch_request(service, method, path, body=None):
    prefijo = "/usuarios/"
    if method == "POST" and path == "/usuarios":
        return crear_usuario_endpoint(service, body)
    if method == "GET" and path.startswith(prefijo):
        nombre = path[len(prefijo):]
        return obtener_usuario_endpoint(service, nombre)
    if method == "PUT" and path.startswith(prefijo):
        nombre = path[len(prefijo):]
        return actualizar_usuario_endpoint(service, nombre, body)
    if method == "DELETE" and path.startswith(prefijo):
        nombre = path[len(prefijo):]
        return eliminar_usuario_endpoint(service, nombre)
    return {"status_code": 404, "error": "Ruta no encontrada"}