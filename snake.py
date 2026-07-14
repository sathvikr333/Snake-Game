from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def reset(self):
        for segment in self.turtles:
            segment.goto(1000,1000)
        self.turtles.clear()
        
        self.create_snake()
        self.head = self.turtles[0]
            

    def add_segment(self,position):
        tim = Turtle()
        
        tim.shape("square")
        tim.color("green")
        tim.penup() 
        tim.goto(position)
        self.turtles.append(tim)
    
    def extend_snake(self):
        self.add_segment(self.turtles[-1].position())
    
    def move(self):
        for seg_num in range(len(self.turtles) - 1,0,-1):
            new_x = self.turtles[seg_num - 1].xcor()
            new_y = self.turtles[seg_num -1].ycor()
            self.turtles[seg_num].goto(new_x,new_y)
        
        self.turtles[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    