import pygame
import sys
from constants import  *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullet_shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (updatable, drawable, bullet_shots)
    AsteroidField.containers = (updatable,)
    player1 = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)) # Player 1 created
    asteroidfield = AsteroidField()    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        for obj in asteroids:
            if obj.collision(player1):
                print("Game Over!")
                sys.exit()
            for single_bullet in bullet_shots:
                if single_bullet.collision(obj):
                    obj.split()
                    single_bullet.kill()
                    break
        pygame.display.flip()
        
        dt = clock.tick(60)* 0.001



if __name__ == "__main__":
    main()