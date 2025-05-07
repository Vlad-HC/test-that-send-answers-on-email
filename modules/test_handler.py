from modules.load_system import load


class Test_handler:
    def __init__(self):
        self.student_name_surname: str = None
        self.ind = 0
        self.answers = {}
        self.questions, self.options = load()
        self.generate_ans()
        self.spended_time = 0
        self.unfocused_window_count = 0

    def generate_ans(self):
        for i in self.questions:
            self.answers[f"{i}"] = [None, None]

    def save_answer(self, answer: str, time: int):
        question = self.questions[self.ind]
        if self.answers[f"{question}"][1] != 0 and self.answers[f"{question}"][1] != None:
            self.answers[f"{question}"] = [
                answer,
                time + self.answers[f"{question}"][1],
            ]
        else:
            self.answers[f"{question}"] = [answer, time]

        for i in self.answers:
            print(f"{i} : {self.answers[i]}")

    def parse_time(self, time: int):
        return f"{time / 1000} s"

    def get_previous_answer(self) -> list[str]:
        prev_answer = self.answers[self.questions[self.ind]][0]
        return prev_answer
