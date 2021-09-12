# Punto 1. Hacer un algoritmo que calcule el total a pagar por la compra de 
# camisas. Si se compran tres camisas o mas se aplica un descuento 
# del 30% sobre el total de la compra y si son menos de tres camisas 
# un descuento del 10%

camisas = int( input("Cantidad camisas: ") )
precio = float( input("Precio camisa: ") )

if( camisas >= 3 ):
  total = float(camisas * precio)
  des_total = float( total - ( total * 0.3 ) )
  print(F"Total a pagar { des_total }")
elif( camisas < 3 ):
  total = float(camisas * precio)
  des_total = float( total - ( total * 0.1 ) )
  print(F"Total a pagar { des_total }")
