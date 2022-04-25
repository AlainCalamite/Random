from sqlite3 import DateFromTicks


product = {
   "name" : "book",
   "quantity" : 3,
   "price" : 4.99
}
person = {
    "first_name": "ryan",
    "last_name": "ray"
}
print(type(product))    #Para imprimir el tipo de dato que es
print(dir(person))      #Para imprimir el directorio del dict
print(person.keys())      #Para solo imprimir las claves del dict
print(person.items())    #Para solo imprimir los items del dict
person.clear()    #Para limpiar 
print(person)

products = [
    {"name" : 'book' , "price" : 9.99},
    {"name" : 'laptop' , "price" : 998.99}   #No olvidar colocar , cada vez que se cree una lista dentro de un dict
]

print(products)
