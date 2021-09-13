# Punto 8. Una empresa quiere hacer una compra de varias piezas de la misma 
# clase a una fábrica de refacciones. La empresa, dependiendo del 
# monto total de la compra, decidirá que hacer para pagar al fabricante. 
# Si el monto total de la compra excede de $500.000 la empresa tendrá 
# la capacidad de invertir de su propio dinero un 55% del monto de la 
# compra, pedir prestado al banco un 30% y el resto lo pagará 
# solicitando un crédito al fabricante. Si el monto total de la compra no 
# excede de $500.00 la empresa tendrá capacidad de invertir de su 
# propio dinero un 70% y el restante 30% lo pagará solicitando crédito 
# al fabricante. El fabricante cobra por concepto de interes un 20% 
# sobre la cantidad que se le pague a crédito. Obtener la cantidad a 
# inverir, valor del préstamo, valor del crédito y los intereses.

monto = float( input('Monto total: ') )

if( monto > 500000 ):
  inver_emp = float( monto * 0.55 )
  pres_banco = float( monto * 0.3 )
  cred_fabric = float( monto * 0.15 )
  interes_fabri = float( cred_fabric * 0.2 )
  print(F'Inversion: { inver_emp }, prestamo: { pres_banco }, credito a fabricante: { cred_fabric } e interes { interes_fabri }')
else:
  inver_emp = float( monto * 0.7 )
  cred_fabric = float( monto * 0.3 )
  interes_fabri = float( cred_fabric * 0.2 )
  print(F'Inversion: { inver_emp }, credito a fabricante: { cred_fabric } e interes { interes_fabri }')