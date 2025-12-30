# Parte 1 - Reutiliza / adapta código previo
# 1 Reutiliza estas piezas (puedes copiarlas del Ejercicio 31):
#   - Excepciones:
#       - DatosUsuarioInvalidosError
#       - UsuarioDuplicadoErro
#   - Y añade una nueva:
#       - UsuarioNoEncontradoError
#       - Docstring:"Se lanza cuando no existe un usaurio con ese nombre"
#   - Clases/funciones:
#       - Usaurio con to_dict
#       - usuario_desde_dict
#       - UsuarioRepository (debe tener agregar y añade buscar_por_nombre)
#       - UsuarioService(debe tener crear_usuario y añade obtener_usaurio(self, nombre))