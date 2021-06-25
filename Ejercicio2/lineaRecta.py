'''
Nombre Completo:
Numero de Cuenta:
Clase Linea donde como atributo se tendrá la lista de puntos
que forman un segmento de línea.
'''
from punto import Punto
class Linea:
	'''
	Constructor de la clase Linea
	@param puntos: lista de puntos que conforman el segmento de línea
	'''
	def __init__(self,puntos):
		self.puntos = puntos

	'''
	Método que permite saber si una línea es recta o no
	@return true en caso de que la línea sea recta, en otro caso regresa false.
	'''
	def esLineaRecta(self):
		return false