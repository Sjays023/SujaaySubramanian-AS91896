import random
import tkinter as tk
from tkinter import messagebox, Frame, Label, Entry, Button, Radiobutton, PhotoImage
from PIL import Image, ImageTk

from Testing_File_For_Code_Fr import ResultsPage

# Colour theme for the quiz
bg_color = "#fcf0ea"
#Question dictionary holds all the questions, answers and images that correlate with each-other
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
        "question": "Which Country is Chichén Itzá in?",
        "choices": ["China", "Jordan", "Mexico", "Brazil" ,],
        "answer": "Mexico",
        "image" : "CI.jpg" },



    8: {
        "question": "Which Country is The Great Wall Of China in?",
        "choices": ["China", "India", "Mexico", "Brazil" ,],
        "answer": "China",
        "image" : "TGWOC.jpg" },



    9: {
        "question": "Which Country is Christ The Redeemer in?",
        "choices": [ "Italy", "Peru", "Greece", "Brazil" ,],
        "answer": "Brazil",
        "image" : "CTR.jpg" },




    10: {
        "question": "Which Country is Petra in?",
        "choices": ["China", "Jordan", "Peru", "Brazil" ,],
        "answer": "Jordan",
        "image" : "P.jpeg" },




    11: {
        "question": "Which Country is Machu Picchu in?",
        "choices": ["China", "Jordan", "Peru", "India" ,],
        "answer": "Peru",
        "image" : "MP.jpg" },




    12: {
        "question": "Which Country is the Colosseum in?",
        "choices": ["Italy", "Jordan", "Mexico", "Brazil" ,],
        "answer": "Italy",
        "image" : "C.jpg" },




    13: {
        "question": "Which Country is the Taj Mahal in?",
        "choices": ["China", "Italy", "India", "Brazil" ,],
        "answer": "India",
        "image" : "TM.jpeg" },

}

#controls the interface
class Quiz:
    #create the quiz screen and makes variables
    def __init__(self, parent, username):
        self.parent = parent
        self.username = username
        self.frame = Frame(parent, bg=bg_color)
        self.frame.pack(fill="both", expand=True)
        #variables for the quiz
        self.current_index = 0
        self.score = 0
        self.selected_choice = tk.StringVar()
        self.choice_buttons = []
        #displays the current question
        self.question_text = tk.StringVar()
        self.question_label = tk.Label(
            self.frame, textvariable=self.question_text, font=("Helvetica", 14),
            bg=bg_color, wraplength=350, justify="center"
        )
        self.question_label.pack(pady=20)
        #displays the current choices
        self.choices_frame = Frame(self.frame, bg=bg_color, width=400, height=200)
        self.choices_frame.pack(pady=10)

        #displays the image for the question
        self.image_label = Label(self.frame, bg=bg_color)
        self.image_label.pack(pady=10)
        #places the submit button on the page
        self.next_button = tk.Button(self.frame, text="Submit Answer",  font=("Helvetica", 28), bg="#417a58", fg="black", command=self.check_and_next)
        self.next_button.pack(pady=50, padx=50)

        self.load_question()

        #loads the current question choices and image
    def load_question(self):
        if self.current_index < len(question_dictionary):
            for btn in self.choice_buttons:
                #this breaks the buttons
                btn.destroy()
            self.choice_buttons = []
            self.selected_choice.set("")
            #gets the current question
            current_q = question_dictionary[self.current_index]
            #displays the text i stored in the dictionary under "question"
            self.question_text.set(current_q["question"])
            #set places for the options to be placed
            specific_positions = [
                (50, 20),
                (50, 70),
                (50, 120),
                (50, 170)
            ]
            #creates a radiobutton for each option
            for i, choice in enumerate(current_q["choices"]):
                rb = tk.Radiobutton(
                    self.choices_frame, text=choice, variable=self.selected_choice,
                    value=choice, font=("Helvetica", 12), bg=bg_color, anchor="w", padx=10, pady=10 , fg="black"

                )
                #places the buttons on the pages
                x_pos, y_pos = specific_positions[i]
                rb.place(x=x_pos, y=y_pos)
                self.choice_buttons.append(rb)
            #loads the question image from the dictionary
            image_path = "Photos/" + current_q["image"]
            try:
                opened_img = Image.open(image_path)
                #reesizes the image to the set pixels to look aesthetic
                resized_img = opened_img.resize((300, 200))
                tk_img = ImageTk.PhotoImage(resized_img)
                self.image_label.config(image=tk_img)
                self.image_label.image = tk_img
            except Exception:
                self.image_label.config(image="")
                print(f"Warning: Could not load image {image_path}")
        else:
            self.frame.destroy()
            ResultsPage(self.parent, self.username, self.score)




    #checks if the answers for the quiz inputted from the user are correct or not
    def check_and_next(self):
        if not self.selected_choice.get():
            messagebox.showwarning(title="Selection Missing", message="Select one of the choices!")
            return

        correct_answer = question_dictionary[self.current_index]["answer"]
        if self.selected_choice.get() == correct_answer:
            self.score += 1
        self.current_index += 1
        self.load_question()
