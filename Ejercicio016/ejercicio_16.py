# Parte 1 - Escritura de JSON
# 1 Crea un diccionario que represente un usuario con las claves:
#   - "nombre" --> Cadena de texto
#   - "edad" --> número entero
#   - "activo" --> booleano
# 2 Usar with y open() para:
#   - Abrir (o crear) el archivo usaurio.json en modo escritura
#   - Guardar el diccionario en el archivo usando json.dump()

# Parte 2 - Escritura de JSON
# 3 Usa with y open() para:
#   - Abrir el archivo usuario.json en modo lectura
#   - Cargar el contenido usando json.load()
# 4 Muestra por pantalla:
#   - El diccionario completo leído del archivo
#   - El valor de la clave "nombre"
import json # Se tiene que importar para trabajar con json

dicionario_usuarios = {"nombre": "Victor", "edad": 20, "activo": True}

with open("Ejercicio016/usuario.json", "w") as archivo:
    json.dump(dicionario_usuarios, archivo, indent=1)
    
with open("Ejercicio016/usuario.json", "r") as archivo:
    datos = json.load(archivo)
    print(datos)
    print(datos["nombre"])
    