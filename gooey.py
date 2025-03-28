import tkinter as tk

def show_frame(frame):
    frame.tkraise()  # Bring the selected frame to the top

root = tk.Tk()
root.title("Multi-Page App")
root.geometry("600x400")

# Create a container frame
container = tk.Frame(root)
container.pack(side="top", fill="both", expand=True)

# Configure grid behavior
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# Create individual frames
start_page = tk.Frame(container)
page_one = tk.Frame(container)
page_two = tk.Frame(container)

for frame in (start_page, page_one, page_two):
    frame.grid(row=0, column=0, sticky="nsew")

# Start Page
tk.Label(start_page, text="Home Page", font=('Arial', 40, 'bold'), relief="raised").pack(pady=20)
tk.Button(start_page, text="Go to Standards Creator", command=lambda: show_frame(page_one)).pack()
tk.Button(start_page, text="Go to Test Creator", command=lambda: show_frame(page_two)).pack()

# Page One (Standards Creator)
tk.Label(page_one, text="Standards Page", font=('Arial', 40, 'bold'), relief="raised").pack(pady=20)
tk.Button(page_one, text="Back to Home Page", command=lambda: show_frame(start_page)).pack(pady=10)

# Page Two (Test Creator)
tk.Label(page_two, text="Test Creator", font=('Arial', 40, 'bold'), relief="raised").pack(pady=20)
tk.Button(page_two, text="Back to Home Page", command=lambda: show_frame(start_page)).pack()

# Show the start page initially
show_frame(start_page)

root.mainloop()
