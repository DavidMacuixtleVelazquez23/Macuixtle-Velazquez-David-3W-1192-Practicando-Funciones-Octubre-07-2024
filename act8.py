#Esto sirve para imprimir el nombre
# '\n' sirva para saltar lineas
print("\nMacuixtle Velazquez David\n")
#aqui se llama una funcion con parentesis
#aqui se tiene que agregar '**' antes del nombre del parametro
#esto se debe porque no se sabe si seran mas argumentos de palabra clave
def my_function(**kid):
  print("este es mi apellodo " + kid["lname"])

my_function(fname = "Agtto", lname = "Kibouto")