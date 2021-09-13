# Punto 9. Leer 2 números; si son iguales que lo multiplique, si el primero es 
# mayor que el segundo que los reste y sino que los sume.

num_1 = int( input('Numero 1: ') )
num_2 = int( input('Numero 2: ') )

if( num_1 == num_2 ):
  total = num_1 * num_2
  print(f'Multiplicacion { total }')
elif( num_1 > num_2 ):
  total = num_1 - num_2
  print(f'Resta { total }')
else:
  total = num_1 + num_2
  print(f'Suma { total }')