import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

label = tk.Label(root, text="Pixel Size Label", bg="lightblue")

# Set exact pixel width and height
label.place(x=50, y=50, width=100, height=100)

root.mainloop()
