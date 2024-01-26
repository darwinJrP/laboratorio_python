""" Conversión de datos """
""" De string: str a enteros:int """

var1 = "700"
var2 = 333333
var3 = 3.1415926535897932384626
suma_1= var2 + var3
print(f"El valor de la suma_1 es: {suma_1}")
'''
Esta suma no es posible por ser un valor string y el otro entero
suma_2= var1 + var2
print(f"El valor de la suma_2 es: {suma_2}")
'''
suma_3 = int(var1) + var2
print(f"El valor de la suma_3 es: {suma_3}")

''' Suma de dos variables: int + float '''
suma_4 = var2 + var3
print(f"El valor de la suma_4 es: {suma_4}")

var4 = int(suma_4)
print(var4)

var1 = "700"
var2 = 333333
var3 = 3.1415926535897932384626

""" La suma de las tres variables como strings """
suma_5 = var1 + str(var2) + str(var3)
print (suma_5)