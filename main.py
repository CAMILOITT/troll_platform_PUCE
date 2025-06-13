import pygame

from src.init import Game_controller

pygame.init()
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Simple Pygame Window")
game_controller = Game_controller()

while game_controller.running:
  game_controller.start()
  # pygame.display.flip()
  pygame.display.update()
  clock.tick(60)

pygame.quit()
