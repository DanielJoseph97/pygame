import pygame
from circleshape import CircleShape
from constants import *
#from player import Player

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, SHOT_RADIUS,width=2)

    def update(self, dt):
        self.position += self.velocity * dt