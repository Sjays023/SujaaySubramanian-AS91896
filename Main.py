import tkinter as tk

from tkinter import *

import random


#variables
name = []
questions_asked = []
score = 0
questionnumber = 0

bg_color = "#fcf0ea"

questions_with_answers = {
    1: ["What Wonder is this?",
        "The Great Wall Of China", "Petra", "Machu Picchu",
        "Christ The Redeemer", 4],

    2: ["What Wonder is this?",
        "Taj Mahal", "Petra", "Colosseum",
        "Christ The Redeemer", 2],

    3: ["What Wonder is this?",
        "The Great Wall Of China", "Chichén Itzá ", "Machu Picchu",
        "Christ The Redeemer", 3],

    4: ["What Wonder is this?",
        "The Great Wall Of China", "Petra", "Chichén Itzá ",
        "Colosseum", 4],

    5: ["What Wonder is this?",
        "Taj Mahal", "Petra", "Machu Picchu",
        "Chichén Itzá ", 1],

    6: ["What Wonder is this?",
        "The Great Wall Of China", "Petra", "Chichén Itzá",
        "Christ The Redeemer", 1],

    7: ["What Wonder is this?",
        "The Great Wall Of China", "Petra", "Machu Picchu",
        "Chichén Itzá", 4],

    8: ["What country is this Wonder in?",
        "China", "Jordan", "Mexico",
        "Brazil", 3],

    9: ["What country is this Wonder in?",
        "China ", "India", "Mexico",
        "Brazil", 1],

    10: ["What country is this Wonder in?",
        "Italy", "Peru", "Italy",
        "Brazil", 4],

    11: ["What country is this Wonder in?",
        "China", "Jordan", "Peru",
        "Brazil", 2],

    12: ["What country is this Wonder in?",
        "China", "Jordan", "Peru",
        "India", 3],

    13: ["What country is this Wonder in?",
        "Italy", "Jordan", "Mexico",
        "Brazil", 1],

    14: ["What country is this Wonder in?",
        "China", "Jordan", "India",
        "Brazil", 3],


}


def randomiser():
    global question_number


    if len(questions_asked) >= len(questions_with_answers):
        print("All questions have been answered!")
        return


    question_number = random.randint(0, len(questions_with_answers) - 1)


    if question_number not in questions_asked:
        questions_asked.append(question_number)
    else:

        randomiser()

class Startingpage:
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(parent, bg=bg_color)
        self.frame.pack(fill="both", expand=True)


        Label(self.frame,
              text="7 Wonders of The World Quiz",
              font=("sans-seriff", 14),
              bg=bg_color).pack(pady=10)















