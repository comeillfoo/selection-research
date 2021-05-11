from shell import *
from collections import OrderedDict
import numpy as np
import matplotlib.pyplot as plt
from math import log
def draw_array( X, Y ):
  plt.plot( X, [ y for y in Y.values() ], 'r-', label='y = f( x )' )
def Mx( Y ):
  sum = 0
  for key in Y.keys():
    sum += Y[ key ] * key
  return sum
def Dx( Y ):
  YY = { key * key: 0 for key in Y.keys() }
  for key in Y.keys():
    YY[ key * key ] += Y[ key ]
  return Mx( YY ) - Mx( Y )**2
def gen( Y ):
  X = [ 0 ]
  p = 0
  for key in Y.keys():
    p += Y[ key ]
    X.append( p )
  Y = list( Y.keys() )
  def F( x ):
    i = 0
    while i < len( Y ) and x > Y[ i ]:
      i += 1
    if i >= len( Y ):
      return 1
    else:
      return X[ i ]  
  return F
def main():
  try:
    X = extract_nodes()
    Y = { x: 0 for x in X }
    for x in X:
      Y[ x ] += 1
    for key in Y.keys():
      Y[ key ] /= len( X )
    Y = OrderedDict( sorted( Y.items() ) )
    _X = X
    _X.sort()
    print( f'Вариационный ряд: {_X}' )
    print( '+---------------+------------+' )
    print( '| x             | p( x )     |' )
    print( '+---------------+------------+' )
    for key in Y.keys():
      print( f'|{ float_format( key ) }\t|{ float_format( Y[ key ] )} |' )
      print( '+---------------+------------+' )
    mx = max( X )
    mn = min( X )
    R = mx - mn
    print( f'\nЭкстремальные значения: [ Макс. { mx }; Мин. { mn }; R = { R } ]\n' )
    print( f'Mx = { Mx( Y ) }; S = { Dx( Y )**(0.5) }' )
    F = gen( Y )
    Xs = np.arange( mn - 2, mx + 2, 1e-2 )
    Ys = { x: F( x ) for x in Xs }
    draw_array( Xs, Ys )
    plt.ylabel( 'y', horizontalalignment='right', y=1.05, rotation=0 )
    plt.xlabel( 'x', horizontalalignment='right', x=1.05 )
    plt.legend()
    h = ( mx - mn ) / ( 1 + log( len( X ) ) / log( 2 ) )
    print( f'Число интервалов: {round(1 + log( len( X ) ) / log( 2 ), 0)}' )
    print( f'h = {h}' ) 
    polyx = mn - h / 2
    polyy = {}
    print( 'Интервальный ряд:' )
    while polyx <= mx:
      print( f'[ {round(polyx, 4)}; {round( polyx + h, 4)} ):', end=' ' )
      p = 0
      for y in Y.keys():
        if y >= polyx and y < polyx + h:
          p += Y[ y ]
      polyx += h
      polyy[ polyx - h / 2 ] = p
      print( f'{round(p, 4)}' )
    fig, ax = plt.subplots()
    ax.plot( list( polyy.keys() ), list( polyy.values() ) )
    ax.set_ylabel( 'p(x)', horizontalalignment='right', y=1.05, rotation=0 )
    ax.set_xlabel( 'x', horizontalalignment='right', x=1.05 )
    a = np.array( X )
    bins = []
    strt = mn - h / 2
    while strt <= mx + h / 2:
      bins.append( strt )
      strt += h
    fig2, ax2 = plt.subplots()
    ax2.hist( a, bins = bins )
    ax2.plot( list( polyy.keys() ), [ x * len( X ) for x in list( polyy.values() ) ] )
    y_vals = ax2.get_yticks()
    ax2.set_yticklabels( [ '{:3.4f}'.format( x / ( len( X ) * h ) ) for x in y_vals ] )
    plt.grid( True, 'both', 'both' )
    plt.show()
  except KeyboardInterrupt:
    exit()
  except EOFError:
    exit()
if __name__ == '__main__':
  main()