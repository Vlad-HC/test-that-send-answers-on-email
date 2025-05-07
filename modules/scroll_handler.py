from modules.UIElement import UIElement
import pygame as pg


class scroll_handler:
    def __init__(self):
        self.scrollable_elems = []
        self.scroll_distance = 30

    def add_scrollable_elems(self, elem_list: list[UIElement]):
        for elem in elem_list:
            if elem.scrollable:
                if elem not in self.scrollable_elems:
                    self.scrollable_elems.append(elem)

    def handle(self, event):
        if event.type == pg.MOUSEWHEEL:
            if event.y < 0:
                for i, elem in enumerate(self.scrollable_elems):
                    elem.rect.y -= self.scroll_distance
                    print(f"{i}: {elem.rect.y}")

            if event.y > 0:
                for i, elem in enumerate(self.scrollable_elems):
                    elem.rect.y += self.scroll_distance
                    print(f"{i}: {elem.rect.y}")

    def clear(self):
        self.scrollable_elems = []
