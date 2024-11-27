import pygame
import os
import random

pygame.init()

## making game window

width, height = 800, 600
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Layne Doffing Final")

"""loading character sprites onto screen"""
def load_image(name, scale=1):
    fullname = os.path.join(directory,name)
    image = pg.image.load(fullname)

    size= image.get_size()
    size==(size[0]*scale,size[1],*scale)
    image= pg.transform.scale(image, size)
    image= image.convert()

    return image, image.get_rect()

class Character(pygame.sprite.Sprite):
    """contains a character's name, text color, font, and sprite images"""

    def __innit__(self):
        """initializing sprite"""
        pg.sprite.Sprite.__innit__(self)
        self.image, self.rect = load_image("x", 1)



## game loop

def main():

    game_running = True

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running == False
                pygame.quit()
                break

main()