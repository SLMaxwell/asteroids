# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroid_field = AsteroidField()

  while True:
    # Quit the game if window "Close" was clicked..
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    # ... Or if the user pressed the Esc Key.
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
       return

    # Update our screen objects
    for u in updatable:
      u.update(dt)

    # Display a Black Universe filled with our objects
    screen.fill("black")
    for d in drawable:
      d.draw(screen)

    # Update the display
    pygame.display.flip()

    # Limit the framerate to 60 FPS
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()