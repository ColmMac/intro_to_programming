class Character:
    def __init__(self, health, speed, strength):
      self.health = health
      self.speed = speed
      self.strength = strength
    def double_speed(self):
        self.speed *= 2
warrior = Character(100,20,30)
warrior.double_speed()
print(warrior.speed)