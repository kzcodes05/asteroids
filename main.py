import pygame
from constants import *
from player import *

time = pygame.time.Clock()
dt = 0

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
    screen.fill((0,0,0))
    player.draw(screen)
    pygame.display.flip()
    dt = time.tick(60) / 1000
    player.update(dt)
    



if __name__ == "__main__":
  main()