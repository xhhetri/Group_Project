import tkinter as tk
from tkinter import Frame, Label
from tkinter import ttk
from tkcalendar import DateEntry

# Create a new window
window = tk.Tk()
window.title("Admin")

# Set the window size
window.geometry("800x500")

def close_and_open(frame_to_close, frame_to_open):
    frame_to_close.destroy()
    frame_to_open.pack()

def new_exam():
    exam: Frame = tk.Frame(window, width=200, height=200)
    exam.pack_propagate(False)
    exam.grid(row=0, column=1, padx=20)

    Term = tk.Label(exam, text="Term :")
    Term.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    option = ["First", "Second", "Third", "Fourth"]
    combobox = ttk.Combobox(exam, values=option)
    combobox.config(width=17, height=5)
    combobox.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

    def get_combo():
        value = combobox.get()
        print("Term : ", value)

    date_label = tk.Label(exam, text='Date :')
    date_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    date_picker = DateEntry(exam, width=17)
    date_picker.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

    def get_date():
        select_date = date_picker.get()
        print("selected date:", select_date)

    submit = tk.Button(exam, text=" Create")
    submit.grid(row=3, column=1, sticky=tk.E)

#create a frame
def add_studnet():
    studnet: Frame = tk.Frame(window, width=200, height=200)
    studnet.pack_propagate(False)
    studnet.grid(row=0, column=1)

    name_label = tk.Label(studnet, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    name_entry = tk.Entry(studnet)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    roll_label = tk.Label(studnet, text="Roll No.:")
    roll_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    roll_entry = tk.Entry(studnet)
    roll_entry.grid(row=1, column=1, padx=5, pady=5)

    class_label = tk.Label(studnet, text="Class:")
    class_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    class_entry = tk.Entry(studnet)
    class_entry.grid(row=2, column=1, padx=5, pady=5)

    section_label = tk.Label(studnet, text="Section:")
    section_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
    section_entry = tk.Entry(studnet)
    section_entry.grid(row=3, column=1, padx=5, pady=5)

    email_label = tk.Label(studnet, text="Email:")
    email_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
    email_entry = tk.Entry(studnet)
    email_entry.grid(row=4, column=1, padx=5, pady=5)

    contact_label = tk.Label(studnet, text="Contact:")
    contact_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
    contact_entry = tk.Entry(studnet)
    contact_entry.grid(row=5, column=1, padx=5, pady=5)


# Create a frame for the buttons in the left 25% part of the window
sidebar = tk.Frame(window, width=150, height=500, bg="gray")
sidebar.pack_propagate(False)
sidebar.grid(row=0, column=0)
#set color change while hovering
def on_enter(e):
    e.widget['background'] = 'dark gray'

def on_leave(e):
    e.widget['background'] = 'gray'


# Create buttons in the button frame

new_term = tk.Button(sidebar, command=new_exam, text="New exam", bd=0, bg="gray", foreground="white")
add_student = tk.Button(sidebar, command=add_studnet, text="Add Student", bd=0, bg="gray", foreground="white")
add_teacher = tk.Button(sidebar, text="Add Teacher", bd=0, bg="gray", foreground="white")
sort_student = tk.Button(sidebar, text="Student Symbol no", bd=0, bg="gray", foreground="white")
sort_teacher = tk.Button(sidebar, text="Teacher position", bd=0, bg="gray", foreground="white")
marksheet = tk.Button(sidebar, text="Mark sheet", bd=0, bg="gray", foreground="white")
send_absent = tk.Button(sidebar, text="Inform absentee", bd=0, bg="gray", foreground="white")
send_marksheet = tk.Button(sidebar, text="Send Mark-Sheet", bd=0, bg="gray", foreground="white")


# Bind the buttons to the Enter and Leave events
add_student.bind("<Enter>", on_enter)
add_student.bind("<Leave>", on_leave)
add_teacher.bind("<Enter>", on_enter)
add_teacher.bind("<Leave>", on_leave)
sort_student.bind("<Enter>", on_enter)
sort_student.bind("<Leave>", on_leave)
sort_teacher.bind("<Enter>", on_enter)
sort_teacher.bind("<Leave>", on_leave)
marksheet.bind("<Enter>", on_enter)
marksheet.bind("<Leave>", on_leave)
send_absent.bind("<Enter>", on_enter)
send_absent.bind("<Leave>", on_leave)
send_marksheet.bind("<Enter>", on_enter)
send_marksheet.bind("<Leave>", on_leave)
new_term.bind("<Enter>", on_enter)
new_term.bind("<Leave>", on_leave)


# Add the buttons to the button frame
new_term.pack(pady=10, fill="x")
add_student.pack(pady=10, fill="x")
add_teacher.pack(pady=10, fill="x")
sort_student.pack(pady=10, fill="x")
sort_teacher.pack(pady=10, fill="x")
marksheet.pack(pady=10, fill="x")
send_absent.pack(pady=10, fill="x")
send_marksheet.pack(pady=10, fill="x")


#other half of the frame of the window

# Run the window
window.mainloop()
