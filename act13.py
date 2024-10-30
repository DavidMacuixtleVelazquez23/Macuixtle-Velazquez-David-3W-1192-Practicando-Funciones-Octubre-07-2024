#Esto sirve para imprimir el nombre
# '\n' sirva para saltar lineas
print("\nMacuixtle Velazquez David\n")
#aqui se llama una funcion con parentesis
#aqui se espesifica una funcion que solo puede tener argumentos posicionales
#esto agregandpo ',/' desúes del argumento
def ni_funcion(x,/):
    print(x)

ni_funcion(3)