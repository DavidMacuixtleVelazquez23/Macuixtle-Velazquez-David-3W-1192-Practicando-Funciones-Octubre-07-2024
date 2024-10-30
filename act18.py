#Esto sirve para imprimir el nombre
# '\n' sirva para saltar lineas
print("\nMacuixtle Velazquez David\n")
#aqui se llama una funcion con parentesis
#pero teniendo '*,' obtendras error si tratas de usar un argumento posicional
def my_function(*, x):
  print(x)

my_function(3)