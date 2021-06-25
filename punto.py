''' 
Nombre Completo:
Número de Cuenta:
Clase Punto donde como atributos se 
tendrán las coordenadas x y. 
'''
class Punto:
	'''
	Constructor de la clase Punto
	@param x: coordenada x
	@param y: coordenada y
	'''
	def __init__(self,x,y):
		# Escribe aquí tu código
		self.x = x
		self.y = y

	'''
	Método que regresa el producto cruz del punto actual y el punto recibido q
	@param q: punto con el que se realizará el producto cruz
	@return : el producto cruz entre el punto actual y q.
	'''	
	def productoCruz(self,p):
		# Escribe aquí tu código
		return 1


	'''
	Método que indica la dirección de una vuelta entre 3 puntos
	@param q: uno de los puntos para conocer la dirección de la vuelta
	@param r: uno de los puntos para conocer la dirección de la vuelta
	@return: regresa un valor negativo si se dio vuelta a la izquierda, 
	         un valor positivo si fue a la derecha y 0 si no hubo vuelta (están sobre la misma recta).
	'''
	def direccionVuelta(self, q, r):
		# Escribe aquí tu código
		return 0



	'''
	Método que regresa el ángulo polar correspondiente a dos puntos
	tomando al punto actual como el origen.
	@param q: uno de los puntos para conocer el ángulo polar.
	@return: el ángulo polar correpondiente a dos puntos  
	         tomando al punto actual como el origen.
	'''
	def anguloPolar(self, q):
		# Escribe aquí tu código
		return 0

	'''
	Método que regresa el ángulo en grados correspondiente a dos puntos
	a partir de su ángulo polar.
	@param q: uno de los puntos para conocer el ángulo en grados
	@return: el ángulo en grados correspondiente a dos puntos a partir de
	su ángulo polar. 
	'''
	def anguloGrados(self,q):
		# Escribe aquí tu código

	'''
	Método que regresa la distancia entre dos puntos.
	@param q: uno de los puntos para determinar la distancia.
	@return: la distancia entre el punto actual y el punto q
	'''
	def distancia(self,q):
		# Escribe aquí tu código
		return 0

	'''
	Método que regresa la representación en cadena de un punto
	de manera que se vea (x,y).
	@return la representación en cadena de un punto de manera
	que se vea (x,y)
	'''
	def __str__(self):
		return ""


#help(Punto)