#from pong import colors
import logging
import collections as c 
color_tuples = c.namedtuple("color_tuples", "black white red green blue")
colors = color_tuples(
    black=(0, 0, 0),
    white=(255, 255, 255),
    red=(255, 0, 0),
    green=(0, 255, 0),
    blue=(0, 0, 255),
)

dx = 10
WIDTH, HEIGHT = 600, 800 

class Paddle:

    COLOR = colors.white
    THICKNESS = 10
    WIDTH = 100
    #X = WIDTH / 2
    #Y = HEIGHT - 10 - THICKNESS
    #DX = 0

    def __init__(self):
        logging.info(f"Instantiating {self.__class__.__name__}")
        self.score = 0
        self.x = WIDTH / 2
        self.y = HEIGHT - 10 - self.THICKNESS
        self.left = False
        self.right = False
        self.dx = 0

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def __str__(self):
        return f"Paddle"

    def update(self):
        logging.debug(f"Paddle position update")
        self.x += self.dx
        return self

    def wall_collision(self):
        logging.debug(f"Paddle wall collision check")
        if self.x < 0:
            self.x = 0
            self.dx = 0
        elif self.x + self.WIDTH> WIDTH:
            self.x = WIDTH - self.WIDTH
            self.dx = 0
        return self