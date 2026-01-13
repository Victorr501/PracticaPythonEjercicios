from app.errors import UsuarioDuplicadoError, UsuarioNoEncontradoError


class UsuarioRepository:
    def __init__(self):
        self._usuarios = []
        
    def agregar(self, usuario):
        for usuario_buscar in self._usuarios:
            if usuario.nombre == usuario_buscar.nombre:
                raise UsuarioDuplicadoError()
        self._usuarios.append(usuario)
        
    def buscar_por_nombre(self, nombre):
        for usuario_buscar in self._usuarios:
            if nombre == usuario_buscar.nombre:
                return usuario_buscar
        raise UsuarioNoEncontradoError()
    
    def eliminar_por_nombre(self, nombre):
        index = -1
        for usuario_buscar in self._usuarios:
            index += 1
            if nombre == usuario_buscar.nombre:
                return self._usuarios.pop(index)
        raise UsuarioNoEncontradoError()
    
    def actualizar_por_nombre(self, nombre, data):
        for usuario_buscar in self._usuarios:
            if nombre == usuario_buscar.nombre:
                if "edad" in data:
                    usuario_buscar.edad = data["edad"]
                if "activo" in data:
                    usuario_buscar.activo = data["activo"]
                return usuario_buscar
        raise UsuarioNoEncontradoError()