horas=input("cuantas horas trabajas")
pago=input("cuanto cobra por hora")
horas_a_entero=int(horas)

pago_a_entero=int(pago)
resultado=horas_a_entero*pago_a_entero
print("tu pago es", resultado)

n=int(input("ingrese un numero entero"))
suma=n*(n+1)/2
print("la suma de los primeros enteros desde 1 hasta", str(n)+" es " + str(suma))

peso=input("indique su peso en kg")
estatura=input("ingrese su estatura en metros")
pesoentero=float(peso)
estaturaentero=float(estatura)
masacorporal=pesoentero / (estaturaentero*estaturaentero) 
print("tu masa corporal es", masacorporal)

cantidad=(input("bienvenido, cuanta cantidad desea invertir"))
interes_anual=(input("Cual es el porcentaje de interes anual"))
años_de_inversion=(input("Ingrese los años que lleva la inversion"))
inversion=int(cantidad)
interes=float(interes_anual)
cantidad_de_años=int(años_de_inversion)
interes_simple= (inversion*interes)*cantidad_de_años
print("la ganancia de inversion", interes_simple)


payasos=int(input("escriba la cantidad de payasos vendidos"))
muñecas=int(input("escriba la cantidad de muñecas vendidas"))
peso_muñeca=75
peso_payasos=112
peso_total_muñecas=muñecas*peso_muñeca
print("el peso total de las muñecas es", peso_total_muñecas)
peso_total_payasos=payasos*peso_payasos
print("el peso total de los payasos es", peso_total_payasos)
peso_de_pedido=(peso_total_payasos+peso_total_muñecas)
cantidad_total=payasos+muñecas
print("la cantidad de jugutes del pedido es", cantidad_total)
print("el peso total del pedido es", peso_de_pedido)

cantidad_depositada = int(input("Digite la cantidad de dinero depositada: "))

ahorros_año1 = cantidad_depositada * 1.04
ahorros_año2 = ahorros_año1 * 1.04
ahorros_año3 = ahorros_año2 * 1.04

print("Ahorros después del primer año:", round(ahorros_año1, 2))
print("Ahorros después del segundo año:", round(ahorros_año2, 2))
print("Ahorros después del tercer año:", round(ahorros_año3, 2))
