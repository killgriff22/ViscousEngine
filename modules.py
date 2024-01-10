import pygame
from config import *
def render(screen,objects,poses,bg=(255,255,255)):
    screen.fill(bg)
    for obj,pos in zip(objects,poses):
        screen.blit(obj,pos)
    pygame.display.update()