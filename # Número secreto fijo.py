# Número secreto fijo
numero_secreto = 27

print("¡Adivina el número secreto entre 1 y 50!")

while True:
    intento = int(input("Ingresa tu intento: "))
    
    if intento < numero_secreto:
        print("Demasiado bajo. Intenta otra vez.")
    if intento > numero_secreto:
        print("Demasiado alto. Intenta otra vez.")
    if intento == numero_secreto:
        print("¡Felicidades! ¡Adivinaste el número secreto!")
        break
