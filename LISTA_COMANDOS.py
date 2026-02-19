# ===============================
# VARIABLES Y ENTRADAS
# ===============================
nombre = input("Ingrese nombre: ")
edad = int(input("Ingrese edad: "))
nota = float(input("Ingrese nota: "))


# ===============================
# CONDICIONALES (if / elif / else)
# ===============================
if edad >= 18:
    print("Mayor de edad")
elif edad >= 0:
    print("Menor de edad")
else:
    print("Edad inválida")


# ===============================
# OPERADORES ARITMÉTICOS
# ===============================
suma = 5 + 3
resta = 5 - 3
multiplicacion = 5 * 3
division = 5 / 3
division_entera = 5 // 3
modulo = 5 % 3
potencia = 5 ** 2


# ===============================
# COMPARADORES
# ===============================
# == igual
# != diferente
# > mayor
# < menor
# >= mayor o igual
# <= menor o igual


# ===============================
# OPERADORES LÓGICOS
# ===============================
# and  or  not


# ===============================
# STRINGS (texto)
# ===============================
texto = "Hola Mundo"

texto = texto.lower()      # pasar a minúsculas
texto = texto.upper()      # pasar a mayúsculas
texto = texto.capitalize() # primera letra en mayúscula
texto = texto.strip()      # quitar espacios
longitud = len(texto)      # tamaño del texto


# ===============================
# RECORRER TEXTO LETRA POR LETRA
# ===============================
for letra in texto:
    print(letra)


# ===============================
# AISLAR LETRAS
# ===============================
letras = ""
for c in texto:
    if c.isalpha():
        letras += c


# ===============================
# AISLAR NÚMEROS DE UN TEXTO
# ===============================
numeros = ""
for c in texto:
    if c.isdigit():
        numeros += c


# ===============================
# CONTAR VOCALES
# ===============================
contador_vocales = 0
for l in texto.lower():
    if l in "aeiou":
        contador_vocales += 1


# ===============================
# LISTAS
# ===============================
lista = [1, 2, 3, 4, 5]

lista.append(6)        # agregar
lista.remove(3)        # eliminar por valor
lista.pop()            # eliminar último
lista.pop(0)           # eliminar por posición
lista.sort()           # ordenar
lista.reverse()        # invertir
tamano = len(lista)    # tamaño


# ===============================
# RECORRER LISTAS
# ===============================
for n in lista:
    print(n)


# ===============================
# PAR O IMPAR
# ===============================
if n % 2 == 0:
    print("Par")
else:
    print("Impar")


# ===============================
# SEPARAR PARES E IMPARES
# ===============================
pares = []
impares = []

for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)


# ===============================
# SUMAR TODOS LOS VALORES
# ===============================
total = 0
for n in lista:
    total += n


# ===============================
# SUMAR CON CONDICIÓN
# ===============================
total = 0
for n in lista:
    if n > 10:
        total += n


# ===============================
# CONTAR CON CONDICIÓN
# ===============================
contador = 0
for n in lista:
    if n % 2 != 0:
        contador += 1


# ===============================
# PROMEDIO
# ===============================
suma = 0
for n in lista:
    suma += n
promedio = suma / len(lista)


# ===============================
# MAYOR Y MENOR DE UNA LISTA
# ===============================
mayor = lista[0]
menor = lista[0]

for n in lista:
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n


# ===============================
# WHILE
# ===============================
i = 0
while i < 5:
    print(i)
    i += 1


# ===============================
# WHILE TRUE
# ===============================
while True:
    opcion = input("Ingrese salir para terminar: ")
    if opcion == "salir":
        break


# ===============================
# DÍAS Y GASTOS (LISTAS PARALELAS)
# ===============================
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
gastos = [0, 0, 0, 0, 0, 0, 0]

dia = "martes"
valor = 5000

if dia in dias:
    pos = dias.index(dia)
    gastos[pos] += valor


# ===============================
# DICCIONARIOS
# ===============================
persona = {
    "nombre": "Kevin",
    "edad": 18
}

persona["edad"] += 1


# ===============================
# RECORRER DICCIONARIO
# ===============================
for clave in persona:
    print(clave, persona[clave])