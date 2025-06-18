import pygame
from player import Player
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius,width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_asteroid1_vector = self.velocity.rotate(random_angle) # two new velocity vectors
            new_asteroid2_vector = self.velocity.rotate(-random_angle)
            self.new_radius = self.radius - ASTEROID_MIN_RADIUS # new radius for split asteroids
            
            new_asteroid1 = Asteroid(*self.position, self.new_radius)
            new_asteroid2 = Asteroid(*self.position, self.new_radius)

            velocity_scale = 1.2
            new_asteroid1.velocity = new_asteroid1_vector * velocity_scale
            new_asteroid2.velocity = new_asteroid2_vector * velocity_scale

            