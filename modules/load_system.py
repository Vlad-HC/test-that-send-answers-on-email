import json


def load():
    questions = []
    answers = []
    with open('questions_ex.json') as f:
        source = json.load(f)
    for i in source['questions']:
        questions.append(i["question"])
        answers.append(i["options"])
    return questions, answers
