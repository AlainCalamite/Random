#Las tuples son una lista con datos inmutables (no van a cambiar), sriven para definir directorios o diccionarios
x = (1, 2, 3)
print(x)
print(type(x))   #Para imprimir que tipo de variable es
y = tuple((4, 5, 6))   #Para generar una tuple desde el generador 
print(dir(y))   #Para ver todo lo que se puede hacer con una tuple
z = (1,)   #Para crear una tuple de un solo elemento se debe de colocar la , 
print(z)
print(type(z))  #Para imprimir que tipo de variable es
print(x[1])  #Para solo imprimir un solo elemento de la tuple
# del  sirve para eliminar una tuple
del y
print(y)