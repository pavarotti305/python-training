import turtle
# each object turtle is member of class Pen
window = turtle.Screen()
aline = turtle.Pen()
karine = turtle.Pen()
jack = turtle.Pen()

aline.forward(50)
aline.right(90)
aline.forward(20)

karine.left(90)
karine.forward(100)

jack.left(180)
jack.forward(80)


turtle.mainloop()