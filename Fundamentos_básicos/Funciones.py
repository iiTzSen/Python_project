"""
def bienvenida():
    print("Bienvenido a python")
    
bienvenida()
---------------------------------------------------------------------------
def bienvenida():
    nombre = input("Introduce tu nombre: ")
    print(f"Bienvenido a python {nombre.title()}")
    
bienvenida()

---------------------------------------------------------------------------
def actividades_realizadas(actividades):
    if actividades:
        return actividades[-1]
    else:
        return "No hay registro de actividades"

actividades = ("Correr", "Jugar", "Luchar", "Volar")
ultima_actividad = actividades_realizadas(actividades)
print("La última actividad a sido: ", ultima_actividad)

---------------------------------------------------------------------------

def juan(n1):
    if n1 == 1 or n1 == 0:
        return 1
    else: 
        return n1 * juan(n1-1)
n1 = int(input("Introduce un número: "))
print(f"El factorial de {n1} es: {juan(n1)}")

---------------------------------------------------------------------------
""" 
porcentaje_iva = input("Introduce IVA: ")
valor_siniva = float(input("Introduce el valor sin IVA: "))

def invoice(amount, vat):
    return amount + amount*vat/100

print(invoice(valor_siniva,porcentaje_iva))