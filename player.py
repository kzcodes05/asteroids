from circleshape import *
from constants import *
from shot import *
import pygame

class Player(CircleShape):

  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    self.rotation = 0
    self.shooting_timer = 0
  
  def triangle(self):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
      a = self.position + forward * self.radius
      b = self.position - forward * self.radius - right
      c = self.position - forward * self.radius + right
      return [a, b, c]
  
  def draw(self, screen):
     pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

  def rotate(self, dt):
     self.rotation += PLAYER_TURN_SPEED * dt

  def move(self, dt):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      self.position += forward * PLAYER_SPEED * dt

  def shoot(self):
    if self.shooting_timer <= 0:
        new_shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_velocity = forward * PLAYER_SHOOT_SPEED   
        new_shot.velocity = shot_velocity
        self.shooting_timer = PLAYER_SHOT_COOLDOWN


  def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shooting_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * - 1)
        if keys[pygame.K_SPACE]:
            self.shoot()

  


  