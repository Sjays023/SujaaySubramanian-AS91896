import random
import tkinter as tk
from tkinter import messagebox, Frame, Label, Entry, Button, PhotoImage

# Variables
name = []
questions_asked = []
score = 0
question_number = 0
bg_color = "#fcf0ea"

questions_with_answers = {
    0: ["What Wonder is this?", "The Great Wall Of China", "Petra", "Machu Picchu", "Christ The Redeemer", 4],
    1: ["What Wonder is this?", "Taj Mahal", "Petra", "Colosseum", "Christ The Redeemer", 2],
    2: ["What Wonder is this?", "The Great Wall Of China", "Chichén Itzá", "Machu Picchu", "Christ The Redeemer", 3],
    3: ["What Wonder is this?", "The Great Wall Of China", "Petra", "Chichén Itzá", "Colosseum", 4],
    4: ["What Wonder is this?", "Taj Mahal", "Petra", "Machu Picchu", "Chichén Itzá", 1],
    5: ["What Wonder is this?", "The Great Wall Of China", "Petra", "Chichén Itzá", "Christ The Redeemer", 1],
    6: ["What Wonder is this?", "The Great Wall Of China", "Petra", "Machu Picchu", "Chichén Itzá", 4],
    7: ["What country is this Wonder in?", "China", "Jordan", "Mexico", "Brazil", 3],
    8: ["What country is this Wonder in?", "China", "India", "Mexico", "Brazil", 1],
    9: ["What country is this Wonder in?", "Italy", "Peru", "Italy", "Brazil", 4],
    10: ["What country is this Wonder in?", "China", "Jordan", "Peru", "Brazil", 2],
    11: ["What country is this Wonder in?", "China", "Jordan", "Peru", "India", 3],
    12: ["What country is this Wonder in?", "Italy", "Jordan", "Mexico", "Brazil", 1],
    13: ["What country is this Wonder in?", "China", "Jordan", "India", "Brazil", 3],
}


def randomiser():
    global question_number
    if len(questions_asked) >= len(questions_with_answers):
        print("All questions have been answered!")
        return None
    question_number = random.randint(0, len(questions_with_answers) - 1)
    if question_number not in questions_asked:
        questions_asked.append(question_number)
    else:
        randomiser()


class Quiz:
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(parent, bg=bg_color)
        self.frame.pack(fill="both", expand=True)
        Label(self.frame, text="Quiz Screen (Add your questions here!)", font=("Arial", 14), bg=bg_color).pack(pady=50)


class Startingpage:
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack(fill="both", expand=True)


        self.bg_label = Label(self.frame, image=bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)


        Label(self.frame, text="7 Wonders of The World Quiz", font=("Arial", 14), bg=bg_color).pack(pady=10)
        Label(self.frame, text="Enter your name:", font=("Arial", 14), bg=bg_color).pack(pady=10)

        self.entry = Entry(self.frame, font=("Arial", 14))
        self.entry.pack(pady=10)

        Button(self.frame, text="Start Quiz", font=("Arial", 14), bg="orange", command=self.start_quiz).pack(pady=10)
        Button(self.frame, text="Exit", font=("Helvetica", 14), bg="red", fg="white", command=self.parent.destroy).pack(
            pady=10)

    def start_quiz(self):
        username = self.entry.get().strip()
        if username:
            name.append(username)
            self.frame.destroy()
            Quiz(self.parent)
        else:
            messagebox.showerror("Error", "Please enter your name.")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("7 Wonders Of The World Quiz")
    root.geometry("1207x675")
    root.configure(bg=bg_color)


    try:
        bg_image = PhotoImage(file="Photos/starting_page.png")
    except Exception:

        bg_image = PhotoImage()
        print("Warning: Photos/starting_page.png not found.")

    app = Startingpage(root)
    root.mainloop()

#repush cause wrong messege