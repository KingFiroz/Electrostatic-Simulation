import pygame 
from random import randint, uniform
from ions import Cation

# Simulation Window
screen = pygame.display.set_mode((400,400), pygame.RESIZABLE)
pygame.display.set_caption("Electrostatic Simulation")
clock = pygame.time.Clock()

cation_group = pygame.sprite.Group()

def main_loop():
    while True:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                direction = pygame.math.Vector2(uniform(-1, 1), uniform(-1, 1))
                direction = direction.normalize()
                speed = randint(50, 400)
                Cation(cation_group, speed, pos, direction)

        # clock
        clock.tick()

        #display
        screen.fill((80,80,80))   
        cation_group.draw(screen)  

        #update
        pygame.display.update()       

if __name__ == "__main__":
    pygame.init()
    main_loop()