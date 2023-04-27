import tkinter as tk
from tkinter import Frame, Label

# Create a new window
window = tk.Tk()

# Set the window size
window.geometry("800x500")




#create a frame
def new_studnet():
    studnet: Frame = tk.Frame(window, width=100, height=200, bg="light gray")
    studnet.pack_propagate(False)

    name: Label = tk.Label(studnet, text=" Student Name ")
    roll: Label = tk.Label(studnet, text=" Roll no ")
    name.pack()
    roll.pack()

    studnet.pack(side="right", pady=30, padx=300)

# Create a frame for the buttons in the left 25% part of the window
sidebar = tk.Frame(window, width=150, height=500, bg="gray")
sidebar.pack_propagate(False)

#set color change while hovering
def on_enter(e):
    e.widget['background'] = 'light gray'

def on_leave(e):
    e.widget['background'] = 'gray'

#Create Icons
# new_size = (32, 32)
# admin_icon = tk.PhotoImage(file="C:\\Users\\oshan\\OneDrive\\Desktop\\icons\\homepage-icon.png" )
# student_icon = tk.PhotoImage(file="C:\\Users\\oshan\\OneDrive\\Desktop\\icons\\student-icon.png")
# attendance_icon = tk.PhotoImage(file="C:\\Users\\oshan\\OneDrive\\Desktop\\icons\\attendance.png")
# schedule_icon = tk.PhotoImage(file="C:\\Users\\oshan\\OneDrive\\Desktop\\icons\\Exam (1).png")
# question_icon = tk.PhotoImage(file="C:\\Users\\oshan\\OneDrive\\Desktop\\icons\\Exam (2).png")
# setting_icon = tk.PhotoImage(file="C:\\Users\\oshan\\OneDrive\\Desktop\\icons\\Settings.png")

# Create buttons in the button frame

add_student = tk.Button(sidebar, command=new_studnet(), text="Add Student", bd=0, bg="gray")
add_teacher = tk.Button(sidebar, text="Add Teacher", bd=0, bg="gray")
sort_student = tk.Button(sidebar, text="Student Symbol no", bd=0, bg="gray")
sort_teacher = tk.Button(sidebar, text="Teacher position", bd=0, bg="gray")
marksheet = tk.Button(sidebar, text="Mark sheet", bd=0, bg="gray")
send_absent = tk.Button(sidebar, text="Inform absentee", bd=0, bg="gray")
send_marksheet = tk.Button(sidebar, text="Send Mark-sheet", bd=0, bg="gray")


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


# Add the buttons to the button frame
add_student.pack(pady=10, fill="x")
add_teacher.pack(pady=10, fill="x")
sort_student.pack(pady=10, fill="x")
sort_teacher.pack(pady=10, fill="x")
marksheet.pack(pady=10, fill="x")
send_absent.pack(pady=10, fill="x")
send_marksheet.pack(pady=10, fill="x")

# Pack the button frame to the left side of the window
sidebar.pack(side="left", fill="y")

#other half of the frame of the window
sidebar = tk.Frame(window, width=100, height=500, bg="red")


# Run the window
window.mainloop()
