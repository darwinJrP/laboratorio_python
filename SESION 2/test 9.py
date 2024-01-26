""" Listas en Python """

""" Listas (count): Cantidad de veces que aparece un elemento en una lista """
#Que valor es el que se está repitiendo y la cantidad de veces
var_1 = ["Python", "Java", "PHP", "Ruby", "JavaScript", "TypeScript"]

var_1.append("Python")
var_1.append("Python")
var_1.append("Python")
var_1.append("Node JS")

print(f"Mi lista actualizada es: {var_1}")

print("La cantidad de veces que se repite 'Python' es: {}" .format(var_1.count("Python")))