import pygame
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    print(f"Starting Asteroids with pygame vesion: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)


    asteroidfield = AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        screen.fill('black')

        # calling .tick(arg) will pause game loop until arg (in milliseconds) has passed
        # .tick() also returns amt of time that has passed since last time it was called
        clock.tick(60)
        dt = clock.tick(60)/1000

        for sprite in drawable:
            sprite.draw(screen)

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event('player_hit')
                print('Game over!')
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event('asteroid_shot')
                    print('nice shot')
                    shot.kill()
                    asteroid.kill()

        pygame.display.flip()
        # refresh the screen/MAKE SURE TO CALL LAST


if __name__ == "__main__":
    main()
