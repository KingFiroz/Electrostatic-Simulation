import pygame


class Cation(pygame.sprite.Sprite):
    def __init__(self, groups, speed, pos, direction):
        super().__init__(groups)
        self.speed = speed
        self.pos = pos
        self.direction = direction

        self.create_surf()
        
    def create_surf(self):
        self.image = pygame.Surface((16,16)).convert_alpha()
        self.image.set_colorkey("black")    # keep all black pixels transparent
        pygame.draw.circle(surface=self.image, color=(137,208,255) , center=(8,8), radius=8)
        self.rect = self.image.get_rect(center=self.pos)