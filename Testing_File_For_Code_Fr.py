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
        self.choice_buttons = []  # Store buttons to clear them later

        self.question_label = tk.Label(
            self.frame, textvariable=self.question_text, font=("Helvetica", 16),
            bg=bg_color, wraplength=350, justify="center"
        )
        self.question_label.pack(pady=20)

        # Frame to hold choices
        self.choices_frame = Frame(self.frame, bg=bg_color)
        self.choices_frame.pack(pady=10)

        self.next_button = tk.Button(self.frame, text="Next Question", command=self.load_question)
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.current_index < len(question_dictionary):
            # 1. Clear previous choices
            for btn in self.choice_buttons:
                btn.destroy()
            self.choice_buttons = []
            self.selected_choice.set(None)

            # 2. Set the question text
            current_q = question_dictionary[self.current_index]["question"]
            self.question_text.set(current_q)

            # 3. Create new radio buttons for the choices
            choices = question_dictionary[self.current_index]["choices"]
            for choice in choices:
                rb = Radiobutton(self.choices_frame, text=choice, variable=self.selected_choice,
                                 value=choice, font=("Arial", 12), bg=bg_color)
                rb.pack(anchor="w", pady=5)
                self.choice_buttons.append(rb)

            self.current_index += 1
        else:
            # Clear screen when completed
            self.question_label.pack_forget()
            self.choices_frame.pack_forget()
            self.question_text.set("Quiz Completed!")
            self.next_button.config(state="disabled")
