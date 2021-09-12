# Punto 3. Una compañía de seguros está abriendo un departamento de 
# finanzas y estableció un programa para captar clientes, que conssite 
# en lo siguiente: Si el monto por el que se efectúa la fianza es menor 
# que $50.000 la cuota a pagar será por el 3% del monto, y si el monto 
# es mayor que $50.000 la cuota a pagar será el 2% del monto. La 
# afianzadora desea determinar cual será la cuota que debe pagar al 
# cliente.

monto = float( input('Monto de la fianza: ') )

if( monto < 50000 ):
  pago = float( monto * 0.03 )
  print(f' La cuota de pago es del 3%, el valor es { pago } ')
elif( monto > 50000 ):
  pago = float( monto * 0.02 )
  print(f' La cuota de pago es del 2%, el valor es { pago } ')