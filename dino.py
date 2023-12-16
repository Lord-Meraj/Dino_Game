import os
import sys
import pygame

WIDTH = 623
HEIGHT = 150

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino")


class Dino:
    def __init__(self):
        self.width = 44
        self.height = 44
        self.x = 10
        self.y = 80
        self.texture_num = 0
        self.set_texture()
        self.show()

    def update(self, loops):
        if loops % 4 == 0:
            self.texture_num = (self.texture_num + 1) % 3
            self.set_texture()

    def show(self):
        screen.blit(self.texture, (self.x, self.y))

    def set_texture(self):
        path = os.path.join(f"assets/image/dino{self.texture_num}.png")
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))


class BG:
    def __init__(self, x):
        self.width = WIDTH
        self.height = HEIGHT
        self.x = x
        self.y = 0
        self.set_texture()
        self.show()

    def update(self, dx):
        self.x += dx
        if self.x <= -WIDTH:
            self.x = WIDTH

    def show(self):
        screen.blit(self.texture, (self.x, self.y))

    def set_texture(self):
        path = os.path.join("assets/image/bg.png")
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))


class Game:
    def __init__(self):
        self.bg = [BG(x=0), BG(x=WIDTH)]
        self.dino = Dino()
        self.speed = 3


def main():
    game = Game()
    dino = game.dino

    clock = pygame.time.Clock()

    looops = 0

    # main loop
    while True:
        looops += 1
        # BG
        for bg in game.bg:
            bg.update(-game.speed)
            bg.show()

        # Dino
        dino.update(looops)
        dino.show()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(80)
        pygame.display.update()


main()
