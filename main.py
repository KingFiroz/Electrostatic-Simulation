import pygame 
from random import randint, uniform
from ions import Ion

# Simulation Window
screen = pygame.display.set_mode((400,400), pygame.RESIZABLE)
pygame.display.set_caption("Electrostatic Simulation")
clock = pygame.time.Clock()

ion_group = pygame.sprite.Group()

def spawn_ions():
    pos = pygame.mouse.get_pos()
    direction = pygame.math.Vector2(uniform(-1, 1), uniform(-1, 1))
    direction = direction.normalize()
    speed = randint(50, 400)
    Ion(ion_group, speed, pos, direction)

def main_loop():
    while True:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                spawn_ions()

        # clock
        dt = clock.tick() / 1000

        #display
        screen.fill((80,80,80))   
        ion_group.draw(screen)  

        #update
        ion_group.update(dt)
        pygame.display.update()       

if __name__ == "__main__":
    pygame.init()
    main_loop()