#impuesto
ingresos=float(input("ingrese la cantidad cantidad"))
if ingresos<85528.0:
 impuesto=ingresos*0.18-556.2
else:
 impuesto=ingresos*0.32+14839.2
print("total a pagar",impuesto)

