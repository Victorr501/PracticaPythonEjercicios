"""
Crea un archivo llamado ejercicio_2.py.

Debes simular una lista de tareas pendientes de un usuario.

Crea una lista con al menos 3 tareas (cadenas de texto).

Muestra por pantalla:

    La lista completa de tareas

    El número total de tareas

Añade una nueva tarea a la lista.

Elimina una tarea existente de la lista.

Muestra de nuevo:

    La lista actualizada

    El número total de tareas actualizado
"""

tareas_pendientes = ["Comprar pan", "Lavar casa", "Ir al gimnasio"]
print("Lista completa de tareas:")
print(tareas_pendientes)
print(f"Número total de tareas: {len(tareas_pendientes)}")

print("------------------------")
tareas_pendientes.append("Correr 10 km")
tareas_pendientes.remove("Lavar casa")

print("Lista actualizada:")
print(tareas_pendientes)
print(f"Número total de tareas actualizado: {len(tareas_pendientes)}")
