from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
DISTANCE=20

UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        segment_1=Turtle("square")
        segment_1.color("white")
        segment_1.penup()
        segment_1.goto(position)
        self.segments.append(segment_1)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x= self.segments[i-1].xcor()
            new_y= self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.head.forward(DISTANCE)

    def UP(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def DOWN(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def RIGHT(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def LEFT(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

