import pygame


class Ion(pygame.sprite.Sprite):
    def __init__(self, groups, speed, pos, direction, color):
        super().__init__(groups)
        self.speed = speed
        self.pos = pos
        self.direction = direction
        self.color = color

        self.create_surf()
        
    def create_surf(self):
        self.image = pygame.Surface((16,16)).convert_alpha()
        self.image.set_colorkey("black")    # keep all black pixels transparent
        pygame.draw.circle(surface=self.image, color=self.color , center=(8,8), radius=8)
        self.rect = self.image.get_rect(center=self.pos)

    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

        # infinite boundary
        if self.pos[0] > 1288:
            self.pos = [-8,720-self.pos[1]]
        if self.pos[0] < -8:
            self.pos = [1288, 720-self.pos[1]]

        if self.pos[1] > 728:
            self.pos = [1280-self.pos[0],-8]
        if self.pos[1] < -8:
            self.pos = [1280-self.pos[0],728]

    def update(self, dt):
        self.move(dt)