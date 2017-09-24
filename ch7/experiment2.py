import turtle

slowpoke = turtle.Turtle()
slowpoke.shape('turtle')

slowpoke.pencolor('blue')
slowpoke.penup()
slowpoke.setposition(-120, 0)
slowpoke.pendown()
slowpoke.circle(50)

slowpoke.pencolor('red')
slowpoke.penup()
slowpoke.setposition(120, 0)
slowpoke.pendown()
slowpoke.circle(50)
turtle.mainloop()
