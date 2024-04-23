#año bisiesto
bisiesto= int(input("ingrese año:"))
if (bisiesto%4==0):
 (bisiesto%100==0) and (bisiesto%400==0)

if  (bisiesto%4==0) and (bisiesto% 100 !=0):
    print("el año:", bisiesto,"es un año bisiesto")
else:
    print("el año no es bisiesto")      