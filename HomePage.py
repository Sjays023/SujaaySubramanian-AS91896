import tkinter as tk
from tkinter import *

from test import canvas1


def start_quiz():
    canvas1.delete("all")

question1_lbl = tk.Label(root, text="Question 1: Where is the Taj Mahal?", fg="black", bg="#fcf4ea", font=("Verdana", 18, "bold") )
canvas1.create_window(600, 100, window=homepage.btn)











root = tk.Tk()
root.title("7 Wonders Of The World Quiz")
root.geometry("1207x675")

bg = PhotoImage(file="Photos/starting_page.png")
canvas1 = Canvas(root, width=1204, height=680)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg, anchor="nw")

#Labels and Entries

lbl1 = tk.Label(root, text="First name",
                fg="black",
                bg="#fcf4ea",
                font=("Verdana", 14, "bold"))

canvas1.create_window(67, 100, window=lbl1)
ent1 = tk.Entry(root)
canvas1.create_window(200, 100, window=ent1)


lbl2 = tk.Label(root, text="Last name",
                fg="black",
                bg="#fcf4ea",
                font=("Verdana", 14, "bold"))
canvas1.create_window(67, 130, window=lbl2)
ent2 = tk.Entry(root, width=20)
canvas1.create_window(200, 130, window=ent2)


#Buttons

button = tk.Button(root, text="Exit", width=25, command=root.destroy, relief="flat", overrelief="raised", background="#fcbe97")
canvas1.create_window(825, 610, window=button)
button.config(height=1, width=5, font=("Verdana", 24, "bold"))


Start_button = tk.Button(root, text="Start Quiz", relief="flat", overrelief="raised", background="#fcbe97", command=lambda: show_frame(page1) )
canvas1.create_window(365, 610, window=Start_button)
Start_button.config(font=("Verdana", 24, "bold") )

var1 = tk.IntVar()
var2 = tk.IntVar()



root.mainloop()
