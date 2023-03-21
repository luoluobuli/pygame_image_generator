import pygame
from pygame.locals import *
import math
import random

pygame.init()

# 1. create a screen
width = 400
height = 400
screen = pygame.display.set_mode((width, height))
screen.fill((0, 0, 0))
pygame.display.set_caption('Image Generator')

# 2. draw random shapes
# 1) a big circle
x1 = random.randint(100, 300)
y1 = random.randint(100, 300)
radius1 = random.randint(100, 390)
r1 = random.randint(0, 80)
g1 = random.randint(0, 80)
b1 = random.randint(0, 80)
circle_l = pygame.draw.circle(screen, (r1, g1, b1), (x1, y1), radius1)

# 2) small circles
for i in range(1, 15):
    x2 = random.randint(0, 200)
    y2 = random.randint(0, 400)
    radius2 = random.randint(50, 100)
    r2 = random.randint(0, 255)
    g2 = random.randint(0, 255)
    b2 = random.randint(0, 255)
    pygame.draw.circle(screen, (r2, g2, b2), (x2, y2), radius2)

for i in range(1, 15):
    x3 = random.randint(201, 400)
    y3 = random.randint(0, 400)
    radius3 = random.randint(50, 100)
    r3 = random.randint(0, 255)
    g3 = random.randint(0, 255)
    b3 = random.randint(0, 255)
    pygame.draw.circle(screen, (r3, g3, b3), (x3, y3), radius3)

# 3) rectangles
for i in range(1, 20):
    x4 = random.randint(0, 400)
    y4 = random.randint(0, 400)
    w = random.randint(10, 100)
    h = random.randint(10, 100)
    r3 = random.randint(0, 255)
    g3 = random.randint(0, 255)
    b3 = random.randint(0, 255)
    pygame.draw.rect(screen, (r3, g3, b3), (x4, y4, w, h))

pygame.image.save(screen, 'drawn.png')


# make the kaleidoscope effect

image = pygame.image.load('drawn.png').convert()
screen.blit(image, (0,0))

part1 = image.subsurface(0, 0, 200, 200)
screen.blit(part1, (0,0))

part2 = pygame.transform.rotozoom(part1, 90, 1)
screen.blit(part2, (0, 200))

part3 = pygame.transform.rotozoom(part1, 180, 1)
screen.blit(part3, (200, 200))

part4 = pygame.transform.rotozoom(part1, 270, 1)
screen.blit(part4, (200, 0))

pygame.image.save(screen, 'kaleidoscope.png')


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()