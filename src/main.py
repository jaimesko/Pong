import pygame
import sys
import logging
import collections as c 

from ball import Ball
from paddle import Paddle

def error_details():
    return (
        f"{sys.exc_info()[0]}: {sys.exc_info()[1]}. Line: {sys.exc_info()[2].tb_lineno}"
    )

color_tuples = c.namedtuple("color_tuples", "black white red green blue")
colors = color_tuples(
    black=(0, 0, 0),
    white=(255, 255, 255),
    red=(255, 0, 0),
    green=(0, 255, 0),
    blue=(0, 0, 255),
)

def draw(win, paddle, ball) -> None:
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

def controls(event, paddle):
    logging.debug(f"Player controls")

    k_left, k_right = pygame.K_LEFT, pygame.K_RIGHT

    if event.type == pygame.KEYDOWN:
        if event.key == k_left:
            paddle.dx = -dx
            paddle.left = True
        elif event.key == k_right:
            paddle.dx = dx
            paddle.right = True

    if event.type == pygame.KEYUP:
        if event.key == k_left:
            paddle.left = False
            if paddle.dx == -dx:
                paddle.dx = 0
            if paddle.right == True:
                paddle.dx = dx
        if event.key == k_right:
            paddle.right = False
            if paddle.dx == dx:
                paddle.dx = 0
            if paddle.left == True:
                paddle.dx = -dx

def main():

    logging.info("Starting main")
    clock = pygame.time.Clock()
    running = True

    paddle = Paddle()
    ball = Ball()
    _, rect = draw(WINDOW, paddle, ball)

    try:
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                logging.debug(f"Event: {event}")

                if event.type == pygame.QUIT:
                    logging.info("Quitting")
                    running = False
                    break

                controls(event, paddle)

            paddle.update().wall_collision()
            ball.update().collisions(rect, paddle)
                
            _, rect = draw(WINDOW, paddle, ball)

        pygame.quit()
        quit()
    except Exception as e:
        logging.critical(error_details())
        # logging.critical(f'{e}', exc_info=True)
        # logging.exception("Exception, quitting")
        pygame.quit()
        raise e
        # quit()




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dx = 10
    WIDTH, HEIGHT = 600, 800 
    pygame.init()
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")
    
    main()