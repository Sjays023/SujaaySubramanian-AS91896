import random
import tkinter as tk
from tkinter import messagebox, Frame, Label, Entry, Button, PhotoImage, Radiobutton

import self

# Variables
name = []
questions_asked = []
score = 0
question_number = 0
bg_color = "#fcf0ea"


question_dictionary = {
    0: {
"question": "What Wonder is this?",
"choices": ["The Great Wall Of China", "Petra", "Machu Picchu", "Christ The Redeemer",],
"answer": "Christ The Redeemer" },


    1: {
"question": "What Wonder is this?",
"choices": ["Taj Mahal", "Petra", "Colosseum", "Christ The Redeemer",],
"answer": "Petra" },


    2: {
"question": "What Wonder is this?",
"choices": ["The Great Wall Of China", "Chichén Itzá", "Machu Picchu", "Christ The Redeemer",],
"answer": "Machu Picchu" },


    3: {
"question": "What Wonder is this?",
"choices": ["The Great Wall Of China", "Petra", "Chichén Itzá", "Colosseum",],
"answer": "Colosseum" },


    4: {
"question": "What Wonder is this?",
"choices": ["Taj Mahal", "Petra", "Machu Picchu", "Chichén Itzá",],
"answer": "Taj Mahal" },

    5: {
"question": "What Wonder is this?",
"choices": ["The Great Wall Of China", "Petra", "Chichén Itzá", "Christ The Redeemer",],
"answer": "The Great Wall Of China" },



    6: {
"question": "What Wonder is this?",
"choices": ["The Great Wall Of China", "Petra", "Machu Picchu", "Chichén Itzá",],
"answer": "Chichén Itzá" },


    7: {
"question": "Which Country is this Wonder in?",
"choices": ["China", "Jordan", "Mexico", "Brazil",],
"answer": "Mexico" },



    8: {
"question": "Which Country is this Wonder in?",
"choices": ["China", "India", "Mexico", "Brazil",],
"answer": "China" },



    9: {
"question": "Which Country is this Wonder in?",
"choices": [ "Italy", "Peru", "Greece", "Brazil",],
"answer": "Brazil" },




    10: {
"question": "Which Country is this Wonder in?",
"choices": ["China", "Jordan", "Peru", "Brazil",],
"answer": "Jordan" },




    11: {
"question": "Which Country is this Wonder in?",
"choices": ["China", "Jordan", "Peru", "India",],
"answer": "Peru" },




    12: {
"question": "Which Country is this Wonder in?",
"choices": ["Italy", "Jordan", "Mexico", "Brazil",],
"answer": "Italy" },




    13: {
"question": "Which Country is this Wonder in?",
"choices": ["China", "Italy", "India", "Brazil",],
"answer": "India" },

}



class Quiz:
    def __init__(self, parent):
        self.question_text = tk.StringVar()
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack(fill="both", expand=True)


        self.bg_label = Label(self.frame, bg=bg_color)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.current_index = 0
        self.selected_choice = tk.StringVar()
        self.choice_buttons = []

        self.question_label = tk.Label(
            self.frame,
            textvariable=self.question_text,
            font=("Helvetica", 14),
            bg=bg_color,
            wraplength=350,
            justify="center"
        )
        self.question_label.pack(pady=20)

        self.choices_frame = Frame(self.frame, bg=bg_color)
        self.choices_frame.pack(pady=10)

        self.next_button = tk.Button(self.frame, text="Next Question", command=self.load_question)
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.current_index < len(question_dictionary):
            for btn in self.choice_buttons:
                btn.destroy()
            self.choice_buttons = []
            self.selected_choice.set(None)

            current_q = question_dictionary[self.current_index]["question"]
            self.question_text.set(current_q)
            choices = question_dictionary[self.current_index]["choices"]

            for choice in choices:
                rb = Radiobutton(self.choices_frame, text=choice, variable=self.selected_choice,
                                 value=choice, font=("Arial", 12), bg=bg_color)
                rb.pack(anchor="w", pady=5)
                self.choice_buttons.append(rb)

            self.current_index += 1
        else:
            self.question_label.pack_forget()
            self.choices_frame.pack_forget()
            self.question_text.set("Quiz Completed!")
            self.next_button.config(state="disabled")




class Startingpage:
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack(fill="both", expand=True)


        self.bg_label = Label(self.frame, image=bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.name_label = Label(self.frame, text="Enter your name:", font=("Arial", 14), bg=bg_color)
        self.name_label.place(x=100, y=50)

        self.entry = Entry(self.frame, font=("Arial", 14))
        self.entry.pack(pady=10)
        self.entry.place(x=67, y=75)

        Button(self.frame, text="Start Quiz", font=("Arial", 25), bg="#f9af8f", command=self.start_quiz).place(x=277, y=580)


        Button(self.frame, text="Exit", font=("Helvetica", 28), bg="#f9af8f", fg="black", command=self.parent.destroy).place(x=790, y=575)



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


    q1_image = PhotoImage(file="Photos/q1page.png")


    try:
        bg_image = PhotoImage(file="Photos/starting_page.png")
    except Exception:

        bg_image = PhotoImage()
        print("Warning: Photos/starting_page.png not found.")

    v = tk.IntVar()
    app = Startingpage(root)
    root.mainloop()

