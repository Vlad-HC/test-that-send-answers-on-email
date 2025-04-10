import pygame as pg
from pygame import Rect, Surface
from modules.answer import Answer
from modules.colors import *


class Answers_group:
    def __init__(
        self,
        answers: list[str],
        pos: tuple,
        max_width: int,
        gap: int = 10,
        multiple_answers: bool = False,
    ):
        self.multiple_answers = multiple_answers
        self.gap = gap
        self.str_answers = answers
        self.pos = pos
        self.answer_pos = pos
        self.max_width = max_width
        self.answers = self.create_answers()
        self.last_active_answer: Answer = None

    def create_answers(self) -> list[Answer]:
        answers = []
        for i, str_answer in enumerate(self.str_answers):
            if len(answers) != 0:
                self.answer_pos = (
                    self.answer_pos[0],
                    self.answer_pos[1] + answer.rect.height + self.gap,
                )
            print(self.answer_pos)
            if len(answers) != 0:
                answer = Answer(
                    str_answer,
                    self.answer_pos,
                    self.max_width,
                    (i + 1),
                )
            else:
                answer = Answer(
                    str_answer,
                    (self.pos[0], self.pos[1]),
                    self.max_width,
                    (i + 1),
                )
            answers.append(answer)
        return answers

    def handle_answers(self, event):
        for answer in self.answers:
            answer.handle(event, answer.rect)
            if answer.clicked:
                if self.last_active_answer != None and self.multiple_answers != True:
                    if self.last_active_answer != answer:
                        self.answers[
                            self.answers.index(self.last_active_answer)
                        ].active = False
                answer.active = not answer.active
                self.last_active_answer = answer
            if answer.hovered:
                answer.background_color = white

            else:
                answer.background_color = hover_green

    def draw(self, root: pg.Surface):
        for answer in self.answers:
            answer.draw(root)
