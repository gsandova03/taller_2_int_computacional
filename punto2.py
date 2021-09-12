# Punto2. En un supermercado se hace una promoción, mediante la cual el 
# cliente obtiene un descuento dependiendo de un número que se 
# escoge al azar. Si el número escogido es menor que 74 el descuento 
# es del 15% sobre el total de la compra, si es mayor o igual a 74 el 
# descuento es del 20%. Obtener cuanto dinero se le descuenta.

valor_compra = float( input('Valor compra: ') )
num = int( input('Numero al azar entre 1 - 100: ') )

if( num < 74 ):
  descuento = float( valor_compra * 0.15 )
  print(f' valor compra: { valor_compra }, descuento total { descuento } ')
elif( num >= 74 ):
  descuento = float( valor_compra * 0.2 )
  print(f' valor compra: { valor_compra }, descuento total { descuento } ')