gastos = [0, 0, 0, 0, 0, 0, 0]  
# 0=lunes, 1=martes, 2=miercoles, 3=jueves, 4=viernes, 5=sabado, 6=domingo

while True:
    print("--- GASTOS SEMANALES ---")
    print("1. Agregar gasto")
    print("2. Ver gasto por día")
    print("3. Ver gasto total de la semana")
    print("4. Salir")
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        dia = input("Ingrese el día: ").lower()
        valor = int(input("Ingrese el gasto: "))

        if valor > 0:
            if dia == "lunes":
                gastos[0] += valor
            elif dia == "martes":
                gastos[1] += valor
            elif dia == "miercoles":
                gastos[2] += valor
            elif dia == "jueves":
                gastos[3] += valor
            elif dia == "viernes":
                gastos[4] += valor
            elif dia == "sabado":
                gastos[5] += valor
            elif dia == "domingo":
                gastos[6] += valor
            else:
                print("Día inválido")

    elif opcion == 2:
        dia = input("Ingrese el día a consultar: ").lower()

        if dia == "lunes":
            print("Gasto lunes:", gastos[0])
        elif dia == "martes":
            print("Gasto martes:", gastos[1])
        elif dia == "miercoles":
            print("Gasto miércoles:", gastos[2])
        elif dia == "jueves":
            print("Gasto jueves:", gastos[3])
        elif dia == "viernes":
            print("Gasto viernes:", gastos[4])
        elif dia == "sabado":
            print("Gasto sábado:", gastos[5])
        elif dia == "domingo":
            print("Gasto domingo:", gastos[6])
        else:
            print("Día inválido")

    elif opcion == 3:
        total = 0
        for gasto in gastos:
            total += gasto
        print("total gastado en la semana:", total)

    elif opcion == 4:
        print("Programa finalizado")
        break

    else:
        print("Opción no válida")
