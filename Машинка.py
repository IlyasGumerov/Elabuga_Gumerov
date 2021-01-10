import os, sys

import pygame

size = width, height = 600, 95
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Машинка')


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    # прозрачный цвет
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Car(pygame.sprite.Sprite):
    image = load_image("car2.png")
    image1 = pygame.transform.flip(image, True, False)

    def __init__(self, group):
        super().__init__(group)
        self.image = Car.image
        self.c = 0
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        if self.rect.x + 95 >= 550:
            self.c = 1
        elif self.rect.x == 0:
            self.c = 0

        if self.c == 0:
            t = 2
            self.image = Car.image
        else:
            t = -2
            self.image = Car.image1
        self.rect.x = self.rect.x + t
        clock.tick(25)




all_sprites = pygame.sprite.Group()
Car(all_sprites)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()

pygame.quit()
