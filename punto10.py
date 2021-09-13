# Punto 10. Leer tres números diferentes e imprimir el número mayor de los 
# tres.

num_1 = int( input('Numero 1: ') )
num_2 = int( input('Numero 2: ') )
num_3 = int( input('Numero 3: ') )

if( num_1 > num_2 and num_1 > num_3 ):
  print( num_1 )
elif( num_2 > num_1 and num_2 > num_3 ):
  print( num_2 )
else:
  print( num_3 )