#holds all of the elements on my results page
class ResultsPage:
    def __init__(self, parent, username, score):
        self.parent = parent
        #sets the background of the code the overall color
        self.frame = Frame(parent, bg=bg_color)
        self.frame.pack(fill="both", expand=True)
        #Displays the final text on the results page in a big font
        Label(self.frame, text="Quiz Finished", font=("Helvetica", 34, "bold"),
            bg=bg_color).pack(pady=(80, 20))
            #message to the user about finishing the quiz
        Label(self.frame, text=f"Well done, {username}", font=("Helvetica", 18, "bold"),
              bg=bg_color,
            ).pack()
        #displays the score on the page
        Label(self.frame, text=f"{score}/{len(question_dictionary)}", font=("Helvetica", 36, "bold"),
              bg=bg_color,
              fg="#333333").pack(pady=(40))

        total_questions = len(question_dictionary)
        pass_threshold = total_questions / 2

        if score >=pass_threshold:
            feedback_text = "Fantastic Job! You really know your world wonders!"
            feedback_color = "green"
        else:
            feedback_text = "Unlucky, try and practice learning more about the 7 Wonders before you try again!"
            feedback_color = "red"
        #colors the feedback depending on the score achieved
        Label(self.frame, text=feedback_text, font=("Helvetica", 14, "italic"), bg=bg_color, fg=feedback_color).pack(pady=(0, 30))
        #places an exit button on the page
        Button(
            self.frame,
        text="Exit",
            font=("Helvetica", 18),
            bg='#417a58',
            fg="white",
            command=parent.destroy).pack(pady=20)

#places all of the elemnts in a clean class
class Startingpage:
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(parent, bg=bg_color)
        self.frame.pack(fill="both", expand=True)
        #colours the background
        self.bg_label = Label(self.frame, image=bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        #Displays text for the user to input their name
        self.name_label = Label(self.frame, text="Enter your name:", font=("Arial", 14), bg=bg_color)
        self.name_label.place(x=100, y=50)

        self.entry = Entry(self.frame, font=("Arial", 14))
        self.entry.place(x=67, y=75)

        #2 buttons to start the quiz and exit the quiz
        Button(self.frame, text="Start Quiz", font=("Arial", 25), bg="#f9af8f", command=self.start_quiz).place(x=277,
                                                                                                               y=580)
        Button(self.frame, text="Exit", font=("Helvetica", 28), bg="#f9af8f", fg="black",
               command=self.parent.destroy).place(x=790, y=575)
        #command to start the quiz is defined here
    def start_quiz(self):
        username = self.entry.get().strip()
        if username:
            self.frame.destroy()
            Quiz(self.parent, username)
        else:
            messagebox.showerror("Error", "Please enter your name.")

    #the main tkinter page that everything runs on
if __name__ == "__main__":
    root = tk.Tk()
    root.title("7 Wonders Of The World Quiz")
    root.geometry("1207x675")
    root.configure(bg=bg_color)
#displays the page for the starting page
    try:
        bg_image = tk.PhotoImage(file="Photos/starting_page.png")
    except Exception:
        bg_image = tk.PhotoImage()
        print("Warning: Photos/starting_page.png not found.")

    app = Startingpage(root)
    root.mainloop()
