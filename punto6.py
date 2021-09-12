# Punto 6.  En una fábrica de computadoras se planea ofrecer a los clientes un 
# descuento que dependerá del número de computadoreas que 
# compre. Si las computadoras son menos de cinco se les dará un 10% 
# de descuento sobre el total de la compra; si el número de 
# computadoras es mayor o igual a cinco pero menos de diez se le 
# otorga un 20% de descuento; y si son 10 o más se les da un 40%. El 
# precio de cada computadora es de $11.000.

cantidad_comp = int( input('Cantidad de computadoras: ') )

total = float( cantidad_comp * 11000 )

if( cantidad_comp < 5 ):
  total_desc = float(total - ( total * 0.1 ))
  print(f'Total { total_desc }')

elif( cantidad_comp >= 5 and cantidad_comp < 10 ):
  total_desc = float(total - ( total * 0.2 ))
  print(f'Total { total_desc }')

elif( cantidad_comp >= 10 ):
  total_desc = float(total - ( total * 0.4 ))
  print(f'Total { total_desc }')