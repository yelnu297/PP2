import pygame, sys
pygame.init()

s = pygame.display.set_mode((500, 500))
pygame.display.set_caption("МЕССИ")

running = True
while running:
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
      running = False

pygame.quit()
sys.exit()