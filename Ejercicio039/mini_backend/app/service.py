from app.models import usuario_desde_dict, validar_update_usuario

class UsuarioService:
    def __init__(self, repo):
        self.repo = repo
    
    def crear_usuario(self, data):
        usuario = usuario_desde_dict(data)
        self.repo.agregar(usuario)
        return usuario.to_dict()
    
    def obtener_usuario(self, nombre):
        usuario = self.repo.buscar_por_nombre(nombre)
        return usuario.to_dict()
    
    def eliminar_usuario(self, nombre):
        self.repo.eliminar_por_nombre( nombre)
        return None
    
    def actualizar_usuario(self, nombre, data):
        validar_update_usuario(data)
        usuario = self.repo.actualizar_por_nombre(nombre, data)
        return usuario.to_dict()