"""

Exercise_1

Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas
el nombre del usuario tantas veces como el número introducido.



nombre = input("Introduce tu nombre: ")
x = int(input("Introduce un número: "))

print(nombre * x)

------------------------------------------------------------------------------------------------------------------------------------

Exercise_2

Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del
usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del 
nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.



nombre = input("Introduzca su nombre y sus apellidos: ")

print(nombre.lower(), nombre.upper(), nombre.title())

------------------------------------------------------------------------------------------------------------------------------------

Exercise_3

Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla
<NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.



nombre = input("Introduzca su nombre: ")

print(nombre.upper(), "tiene", len(nombre), "letras")

-------------------------------------------------------------------------------------------------------------------------------------

Exercise_4

Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la
extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este 
formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.



tel = input("introduce un número con el formato +xx-xxxxxxxxx-xx: ")

print("El número de telefono es ",  tel[4:-3])

-------------------------------------------------------------------------------------------------------------------------------------

Exercise_5

Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.


frase = input("Escribe una frase: ")

print(frase[::-1])

-------------------------------------------------------------------------------------------------------------------------------------

Exercise_6

Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma
frase pero con la vocal introducida en mayúscula.


frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minúscula: ")

print(frase.replace(vocal, vocal.upper()))

-------------------------------------------------------------------------------------------------------------------------------------

Exercise_7

Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con 
el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.



correo = input("Introduce tu correo electrónico: ")
print(correo[: correo.find("@")] + "@ceu.es")

------------------------------------------------------------------------------------------------------------------------------------

Exercise_8

Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número 
de euros y el número de céntimos del precio introducido.


precio = input("Introduce el precio con dos decimales: ")

print("Son ", precio[:precio.find(".")], "euros, y ", precio[precio.find(".")+1:], "céntimos")

-------------------------------------------------------------------------------------------------------------------------------------

Exercise_9

Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y
el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
"""

fecha = input("Introduce tu fecha de nacimiento con formato dd/mm/aaaa: ")


print("Uste nació el ", fecha[:2], "de ", fecha[3:5], "del año ", fecha[6:])
