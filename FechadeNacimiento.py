fecha1 = int(input("ingrese la fecha: "))
dia1 = fecha1 // 10000
mes1 = fecha1 % 10000
mes1 = mes1 // 100
year1 = fecha1 % 100

fecha2 = int(input("ingrese La fecha: "))
dia2 = fecha2 // 10000
mes2 = fecha2 % 10000
mes2 = mes2 // 100
year2 = fecha2 % 100


if year1 > 100 or year2 > 100 :
    print("Año Incorrecto")

elif(year1%4 == 0) and (year1%100 != 0) or (year1%400 == 0) or (year2%4 == 0) and (year2%100 != 0) or (year2%400 == 0): #Si es Bisiesto
    if mes1 <= 12 and mes2 <= 12:
        if (mes1 == 1 and dia1 <= 31) or (mes1 == 3 and dia1 <= 31) or (mes1 == 5 and dia1 <= 31) or (mes1 == 7 and dia1 <= 31) or (mes1 == 8 and dia1 <= 31) or (mes1 == 10 and dia1 <= 31) or (mes1 == 12 and dia1 <= 31) or (mes1 == 4 and dia1 <= 30) or (mes1 == 6 and dia1 <= 30) or (mes1 == 9 and dia1 <= 30) or (mes1 == 11 and dia1 <= 30) or (mes1 == 2 and dia1 <= 29):  #comparando meses con sus respectivos dias
            if (mes2 == 1 and dia2 <= 31) or (mes2 == 3 and dia2 <= 31) or (mes2 == 5 and dia2 <= 31) or (mes2 == 7 and dia2 <= 31) or (mes2 == 8 and dia2 <= 31) or (mes2 == 10 and dia2 <= 31) or (mes2 == 12 and dia2 <= 31) or (mes2 == 4 and dia2 <= 30) or (mes2 == 6 and dia2 <= 30) or (mes2 == 9 and dia2 <= 30) or (mes2 == 11 and dia2 <= 30) or (mes2 == 2 and dia2 <= 29):
                if year1 < year2:
                    print("La persona 1 es mayor que la persona 2")
                elif year1 == year2:
                    if mes1 < mes2:
                        print("La persona 1 es mayor que la persona 2")
                    elif mes1 > mes2:
                        print("La persona 2 es mayor que la persona 1")
                    elif mes1 == mes2:
                        if dia1 < dia2:
                            print("La persona 1 es mayor que la persona 2")
                    if dia1 > dia2:
                        print("La persona 2 es mayor que la persona 1")    
                elif year1 > year2:
                    print("La persona 2 es mayor que la persona 1")
            else:
                print("Dia Invalido Persona 2")        
        else:
            print("Dia invalido Persona 1")
    else:
        print("Mes invalido")

elif(year1%4 != 0) and (year1%100 == 0) or (year1%400 != 0) or (year2%4 != 0) and (year2%100 == 0) or (year2%400 != 0): #No es bisiesto
    if mes1 <= 12 and mes2 <= 12:
        if (mes1 == 1 and dia1 <= 31) or (mes1 == 3 and dia1 <= 31) or (mes1 == 5 and dia1 <= 31) or (mes1 == 7 and dia1 <= 31) or (mes1 == 8 and dia1 <= 31) or (mes1 == 10 and dia1 <= 31) or (mes1 == 12 and dia1 <= 31) or (mes1 == 4 and dia1 <= 30) or (mes1 == 6 and dia1 <= 30) or (mes1 == 9 and dia1 <= 30) or (mes1 == 11 and dia1 <= 30) or (mes1 == 2 and dia1 <= 28):  #comparando meses con sus respectivos dias
            if (mes2 == 1 and dia2 <= 31) or (mes2 == 3 and dia2 <= 31) or (mes2 == 5 and dia2 <= 31) or (mes2 == 7 and dia2 <= 31) or (mes2 == 8 and dia2 <= 31) or (mes2 == 10 and dia2 <= 31) or (mes2 == 12 and dia2 <= 31) or (mes2 == 4 and dia2 <= 30) or (mes2 == 6 and dia2 <= 30) or (mes2 == 9 and dia2 <= 30) or (mes2 == 11 and dia2 <= 30) or (mes2 == 2 and dia2 <= 28):
                if year1 < year2:
                    print("La persona 1 es mayor que la persona 2")
                elif year1 == year2:
                    if mes1 < mes2:
                        print("La persona 1 es mayor que la persona 2")
                    elif mes1 > mes2:
                        print("La persona 2 es mayor que la persona 1")
                    elif mes1 == mes2:
                        if dia1 < dia2:
                            print("La persona 1 es mayor que la persona 2")
                    if dia1 > dia2:
                        print("La persona 2 es mayor que la persona 1")    
                elif year1 > year2:
                    print("La persona 2 es mayor que la persona 1")
            else:
                print("Dia Invalido Persona 2")        
        else:
            print("Dia invalido Persona 1")
    else:
        print("Mes invalido")
