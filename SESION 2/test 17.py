""" Diccionarios en Python """

""" del: eliminar un key y valor del diccionario """

var_1 = {"nombre": "Margarita", "edad": 27, "promedio": 15}

""" Para eliminar valores de nuestro diccionario vamos a usar a del delante de la variable """

del var_1["edad"]
del var_1["nombre"]

print(f"El diccionario actualizado tiene los siguientes valores: {var_1}")