""" Diccionarios en Python """

var_1 = {"nombre": "Mysql", "tipo": "BD relacional"}

""" Convirtiendo diccionarios a lista """
var_2 = list(var_1)
print(f"Mi diccionario convertido es el siguiente:{var_2}")

var_1_values = list(var_1.values())
print(var_1_values)

keys = list(var_1.keys())
print(keys)

var_3 = list(var_1.items())
print(var_3)