import pygame 

# Simulation Window
screen = pygame.display.set_mode((400,400), pygame.RESIZABLE)
pygame.display.set_caption("Electrostatic Simulation")

# Main Loop
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quits pygame after closing window 
pygame.quit()

