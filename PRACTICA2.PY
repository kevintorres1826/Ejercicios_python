print("hola mundo")
print("al final de mi cuadra hay un paradero")
print("alli me subo en el alimentador 9-9")
print("que me deja en el portal de las americas")
print("en el portal me subo al A61, el cual siempre esta lleno de gente con mi mismo estrato y es una mamera porque nunca me puedo sentar y me tocair parado")
print("el cual me trae hasta la estacion las flores-area andina")
print("--------------------------------------------------------------------")
print("despues de hechar 1 hora de ping pong con gente que no conozoco me voy de vuelta a la estacion area-andina y me subo el F19 el cual me lleva hasta la estacion de BANDERAS, el cual es una mrd, pero fui afortunado de nacer pobre, en vez de esos hp que andan en moto")
print("alli puedo hacer transbordo a 3 trasmilenios F23, F32, F60")
print("los cuales, siempre se suben a vender cualquier pendejada pero me lleva devuelta al portal de las americas")
print("y denuevo me subo al 9-9 que me deja cerca de mi casa, donde invaden mi espacio personal y me dan ganar de meter codasos")
print("gracias por leer, besos en esas nalgas")

precio_pan=500
pan_comprado=5000
pan_consumido=3000
lo_que_queda=pan_comprado-pan_consumido
print("lo que queda de pan es", lo_que_queda)

#planea una salida, vas al cine con tu pareja, crea variables para costos de entradas, costos de combos, tiempo de la pelicula, 
#tiempo de llegada al cine, y tiempo de llegada a la casa GASTO TOTAL Y TIEMPO TOTAL
print("--------------------------------------------------------")

print("Hola vamos a calcular el tiempo y el costo de tu salida al cine")
Tiempo_llegada_cine=int(input("en cuantos minutos llegaste al cine"))
Tiempo_pelicula=int(input("cuanto es la duracion de la pelicula en minutos"))
Tiempo_llegada_casa=int(input("cuantos minutos tardaste llendo del cine a la casa"))
costo_entrada=float(input("cuanto costaron las entradas"))
costo_combo=float(input("cual es el costo de el combo que pidieron"))
entradas=costo_entrada*2
gasto_total=costo_combo+entradas
tiempo_total=Tiempo_llegada_cine+Tiempo_pelicula+Tiempo_llegada_casa
print("tu costo total de tu salida el cine fue de ", gasto_total)
print("tu tiempo total de tu salida al cine fue de ", tiempo_total, " minutos")

print("-------------------------------------------------------")
presupuesto=int(input("cual es tu presupuesto para salir"))
if presupuesto < 60000:
    print("no le alcanza para salir eres un pobre muy desocupado, le alcanza para las entradas pero no para el combo, trabaje mk")
else: 
    print("si le alcanza para ir al cine sigue asi bro")

print("--------------------------------------------------------")
semana=["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
def puedes_salir(dia):
    if dia == "sabado" or dia=="domingo":
        print("puedes salir", dia)
    else: print("no puedes salir", dia)
for dia in semana:
    puedes_salir(dia)
    