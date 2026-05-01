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

var1 = tk.IntVar()
var2 = tk.IntVar()

tk.Checkbutton(root, text="Male", variable=var1).grid(row=0, sticky="w")
tk.Checkbutton(root, text="Female", variable=var2).grid(row=1, sticky=tk.W)




root.mainloop()
