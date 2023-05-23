import pygame
from settings import *
from debug import debug
from Tile import Tile
from Player import Player
from CameraManager import YSortCameraGroup

class Level:
    def __init__(self) -> None:
        # Get the display surface
        self.displaySurface = pygame.display.get_surface()

        # Groups setup
        self.visibleSprites = YSortCameraGroup()
        self.obstaclesSprites = pygame.sprite.Group()

        # Sprite setup
        self.create_map()

    def create_map(self):
        for rowIndex, row in enumerate(MAP):
            for colIndex, col in enumerate(row):
                x = colIndex * TILESIZE
                y = rowIndex * TILESIZE

                if col == 'x':
                    Tile((x,y), [self.visibleSprites, self.obstaclesSprites])
                if col == 'p':
                    self.player = Player((x,y), [self.visibleSprites], self.obstaclesSprites)


    def run(self):
        # Update and draw the game
        self.visibleSprites.custom_draw(self.player)
        self.visibleSprites.update()