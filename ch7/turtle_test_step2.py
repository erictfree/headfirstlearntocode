import turtle

slowpoke = turtle.Turtle()
slowpoke.shape('turtle')
pokey = turtle.Turtle()
pokey.shape('turtle')
pokey.color('red')

def make_square(the_turtle):
    for i in range(0,4):
        the_turtle.forward(100)
        the_turtle.right(90)

make_square(slowpoke)
pokey.right(45)
make_square(pokey)

turtle.mainloop()
