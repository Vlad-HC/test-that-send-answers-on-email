import pygame as pg
from pygame import Rect, Surface
from modules.answer import Answer
from modules.colors import *
from modules.UIElement import UIElement


class Answers_group(UIElement):
    def __init__(
        self,
        root: Surface,
        str_answers: list[str],
        pos: tuple,
        max_width: int,
        gap: int = 10,
        multiple_answers: bool = False,
    ):
        super().__init__()
        self.scrollable = False
        self.root = root
        self.multiple_answers = multiple_answers
        self.gap = gap
        self.str_answers = str_answers
        self.pos = pos
        self.answer_pos = pos
        self.max_width = max_width
        self.answers = self.create_answers()
        self.last_active_answer: Answer = None

    def create_answers(self) -> list[Answer]:
        self.answers = []
        if self.str_answers != None:
            for i, str_answer in enumerate(self.str_answers):
                if len(self.answers) != 0:
                    self.answer_pos = (
                        self.answer_pos[0],
                        self.answer_pos[1] + answer.rect.height + self.gap,
                    )
                else:
                    self.answer_pos = (self.pos[0], self.pos[1])

                answer = Answer(
                    self.root,
                    str_answer,
                    self.answer_pos,
                    self.max_width,
                    (i + 1),
                )
                self.answers.append(answer)
            return self.answers

    def handle(self, event):
        for answer in self.answers:
            answer.handle(event, answer.rect)
            if answer.clicked:
                if self.last_active_answer != None and self.multiple_answers != True:
                    if self.last_active_answer != answer:
                        self.answers[self.answers.index(self.last_active_answer)].active = False
                answer.active = not answer.active
                self.last_active_answer = answer
            if answer.hovered:
                answer.background_color = white

            else:
                answer.background_color = hover_green

    def get(self):
        lst = [i.textbox.text for i in self.answers if i.active]
        return lst if len(lst) > 0 else None

    def set_previous(self, prev_ans: list[str]):
        if prev_ans == None:
            return
        else:
            for prev_ans_str in prev_ans:
                for answer in self.answers:
                    if prev_ans_str == answer.textbox.text:
                        self.last_active_answer = answer
                        answer.active = True

    def draw(self):
        for answer in self.answers:
            answer.draw()
