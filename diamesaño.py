def es_bisiesto(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

try:
    # Ingresa día, mes y año
    dia = int(input("Ingresa el día: "))
    mes = int(input("Ingresa el mes: "))
    year = int(input("Ingresa el año: "))

    if mes==1:
            if 1<=dia<31:
        print("Fecha válida.")

    if mes==2:
            if 2<=dia<29:
        print("Fecha válida.")  

    if mes==3:
            if 3<=dia<31:
        print("Fecha válida.")

    if mes==4:
            if 4<=dia<31:
        print("Fecha válida.")

    if mes==5:
            if 5<=dia<31:
        print("Fecha válida.")

    if mes==6:
            if 6<=dia<30:
        print("Fecha válida.")

    if mes==7:
            if 7<=dia<31:
        print("Fecha válida.")

    if mes==8:
            if 8<=dia<31:
        print("Fecha válida.")

    if mes==9:
            if 9<=dia<30:
        print("Fecha válida.")

    if mes==10:
            if 10<=dia<31:
        print("Fecha válida.")

    if mes==11:
            if 11<=dia<30:
        print("Fecha válida.")

    if mes==12:
            if 12<=dia<31:
        print("Fecha válida.")
        
    else:
    print("Fecha no válida. Ingresa valores dentro de los rangos permitidos.")

except ValueError:
    print("Error: Ingresa valores numéricos para día, mes y año.")