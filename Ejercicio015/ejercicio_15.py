# Debes trabajar con un archivo de texto llamado datos.txt
# 1 Usa with y open() para:
#   - Abrir (o crear si no existe) el archivo datos.txt en modo escritura
#   - Escribir al menos 3 líneas de texto en el archivo
# 2 Usa de nuevo with y open() para:
#   - Abrir el mismo archivo en modo lectura
#   - Leer todo su contenido
#   - Mostrar el contenido por pantalla

with open("Ejercicio015/datos.txt","w") as archivo:
    archivo.write("Hola mundo \n")
    archivo.write("Hola mundo \n")
    archivo.write("Hola mundo \n")

with open("Ejercicio015/datos.txt","r") as archivo:
    lineas = archivo.read()
    
print(lineas)