import tkinter as tk
from tkinter import ttk
from datatype.standard import Standard
# import standardsInterface
from collections import defaultdict
import test_maker_interface

SPREADSHEET_ID = "1EmozOHR-QQGPJ6bn7PnuTBzbWDqNUDW_KA9hFfXAwcE"

def show_frame(frame):
    frame.tkraise()

def pull_from_google(parent, spreadsheet_id):
    grid_frame = tk.Frame(parent, padx=20, pady=20)
    grid_frame.pack()

    student_standards = test_maker_interface.get_all_student_standards(spreadsheet_id)
    for row_num, (student, standards) in enumerate(student_standards.items()):
        tk.Label( # student
            grid_frame,
            text=student,
            width=10,
            height=2
        ).grid(row=row_num, column=0)
        tk.Label( # standards
            grid_frame,
            text=standards,
            width=10,
            height=2
        ).grid(row=row_num, column=1)


root = tk.Tk()
root.geometry("800x600")
root.title("User Story 4: Main Page")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create frames (pages)
mainPage = tk.Frame(root)
page1 = tk.Frame(root)
page2 = tk.Frame(root)

# Stack frames
for frame in (mainPage, page1, page2):
    frame.grid(row=0, column=0, sticky="nsew")

# ------------ Main Page -------------

# Configure grid layout
mainPage.columnconfigure(0, weight=1)
mainPage.columnconfigure(1, weight=1)

# Header
header = tk.Label(mainPage, text="USER STORY 4: Main Page", font=('Arial', 40, 'bold'))
header.grid(row=0, column=0, columnspan=2, pady=10)

new_standard = tk.Button(mainPage, text="+ New Standard", command=lambda: show_frame(page1), font=('Arial', 30, 'bold'))
generate_test = tk.Button(mainPage, text="+ Generate Test", command=lambda: show_frame(page2), font=('Arial', 30, 'bold'))

new_standard.grid(row=1, column=0, padx=20, pady=5, sticky="w")
generate_test.grid(row=2, column=0, padx=20, pady=5, sticky="w")

# Treeview (Hierarchical Structure)
tree_frame = tk.Frame(mainPage)
tree_frame.grid(row=1, column=1, rowspan=4, padx=20, pady=10, sticky="nsew")

tree = ttk.Treeview(tree_frame)
tree.pack(expand=True)

tree.column("#0", width=200)  # Main column
tree.heading("#0", text="All Standards", anchor="w")

# ------------ Page 1 ------------
tk.Label(page1, text="New Standards Creation",font=('Arial', 40, 'bold')).pack(pady=20)
tk.Button(page1, text="+ Back to Main Page", command=lambda: show_frame(mainPage),font=('Arial', 30, 'bold')).pack(pady=10)

# ------------ Page 2 ------------
tk.Label(page2, text="Generate Test Page", font=('Arial', 40, 'bold')).pack(pady=20)
tk.Button(page2, text="+ Back to Main Page", command=lambda: show_frame(mainPage), font=('Arial', 30, 'bold')).pack(pady=10)
tk.Button(page2, text="Pull Students from Google", command=lambda: pull_from_google(page2, SPREADSHEET_ID), font=('Arial', 24)).pack(pady=20)


# Set starting page
show_frame(mainPage)

root.mainloop()
