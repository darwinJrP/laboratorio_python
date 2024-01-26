"""
Crear 3 variables: nombre edad o distrito.
Requisitos:
-Nombre: string
-edad: int
-distrito: string
-Concatenar estos 2 datos e indicar una oración como la siguiente:
x tiene x años y es de "distrito"
-Obtener el modulo de su edad al usarlo con el numero 5

"""
nombre = "Darwin"
edad = 20
distrito = "Callao"
modulo = edad % 5
#residuo
print(f"{nombre} tiene {edad} años y es de {distrito}")
print(f"El modulo de la edad al usarlo con el numero 5 es: {modulo}")
