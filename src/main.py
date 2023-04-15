import sys
import logging
import pygame
from ball import Ball
from paddle import Paddle
from drawing import draw
from settings import *

def error_details():
    """Return error information."""
    return (
        f"{sys.exc_info()[0]}: {sys.exc_info()[1]}. Line: {sys.exc_info()[2].tb_lineno}"
    )

def controls(event, paddle):
    """Paddle movement controls & keys."""
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
    """Game loop."""
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
        
    except Exception as exc:
        logging.critical(error_details())
        # logging.critical(f'{exc}', exc_info=True)
        # logging.exception("Exception, quitting")
        pygame.quit()
        raise exc
        #quit()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    pygame.init()
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")
    
    main()