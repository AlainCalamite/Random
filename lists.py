#demo_list = [1, 'Hello', 2, 3, 4, 5, [1.34, True] ] #Se pueden crear listas con varios tipos de valores y listas dentro de las listas 
demo_list = [1, "Hello", 1.34, True, [1, 2, 3]]
colors = ['blue', 'yellow', 'black']
numbers_list = list(( 1, 2, 3, 4 ))  #Otra forma de crear listas
print(numbers_list)

#r = list(range(1, 10)) #Para crear un rango, se debe de tener en cuenta que comienza a contar a partir del 0 por eso de se debe agregar un numero mas  
r = list(range(1, 11))
print(r)
print(type(colors))  #Para saber que tipo de dato es la lista
print(dir(colors))   #Para saber todo lo que se puede hacer con una lista 
print(len(colors))   #Para saber cuantos elementos tiene la lista
print(len(demo_list))
print(colors[1])     #Para solo imprimir un solo valor de la lista
print(colors[-1])
print(colors[0])
print("blue" in colors)  #Para saber si un valor se encuentra en la lista
print("red" in colors)
print(colors)
colors [1] = "green"  #Para modificar un valor de la lista  (sustituir)
print(colors)
colors.append("violet")  #Para agregar un nuevo elemento a la lista 
colors.extend(["yellow", "purple"])  #Para agregar una lista y lo coloque como elementos independientes
colors.extend(["pink"])
colors.insert(1, "cyan")  #Para insertar otro elemento en un lugar en específico
colors.insert(len(colors), "white")  #Para insertarlo al final
print(colors)
colors.pop()   #Para quitar el último elemento agregado
colors.remove("pink")    #Para remover un caracter en específico
print(colors)
colors.sort()   #Para ordenar en orden alfabetico
print(colors)
colors.sort(reverse=True)   #Para ordenar en orden inverso
print(colors)
print(colors.index("green"))  #Para obter algún indice de la lista
print(colors.count("green"))  #Para saber cuantas unidades hay en la lista  de un elemento 