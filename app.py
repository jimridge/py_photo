import tkinter as tk

# window = tk.Tk()



# frame1 = tk.Frame(master=window, height=100, bg="red")
# frame1.pack(fill=tk.X)

# frame2 = tk.Frame(master=window, height=50, bg="yellow")
# frame2.pack(fill=tk.X)

# frame3 = tk.Frame(master=window, height=25, bg="blue")
# frame3.pack(fill=tk.X)

# Create an event handler
# def handle_keypress(event):
#     """Print the character associated to the key pressed"""
#     print(event.char)


# # Bind keypress event to handle_keypress()
# window.bind("<Key>", handle_keypress)

# def handle_click(event):
#     print("The button was clicked!")

# button = tk.Button(text="Click me!")
# button.pack()
# button.bind("<Button-1>", handle_click)



# def increase():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value + 1}"


# def decrease():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value - 1}"



# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure([0, 1, 2], minsize=50, weight=1)

# btn_decrease = tk.Button(master=window, text="-", command=decrease)
# btn_decrease.grid(row=0, column=0, sticky="nsew")

# lbl_value = tk.Label(master=window, text="0")
# lbl_value.grid(row=0, column=1)

# btn_increase = tk.Button(master=window, text="+", command=increase)
# btn_increase.grid(row=0, column=2, sticky="nsew")
def callback():
    print("called the callback!")

root = tk.Tk()

# create a menu
menu = tk.Menu(root)
root.config(menu=menu)

filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=callback)
filemenu.add_command(label="Open...", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=callback)

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=callback)


# for i in range(3):
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j)
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack()

root.mainloop()
# border_effects = {
#     "flat": tk.FLAT,
#     "sunken": tk.SUNKEN,
#     "raised": tk.RAISED,
#     "groove": tk.GROOVE,
#     "ridge": tk.RIDGE,
# }

# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master=frame, text=relief_name)
#     label.pack()

# label = tk.Label(
#     text="Hello, Tkinter",
#     fg="white",
#     bg="black",
#     width=10,
#     height=10
# )

# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow",
# )



# button.pack()
# label.pack()

window.mainloop()