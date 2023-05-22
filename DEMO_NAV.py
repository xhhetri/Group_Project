import tkinter as tk
from tkinter import Frame
from tkinter import ttk
from tkcalendar import DateEntry
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create a new window
root = tk.Tk()
root.title("Admin")

# Set the window size
root.geometry("800x500")


mainframe = tk.Frame(root)
mainframe.pack_propagate(False)
mainframe.grid(row=0, column=1)


#----------UI for crating new term--------------------------------------------------------------------------------------

def new_exam():
    exam: Frame = tk.Frame(root, width=200, height=200)
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

#----------------UI For adding new student------------------------------------------------------------------------------

#create a frame
def new_studnet():
    studnet: Frame = tk.Frame(root)
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

    submit = tk.Button(studnet, text="Submit")
    submit.grid(row=7, column=1, sticky=tk.E, pady=10)


#------------Side Bar Buttons and side Frame----------------------------------------------------------------------------
def new_teacher():
    teach: Frame = tk.Frame(root, height=100, width=100)
    teach.grid(row=0, column=1, padx=20, pady=20, sticky=tk.NSEW)

    name_label = tk.Label(teach, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    name_entry = tk.Entry(teach)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    roll_label = tk.Label(teach, text="ID number:")
    roll_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    roll_entry = tk.Entry(teach)
    roll_entry.grid(row=1, column=1, padx=5, pady=5)

    subject_label = tk.Label(teach, text="Email:")
    subject_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    subject_entry = tk.Entry(teach)
    subject_entry.grid(row=2, column=1, padx=5, pady=5)

    contact_label = tk.Label(teach, text="Contact:")
    contact_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
    contact_entry = tk.Entry(teach)
    contact_entry.grid(row=3, column=1, padx=5, pady=5)

    address_label = tk.Label(teach, text="Address:")
    address_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
    address_entry = tk.Entry(teach)
    address_entry.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

    submit = tk.Button(teach, text="Submit")
    submit.grid(row=5, column=1, sticky=tk.E, pady=10)

#-----------------------------------------------------------------------------------------------------------------------

def seats():
    seat = tk.Frame(root)
    seat.pack_propagate(False)
    seat.grid(row=0, column=1, padx=20, pady=20, sticky=tk.NSEW)

    seats_label = tk.Label(seat, text="class:")
    seats_label.grid(row=0, column=0, padx=5, sticky=tk.W)
    seats_entry = tk.Entry(seat)
    seats_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

    room_label1 = tk.Label(seat, text="Room :")
    room_label1.grid(row=2, column=0, padx=5, sticky=tk.W)
    room_entry1 = tk.Entry(seat)
    room_entry1.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

    room_label2 = tk.Label(seat, text="Range :")
    room_label2.grid(row=3, column=0)
    room_entry2 = tk.Entry(seat)
    room_entry2.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)


    submit = tk.Button(seat, text="Submit")
    submit.grid(row=4, column=1, sticky=tk.E)


#-----------------------------------------------------------------------------------------------------------------------

