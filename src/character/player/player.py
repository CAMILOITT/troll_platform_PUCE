class Player:
  def __init__(self, name: str, level: int = 1):
    self.name = name
    self.level = level
    self.health = 100
    self.mana = 50
    self.experience = 0

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
