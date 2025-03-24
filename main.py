import pygame as pg

import sys

pg.init()

WIDTH, HEIGHT = 600, 600

ROOT = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("TEST")

fpslock = 60

clock = pg.time.Clock()


while True:
    clock.tick(fpslock)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    ROOT.fill((255,255,255))

    pg.draw.rect(ROOT, (255,0,0), (WIDTH//2, HEIGHT//2,100, 100))

    pg.display.update()