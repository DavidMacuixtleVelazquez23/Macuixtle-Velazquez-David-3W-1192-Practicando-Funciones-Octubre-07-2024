#Esto sirve para imprimir el nombre
# '\n' sirva para saltar lineas
print("\nMacuixtle Velazquez David\n")
#aqui se llama una funcion con parentesis
#si se desea especificar una funcion que solo pueda contener 
#argumentos de palabras clave se tiene que agregar '*,' despues de cada argumento
def mi_funcion(*,x):
    print(x)

mi_funcion(x=3)