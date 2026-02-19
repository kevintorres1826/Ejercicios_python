from datetime import datetime

def registrar_movimiento(historial, tipo, monto):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    historial.append(f"{fecha} - {tipo}: ${monto}")

def consultar_saldo(saldo):
    print(f"Saldo actual: ${saldo}")

def retirar_dinero(saldo, historial):
    monto = float(input("Ingrese el monto a retirar: "))
    if monto <= saldo:
        saldo -= monto
        registrar_movimiento(historial, "Retiro", monto)
        print("Retiro exitoso.")
    else:
        print("Saldo insuficiente.")
    return saldo

def depositar_dinero(saldo, historial):
    monto = float(input("Ingrese el monto a depositar: "))
    saldo += monto
    registrar_movimiento(historial, "Depósito", monto)
    print("Depósito exitoso.")
    return saldo

def ver_historial(historial):
    print("\n--- HISTORIAL ---")
    if historial:
        for movimiento in historial:
            print(movimiento)
    else:
        print("No hay movimientos registrados.")

def menu():
    saldo = 0
    historial = []

    while True:
        print("\n--- CAJERO AUTOMÁTICO ---")
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Ver historial")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultar_saldo(saldo)
        elif opcion == "2":
            saldo = retirar_dinero(saldo, historial)
        elif opcion == "3":
            saldo = depositar_dinero(saldo, historial)
        elif opcion == "4":
            ver_historial(historial)
        elif opcion == "5":
            print("Gracias por usar el cajero. Hasta luego.")
            break
        else:
            print("Opción inválida.")

menu()