def add_mark():
    addmark = tk.Frame(root)
    addmark.pack_propagate(False)
    addmark.grid(row=0, column=1, padx=20, pady=20, sticky=tk.NSEW)

    class_label = tk.Label(addmark, text="Class :")
    class_label.grid(row=0, column=0, sticky=tk.W)
    class_entry = tk.Entry(addmark)
    class_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

    name_label = tk.Label(addmark, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    name_entry = tk.Entry(addmark)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    roll_label = tk.Label(addmark, text="ID number:")
    roll_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    roll_entry = tk.Entry(addmark)
    roll_entry.grid(row=1, column=1, padx=5, pady=5)

    subject_label = tk.Label(addmark, text="Email:")
    subject_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    subject_entry = tk.Entry(addmark)
    subject_entry.grid(row=2, column=1, padx=5, pady=5)





#-----------------------------------------------------------------------------------------------------------------------

def send_email(sender_email, sender_password, receiver_email, subject, message):
    # Create a multipart message object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    # Establish a secure connection with the SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        # Login to the sender's email account
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(msg)


def absent_mail():
    absent = tk.Frame(root)
    absent.pack_propagate(False)
    absent.grid(row=0, column=1, padx=20, pady=20, sticky=tk.NSEW)

    name_label = tk.Label(absent, text="Name:")
    name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
    name_entry = tk.Entry(absent)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    roll_label = tk.Label(absent, text="Roll no:")
    roll_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    roll_entry = tk.Entry(absent)
    roll_entry.grid(row=1, column=1, padx=5, pady=5)

    class_label = tk.Label(absent, text="Class:")
    class_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    class_entry = tk.Entry(absent)
    class_entry.grid(row=2, column=1, padx=5, pady=5)

    section_label = tk.Label(absent, text="Section:")
    section_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
    section_entry = tk.Entry(absent)
    section_entry.grid(row=3, column=1, padx=5, pady=5)

    email_label = tk.Label(absent, text="Email:")
    email_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
    email_entry = tk.Entry(absent)
    email_entry.grid(row=4, column=1, padx=5, pady=5)

    def send_absent_email():
        sender_email = "oshan9814158662@gmail.com"
        sender_password = "your_sender_password"
        receiver_email = email_entry.get()
        subject = "Absent Notification"
        message = "Test run".format(name_entry.get(), name_entry.get(), roll_entry.get(), class_entry.get(), section_entry.get())

        # Call the send_email function to send the email
        send_email(sender_email, sender_password, receiver_email, subject, message)

    send_button = tk.Button(absent, text="Send", command=send_absent_email, width=7)
    send_button.grid(row=5, column=1, padx=5, pady=5, sticky=tk.E)

#-----------------------------------------------------------------------------------------------------------------------

def close_and_open(frame_to_open):
    frames = [new_teacher(), new_studnet(), new_exam()]
    frames.destroy()
    frame_to_open.pack()

#------------Side Bar Buttons and side Frame----------------------------------------------------------------------------


# Create a frame for the buttons in the left 25% part of the window
sidebar = tk.Frame(root, width=150, height=500, bg="gray")
sidebar.pack_propagate(False)
sidebar.grid(row=0, column=0)


#set color change while hovering
def on_enter(e):
    e.widget['background'] = 'dark gray'

def on_leave(e):
    e.widget['background'] = 'gray'

#-------------------------Buttons---------------------------------------------------------------------------------------

# Create buttons in the button frame

new_term = tk.Button(sidebar, command=new_exam, text="New exam", bd=0, bg="gray", foreground="white")
add_student = tk.Button(sidebar, command=new_studnet, text="Add Student", bd=0, bg="gray", foreground="white")
add_teacher = tk.Button(sidebar, command=new_teacher, text="Add Teacher", bd=0, bg="gray", foreground="white")
sort_student = tk.Button(sidebar, command=seats, text="Assign seat", bd=0, bg="gray", foreground="white")
fill_marks = tk.Button(sidebar, command=add_mark, text="Add Mark", bd=0, bg="gray", foreground="white")
edit_mark = tk.Button(sidebar, text="Manage Mark", bd=0, bg="gray", foreground="white")
send_absent = tk.Button(sidebar, command=absent_mail, text="Inform absentee", bd=0, bg="gray", foreground="white")
send_marksheet = tk.Button(sidebar, text="Send Mark-Sheet", bd=0, bg="gray", foreground="white")


# Bind the buttons to the Enter and Leave events
add_student.bind("<Enter>", on_enter)
add_student.bind("<Leave>", on_leave)
add_teacher.bind("<Enter>", on_enter)
add_teacher.bind("<Leave>", on_leave)
sort_student.bind("<Enter>", on_enter)
sort_student.bind("<Leave>", on_leave)
fill_marks.bind("<Enter>", on_enter)
fill_marks.bind("<Leave>", on_leave)
edit_mark.bind("<Enter>", on_enter)
edit_mark.bind("<Leave>", on_leave)
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
fill_marks.pack(pady=10, fill="x")
edit_mark.pack(pady=10, fill="x")
send_absent.pack(pady=10, fill="x")
send_marksheet.pack(pady=10, fill="x")



# Run the window
root.mainloop()
