import tkinter as tk
from tkinter import Frame
from tkinter import ttk
from tkcalendar import DateEntry

# Create a new window
window = tk.Tk()
window.title("Admin")

# Set the window size
window.geometry("800x500")

mainframe = tk.Frame(window)
mainframe.pack_propagate(False)
mainframe.grid(row=0, column=1)


# ----------UI for crating new term--------------------------------------------------------------------------------------

def new_exam():
    exam: Frame = tk.Frame(window, width=200, height=200)
    exam.pack_propagate(False)
    exam.grid(row=0, column=1, padx=20, pady=20, sticky=tk.NSEW)

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


# ----------------UI For adding new student------------------------------------------------------------------------------

# create a frame
def new_studnet():
    studnet: Frame = tk.Frame(window)
    studnet.pack_propagate(False)
    studnet.grid(row=0, column=1, padx=20, pady=20, sticky=tk.NSEW)

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

    address_label = tk.Label(studnet, text="Address:")
    address_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
    address_entry = tk.Entry(studnet)
    address_entry.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)


# ------------Side Bar Buttons and side Frame----------------------------------------------------------------------------
def new_teacher():
    teach: Frame = tk.Frame(window, height=100, width=100)
    teach.grid(row=0, column=1, padx=20, pady=20, sticky=tk.NSEW)

    name_label = tk.Label(teach, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    name_entry = tk.Entry(teach)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    subject_label = tk.Label(teach, text="Email:")
    subject_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    subject_entry = tk.Entry(teach)
    subject_entry.grid(row=1, column=1, padx=5, pady=5)

    contact_label = tk.Label(teach, text="Contact:")
    contact_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    contact_entry = tk.Entry(teach)
    contact_entry.grid(row=2, column=1, padx=5, pady=5)

    address_label = tk.Label(teach, text="Address:")
    address_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
    address_entry = tk.Entry(teach)
    address_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)


# -----------------------------------------------------------------------------------------------------------------------

def seats():
    seat = tk.Frame(window)
    seat.pack_propagate(False)
    seat.grid(row=0, column=1, padx=20, pady=20, sticky=tk.NSEW)

    def validate_input(input_str):
        # Check if the input is a valid integer or not
        try:
            int(input_str)
            return True
        except ValueError:
            return True

    validate_input_cmd = (seat.register(validate_input), '%P')

    seats_label = tk.Label(seat, text="class:")
    seats_label.grid(row=0, column=0, padx=5, sticky=tk.W)
    seats_entry = tk.Entry(seat, validate="key", validatecommand=(validate_input_cmd, "%P"))
    seats_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

    seats_text = seats_entry.get()
    if seats_text.isdigit():
        seats_int = int(seats_text)
        print("The value entered in the seats entry is an integer: ", seats_int)
    else:
        print("The value entered in the seats entry is not an integer: ", seats_text)

    room_label1 = tk.Label(seat, text="Room :")
    room_label1.grid(row=2, column=0, padx=5, sticky=tk.W)
    room_entry1 = tk.Entry(seat, validate="key", validatecommand=(validate_input_cmd, "%P"))
    room_entry1.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

    room_label2 = tk.Label(seat, text="Range :")
    room_label2.grid(row=3, column=0)
    room_entry2 = tk.Entry(seat, validate="key", validatecommand=(validate_input_cmd, "%P"))
    room_entry2.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

    def assign_table():
        student_no = 50
        room_diff = 0
        room = int(room_entry1.get())
        diff = int(room_entry2.get())

        table = ttk.Treeview(seat, columns=("Room", "Student"), show="headings")
        table.heading("Room", text="Room")
        table.heading("Students", text="Students")

        for i in range(room):
            room_diff += diff
            if student_no > diff:  # if the room is full
                table.insert("", "end", values=(room, diff))  # insert the room into the table
                student_no -= 17  # start a new room with the remaining students
                room += 1  # increment the room number
            else:
                table.insert("", "end", values=(room, student_no))
        table.grid(row=4, column=0, columnspan=2)

    submit = tk.Button(seat, text="Submit", command=assign_table)
    submit.grid(row=4, column=1, sticky=tk.E)


# -----------------------------------------------------------------------------------------------------------------------

def view_mark():
    mark = tk.Frame(window)
    mark.pack_propagate(False)
    mark.grid(row=0, column=1, pady=20, padx=20, sticky=tk.N)


# -----------------------------------------------------------------------------------------------------------------------

def close_and_open(frame_to_open):
    frames = [new_teacher(), new_studnet(), new_exam()]
    frames.destroy()
    frame_to_open.pack()


# ------------Side Bar Buttons and side Frame----------------------------------------------------------------------------


# Create a frame for the buttons in the left 25% part of the window
sidebar = tk.Frame(window, width=150, height=500, bg="gray")
sidebar.pack_propagate(False)
sidebar.grid(row=0, column=0)


# set color change while hovering
def on_enter(e):
    e.widget['background'] = 'dark gray'


def on_leave(e):
    e.widget['background'] = 'gray'


# -------------------------Buttons---------------------------------------------------------------------------------------

# Create buttons in the button frame

new_term = tk.Button(sidebar, command=new_exam, text="New exam", bd=0, bg="gray", foreground="white")
add_student = tk.Button(sidebar, command=new_studnet, text="Add Student", bd=0, bg="gray", foreground="white")
add_teacher = tk.Button(sidebar, command=new_teacher, text="Add Teacher", bd=0, bg="gray", foreground="white")
sort_student = tk.Button(sidebar, command=seats, text="Assign seat", bd=0, bg="gray", foreground="white")
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
marksheet.pack(pady=10, fill="x")
send_absent.pack(pady=10, fill="x")
send_marksheet.pack(pady=10, fill="x")

# Run the window
window.mainloop()
