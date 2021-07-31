from punto import Punto
'''
Clase Cierre Convexo encargada de calcular
el cierre convexo de un conjunto de puntos
'''
class CierreConvexo:

	'''
	Constructor de la clase Cierre Convexo
	@param puntos: el conjunto de puntos para calcular su ciere convexo.
	@param d: la dirección que se tomará para encontrar el punto más chaparro.
	'''
	def __init__(self, puntos,d):
		self.puntos = puntos
		self.d = d
		self.chaparro = self.encuentraChaparro(d)

	'''
	Método que regresa el punto con la menor coordenada.
	@param d: Indica qué dirección tomaremos en caso de que haya 
	dos puntos con la misma coordenada y.
	@return: el punto con menor coordenada y, si d = -1, entonces
	el más chaparro será el punto con coordenada x menor, en caso de
	que sea 1, entonces se toma el de mayor coordenada x.
	'''
	def encuentraChaparro(self, d):
		return none
	
	'''
	Método que regresa una lista de puntos ordenados de acuerdo 
	a los ángulos polares formados entre el punto más chaparro
	@return: la lista de puntos ordenados de acuerdo a los ángulos
	'''
	def ordenaPuntos(self):
		return []

	def grahamScan(self):
		return []