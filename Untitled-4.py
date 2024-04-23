fecha = int(input("ingrese un numero: "))
dia = fecha // 10000
mes = fecha % 10000
mes = mes // 100
año = fecha % 100

print(dia,mes,año)


