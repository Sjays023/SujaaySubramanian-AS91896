import tkinter as tk

root = tk.Tk()
root.title("7 Wonders Of The World Quiz")


label = tk.Label(root, text="7 Wonders Of The World Quiz", font=("Arial", 14, "bold"))
label.grid(row=0, column=0, columnspan=2, pady=10)


tk.Label(root, text="First name").grid(row=1, column=0, sticky="e")
tk.Label(root, text="Last name").grid(row=2, column=0, sticky="e")

tk.Entry(root).grid(row=1, column=1)
tk.Entry(root).grid(row=2, column=1)


button = tk.Button(root, text="Exit", width=25, command=root.destroy)
button.grid(row=3, column=0, columnspan=2, pady=10)



root.geometry("400x400")
bg = PhotoImage(file = "image.png")
label1 = Label(root, image = bg)
label1.place(x = 0, y = 0)
tk.PhotoImage =

root.mainloop()
