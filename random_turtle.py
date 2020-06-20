import turtle
def _draw():
	window=turtle.Screen()
	
 	a=turtle.Turtle()
	i=0
	j=-20
	x=['grey','black','blue','green','red','white','yellow','white']
	while(i<7):
	 a.circle(20+j,10+j)
	 j=j+40
	 i=i+1
	 window.bgcolor(x[i-1])
	 if (i==7):
	  i=0
	 # a.fill(x[i]) # uncomment this and see strange phenomenon :) 
	 a.color(x[i])
_draw()

input()
