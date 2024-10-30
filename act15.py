#Esto sirve para imprimir el nombre
# '\n' sirva para saltar lineas
print("\nMacuixtle Velazquez David\n")
#aqui se llama una funcion con parentesis
#pero al agregar '/' obtendremos un error
def mi_funcion(x, /):
  print(x)

mi_funcion(x = 3)
