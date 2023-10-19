"""
Tipos de datos simples

Exercise_1

Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
"""

print("Hola Mundo")

"""
--------------------------------------------------------------------

Exercise_2

Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y 
luego muestre por pantalla el contenido de la variable.
"""

Saludo = "Hola Mundo"

print(Saludo)

"""
--------------------------------------------------------------------

Exercise_3

Escribir un programa que pregunte el nombre del usuario en la consola y 
después de que el usuario lo introduzca muestre por pantalla la cadena
¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
"""

nombre = input("Escriba su nombre: ")

print("¡Hola ", nombre, "!")

"""
---------------------------------------------------------------------

Exercise_4

Escribir un programa que muestre por pantalla el resultado de la
siguiente operación aritmética.
"""

print(((3 + 2) / (2 * 5)) ** 2)

"""
---------------------------------------------------------------------

Exercise_5

Escribir un programa que pregunte al usuario por el número de horas trabajadas
y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
"""

horas = int(input("Introduce tus horas trabajadas: "))
coste = float(input("Introduce pago por hora: "))

print("Te corresponden ", horas * coste,"euros")

"""
---------------------------------------------------------------------

Exercise_6

Escribir un programa que lea un entero positivo, 
,introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta
La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
"""


n = int(input("Introduce valor de n: "))

print("La suma de todos los enteros de 1 hasta ", n , "es", (n * (n + 1)) / 2)

"""
----------------------------------------------------------------------

Exercise_7

Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, 
y muestre por pantalla la frase Tu índice de masa corporal es <imc> 
donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
"""

altura = float(input("Introduce tu estatura en m: "))
peso = int(input("Introduce tu peso en kg: "))

print("Tu IMC es de:", round((peso / (altura ** 2)), 2))

"""
----------------------------------------------------------------------

Exercise_8

Escribir un programa que pida al usuario dos números enteros y muestre
por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde 
<n> y <m> son los números introducidos por el usuario, y <c> y <r> son 
el cociente y el resto de la división entera respectivamente.
"""

n1 = int(input("Introduce un número: "))
n2 = int(input("Introduzca otra número: "))

print("El cociente de la división ",n1, " entre ",n2, " es ", int(n1 / n2),"," " y el resto es ", n1 % n2)

"""
----------------------------------------------------------------------

Exercise_9

Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
"""

n1 = int(input("Introduzca la cantidad a invertir: "))
n2 = float(input("Introduzca el interes anual de la inversión: "))
n3 = int(input("El número de años de la inversión: "))

total = (n1 + (((n2 / 100) * n1) * n3 )) #Interés simple

print("El capital total de la inversión después de ", n3, " años, es de ", total) 

"""
-----------------------------------------------------------------------

Exercise_10

Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada
paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada 
paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa 
que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso 
total del paquete que será enviado.
"""

payasos = int(input("Número de payasos:"))
munecas = int(input("Número de muñecas: "))

print("El peso total del paquete es de ", (112 * payasos) + (75 * munecas)," g")

"""
-----------------------------------------------------------------------

Exercise_11

Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de 
interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales 
de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa
que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
introducida por el usuario. Después el programa debe calcular y mostrar por pantalla
la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad
a dos decimales.
"""

cantidad = float(input("Cantidad a introducir: "))

a1 = cantidad + (0.04 * cantidad)
a2 = a1 + (0.04 * a1)
a3 = a2 + (0.04 * a2)

print("El primer año: ",round(a1, 2), ".  El segundo año: ",round(a2, 2) , ".  El tercer año: ",round(a3, 2))

"""
------------------------------------------------------------------------

Exercise_12

Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el
día tiene un descuento del 60%. Escribir un programa que comience leyendo 
el número de barras vendidas que no son del día. Después el programa debe
mostrar el precio habitual de una barra de pan, el descuento que se le
hace por no ser fresca y el coste final total.
"""

barras = int(input("Número de barras vendidas: "))
barraf = 3.49

print("PRECIO: ",barraf)
print("El descuento es del 60%")
print("Total: ", round(((barraf - (0.60 * barraf)) * barras), 2), "€")

