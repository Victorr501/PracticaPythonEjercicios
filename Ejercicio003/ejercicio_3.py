# 1 Crea una lista con 4 prioridades (Cadenas de texot)
# 2 Muestra por pantalla:
#   - La lista completa
#   - La primera prioridad
#   - La ultima prioridad usando indexación negativa
# 3 Modifica
#   - La segunda prioridad por un nuevo valor
#   - La ultima prioridad por otro nuevo valor
# 4 Muestra de nuevo la lista completa tras las modificaciones

lista_prioridades = ["alta", "media", "baja", "muy baja"]
print("Mostar prioridades")
print(lista_prioridades)
print(lista_prioridades[0])
print(lista_prioridades[-1])
print("--------------------")

lista_prioridades[1] = "media baja"
lista_prioridades[-1] = "muy muy baja" #Actualizacion, ya que si pones -1 siempre va a ser la ultima y si no sabes la longitud de la lista
print("Mostar la lista actualizada")
print(lista_prioridades)
