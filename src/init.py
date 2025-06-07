import pygame

from src.character.player.player import Player
from src.const.game import SCREEN


class Game_controller:
  running = True
  player = Player("Player")

  def __init__(self):
    self._game = None

  def start(self):
    SCREEN.fill((0, 0, 0))

    self.player.draw()

  def get_events(self, event):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
