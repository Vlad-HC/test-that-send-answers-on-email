import pygame as pg
from pygame import Rect, Surface

class Button:
    def __init__(self, rect: Rect, surface:Surface, text:str, colors:tuple[tuple, tuple]):
        self.rect = rect
        self.x = self.rect.x
        self.y = self.rect.y
        self.root = surface
        self.text = text
        self.color = colors[0]
        self.hoverColor = colors[1]
        self.FONT = pg.font.SysFont("comicsans", 40)
    
    def draw(self):
        mousePos = pg.mouse.get_pos()

        if self.rect.collidepoint(mousePos):
            pg.draw.rect(self.root,self.hoverColor, self.rect)
        else:
            pg.draw.rect(self.root,self.color, self.rect)
        
        text_surface = self.FONT.render(self.text, True, (0,0,0))
        # text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        # self.root.blit(text_surface, text_rect)
    
    def is_clicked(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                return True
        return False