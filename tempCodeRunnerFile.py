k = 0.0001
                x1,x2,y1,y2 = ion.rect.x, other_ion.rect.x, ion.rect.y, other_ion.rect.y
                distance = sqrt((x2-x1)**2 + (y2-y1)**2)
                f = (ion.charge * other_ion.charge )/ distance ** 2

                ion.vel += k*f * dt 
                other_ion.vel += k*f * dt 