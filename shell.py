def float_format( number ):
  return "{: > .4e}".format( number )

def std_read_nodes_number():
  nodes_number = None
  while True:
    nodes_number = input( "Введите число чисел в выборке: " )
    try:
      nodes_number = int( nodes_number )
      if ( nodes_number >= 1 ):
        break
      else:
        print( "Узлов аппроксимации должно быть не менее 1. Попробуйте еще раз..." )
    except ( ValueError ):
      print( "Неверный формат данных. Попробуйте еще раз..." )
  return nodes_number

def std_read_isingle( i ):
  x = None
  while True:
    x = input( f'[ {i + 1} ]: Введите число ( x_{i + 1} ): ' )
    try:
      return float( x )
    except ( ValueError ):
      print( "Неверный формат данных. Попробуйте еще раз..." )

def extract_nodes():
  # number of approximation nodes
  nodes_number = std_read_nodes_number()

  # starting getting nodes itself
  print( f'Будет считано {nodes_number} чисел выборки' )
  X = []
  for i in range( nodes_number ):
    x = std_read_isingle( i )
    X.append( x )
    print( f'Считано число: ( {x} )' )
  return X