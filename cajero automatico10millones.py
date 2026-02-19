from datetime import datetime

saldo = 10000000
historial = []  # aquí guardamos los movimientos

while True:
    print("\n--- CAJERO AUTOMÁTICO ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Ver historial")
    print("5. Salir")
    
    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("por favor ingrese un numero valido")
        continue
   
    if opcion == 1:
        print("Tu saldo actual es:", saldo)

    elif opcion == 2:
        deposito = int(input("Ingrese el monto a depositar: "))
        if deposito > 0:
            saldo += deposito
            historial.append(f"Depósito: +{deposito}")
            print("Depósito exitoso. Nuevo saldo:", saldo)
        else:
            print("El monto debe ser mayor a 0")

    elif opcion == 3:
        retiro = int(input("Ingrese el monto a retirar: "))
        if retiro > 0:
            if retiro <= saldo:
                saldo -= retiro
                historial.append(f"Retiro: -{retiro}")
                print("Retiro exitoso. Saldo restante:", saldo)
            else:
                print("Saldo insuficiente")
        else:
            print("El monto debe ser mayor a 0")

    elif opcion == 4:
        print("\n--- HISTORIAL DE MOVIMIENTOS ---")
        if len(historial) == 0:
            print("No hay movimientos registrados")
        else:
            for movimiento in historial:
                print(movimiento)

    elif opcion == 5:
        print("Gracias por usar el cajero") 
        break

else: 
        print("Opción no valida") 
    