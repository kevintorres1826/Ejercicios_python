num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if num1 > num2:
    print("El primer número es mayor.")
else:
    if num1 < num2:
        print("El segundo número es mayor.")
    else:
        print("Los dos números son iguales.")