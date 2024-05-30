from turtle import Turtle
class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_text(self, x_cod,y_cod,text):
        self.goto(x=x_cod, y=y_cod)
        self.write(arg=f"{text}",move=False)
