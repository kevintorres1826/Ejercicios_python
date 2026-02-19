dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
gastos = [0, 0, 0, 0, 0, 0, 0]
while True:
    print("\n--- GASTOS SEMANALES ---")
    print("1. Agregar gasto")
    print("2. Ver gasto por día")
    print("3. Ver gasto total de la semana")
    print("4. Salir")
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        dia = input("Ingrese el día: ").lower()
        valor = int(input("Ingrese el gasto: "))
        if dia in dias:
            posicion = dias.index(dia)
            gastos[pos] += valor
        else:
            print("Día inválido")
    elif opcion == 2:
        dia = input("Ingrese el día a consultar: ").lower()

        if dia in dias:
            pos = dias.index(dia)
            print("Gasto de", dia, ":", gastos[pos])
        else:
            print("Día inválido")
    elif opcion == 3:
        total = 0
        for i in gastos:
            total += i 
        print("Total gastado en la semana:", total)
    elif opcion == 4:
        print("Programa finalizado")
        break
    else:
        print("Opción no válida")

