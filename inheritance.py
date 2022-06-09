# Basic Collision Detection
# originally by @TokyoEdtech
# adapted to use inheritance by @codingalzi

# Topics: Collision Detection, Overlapping Coordinates,
# Distance Checking, Axis-Aligned Bounding Box

# Shoutouts:
# 16-Bit Members Kevin, Paul, and Jan

import turtle
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Collision Detection by @TokyoEdtech")
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

shapes = ["wizard.gif", "goblin.gif", "pacman.gif", "cherry.gif", "bar.gif", "ball.gif", "x.gif"]

for shape in shapes:
    wn.register_shape(shape)
    
# Sprite 클래스 
class Sprite():
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.stamp()
    
    def is_overlapping_collision(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
            
    def is_distance_collision(self, other):
        distance = (((self.x-other.x) ** 2) + ((self.y-other.y) ** 2)) ** 0.5
        if distance < (self.width + other.width)/2.0:
            return True
        else:
            return False
        
    def is_aabb_collision(self, other):
        # Axis Aligned Bounding Box
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)
        
# Sprite 클래스 상속 
class Character(Sprite):
    def __init__(self, x, y, width, height, image, jump=False):
        super().__init__(x, y, width, height, image)
        self.jump = jump 

    def hop(self):
        if self.jump == True:
            self.x += 300


wizard = Character(-128, 200, 128, 128, "wizard.gif")
goblin = Character(128, 200, 108, 128, "goblin.gif")

pacman = Character(-128, 0, 128, 128, "pacman.gif", True)
cherry = Character(128, 0, 128, 128, "cherry.gif")

bar = Character(0, -400, 128, 24, "bar.gif")
ball = Character(0,-200, 32, 32, "ball.gif")

sprites = [wizard, goblin, pacman, cherry, bar, ball]

def move_goblin():
    goblin.x -= 64

def move_pacman():
    pacman.x += 30
    
def jump_pacman():
    pacman.hop()

def move_ball():
    ball.y -= 24

wn.listen()
wn.onkeypress(move_goblin, "Left")
wn.onkeypress(move_pacman, "Right")
wn.onkeypress(jump_pacman, "space")
wn.onkeypress(move_ball, "Down")

while True:
    
    for sprite in sprites:
        sprite.render(pen)
        
    # Collision detection
    if wizard.is_aabb_collision(goblin):
        wizard.image = "x.gif"
        
    if pacman.is_aabb_collision(cherry):
        cherry.image = "x.gif"
        
    if bar.is_aabb_collision(ball):
        ball.image = "x.gif"
        
    wn.update()
    pen.clear()

# wn.mainloop()
