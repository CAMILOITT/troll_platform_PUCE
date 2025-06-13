class physics:
  def __init__(self, gravity=9.81):
    self.gravity = gravity

  def calculate_fall(self, weight):
    weight = weight if weight > 0 else 1  # Prevent division by zero
    fall_speed = self.gravity / weight
    return fall_speed
