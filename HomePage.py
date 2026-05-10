import tkinter as tk
from tkinter import *



def start_quiz():

    canvas1.delete("all")

    new_bg = PhotoImage(file="Photos/question1_page.png")  # Fixed potential typo
    canvas1.create_image(0, 0, image=new_bg, anchor="nw")
    canvas1.new_bg = new_bg



    back_btn = tk.Button(root, text="", command=setup_main_menu)
    canvas1.create_window(50, 50, window=back_btn, )



def setup_main_menu():

    canvas1.delete("all")
    canvas1.create_image(0, 0, image=bg, anchor=NW)


    canvas1.create_window(67, 100, window=lbl1)
    canvas1.create_window(200, 100, window=ent1)
    canvas1.create_window(67, 130, window=lbl2)
    canvas1.create_window(200, 130, window=ent2)
    canvas1.create_window(825, 610, window=exit_button)
    canvas1.create_window(365, 610, window=start_button)


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
exit_button = tk.Button(root, text="Exit", width=25, command=root.destroy, relief="flat", overrelief="raised", background="#fcbe97", )
canvas1.create_window(825, 610, window=exit_button)
exit_button.config(height=1, width=5, font=("Verdana", 24, "bold"))


start_button = tk.Button(root, text="Start Quiz", relief="flat", overrelief="raised", background="#fcbe97", command=start_quiz )
canvas1.create_window(365, 610, window=start_button)
start_button.config(font=("Verdana", 24, "bold") )

var1 = tk.IntVar()
var2 = tk.IntVar()



root.mainloop()
