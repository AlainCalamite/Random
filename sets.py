#Set es una colección de datos de manera desordenada que no contiene un indice
colors = {"Red", "Green", "Blue"}
print(type(colors))  #Para saber el tipo de dato
print(colors)
print("Red" in colors)   #Para saber si se encuentra un dato en la lista
colors.add("Violet")     #Para agregar un nuevo elemento
print(colors)
colors.remove("Red")     #Para quitar un elemento 
print(colors)
colors.clear()  #Para limpiar todo el set 
print(colors)
del colors    #Para eliminar toda la lista
print(colors)
