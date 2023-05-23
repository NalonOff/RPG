import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacleSprites) -> None:
        super().__init__(groups)
        self.image = pygame.image.load('assets\Actor\Characters\Greenman\SeparateAnim\Item.png').convert()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)

        self.direction = pygame.math.Vector2()
        self.velocity = 5

        self.obstacleSprites = obstacleSprites

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, velocity):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * velocity
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * velocity
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacleSprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # Is moving right ?
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # Is moving left ?
                        self.hitbox.left = sprite.hitbox.right
        
        if direction == 'vertical':
            for sprite in self.obstacleSprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # Is moving down ?
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # Is moving up ?
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.input()
        self.move(self.velocity)