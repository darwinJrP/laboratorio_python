""" Listas en Python """

""" Listas (del): Eliminar un valor indicando el índice del valor en la lista """

paises = []
paises.append("Perú")
paises.append("Brasil")
paises.append("Canadá")
paises.append("España")
paises.append("Chile")

print(f"Los valores de mi lista de paises son: {paises}")

del paises[2]

print(f"Mi lista actualizada tiene los siguientes valores: {paises}")
