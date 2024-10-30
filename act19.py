#Esto sirve para imprimir el nombre
# '\n' sirva para saltar lineas
print("\nMacuixtle Velazquez David\n")
#aqui se llama una funcion con parentesis
#para diferenciar de palabras clave y argumentos posicionales
#los argumentos posicinales llevan antes '/,' 
#las palabras clave llevan '*,'
def mi_function(a, b, /, *, c, d):
  print(a + b + c + d)

mi_function(5, 6, c = 7, d = 8)