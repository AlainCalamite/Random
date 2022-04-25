myStr = "Hello World"

# print(dir(myStr))
print(myStr.upper()) #Todo Mayusculas
print(myStr.lower()) #TodoMinusculas
print(myStr.swapcase()) #intercala una letra mayuscula y una minuscula 
print(myStr.capitalize())  #Primer letra de cada palabra la coloca en mayuscula
print(myStr.replace("Hello", "Bye")) #Para remplazar una palabra
print(myStr.replace("Hello", "Bye").upper()) #(Metodos encadenados)Un metodo va dentro de otro
print(myStr.count(" ")) #Para contar cuantos caracteres hay 
print(myStr.startswith("hola")) #Para preguntar si se inicia con
print(myStr.startswith("Hello")) 
print(myStr.endswith("hola")) #Para preguntar si se iniciafinaliza con
print(myStr.endswith("ld"))
print(myStr.split())  #Para separar, a partir de un caracter dentro del ()
print(myStr.find("o"))  #Para buscar un caracter dentro de una cadena 
print(myStr.find("d"))
print(len(myStr))  #Para contar todos los caracteres (longitud)
print(myStr.index("e"))  #Para saber en indice de un caracter 
print(myStr.isnumeric()) #Para saber si es numerico
print(myStr.isalpha())   #Para saber si es alfanumerico
print(myStr[6])    #Para imprimir solo un caracter
print(myStr[0])
print(myStr[-1])   #Para imprimir solo un caracter, orden inverso
print(myStr[-5])
print("Hola " + myStr) #Para concatenar 
print(f"Hola {myStr} :)")  #Concatenar de otra forma
print(" :) Hola {0}".format(myStr))  #Otra forma de concatenar