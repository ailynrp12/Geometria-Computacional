'''
Aprendiendo a usar turtle
--------------------------
Ejercicio 1
Dibujar un segmento de línea dados 2 puntos
'''
import turtle

# Creamos el objeto Turtle para poder dibujar
segmento = turtle.Turtle()
# Levantamos el lápiz (es decir no dibuja)
segmento.up()
# Nos movemos a la posición
segmento.setposition(30,50)
# Bajamos el lápiz (para poder dibujar)
# Dibujamos el primer punto
segmento.dot(10,"black")
# Cambiamos de posición para el siguiente punto
segmento.setposition(60,100)
# Dibujamos el segundo punto
segmento.dot(10,"black")
# Última declaración de un programa gráfico de turtle
turtle.done()

'''
Ejercicio 2 
Dibujar un triángulo dados 3 puntos
'''
triangulo = turtle.Turtle()
triangulo.up()
# Esconde u oculta la tortuta o puntero
triangulo.hideturtle()
triangulo.setposition(30,150)
triangulo.dot(20,"black")
triangulo.down()
triangulo.setposition(60,100)
triangulo.dot(20,"black")
triangulo.setposition(30,50)
triangulo.dot(20,"black")
triangulo.setposition(30,150)
turtle.done()

'''
Ejercicio 3
Dibujar un pentágono con giros a la derecha
'''
poligono = turtle.Turtle()
poligono.down()

tamnaño = 100
angulo = 360.0 / 5
 
for i in range(5):
	poligono.dot()
	poligono.forward(tamaño)
	poligono.right(angulo)
     
turtle.done()

'''
Ejercicio 4
Dibujar un polígono de n lados de acuerdo a la orientación
dada por el usuario, 1 es derecha y 0 izquierda.
'''
def dibujaPoligono(lados, orientacion):
	poligono = turtle.Turtle()
	poligono.up()
	poligono.setposition(-20,-200)

	poligono.down()
	tamaño = 50
	angulo = 360.0 / lados

	for i in range(lados):
		poligonos.dot()
		poligonos.forward(tamaño)
		if(orientacion == 1):
			poligono.right(angulo)
		else:
			poligono.left(angulo)

	turtle.done()

dibujaPoligono(12,0)
