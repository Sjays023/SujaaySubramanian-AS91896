import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("7 Wonders Of The World Quiz")
root.geometry("1207x675")

bg = PhotoImage(file="Photos/starting_page.png")
canvas1 = Canvas(root, width=1204, height=680)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg, anchor="nw")

lbl1 = tk.Label(root, text="First name",
                fg="black",
                bg="#fce6b4",
                font=("Verdana", 14, "bold"))

canvas1.create_window(67, 100, window=lbl1)
ent1 = tk.Entry(root)
canvas1.create_window(200, 100, window=ent1)


lbl2 = tk.Label(root, text="Last name",
                fg="black",
                bg="#fce6b4",
                font=("Verdana", 14, "bold"))
canvas1.create_window(67, 130, window=lbl2)
ent2 = tk.Entry(root, width=20)
canvas1.create_window(200, 130, window=ent2)


button = tk.Button(root, text="Exit", width=25, command=root.destroy)
canvas1.create_window(1050, 635, window=button)
button.config(background= "#fce6b4", height=1, width=5, font=("Verdana", 24, "bold"))


Start_button = tk.Button(root, text="Start Quiz", width=20, command=root.destroy)
canvas1.create_window(602, 600, window=Start_button)
button.config(background= "#fce6b4", height=1, width=5, font=("Verdana", 24, "bold"))




var1 = tk.IntVar()
var2 = tk.IntVar()


#Spend next Lesson to make a button that moves to the next quiz page :)


root.mainloop()
