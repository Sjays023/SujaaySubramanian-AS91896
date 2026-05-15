import tkinter as tk
from tkinter import PhotoImage, Canvas

root = tk.Tk()
root.title("7 Wonders Of The World Quiz")
root.geometry("1207x675")

def show_frame(frame):
    frame.tkraise()

container = tk.Frame(root)
container.pack(fill="both", expand=True)
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)


home_frame = tk.Frame(container)
home_frame.grid(row=0, column=0, sticky="nsew")


bg_image = PhotoImage(file="Photos/starting_page.png")

canvas1 = Canvas(home_frame, width=1207, height=675, highlightthickness=0)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg_image, anchor="nw")
home_frame.image = bg_image


start_button = tk.Button(home_frame, text="Start Quiz",relief="flat", overrelief="raised", background="#fcbe97" ,command=lambda: show_frame(q1_frame))
start_button.config(font=("Verdana", 24, "bold") )
canvas1.create_window(365, 610, window=start_button)

exit_button = tk.Button(home_frame, text="Exit", width=25, command=root.destroy, relief="flat", overrelief="raised", background="#fcbe97", )
canvas1.create_window(825, 610, window=exit_button)
exit_button.config(height=1, width=5, font=("Verdana", 24, "bold"))


q1_frame = tk.Frame(container,)
q1_frame.grid(row=0, column=0, sticky="nsew")
q1bg_Image = PhotoImage("Photos/question1_page.png")
q1_frame.image = q1bg_Image
canvas2 = Canvas(q1_frame, width=1207, height=675, highlightthickness=0)
canvas2.pack(fill="both", expand=True)
canvas2.create_image(0, 0, anchor="nw", image=q1bg_Image)



lbl_q1 = tk.Label(q1_frame, text="Question 1: What is the tallest wonder?")
lbl_q1.pack(pady=50, bg = "Photos/question1_page.png")

back_button = tk.Button(q1_frame, text="Back?", relief="flat", overrelief="raised", background="#fcbe97", command=lambda: show_frame(home_frame))
back_button.config(font=("Verdana", 15,) )
canvas2.create_window(100, 500, window=back_button)

show_frame(home_frame)

root.mainloop()

#Why doesn't the background work/Fix it :(