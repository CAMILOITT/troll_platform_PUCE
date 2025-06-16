import pygame


class Player(pygame.sprite.Sprite):
  x: int = 0
  y: int = 0
  name: str
  level: int
  health: int
  mana: int
  experience: int

  def __init__(self, name: str, level: int = 1):
    super().__init__()
    # self.image = pygame.Surface((50, 50))  # Reemplaza con tu sprite real
    # self.image.fill((255, 0, 0))  # Color de prueba
    self.image = pygame.image.load("src/character/player/assets/player_walk.png").convert_alpha()
    # self.image = pygame.transform.scale(self.image, (50, 50))  # Ajusta el tamaño del sprite
    # self.image.blit(self.image, (0, 0), (50, 50))  # Blit the image onto itself to ensure it's ready for use
    self.image
    self.rect = self.image.get_rect(
      topleft=(self.x, self.y),
    )

    self.name = name
    self.level = level
    self.health = 100
    self.mana = 50
    self.experience = 0

  def update(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      self.x -= 5  # Move left
    if keys[pygame.K_RIGHT]:
      self.x += 5
    if keys[pygame.K_SPACE]:
      self.jump()
    self.rect.x = self.x

  def jump(self):
    pass

  def draw(self):
    pygame.draw.rect(
      pygame.display.get_surface(),
      pygame.Color("blue"),
      (self.x, self.y, 50, 50),  # Example position and size
    )

  def level_up(self):
    self.level += 1
    self.health += 20
    self.mana += 10
    print(f"{self.name} leveled up to level {self.level}!")

  def take_damage(self, amount: int):
    self.health -= amount
    if self.health <= 0:
      print(f"{self.name} has been defeated!")
      self.health = 0

  def heal(self, amount: int):
    self.health += amount
    print(f"{self.name} healed for {amount} health points.")
