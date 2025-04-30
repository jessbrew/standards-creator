import tkinter as tk
from tkinter import ttk
from datatypes import Standard
import standardsInterface
from collections import defaultdict
import test_maker_interface

SPREADSHEET_ID = "1EmozOHR-QQGPJ6bn7PnuTBzbWDqNUDW_KA9hFfXAwcE"

def show_frame(frame):
    frame.tkraise()


def delete_student_standard(student_label, standards_label, delete_button, student_standards_dict, student):    
    # destroy GUI labels
    student_label.destroy()
    standards_label.destroy()
    delete_button.destroy()

    # remove from dictionary
    student_standards_dict.pop(student)


def display_students_grid(parent, student_standards_dict):
    # clear grid
    for widget in parent.winfo_children():
        widget.destroy()

    for row_num, (student, standards) in enumerate(student_standards_dict.items()):
        student_label = tk.Label( # Student
            parent,
            text=student,
            width=20,
            height=1,
            bg="#c7c7c7",
        )
        student_label.grid(row=row_num, column=0, padx=5, pady=5)

        standard_label = tk.Label( # Standards
            parent,
            text=standards,
            width=20,
            height=1,
            bg="#c7c7c7",
        )
        standard_label.grid(row=row_num, column=1, padx=5, pady=5)

        print(standards)

        # Delete button
        delete_button = tk.Button(
            parent,
            text="-",
            width=1,
            height=1,
            bg="red",
            fg="white",
        )
        delete_button.config(command=lambda stud_label=student_label, stand_label=standard_label, delete=delete_button,
                                            standards_dict=student_standards_dict, student_key=student:
        delete_student_standard(stud_label, stand_label, delete, standards_dict, student_key))

        delete_button.grid(row=row_num, column=2, padx=5, pady=5)

    # Add student button
    tk.Button(parent, text="Add Student",
            command=lambda: add_student(parent, student_standards_dict)
    ).grid(row=len(student_standards_dict)+2, column=0, padx=5, pady=5)

def pull_from_google(parent, spreadsheet_id):
    student_standards_dict = test_maker_interface.get_all_student_standards(spreadsheet_id)
    display_students_grid(parent, student_standards_dict)


def add_student(parent_grid, student_standards_dict):
    student_name_entry = tk.Entry(parent_grid, width=20)
    student_name_entry.grid(row=len(student_standards_dict)+1, column=0, padx=5, pady=5)

    standards_entry = tk.Entry(parent_grid, width=20)
    standards_entry.grid(row=len(student_standards_dict)+1, column=1, padx=5, pady=5)

    tk.Button(parent_grid, text="Done",
        command=lambda: push_new_student(parent_grid, student_standards_dict, student_name_entry.get().strip(), standards_entry.get().strip())
    ).grid(row=len(student_standards_dict)+2, column=1, padx=5, pady=5)

def push_new_student(parent_grid, student_standards_dict, new_student, new_standards):
    # Add student/standards to dictionary
    test_maker_interface.add_student_standards(student_standards_dict, new_student, new_standards)
    display_students_grid(parent_grid, student_standards_dict)



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

new_standard = tk.Button(mainPage, text="+ New Standard", command=lambda: show_frame(page2), font=('Arial', 30, 'bold'))
generate_test = tk.Button(mainPage, text="+ Generate Test", command=lambda: show_frame(page1), font=('Arial', 30, 'bold'))

new_standard.grid(row=1, column=0, padx=20, pady=5, sticky="w")
generate_test.grid(row=2, column=0, padx=20, pady=5, sticky="w")

# Treeview (Hierarchical Structure)
tree_frame = tk.Frame(mainPage)
tree_frame.grid(row=1, column=1, rowspan=4, padx=20, pady=10, sticky="nsew")

tree = ttk.Treeview(tree_frame)
tree.pack(expand=True)

tree.column("#0", width=200)  # Main column
tree.heading("#0", text="All Standards", anchor="w")

standards = standardsInterface.getAllStandards()
orgStandards = {}

for s in standards:
    num = s.standardNumber
    if num not in orgStandards:
        orgStandards[num] = []
        # print(num)
    orgStandards[s.standardNumber].append(s)

for s, values in sorted(orgStandards.items()):
    if len(values) > 1:
        first_standard = values[0]
        parent = tree.insert("", "end", text=f"{first_standard.name}: {first_standard.standardNumber}")


        for v in range(1, len(values) + 1):
            print(values[v-1])
            print(v)
            tree.insert(parent, "end", text=f" Version:{v}")
    else:
        single_standard = values[0] # no versions
        parent = tree.insert("", "end", text=f"{single_standard.name}: {s}")

# ------------ Page 1 ------------
tk.Label(page1, text="Generate Test Page", font=('Arial', 40, 'bold')).pack(pady=20)
tk.Button(page1, text="+ Back to Main Page", command=lambda: show_frame(mainPage), font=('Arial', 30, 'bold')).pack(pady=10)

# Pull students from Google
tk.Button(page1, text="Pull Students from Google", command=lambda: pull_from_google(grid_frame, SPREADSHEET_ID), font=('Arial', 24)).pack(pady=20)
grid_frame = tk.Frame(page1, padx=20, pady=20)
grid_frame.pack()

# ------------ Page 2 ------------
tk.Label(page2, text="New Standards Creation",font=('Arial', 40, 'bold')).pack(pady=20)
tk.Button(page2, text="+ Back to Main Page", command=lambda: show_frame(mainPage),font=('Arial', 30, 'bold')).pack(pady=10)

class Options:
    def __init__(self, root):
        self.root = root

        self.main_frame = ttk.Frame(self.root, padding=10)
        self.main_frame.pack()

        self.plus_button = ttk.Button(self.main_frame, text="+", width=3, command=self.toggle_menu)
        self.plus_button.grid(row=0, column=0, sticky="w")

        self.menu_frame = ttk.Frame(self.main_frame)
        self.menu_visible = False

        self.options = ["Question", "Part", "Hint"]
        for i, option in enumerate(self.options):
            button = ttk.Button(self.menu_frame, text=option, command=lambda o=option: self.select_option(o))
            button.pack(fill="x", pady=2)

        self.entries_frame = ttk.Frame(self.main_frame)
        self.entries_frame.grid(row=2, column=0, sticky="w", pady=10)

    def toggle_menu(self):
        if self.menu_visible:
            self.menu_frame.grid_forget()
        else:
            self.menu_frame.grid(row=1, column=0, sticky="w")
        self.menu_visible = not self.menu_visible

    def select_option(self, option):
        entry_frame = ttk.Frame(self.entries_frame)
        entry_frame.pack(fill="x", pady=5)

        top_row = ttk.Frame(entry_frame)
        top_row.pack(fill="x")

        header_label = ttk.Label(top_row, text=option, font=("Arial", 20, "bold"))
        header_label.pack(side="left", anchor="w")

        delete_button = ttk.Button(top_row, text="-", width=3, command=lambda: self.delete_option(entry_frame))
        delete_button.pack(side="right")

        text_box = tk.Text(entry_frame, height=5, width=40, wrap="word")
        text_box.pack()

        self.toggle_menu()

    def delete_option(self, frame):
        frame.destroy()

app = Options(page2)

# Set starting page
show_frame(mainPage)

root.mainloop()
