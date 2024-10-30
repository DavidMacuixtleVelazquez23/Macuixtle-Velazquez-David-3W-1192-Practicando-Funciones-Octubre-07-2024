#Esto sirve para imprimir el nombre
# '\n' sirva para saltar lineas
print("\nMacuixtle Velazquez David\n")
#aqui se llama una funcion con parentesis
#aqui se tiene que agregar '*' antes del nombre del parametro
#esto se debe porque no se sabe si seran mas argumentos
def mi_funcion(*fire):
    print("hols mi mejor amiga " + fire[1])
#aqui se ejecuta la funcion
mi_funcion("emil", "zoe","aris")