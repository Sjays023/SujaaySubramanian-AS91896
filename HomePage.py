import tkinter as tk
from tkinter import *


root = tk.Tk()
root.title("7 Wonders Of The World Quiz")
root.geometry("1207x675")

def show_frame(frame):
    frame.tkraise()

container = tk.Frame(root)
container.pack(fill="both", expand=True)
container.grid_columnconfigure(0, minsize=1207, weight=1)
container.grid_rowconfigure(0, minsize=675, weight=1)


#Start of Home Page
home_frame = tk.Frame(container)
home_frame.grid(row=0, column=0, sticky="nsew")

bg_image = PhotoImage(file="Photos/starting_page.png")
home_frame.image = bg_image


canvas1 = Canvas(root, width=1204, height=680)
canvas1.pack(fill="both", expand=True)


#Labels and Entries
lbl1 = tk.Label(home_frame, text="First name",
                fg="black",
                bg="#fcf4ea",
                font=("Verdana", 14, "bold"))

canvas1.create_window(67, 100, window=lbl1)
ent1 = tk.Entry(root)
canvas1.create_window(200, 100, window=ent1)

lbl2 = tk.Label(home_frame, text="Last name",
                fg="black",
                bg="#fcf4ea",
                font=("Verdana", 14, "bold"))
canvas1.create_window(67, 130, window=lbl2)
ent2 = tk.Entry(home_frame, width=20)
canvas1.create_window(200, 130, window=ent2)

#Buttons
exit_button = tk.Button(home_frame, text="Exit", width=25, command=root.destroy, relief="flat", overrelief="raised", background="#fcbe97", )
canvas1.create_window(825, 610, window=exit_button)
exit_button.config(height=1, width=5, font=("Verdana", 24, "bold"))

start_button = tk.Button(home_frame, text="Start Quiz", relief="flat", overrelief="raised", background="#fcbe97", )
canvas1.create_window(365, 610, window=start_button)
start_button.config(font=("Verdana", 24, "bold") )
#End of Home page

show_frame(home_frame)


var1 = tk.IntVar()
var2 = tk.IntVar()

#_tkinter.TclError: can't use .!frame.!frame.!label in a window item of this canvas
fix this Problem tmmrw

root.mainloop()
