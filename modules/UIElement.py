import pygame as pg


class UIElement:
    instances = []

    def __init__(self):

        self.hovered = False
        self.clicked = False
        self.pressed = False
        UIElement.instances.append(self)

    def is_clicked(self, event, rect: pg.Rect):
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1 and rect.collidepoint(event.pos):
                return True
        return False

    def is_pressed(self, event, rect: pg.Rect):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and rect.collidepoint(event.pos):
                return True
        return False

    def is_hovered(self, rect: pg.Rect):
        mousePos = pg.mouse.get_pos()

        if rect.collidepoint(mousePos):
            return True
        else:
            return False

    def handle(self, event, rect: pg.Rect):
        self.clicked = self.is_clicked(event, rect)
        self.pressed = self.is_pressed(event, rect)
        self.hovered = self.is_hovered(rect)

    def draw(self):
        pass

    @classmethod
    def draw_ui(cls):
        for instance in cls.instances:
            instance.draw()

    @classmethod
    def swap(cls, i1, i2):
        cls.instances[i1], cls.instances[i2] = cls.instances[i2], cls.instances[i1]

    @classmethod
    def swap_instances(cls, a, b):
        i1 = cls.instances.index(a)
        i2 = cls.instances.index(b)
        cls.swap(i1, i2)

    @classmethod
    def remove(cls, instance):
        if instance in cls.instances:
            cls.instances.remove(instance)

    @classmethod
    def add(cls, instance):
        if instance not in cls.instances:
            cls.instances.append(instance)

    @classmethod
    def check(cls, instance):
        return True if instance in cls.instances else False

    @classmethod
    def replace_instance(cls, old_instance, new_instance):
        if old_instance in cls.instances and new_instance not in cls.instances:
            idx = cls.instances.index(old_instance)
            cls.instances[idx] = new_instance

    @classmethod
    def clear(cls):
        cls.instances = []
