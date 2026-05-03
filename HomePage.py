import tkinter as tk
from tkinter import PhotoImage
from tkinter import Canvas

root = tk.Tk()
root.title("7 Wonders Of The World Quiz")
root.geometry("1204x680")

bg = PhotoImage(file="Photos/starting-page.png")
canvas1 = Canvas(root, width=1204, height=680)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg, anchor="nw")


label = tk.Label(root, text="7 Wonders Of The World Quiz", font=("Arial", 14, "bold"))
canvas1.create_window(640, 50, window=label)


lbl1 = tk.Label(root, text="First name")
canvas1.create_window(100, 75, window=lbl1)
ent1 = tk.Entry(root)
canvas1.create_window(200, 75, window=ent1)


lbl2 = tk.Label(root, text="Last name")
canvas1.create_window(100, 100, window=lbl2)
ent2 = tk.Entry(root)
canvas1.create_window(200, 100, window=ent2)


button = tk.Button(root, text="Exit", width=25, command=root.destroy)
canvas1.create_window(640, 200, window=button)

var1 = tk.IntVar()
var2 = tk.IntVar()

root.mainloop()
