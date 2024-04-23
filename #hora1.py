#hora1
hora=int(input("ingrese la hora"))
minutos=int(input("ingrese los minutos"))
duracion=int(input("ingrese la duaracion"))
min_totales=minutos+duracion
hora_totales=min_totales//60
min_totales=min_totales%60
hora_totales=hora_totales%24
print("finalizara a las", hora_totales,",",min_totales)