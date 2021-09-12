# Punto 5. Una persona se encuentra con un problema de comprar un automóvil 
# o un terreno, los cuales cuestan exactamente lo mismo. Sabe que 
# mientras el automóvil se devalúa, con el terreno sucede lo contrario. 
# Esta persona comprará el automóvil si al cabo de tres años la 
# devaluación de este no es mayor que la mitad del incremento del 
# valor del terreno. Ayúdale a esta pesona a determinar si debe o no 
# comprar el automóvil.

dinero = float( input('Dinero total: ') )
devalu = float( dinero * 0.07 )
increm = float( dinero * 0.10 )

if( devalu < ( increm / 2 ) ):
  print( 'Si compra el carro' )
else:
  print( 'No compra el carro' )