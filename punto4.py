#  Punto 4. Una fábrica ha sido sometida a un programa de control de 
# contaminación para lo cual se efectúa una revisión de los puntos de 
# contaminación generados por la fábrica. El programa de control de 
# contaminación consiste en medir los puntos que emite la fábrica en 
# cinco días de una semana y si el promedio es superior a los 170 
# puntos entonces tendrá la sanción de parar su producción por una 
# semana y una multa del 50% de las ganancias diarias cuando no se 
# detiene la producción. Si el promedio obtenido de puntos es de 170 o 
# menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica 
# desea saber cuanto dinero perderá después de ser sometido a la 
# revisión.

ganancias = float( input('Ganancias diarias: ') )
prom = int( input('Promedio de puntos: ') )

if( prom > 170 ):
  multa = float( ganancias * 0.5 )
  print(f'Valor de la multa es { multa }')
elif( prom < 170 ):
  print('No se paga ninguna multa ')