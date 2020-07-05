import turtle
a=turtle.Turtle()
def _draw():
	window=turtle.Screen()
	window.bgcolor("indigo")
	i=0
	j=-20
	x=['grey','black','blue','green','red','white','yellow','white','green','red']
	while(i<len(x)):
	 a.circle(20+j,10+j)
	 j=j+30
	 
	 # window.bgcolor(x[i-1]) // don;t uncomment it 
	 #a.fill(x[i]) # uncomment this and see strange phenomenon :) , well not all strange though 
	 a.color(x[i]) # using a.color(x[i-1]) draws violently , try it !
	 i=i+1
_draw()

input()
