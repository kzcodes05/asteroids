import pygame
import sys
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from shot import *

time = pygame.time.Clock()
dt = 0

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

  updatables = pygame.sprite.Group()
  drawables = pygame.sprite.Group()
  updatables.add(player)
  drawables.add(player)

  asteroids = pygame.sprite.Group()
  Asteroid.containers = (asteroids, updatables, drawables)
  AsteroidField.containers = (updatables)
  new_field = AsteroidField()

  shots = pygame.sprite.Group()
  Shot.containers = (shots, updatables, drawables)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
    screen.fill((0,0,0))
    dt = time.tick(60) / 1000
    for updateable in updatables:
      updateable.update(dt)

    for asteroid in asteroids:
      if asteroid.collision(player):
        print("Game Over!")
        sys.exit()

    for asteroid in asteroids:
      for bullet in shots:
        if asteroid.collision(bullet):
          asteroid.kill()
          bullet.kill()

    for drawable in drawables:
      drawable.draw(screen)
    pygame.display.flip()
    
    
    
    



if __name__ == "__main__":
  main()