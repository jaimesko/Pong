import collections
import logging
import pygame
from settings import HEIGHT, WIDTH

color_tuples = collections.namedtuple("color_tuples", "black white red green blue")

colors = color_tuples(
    black=(0, 0, 0),
    white=(255, 255, 255),
    red=(255, 0, 0),
    green=(0, 255, 0),
    blue=(0, 0, 255),
)

def draw(win, paddle, ball) -> None:
    """Draw game window."""
    logging.debug("Drawing window")
    win.fill(colors.black)
    pygame.draw.line(win, colors.white, (0, HEIGHT/2), (WIDTH, HEIGHT/2))
    circle = pygame.draw.circle(
        win, ball.COLOR, (int(ball.x), int(ball.y)), ball.RADIUS
    )
    rect = pygame.draw.rect(
        win,
        paddle.COLOR,
        (int(paddle.x), int(paddle.y), paddle.WIDTH, paddle.THICKNESS),
        0,
    )
    pygame.display.update()
    return circle, rect