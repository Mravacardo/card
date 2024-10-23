import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

display_surface=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.diplay.set_caption("Christmas Greeting Card")

img=pygame.image.load("background1.jpg")
image = pygame.transform.scale(img, (WIDTH,HEIGHT))


while(True):
    font=pygame.font.SysFont("Times New Roman",72)
    text=font.render("Merry",True,(0,0,0))
    text2=font.render("Christmas",True,(0,0,0))
    display_surface.fill((255,255,255))
    display_surface.blit(image,(0,0))
    display_surface.blit(text,(210,180))
    display_surface.blit(text2,(180,264))
    pygame.display.update()
    time.sleep(2)

    image2
