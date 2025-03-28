import tkinter as tk

def show_frame(frame):
    frame.tkraise() 

root = tk.Tk()
root.title("Final Project")
root.geometry("600x400")

container = tk.Frame(root)
container.pack(side="top", fill="both", expand=True)

container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

#individual frames
start_page = tk.Frame(container)
page_one = tk.Frame(container)
page_two = tk.Frame(container)

for frame in (start_page, page_one, page_two):
    frame.grid(row=0, column=0, sticky="nsew")

# Start Page
tk.Label(start_page, text="Home Page", font=('Arial', 40, 'bold'), relief="raised").pack(pady=20)
tk.Button(start_page, text="Go to Standards Creator", command=lambda: show_frame(page_one)).pack(padx=10)
tk.Button(start_page, text="Go to Test Creator", command=lambda: show_frame(page_two)).pack()

# Page One (Standards Creator)
tk.Label(page_one, text="Standards Page", font=('Arial', 40, 'bold'), relief="raised").pack(pady=20)
tk.Button(page_one, text="Back to Home Page", command=lambda: show_frame(start_page)).pack(pady=10)

# Page Two (Test Creator)
tk.Label(page_two, text="Test Creator", font=('Arial', 40, 'bold'), relief="raised").pack(pady=20)
tk.Button(page_two, text="Back to Home Page", command=lambda: show_frame(start_page)).pack()

show_frame(start_page)

root.mainloop()


# import tkinter as tk

# def show_frame(frame):
#     frame.tkraise() 

# root = tk.Tk()
# root.geometry("600x400")

# var = tk.BooleanVar()
# var2 = tk.BooleanVar()


# page1 = tk.Frame(root)
# page2 = tk.Frame(root)

# # Header
# header = tk.Label(root, text="Main Page", font=('Arial', 40, 'bold'))
# # Standars class name/number/id 


# # Use grid for all widgets
# new_standard = tk.Label(root, text="New Standard", padx=0, pady=40)
# generate_test = tk.Label(root, text="Generate Test")

# checkbox = tk.Checkbutton(root, variable=var, command=lambda: show_frame(page1))
# checkbox2 = tk.Checkbutton(root, variable=var2)


# # Place everything using grid
# checkbox.grid(row=1, column=0, padx=10, pady=5)
# new_standard.grid(row=1, column=1, padx=0, pady=5)
# generate_test.grid(row=2, column=1, padx=0, pady=5)
# checkbox2.grid(row=2, column=0, padx=10, pady=5)
# header.grid(row=0, column=20, padx=40)

# page1 = tk.Label(page1, text="New Standards Creation", relief="raised", font=('Arial', 40, 'bold'))
# page1.grid(row=0, column=0, padx=10, pady=5)


# root.mainloop()
