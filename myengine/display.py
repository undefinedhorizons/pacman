import pygame


class Display:
    screen = None
    font = None

    def __init__(self):
        pass

    @staticmethod
    def set_mode(width, height):
        Display.screen = pygame.display.set_mode((width, height))
        Display.font = pygame.font.Font(None, 35)

    @staticmethod
    def set_caption(text):
        pygame.display.set_caption(text)

    @staticmethod
    def clear(color=(0, 0, 0)):
        Display.screen.fill(color)

    @staticmethod
    def render():
        pygame.display.flip()

    @staticmethod
    def get_size():
        return pygame.display.get_surface().get_size()

    @staticmethod
    def set_label(label, x=0, y=0):
        Display.screen.blit(label.label, (x, y))

    @staticmethod
    def set_line(context, color, start_pos, stop_pos,  width=1):
        pygame.draw.line(context, color, start_pos, stop_pos, width)

    @staticmethod
    def set_ellipse(context, color, rect):
        pygame.draw.ellipse(context, color, rect)

    @staticmethod
    def set_group(group):
        group.group.draw(Display.screen)

    @staticmethod
    def set_sprite(sprite):
        Display.screen.blit(sprite.sprite.image, sprite.sprite.rect)

    @staticmethod
    def move_sprite(sprite, d_x, d_y):
        w, h = Display.get_size()

        sprite.sprite.rect.x += d_x
        sprite.sprite.rect.y += d_y
        if sprite.sprite.rect.right < 0:
            sprite.sprite.rect.left = w
        elif sprite.sprite.rect.left > w:
            sprite.sprite.rect.right = 0
        if sprite.sprite.rect.bottom < 0:
            sprite.sprite.rect.top = h
        elif sprite.sprite.rect.top > h:
            sprite.sprite.rect.bottom = 0

