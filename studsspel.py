import pygame
from pygame.locals import *
import sys
import pymunk
import pymunk.pygame_util

pygame.init()
clock = pygame.time.Clock()

windowSize = (800, 600)

screen = pygame.display.set_mode(windowSize)

running = True

rad = 14
ball_elasticity = 1
friction = 0.8
space = pymunk.Space()
wind = 0.0
gravity = -900.0
space.gravity = (wind, gravity)
circles = []



def create_circle(position):
    mass = 0.1
    inertia = pymunk.moment_for_circle(mass, 0, rad)
    body = pymunk.Body(mass, inertia)
    body.position = position
    # body.position = position
    shape = pymunk.Circle(body, rad)
    shape.elasticity = ball_elasticity
    shape.friction = friction
    space.add(body, shape)
    return shape

def create_line():
    body = pymunk.Body()
    body.position = (400,600)
    line_shape = pymunk.Segment(body, (-400,-600), (400,-600), 15)
    line_shape.elasticity = 0.9
    space.add(line_shape)
    return line_shape

def create_line2():
    mass = 10000
    inertia = pymunk.moment_for_circle(mass, 10, rad)
    
    body = pymunk.Body(mass, inertia)
    body.position = (650,600)
    
    line_shape = pymunk.Segment(body, (-30,-510), (30,-500), 3)
    line_shape.elasticity = 1
    space.add(line_shape)
    return line_shape

def create_line3():
    mass = 10000
    inertia = pymunk.moment_for_circle(mass, 10, rad)
    
    body = pymunk.Body(mass, inertia)
    body.position = (150,600)
    
    line_shape = pymunk.Segment(body, (-30,-500), (30,-520), 3)
    line_shape.elasticity = 1
    space.add(line_shape)
    return line_shape

def create_line4():
    body = pymunk.Body()
    body.position = (400,600)
    line_shape = pymunk.Segment(body, (-10,-600), (-10,-400), 15)
    line_shape.elasticity = 0.9
    space.add(line_shape)
    return line_shape

def create_line5():
    body = pymunk.Body()
    body.position = (800,600)
    line_shape = pymunk.Segment(body, (-10,-800), (-10,100), 15)
    line_shape.elasticity = 0.9
    space.add(line_shape)
    return line_shape

def create_line6():
    body = pymunk.Body()
    body.position = (20,600)
    line_shape = pymunk.Segment(body, (-10,-800), (-10,100), 15)
    line_shape.elasticity = 0.9
    space.add(line_shape)
    return line_shape

def create_line7():
    body = pymunk.Body()
    body.position = (400,600)
    line_shape = pymunk.Segment(body, (-400,-10), (400,-10), 15)
    line_shape.elasticity = 0.9
    space.add(line_shape)
    return line_shape

line = create_line()
line.color = (240, 150, 5)

line2 = create_line2()
line2.color = (240, 150, 5)


line3 = create_line3()
line3.color = (230, 130, 40)

line4 = create_line4()
line4.color = (210, 130, 40)

line5 = create_line5()
line5.color = (220, 120, 40)

line6 = create_line6()
line6.color = (220, 140, 40)

line7 = create_line7()
line7.color = (200, 140, 20)

while running:
    clock.tick(60)

    movex = line2.body.position
    
    movey = line3.body.position
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                movex += (0, 20)
            elif event.key == pygame.K_DOWN:
                movex += (0, -20)
            elif event.key == pygame.K_LEFT:
                movex += (-20, 0)
               
            elif event.key == pygame.K_RIGHT:
                movex += (20, 0)

            elif event.key == pygame.K_w:
                movey += (0, 20)
            elif event.key == pygame.K_s:
                movey += (0, -20)
            elif event.key == pygame.K_a:
                movey += (-20, 0)
            elif event.key == pygame.K_d:
                movey += (20, 0)
                
            elif event.key == pygame.K_l:
                rad = 20
                friction = 0.1
            elif event.key == pygame.K_SPACE:
                originalMousePos = pygame.mouse.get_pos()
                realPos = pymunk.pygame_util.to_pygame(originalMousePos, screen)
                newCircle = create_circle(realPos)
                circles.append(newCircle)
                print(len(circles))

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                movex += (0,0)
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                movex += (0,0)


    screen.fill((255, 255, 255))
    
    for circle in circles:
        circlePosition = int(circle.body.position.x), 600-int(circle.body.position.y)
        pygame.draw.circle(screen, (0, 0, 0), circlePosition, int(circle.radius), 0)

    #pymunk.pygame_util.draw(screen, circles)
    pymunk.pygame_util.draw(screen, line)
    pymunk.pygame_util.draw(screen, line2)
    pymunk.pygame_util.draw(screen, line3)
    pymunk.pygame_util.draw(screen, line4)
    pymunk.pygame_util.draw(screen, line5)
    pymunk.pygame_util.draw(screen, line6)
    pymunk.pygame_util.draw(screen, line7)
    

    pygame.display.flip()
    
    space.gravity = (wind, gravity)

    space.step(1/60.0)

sys.exit()
