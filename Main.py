import random
import tkinter as tk
from tkinter import messagebox, Frame, Label, Entry, Button, Radiobutton
from PIL import Image, ImageTk

# App styling constants
bg_color = "#fcf0ea"

question_dictionary = {
    0: {
        "question": "What Wonder is this?",
        "choices": ["The Great Wall Of China", "Petra", "Machu Picchu", "Christ The Redeemer" ,],
        "answer": "Christ The Redeemer",
        "image": "CTR.jpg"},


    1: {
        "question": "What Wonder is this?",
        "choices": ["Taj Mahal", "Petra", "Colosseum", "Christ The Redeemer" ,],
        "answer": "Petra",
        "image" : "P.jpeg"},


    2: {
        "question": "What Wonder is this?",
        "choices": ["The Great Wall Of China", "Chichén Itzá", "Machu Picchu", "Christ The Redeemer" ,],
        "answer": "Machu Picchu",
        "image" : "MP.jpg" },


    3: {
        "question": "What Wonder is this?",
        "choices": ["The Great Wall Of China", "Petra", "Chichén Itzá", "Colosseum" ,],
        "answer": "Colosseum",
        "image" : "C.jpg" },


    4: {
        "question": "What Wonder is this?",
        "choices": ["Taj Mahal", "Petra", "Machu Picchu", "Chichén Itzá" ,],
        "answer": "Taj Mahal",
        "image" : "TM.jpeg" },

    5: {
        "question": "What Wonder is this?",
        "choices": ["The Great Wall Of China", "Petra", "Chichén Itzá", "Christ The Redeemer" ,],
        "answer": "The Great Wall Of China",
        "image" : "TGWOC.jpg" },



    6: {
        "question": "What Wonder is this?",
        "choices": ["The Great Wall Of China", "Petra", "Machu Picchu", "Chichén Itzá" ,],
        "answer": "Chichén Itzá",
        "image" : "CI.jpg" },


    7: {
        "question": "Which Country is this Wonder in?",
        "choices": ["China", "Jordan", "Mexico", "Brazil" ,],
        "answer": "Mexico",
        "image" : "CI.jpg" },



    8: {
        "question": "Which Country is this Wonder in?",
        "choices": ["China", "India", "Mexico", "Brazil" ,],
        "answer": "China",
        "image" : "TGWOC.jpg" },



    9: {
        "question": "Which Country is this Wonder in?",
        "choices": [ "Italy", "Peru", "Greece", "Brazil" ,],
        "answer": "Brazil",
        "image" : "CTR.jpg" },




    10: {
        "question": "Which Country is this Wonder in?",
        "choices": ["China", "Jordan", "Peru", "Brazil" ,],
        "answer": "Jordan",
        "image" : "P.jpeg" },




    11: {
        "question": "Which Country is this Wonder in?",
        "choices": ["China", "Jordan", "Peru", "India" ,],
        "answer": "Peru",
        "image" : "MP.jpg" },




    12: {
        "question": "Which Country is this Wonder in?",
        "choices": ["Italy", "Jordan", "Mexico", "Brazil" ,],
        "answer": "Italy",
        "image" : "C.jpg" },




    13: {
        "question": "Which Country is this Wonder in?",
        "choices": ["China", "Italy", "India", "Brazil" ,],
        "answer": "India",
        "image" : "TM.jpeg" },

}


class Quiz:
    def __init__(self, parent, username):
        self.parent = parent
        self.username = username
        self.frame = Frame(parent, bg=bg_color)
        self.frame.pack(fill="both", expand=True)

        self.current_index = 0
        self.score = 0
        self.selected_choice = tk.StringVar()
        self.choice_buttons = []

        self.question_text = tk.StringVar()
        self.question_label = tk.Label(
            self.frame, textvariable=self.question_text, font=("Helvetica", 14),
            bg=bg_color, wraplength=350, justify="center"
        )
        self.question_label.pack(pady=20)

        self.choices_frame = Frame(self.frame, bg=bg_color)
        self.choices_frame.pack(pady=10)

        self.image_label = Label(self.frame, bg=bg_color)
        self.image_label.pack(pady=10)

        self.next_button = tk.Button(self.frame, text="Submit Answer", command=self.check_and_next)
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.current_index < len(question_dictionary):
            for btn in self.choice_buttons:
                btn.destroy()
            self.choice_buttons = []
            self.selected_choice.set("")

            current_q = question_dictionary[self.current_index]
            self.question_text.set(current_q["question"])

            for choice in current_q["choices"]:
                rb = tk.Radiobutton(
                    self.choices_frame, text=choice, variable=self.selected_choice,
                    value=choice, font=("Helvetica", 12), bg=bg_color, anchor="w"
                )
                rb.pack(fill="x", pady=5)
                self.choice_buttons.append(rb)

            image_path = "Photos/" + current_q["image"]
            try:
                opened_img = Image.open(image_path)
                resized_img = opened_img.resize((300, 200))
                tk_img = ImageTk.PhotoImage(resized_img)
                self.image_label.config(image=tk_img)
                self.image_label.image = tk_img
            except Exception:
                self.image_label.config(image="")
                print(f"Warning: Could not load image {image_path}")
        else:
            messagebox.showinfo("Quiz Finished",
                                f"Great job {self.username}!\nYour final score is: {self.score}/{len(question_dictionary)}")
            self.parent.destroy()

    def check_and_next(self):
        if not self.selected_choice.get():
            messagebox.showwarning(title="Selection Missing", message="Select one of the choices!")
            return

        correct_answer = question_dictionary[self.current_index]["answer"]
        if self.selected_choice.get() == correct_answer:
            self.score += 1

        # FIXED: This now runs regardless of whether the answer was right or wrong
        self.current_index += 1
        self.load_question()


class Startingpage:
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(parent, bg=bg_color)
        self.frame.pack(fill="both", expand=True)

        self.bg_label = Label(self.frame, image=bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.name_label = Label(self.frame, text="Enter your name:", font=("Arial", 14), bg=bg_color)
        self.name_label.place(x=100, y=50)

        self.entry = Entry(self.frame, font=("Arial", 14))
        self.entry.place(x=67, y=75)

        Button(self.frame, text="Start Quiz", font=("Arial", 25), bg="#f9af8f", command=self.start_quiz).place(x=277,
                                                                                                               y=580)
        Button(self.frame, text="Exit", font=("Helvetica", 28), bg="#f9af8f", fg="black",
               command=self.parent.destroy).place(x=790, y=575)

    def start_quiz(self):
        username = self.entry.get().strip()
        if username:
            self.frame.destroy()
            Quiz(self.parent, username)  # FIXED: Pass the username string here directly
        else:
            messagebox.showerror("Error", "Please enter your name.")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("7 Wonders Of The World Quiz")
    root.geometry("1207x675")
    root.configure(bg=bg_color)

    try:
        bg_image = tk.PhotoImage(file="Photos/starting_page.png")
    except Exception:
        bg_image = tk.PhotoImage()
        print("Warning: Photos/starting_page.png not found.")

    app = Startingpage(root)
    root.mainloop()
