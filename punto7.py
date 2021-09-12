# Punto 7. Un proveedor de estéreos ofrece un descuento del 10% sobre el 
# precio sin IVA, de algún aparato si este cuesta $2000 o más. Además, 
# independientemente de esto, ofrece un 5% de descuento si la marca 
# es NOSY. Determinar cuanto pagará, con IVA incluido, un cliente 
# cualquiera por la compra de su aparato. IVA es del 16%.

precio = float( input('Valor del estereo: ') )
tipo = int( input( '1. NOSY, 2.Cualquiera: ' ) )

if( tipo == 1 ):
  if( precio >= 2000 ):
    total = precio - ( precio * 0.15 )
    total_iva = total + ( precio * 0.16 )
    print(f'Precio final { total_iva }')
  else:
    total = precio - ( precio * 0.05 )
    total_iva = total + ( precio * 0.16 )
    print(f'Precio final { total_iva }')
else:
  if( precio >= 2000 ):
    total = precio - ( precio * 0.1 )
    total_iva = total + ( precio * 0.16 )
    print(f'Precio final { total_iva }')
  else:
    total_iva = precio + ( precio * 0.16 )
    print(f'Precio final { total_iva }')