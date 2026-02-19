from datetime import datetime

saldo = 10000000
historial = [] 

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
        print("Por favor ingrese un número válido")
        continue  
    
    if opcion == 1:
        print("Tu saldo actual es:", saldo)
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    elif opcion == 2:
        try:
            deposito = int(input("Ingrese el monto a depositar: "))
        except ValueError:
            print("Ingrese un número válido")
            continue

        if deposito > 0:
            saldo += deposito
            fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            historial.append(f" {fecha} - Depósito: +{deposito}")
            print("Depósito exitoso. Nuevo saldo:", saldo)
        else:
            print("El monto debe ser mayor a 0")

    elif opcion == 3:
        try:
            retiro = int(input("Ingrese el monto a retirar: "))
            fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        except ValueError:
            print("Ingrese un número válido")
            continue

        if retiro > 0:
            if retiro <= saldo:
                saldo -= retiro
                fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                historial.append(f" {fecha} - Retiro: -{retiro}")
        
                print("Retiro exitoso. Saldo restante:", saldo)
            else:
                print("Saldo insuficiente")
        else:
            print("El monto debe ser mayor a 0")

    elif opcion == 4:
        print("\n--- HISTORIAL DE MOVIMIENTOS ---")
        if len(historial) == 0:
            fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print("No hay movimientos registrados")
        else:
            for movimiento in historial:
                print(movimiento)

    elif opcion == 5:
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("Gracias por usar el cajero") 
        break 

    else: 
        print("Opción no válida")
