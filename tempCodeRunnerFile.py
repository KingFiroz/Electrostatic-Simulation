       pos = pygame.mouse.get_pos()
        direction = pygame.math.Vector2(uniform(-1, 1), uniform(-1, 1))
        direction = direction.normalize()
        speed = randint(100, 400)
        color = choice(((137,208,255), (65,105,225), (30,144,255), (0,0,205)))
        Ion(ion_group, speed, pos, direction, color)