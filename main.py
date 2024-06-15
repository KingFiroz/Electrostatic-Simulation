import pygame 
from math import sqrt
from random import randint, uniform, choice
from ions import Ion
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

# Simulation Window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Electrostatic Simulation")
clock = pygame.time.Clock()
boundary = "closed"
toggle_collisions = False

ion_group = pygame.sprite.Group()

def display_text(clock, ion_group):
    font = pygame.font.SysFont("Arial", 15, bold = True)
    fps = str(int(clock.get_fps()))
    fps_surface = font.render(f"FPS: {fps}", False, "White")

    ball_count_surface = font.render(f"Ball #: {len(ion_group)}", False, "White")

    cations = []
    anions = []
    for ion in ion_group:
        if ion.charge == 1:
            cations.append(ion)
        else:
            anions.append(ion)
    cations_surface = font.render(f"Positive: {len(cations)}", False, "White")
    anions_surface = font.render(f"Negative: {len(anions)}", False, "White")

    screen.blit(fps_surface, (10,10))
    screen.blit(ball_count_surface, (10, 25))
    screen.blit(cations_surface, (10, 40))
    screen.blit(anions_surface, (10, 55))

def spawn_ions(n=1):
    for i in range(n):
        pos = pygame.mouse.get_pos()
        direction = pygame.math.Vector2(uniform(-1, 1), uniform(-1, 1))
        direction = direction.normalize()
        speed = randint(100, 400)
        charge = choice([1, -1])
        if charge == 1:
            color = choice(((137,208,255), (65,105,225), (30,144,255), (0,0,205)))
        else:
            color = choice(((247, 42, 12), (235, 84, 164), (189, 0, 16), (217, 100, 110)))
        Ion(ion_group, speed, pos, direction, color, charge)

def remove_ions():
    ion_death = 0
    ion_population = len(ion_group) / 2
    for ion in ion_group:
        if ion_death < ion_population:
            ion.kill()
            ion_death += 1
        else: 
            break

def toggle_boundary():
    global boundary
    if boundary == "infinite":
        boundary = "closed"
    else:
        boundary = "infinite"

def adjust_velocity(ion, other_ion):
    try:
        x1,x2,y1,y2 = ion.rect.x, other_ion.rect.x, ion.rect.y, other_ion.rect.y
    
        c1 = pygame.math.Vector2(x1,y1)
        c2 = pygame.math.Vector2(x2,y2)
        vec_d1 = c1-c2
        vec_d2 = c2-c1
        vec_one = ion.vel - ((ion.vel- other_ion.vel).dot(vec_d1) * (vec_d1) / vec_d1.magnitude()**2) 
        vec_two = other_ion.vel - ((other_ion.vel - ion.vel).dot(vec_d2 ) * (vec_d2) / vec_d2.magnitude()**2) 

        ion.vel = vec_one
        other_ion.vel = vec_two
    except:
        ion.kill()
        other_ion.kill()

def check_collisions():
    target = []
    for ion in ion_group:
        for other_ion in ion_group:
            if ion == other_ion or ion in target:
                pass
            else:
                if pygame.sprite.collide_mask(ion, other_ion):
                    target.append(other_ion)
                    adjust_velocity(ion, other_ion)

def electrostatic_attraction(dt):
    target = []
    for ion in ion_group:
        for other_ion in ion_group:
            if ion == other_ion or ion in target:
                pass
            else:
                k = 1000000
                x1,x2,y1,y2 = ion.rect.x, other_ion.rect.x, ion.rect.y, other_ion.rect.y
                distance = sqrt((x2-x1)**2 + (y2-y1)**2)
                f = (ion.charge * other_ion.charge )/ distance ** 2

                ion.vel *= k * f 
                other_ion.vel *= k * f 
                print(k*f)
                #except:
                 #   ion.kill()
                  #  other_ion.kill()
                    
def main_loop():
    while True:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                spawn_ions()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    toggle_boundary()
                    print(f"Boundary: {boundary}")  
                if event.key == pygame.K_c:
                    global toggle_collisions
                    if toggle_collisions:
                        toggle_collisions = False
                        print(f"Toggle Collisions: {toggle_collisions}")
                    else:
                        toggle_collisions = True
                        print(f"Toggle Collisions: {toggle_collisions}")
                if event.key == pygame.K_n:
                    spawn_ions(100)
                if event.key == pygame.K_r:
                    remove_ions()


        #display
        screen.fill((80,80,80))   
        ion_group.draw(screen)
        display_text(clock, ion_group)

        # clock
        dt = clock.tick() / 1000

        if toggle_collisions:
            check_collisions()
            electrostatic_attraction(dt)

        #update
        ion_group.update(dt, boundary)
        pygame.display.update()  

if __name__ == "__main__":
    pygame.init()
    main_loop()