import pygame

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.displaySurface = pygame.display.get_surface()
        self.halfWidth = self.displaySurface.get_size()[0] // 2
        self.halfHeight = self.displaySurface.get_size()[1] // 2
        self.offset = pygame.math.Vector2(100, 200)

    def custom_draw(self, player):
        # Get the offset
        self.offset.x = player.rect.centerx - self.halfWidth
        self.offset.y = player.rect.centery - self.halfHeight

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offsetPos = sprite.rect.topleft - self.offset
            self.displaySurface.blit(sprite.image, offsetPos)