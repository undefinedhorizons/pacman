import pygame

from myengine.display import Display


class Sprite:
    sprite = None

    def __init__(self, x, y, height=None, width=None, color=None, filename=None):
        self.sprite = pygame.sprite.Sprite()
        if filename is None:
            self.sprite.image = pygame.Surface([width, height])
            self.sprite.image.fill(color)
        else:
            self.sprite.image = pygame.image.load(filename).convert()
            self.sprite.image.set_colorkey(color)

        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.topleft = (x, y)

    def move(self, d_x, d_y):
        Display.move_sprite(self, d_x, d_y)

    '''
    def update(self, *args, **kwargs):
        self.sprite.update(args, kwargs);
        pass
    '''

    def get_rect(self):
        return self.sprite.rect

    def set_rect(self, rect):
        self.sprite.rect = rect


class Group:
    group = None
    sprites = None

    def __init__(self):
        self.group = pygame.sprite.Group()
        self.sprites = []

    def add(self, sprite):
        self.group.add(sprite.sprite)
        self.sprites.append(sprite)

    def update(self, *args, **kwargs):
        self.group.update(args, kwargs)

        for sprite in self.sprites:
            sprite.update(args, kwargs)


def spritecollide(sprite, group, dokill, collided=None):
    return pygame.sprite.spritecollide(sprite.sprite, group.group, dokill, collided)


def rotateimage(image, angle=0):
    return pygame.transform.rotate(image, angle)
