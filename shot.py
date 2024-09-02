import pygame
from main import *
from circleshape import *
from constants import *

class Shot(CircleShape):
  
  def __init__ (self, x, y):
    super().__init__(x, y, SHOT_RADIUS)
    self.velocity = PLAYER_SHOOT_SPEED

  def draw(self, screen):
    pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

  def update(self, dt):
    self.position += (self.velocity * dt)