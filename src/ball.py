import logging
from drawing import colors
from settings import *

class Ball:

    COLOR = colors.white
    RADIUS = 5

    def __init__(self):
        logging.info(f"Instantiating {self.__class__.__name__}")
        self.x = int(WIDTH / 2)
        self.y = int(HEIGHT / 2)
        # ball_dxy = [random.randint(-60,60),200]
        self.dx = 0 / 60
        self.dy = 300 / 60 
        self.counter = 1

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def __str__(self):
        return f"Ball"
    
    def reset_ball(self):
        """Resets the ball to its starting position."""
        logging.info(f"Reseting {self.__class__.__name__}")
        self.x = int(WIDTH / 2)
        self.y = int(HEIGHT / 2)
        self.dx = 0 / 60
        self.dy = 300 / 60
        self.counter = 1
        return self

    def update(self):
        """Update the the ball's position after a game tick."""
        logging.debug(f"Ball position update")
        self.x += self.dx
        self.y += self.dy
        return self

    def collisions(self, rect, paddle):
        """Checks for collision with the paddle and the walls."""
        logging.debug(f"Ball collisions check")
        
        # Paddle collision
        col = rect.collidepoint(
            self.x, self.y + self.RADIUS
        )
        if col:
            logging.info(f"Paddle collision")
            self.dy = -self.dy
            self.dx += paddle.dx / dx
            
        # Right wall collision
        elif self.x + self.RADIUS > WIDTH:
            logging.info("Right wall collision")
            self.dx = -self.dx
            
        # Left wall collision
        elif self.x - self.RADIUS < 0:
            logging.info("Left wall collision")
            self.dx = -self.dx
            
        # Top wall collision
        elif self.y - self.RADIUS < 0:
            logging.info("Top wall collision")
            self.dy = -self.dy
            
        # Bottom wall collision
        elif self.y + self.RADIUS > HEIGHT:
            logging.info("Bottom wall collision")
            self.x, self.y = int(WIDTH / 2), int(HEIGHT / 2)
            self.dx, self.dy = 0 / 60, 200 / 60
            self.counter += 1
            self.reset_ball()
            
        return self