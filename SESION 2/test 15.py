lista_1 = []
lista_2 = []
print(f"El valor de mi lista_1 es: {lista_1}")
print(f"El valor de mi lista_2 es: {lista_2}")
lista_1.append("Darwin")
lista_1.append(20)
lista_1.append("astronauta")
lista_2.append("Roy")
lista_2.append(50)
lista_2.append("abogado")

print(f"Los valores actualizados de mi lista_1 son: {lista_1}")
print(f"Los valores actualizados de mi lista_2 son: {lista_2}")

suma_listas = lista_1 + lista_2
print(f"Los valores de suma_listas son los siguientes: {suma_listas}")

suma_listas.reverse()
print(f"Los valores inversos de la suma de listas son los siguientes: {suma_listas}")
del lista_1[1]
del lista_2[1]
print(f"El valor de mi lista_1 actualizada es: {lista_1}")
print(f"El valor de mi lista_2 actualizada es: {lista_2}")