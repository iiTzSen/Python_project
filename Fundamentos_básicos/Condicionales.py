"""
Exercise_1

Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.


edad = int(input("Introduce tu edad: "))

if edad > 17:
    print("Es mayor de edad")
elif edad < 18:
    print("Es menor de edad")
    
---------------------------------------------------------------------------------------------------------

Exercise_2

Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario
por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada 
en la variable sin tener en cuenta mayúsculas y minúsculas.


key = "contraseña"

password = input("Introduce la contraseña: ")

if key == password.lower():
    print("La contraseña si coincide")
else:
    print("La contrseña no coincide")

------------------------------------------------------------------------------------------------------------

Exercise_3

Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es 
cero el programa debe mostrar un error.


n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce otro número: "))

if n2 < 1:
    print("¡ERROR! No se puee dividir por 0.")
else:
    print("El resultado es: ",n1 / n2)

----------------------------------------------------------------------------------------------------------------

Exercise_4

Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.


n1 = int(input("Introduce un número: "))

if n1 % 2 == 0:
    print(f"{n1} es un número par.")
else:
    print(f"{n1} no es un número par")

-----------------------------------------------------------------------------------------------------------------

Exercise_5

Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a
1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por 
pantalla si el usuario tiene que tributar o no.


edad = int(input("Introduce tu edad: "))
ingresos = int(input("Introduce tus ingresos mensuales: "))

if edad > 16 and ingresos > 999:
    print("Tienes que tributar")
else:
    print("No tienes que tributar")
    
---------------------------------------------------------------------------------------------------------------------

Exercise_6

Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado
por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""

name = input("Introduce yu nombre: ")
sex = input("Introduce tu sexo: ")


