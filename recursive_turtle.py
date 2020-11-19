
import turtle
T=turtle.Turtle()

def recur(meter):
    if meter>0:
        T.forward(meter)
        T.left(90)
        recur(meter-5)

recur(200)