import os, sys

import pygame

size = width, height = 600, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Game Over')


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


class Game(pygame.sprite.Sprite):
    image = load_image("gameover.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Game.image
        self.c = 0
        self.rect = self.image.get_rect()
        self.rect.x = -600
        self.rect.y = 0

    def update(self):
        if self.rect.x != 0:
            self.rect.x = self.rect.x + 8  # Для плавности картинки частота 25 кад/с
            clock.tick(FPS)  # тогда по 8 пикс через 40 милисекунд


all_sprites = pygame.sprite.Group()
Game(all_sprites)
FPS = 25
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("blue"))
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()

pygame.quit()
