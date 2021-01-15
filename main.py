import pygame
from pygame.locals import *

pygame.init()

screen_width=400
screen_height=400

screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption('Snake')

cell_size = 10

snake_body = [[int(screen_width/2),int(screen_height/2)]]
snake_body.append([int(screen_width/2),int(screen_height/2)*cell_size])
snake_body.append([int(screen_width/2),int(screen_height/2)*cell_size*2])
snake_body.append([int(screen_width/2),int(screen_height/2)*cell_size]*3)

background = (255,200,150)
def draw_screen():
  screen.fill(background)
run = True

while run:
  draw_screen()
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      run = False
  
  pygame.display.update()

pygame.quit()