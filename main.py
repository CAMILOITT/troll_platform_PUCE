import pygame

import src.character.ball as ball
from src.const.game import SCREEN

pygame.init()
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Simple Pygame Window")

ball = ball.Ball(radius=20, color="blue")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    SCREEN.fill((0, 0, 0))
    ball.drawing()  # Draw the ball on the screen
    pygame.display.flip()  # Update the display
    clock.tick(60)  # Limit the frame rate to 60 FPS

pygame.quit()
