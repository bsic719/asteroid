import pygame
from logger import log_state
from constants import *
from player import *

def main():
    print(f"Starting Asteroids with pygame vesion: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        screen.fill('black')
        player.draw(screen)

        # calling .tick(arg) will pause game loop until arg (in milliseconds) has passed
        # .tick() also returns amt of time that has passed since last time it was called
        clock.tick(60)
        dt = clock.tick(60)/1000

        player.update(dt)

        pygame.display.flip()
        # refresh the screen/MAKE SURE TO CALL LAST


if __name__ == "__main__":
    main()
