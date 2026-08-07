from turtle import Turtle
import random

# CONSTANTS DEFINE..
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        
    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def extend_snake(self):
        self.add_segment(self.segments[-1].position())        
        

    def move(self):
        for each_seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[each_seg-1].xcor()
            new_y = self.segments[each_seg-1].ycor()
            self.segments[each_seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Define movement functions
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)   # Point North    

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)  # Point South

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)  # Point West

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)    # Point East

