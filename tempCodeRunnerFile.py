    #print(ion.id)
    #print(f"My original velocity is{ion.vel}")
    # Normal vector 
    vec_n = pygame.math.Vector2(x2-x1, y2-y1)
    vec_un = pygame.math.Vector2(vec_n.x / vec_n.magnitude(), vec_n.y / vec_n.magnitude())
    v1in = vec_un.dot(ion.vel)
    v2in = vec_un.dot(other_ion.vel)
    v1fn = v2in
    v2fn = v1in
    vec_v1fn = v1fn * vec_un
    vec_v2fn = v2fn * vec_un

    # Tangent Vector
    vec_ut = pygame.math.Vector2(-1*vec_un.y, vec_un.x)
    v1it = vec_ut.dot(ion.vel)
    v2it = vec_ut.dot(other_ion.vel)
    v1ft = v1it
    v2ft = v2it
    vec_v1ft = v1ft * vec_ut
    vec_v2ft = v2ft * vec_ut

    vec_one = vec_v1fn + vec_v1ft
    vec_two = vec_v2fn + vec_v2ft
    ion.vel = vec_one
    other_ion.vel = vec_two
    #print(f"My new velocity is {ion.vel}")