import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

id = 0

class Ion(pygame.sprite.Sprite):
    def __init__(self, groups, speed, pos, direction, color):
        super().__init__(groups)
        self.speed = speed
        self.pos = pos
        self.direction = direction
        self.color = color

        self.vel = self.direction * self.speed
        self.radius = 4
        global id
        id += 1
        self.id = id


        self.create_surf()
        
    def create_surf(self):
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius)).convert_alpha()
        self.image.set_colorkey("black")    # keep all black pixels transparent
        pygame.draw.circle(surface=self.image, color=self.color , center=(self.radius,self.radius), radius=self.radius)
        self.rect = self.image.get_rect(center=self.pos)
        self.mask = pygame.mask.from_surface(self.image)

    def move(self, dt, boundary):
        self.pos += self.vel * dt
        self.rect.center = self.pos

        # boundary
        if boundary == "infinite":
            if self.pos[0] > SCREEN_WIDTH + self.radius:
                self.pos = [-self.radius,SCREEN_HEIGHT-self.pos[1]]
            if self.pos[0] < -self.radius:
                self.pos = [SCREEN_WIDTH + self.radius, SCREEN_HEIGHT-self.pos[1]]

            if self.pos[1] > SCREEN_HEIGHT + self.radius:
                self.pos = [SCREEN_WIDTH-self.pos[0],-self.radius]
            if self.pos[1] < -self.radius:
                self.pos = [SCREEN_WIDTH-self.pos[0],SCREEN_HEIGHT + self.radius]

        elif boundary == "closed":
            if self.pos[0] > SCREEN_WIDTH or self.pos[0] < 0:
                #self.direction = pygame.math.Vector2((-1 * self.direction[0], self.direction[1]))
                self.vel = pygame.math.Vector2(-1 * self.vel.x, self.vel.y)
                #self.direction.normalize()

            if self.pos[1] > SCREEN_HEIGHT or self.pos[1] < 0:
                #self.direction = pygame.math.Vector2((self.direction[0], -1 * self.direction[1]))
                #self.direction.normalize()
                self.vel = pygame.math.Vector2(self.vel.x, -1 * self.vel.y)

    def update(self, dt, boundary):
        self.move(dt, boundary)