import smtplib
import tkinter as tk
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from tkinter import ttk, messagebox
import mysql.connector
import tkcalendar
from reportlab.lib.pagesizes import letter
from reportlab.platypus import TableStyle, SimpleDocTemplate, Table


class SplitWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Admin Window")
        self.submit = None
        self.propagate(False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=5)
        self.left_frame = tk.Frame(self, bg="#2d3032", height="1000")
        self.left_frame.place()
        self.left_frame.grid(row=0, column=0, sticky="nsew")
        self.left_frame.grid_rowconfigure(0, weight=1)
        self.left_frame.grid_columnconfigure(0, weight=1)
        self.left_frame.propagate(True)

        self.right_frame = tk.Frame(self, bg="#1e2222", height="1000")
        self.right_frame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)
        self.right_frame.grid(row=0, column=1, sticky="nsew", )
        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)
        self.right_frame.propagate(True)

        self.default_dashboard()

        ##############################################################################################################
        # creating hover event
        def on_enter(event):
            event.widget.config(bg="#3f4747")

        def on_leave(event):
            event.widget.config(bg="#2d3032")

        #############################################################################################
        # main category label
        self.left_frame.main_category_label = tk.Label(self.left_frame, text="Main Category", bg="#2d3032",
                                                       fg="#ADACAA")
        self.left_frame.main_category_label.pack(side="top", pady=5, padx=10, anchor="w")
        self.left_frame.main_category_label.propagate(True)

        ################################################################################################################
        # Dashboard Button
        self.left_frame.dashboard_button = tk.Button(self.left_frame, text="Dashboard", bg="#2d3032", fg="#E0DDD9", bd=0
                                                     , highlightthickness=0, activebackground="#3f4747",
                                                     activeforeground="#E0DDD9", command=self.default_dashboard, anchor="w"
                                                     )
        self.left_frame.main_category_label.propagate(True)
        self.left_frame.dashboard_button.pack(side="top", fill="x", padx=5)
        self.left_frame.dashboard_button.config(width=3, height=2)
        self.left_frame.dashboard_button.bind("<Enter>", on_enter)
        self.left_frame.dashboard_button.bind("<Leave>", on_leave)

        self.left_frame.add_subject = tk.Button(self.left_frame, text="Assign Seat", bg="#2d3032", fg="#E0DDD9",
                                                bd=0, highlightthickness=0, activebackground="#3f4747"
                                                , command=self.assign_seat, activeforeground="#E0DDD9", anchor="w")
        self.left_frame.add_subject.pack(side="top", fill="x", padx=5)
        self.left_frame.add_subject.config(width=3, height=2)
        self.left_frame.add_subject.bind("<Enter>", on_enter)
        self.left_frame.add_subject.bind("<Leave>", on_leave)


        ########################################################################################################################
        # Apperance
        self.left_frame.apperance_label = tk.Label(self.left_frame, text="Teacher", bg="#2d3032"
                                                   , fg="#ADACAA")
        self.left_frame.apperance_label.pack(side="top", pady=8, padx=10, anchor="w")

        ########################################################################################################################
        # Add teacher

        self.left_frame.manage_subject = tk.Button(self.left_frame, text="Add Teacher", bg="#2d3032", fg="#E0DDD9",
                                                   bd=0, command=self.add_teacher
                                                   , highlightthickness=0, activebackground="#3f4747",
                                                   activeforeground="#E0DDD9",
                                                   anchor="w"
                                                   )
        self.left_frame.manage_subject.pack(side="top", fill="x", padx=5)
        self.left_frame.manage_subject.config(width=3, height=2)
        self.left_frame.manage_subject.bind("<Enter>", on_enter)
        self.left_frame.manage_subject.bind("<Leave>", on_leave)


        self.left_frame.manage_subject = tk.Button(self.left_frame, text="Manage Teacher", bg="#2d3032", fg="#E0DDD9",
                                                   bd=0, command=self.manage_teachers
                                                   , highlightthickness=0, activebackground="#3f4747",
                                                   activeforeground="#E0DDD9",
                                                   anchor="w"
                                                   )
        self.left_frame.manage_subject.pack(side="top", fill="x", padx=5)
        self.left_frame.manage_subject.config(width=3, height=2)
        self.left_frame.manage_subject.bind("<Enter>", on_enter)
        self.left_frame.manage_subject.bind("<Leave>", on_leave)

        ########################################################################################################################

        # Add student
        self.left_frame.apperance_label = tk.Label(self.left_frame, text="Student", bg="#2d3032"
                                                   , fg="#ADACAA")
        self.left_frame.apperance_label.pack(side="top", pady=8, padx=10, anchor="w")

        self.left_frame.add_student = tk.Button(self.left_frame, text="Add Student", bg="#2d3032", fg="#E0DDD9", bd=0
                                                , highlightthickness=0, activebackground="#3f4747",
                                                command=self.add_student
                                                , activeforeground="#E0DDD9",
                                                anchor="w")
        self.left_frame.add_student.pack(side="top", fill="x", padx=5)
        self.left_frame.add_student.config(width=3, height=2)
        self.left_frame.add_student.bind("<Enter>", on_enter)
        self.left_frame.add_student.bind("<Leave>", on_leave)

        self.left_frame.man_student = tk.Button(self.left_frame, text="Manage Student", bg="#2d3032", fg="#E0DDD9", bd=0
                                                , highlightthickness=0, activebackground="#3f4747",
                                                command=self.manage_student,
                                                activeforeground="#E0DDD9",
                                                anchor="w")
        self.left_frame.man_student.pack(side="top", fill="x", padx=5)
        self.left_frame.man_student.config(width=3, height=2)
        self.left_frame.man_student.bind("<Enter>", on_enter)
        self.left_frame.man_student.bind("<Leave>", on_leave)

        ################################################################################################################

        # Result
        self.left_frame.apperance_label = tk.Label(self.left_frame, text="Result", bg="#2d3032"
                                                   , fg="#ADACAA")
        self.left_frame.apperance_label.pack(side="top", pady=8, padx=10, anchor="w")

        self.left_frame.add_result = tk.Button(self.left_frame, text="Add Result", bg="#2d3032", fg="#E0DDD9",
                                               bd=0
                                               , highlightthickness=0, activebackground="#3f4747",
                                               command=self.add_result,
                                               activeforeground="#E0DDD9", anchor="w"
                                               )
        self.left_frame.add_result.pack(side="top", fill="x", padx=5)
        self.left_frame.add_result.config(width=3, height=2)
        self.left_frame.add_result.bind("<Enter>", on_enter)
        self.left_frame.add_result.bind("<Leave>", on_leave)

        self.left_frame.manage_result = tk.Button(self.left_frame, text="Manage Result", bg="#2d3032", fg="#E0DDD9",
                                                  bd=0, command=self.manage_mark
                                                  , highlightthickness=0, activebackground="#3f4747",
                                                  activeforeground="#E0DDD9", anchor="w"
                                                  )
        self.left_frame.manage_result.pack(side="top", fill="x", padx=5)
        self.left_frame.manage_result.config(width=3, height=2)
        self.left_frame.manage_result.bind("<Enter>", on_enter)
        self.left_frame.manage_result.bind("<Leave>", on_leave)

        ################################################################################################################
        # Admin Change Password

        self.left_frame.apperance_label = tk.Label(self.left_frame, text="Change Password", bg="#2d3032"
                                                   , fg="#ADACAA")
        self.left_frame.apperance_label.pack(side="top", pady=8, padx=10, anchor="w")
        self.left_frame.subject_button = tk.Button(self.left_frame, text="Admin Change Password", bg="#2d3032",
                                                   fg="#E0DDD9", bd=0, highlightthickness=0, activebackground="#3f4747",
                                                   activeforeground="#E0DDD9", command=self.change_password,
                                                   anchor="w"
                                                   )
        self.left_frame.subject_button.pack(side="top", fill="x", padx=5)
        self.left_frame.subject_button.config(width=3, height=2)
        self.left_frame.subject_button.bind("<Enter>", on_enter)
        self.left_frame.subject_button.bind("<Leave>", on_leave)
        ################################################################################################################
        # Send Mail

        self.left_frame.apperance_label = tk.Label(self.left_frame, text="Mail the Result", bg="#2d3032"
                                                   , fg="#ADACAA")
        self.left_frame.apperance_label.pack(side="top", pady=8, padx=10, anchor="w")
        self.left_frame.subject_button = tk.Button(self.left_frame, text="Send Email", bg="#2d3032",
                                                   fg="#E0DDD9", bd=0, highlightthickness=0, activebackground="#3f4747",
                                                   activeforeground="#E0DDD9", command=self.send_mail,
                                                   anchor="w"
                                                   )
        self.left_frame.subject_button.pack(side="top", fill="x", padx=5)
        self.left_frame.subject_button.config(width=3, height=2)
        self.left_frame.subject_button.bind("<Enter>", on_enter)
        self.left_frame.subject_button.bind("<Leave>", on_leave)

####################################################################################################################
    def default_dashboard(self):
        # destroy any existing frame in right_frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # create new frame with desired content
        self.top_frame = tk.Frame(self.right_frame, bg="#181a1b", bd=1, height=80)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.top_frame.propagate(False)

        self.top_label = tk.Label(self.top_frame, text="Dashboard", bg="#181a1b", foreground="white", font=5, height=4)
        self.top_label.pack(anchor=tk.NW, padx=10)
        self.top_label.propagate(True)

        self.buttom_frame = tk.Frame(self.right_frame, bg="#1e2222", bd=1, height=self.winfo_height())
        self.buttom_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.buttom_frame.propagate(False)

        # Function to handle button hover
        def on_enter(event):
            event.widget.configure(bg="darkgrey")

        def on_leave(event):
            event.widget.configure(bg="white")

        # Adding buttons to the buttom_frame
        std_btn = tk.Button(self.buttom_frame, text="Student", bg="white", fg="black", font=("Arial", 12), width=50,
                            height=3, command=self.add_student)
        std_btn.pack(side=tk.TOP, padx=10, pady=10, anchor=tk.NW)
        std_btn.bind('<Enter>', on_enter)
        std_btn.bind('<Leave>', on_leave)

        sub_btn = tk.Button(self.buttom_frame, text="Teacher", bg="white", fg="black", font=("Arial", 12), width=50,
                            height=3, command=self.add_teacher)
        sub_btn.pack(side=tk.TOP, padx=10, pady=10, anchor=tk.NE)
        sub_btn.bind('<Enter>', on_enter)
        sub_btn.bind('<Leave>', on_leave)

        result_btn = tk.Button(self.buttom_frame, text="Result", bg="white", fg="black", font=("Arial", 12), width=50,
                               height=3, command=self.add_result)  # Removed the parentheses after add_result
        result_btn.pack(side=tk.TOP, padx=10, pady=10, anchor=tk.NW)
        result_btn.bind('<Enter>', on_enter)
        result_btn.bind('<Leave>', on_leave)

        mail_btn = tk.Button(self.buttom_frame, text="Send Mail", bg="white", fg="black", font=("Arial", 12), width=50,
                             height=3, command=self.send_mail)
        mail_btn.pack(side=tk.TOP, padx=10, pady=10, anchor=tk.NE)
        mail_btn.bind('<Enter>', on_enter)
        mail_btn.bind('<Leave>', on_leave)

#######################################################################################################################

    def assign_seat(self):
        # destroy any existing frame in right_frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # create new frame with desired content
        self.top_frame = tk.Frame(self.right_frame, bg="#181a1b", bd=1, height=80)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.top_frame.propagate(False)

        self.top_label = tk.Label(self.top_frame, text="Subject Creation", bg="#181a1b", foreground="white", font=5,
                                  height=4)
        self.top_label.pack(anchor=tk.NW, padx=10)
        self.top_label.propagate(True)

        self.buttom_frame = tk.Frame(self.right_frame, bg="#1e2222", bd=1, height=self.winfo_height())
        self.buttom_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.buttom_frame.propagate(False)

        self.sno_label = tk.Label(self.buttom_frame, text="sno", bg="#1e2222", foreground="white")
        self.sno_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.sno_entry = tk.Entry(self.buttom_frame)
        self.sno_entry.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.class_label = tk.Label(self.buttom_frame, text="Class", bg="#1e2222", foreground="white")
        self.class_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.class_entry= tk.Entry(self.buttom_frame)
        self.class_entry.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.room_label = tk.Label(self.buttom_frame, text="Room Number", bg="#1e2222", foreground="white")
        self.room_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.room_entry = tk.Entry(self.buttom_frame)
        self.room_entry.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.from_label = tk.Label(self.buttom_frame, text="Roll no From  ", bg="#1e2222", foreground="white")
        self.from_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.from_entry = tk.Entry(self.buttom_frame)
        self.from_entry.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.to_label = tk.Label(self.buttom_frame, text="Roll no TO", bg="#1e2222", foreground="white")
        self.to_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.to_entry = tk.Entry(self.buttom_frame)
        self.to_entry.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)


        def submit_data():
            sno = self.sno_entry.get()
            class_no = self.class_entry.get()
            room = self.room_entry.get()
            roll_from = self.from_entry.get()
            roll_to = self.to_entry.get()

            # Create a connection to the MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                port='3307',
                user='root',
                password='root',
                database='summer_project'
            )

            # Create a cursor object to execute queries
            cursor = conn.cursor()
            if sno:
                query = "UPDATE seat_placement set class=%s, room_number=%s, roll_from=%s, roll_to=%s where sno = %s"
                data = (class_no, room, roll_from, roll_to, sno)
                cursor.execute(query, data)
            else:
                # Insert data into the subjects table
                query = "INSERT INTO seat_placement (class, room_number, roll_from, roll_to) VALUES (%s, %s, %s, %s)"
                data = (class_no, room, roll_from, roll_to)
                cursor.execute(query, data)
            conn.commit()
            cursor.close()
            conn.close()

        self.submit = tk.Button(self.buttom_frame, text="Submit", command=submit_data)
        self.submit.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )

        def display_seat_placement_data():
            # Create a connection to the MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                port='3307',
                user='root',
                password='root',
                database='summer_project'
            )

            # Create a cursor object to execute queries
            cursor = conn.cursor()

            # Execute the SQL query to select all data from the seat_placement table
            cursor.execute("SELECT sno, class, room_number, roll_from, roll_to FROM seat_placement")

            # Fetch all the rows returned by the query
            rows = cursor.fetchall()

            # Create a new Tkinter window to display the table
            window = tk.Tk()
            window.title("Seat Placement Data")

            # Create a treeview widget to display the data in a table format
            tree = ttk.Treeview(window)
            tree["columns"] = ("sno", "class", "room_number", "roll_from", "roll_to")

            # Configure the treeview columns
            tree.column("#0", width=0, stretch=tk.NO)
            tree.column("sno", width=50)
            tree.column("class", width=100)
            tree.column("room_number", width=100)
            tree.column("roll_from", width=100)
            tree.column("roll_to", width=100)

            # Add column headings
            tree.heading("sno", text="SNO")
            tree.heading("class", text="Class")
            tree.heading("room_number", text="Room Number")
            tree.heading("roll_from", text="Roll From")
            tree.heading("roll_to", text="Roll To")

            # Insert data into the treeview
            for row in rows:
                tree.insert("", tk.END, values=row)

            # Pack the treeview widget
            tree.pack(fill="both", expand=True)

            # Main event loop for the Tkinter window
            window.mainloop()

        # Call the function to display seat placement data in a table
        display_seat_placement_data()

#####################################################################################
    def add_teacher(self):
        # destroy any existing frame in right_frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # create new frame with desired content
        self.top_frame = tk.Frame(self.right_frame, bg="#181a1b", bd=1, height=80)
        self.top_frame.place(relx=0.2, rely=0, relwidth=1, relheight=1)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.top_frame.propagate(False)

        self.top_label = tk.Label(self.top_frame, text="Subject Manage", bg="#181a1b", foreground="white", font=5,
                                  height=4)
        self.top_label.pack(anchor=tk.NW, padx=10)
        self.top_label.propagate(True)

        self.buttom_frame = tk.Frame(self.right_frame, bg="#1e2222", bd=1, height=self.winfo_height())
        self.buttom_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.buttom_frame.propagate(False)

        self.name_label = tk.Label(self.buttom_frame, text="Teacher Name", bg="#1e2222", foreground="white")
        self.name_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_name = tk.Entry(self.buttom_frame)
        self.entry_name.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.roll_label = tk.Label(self.buttom_frame, text="Teacher ID", bg="#1e2222", foreground="white")
        self.roll_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_roll = tk.Entry(self.buttom_frame)
        self.entry_roll.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.email_label = tk.Label(self.buttom_frame, text="Email ID", bg="#1e2222", foreground="white")
        self.email_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_email = tk.Entry(self.buttom_frame)
        self.entry_email.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.add_label = tk.Label(self.buttom_frame, text="Address", bg="#1e2222", foreground="white")
        self.add_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.add_entry = tk.Entry(self.buttom_frame)
        self.add_entry.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.gender_label = tk.Label(self.buttom_frame, text="Gender (Male/Female/Other)", bg="#1e2222",
                                     foreground="white")
        self.gender_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.gender_entry = tk.Entry(self.buttom_frame)
        self.gender_entry.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.DOB_label = tk.Label(self.buttom_frame, text="Date Of Birth", bg="#1e2222", foreground="white")
        self.DOB_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_date = tkcalendar.DateEntry(self.buttom_frame, width=12)
        self.entry_date.bind("<<DateEntrySelected>>", self.handle_date_selection)
        self.entry_date.pack(padx=10, pady=10, anchor=tk.W)

        def submit_clicked():
            # Retrieve values from the entry fields
            name = self.entry_name.get()
            teacher_id = self.entry_roll.get()
            email = self.entry_email.get()
            gender = self.gender_entry.get()
            address = self.add_entry.get()
            dob = self.entry_date.get()

            # Create a connection to the MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                port='3307',
                user='root',
                password='root',
                database='summer_project'
            )
            cursor = conn.cursor()

            # Insert data into the students table
            query = "INSERT INTO teachers (name, teacher_id, email, address, gender, dob) " \
                    "VALUES (%s, %s, %s, %s, %s, %s)"
            data = (name, teacher_id, email, address, gender, dob)
            cursor.execute(query, data)

            # Commit the changes and close the cursor and connection
            conn.commit()
            cursor.close()
            conn.close()

        self.submit = tk.Button(self.buttom_frame, text="Submit", command=submit_clicked)
        self.submit.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )


########################################################################################
    def manage_teachers(self):
        # destroy any existing frame in right_frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # create new frame with desired content
        self.top_frame = tk.Frame(self.right_frame, bg="#181a1b", bd=1, height=80)
        self.top_frame.place(relx=0.2, rely=0, relwidth=1, relheight=1)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.top_frame.propagate(False)

        self.top_label = tk.Label(self.top_frame, text="Subject Manage", bg="#181a1b", foreground="white", font=5,
                                  height=4)
        self.top_label.pack(anchor=tk.NW, padx=10)
        self.top_label.propagate(True)

        self.buttom_frame = tk.Frame(self.right_frame, bg="#1e2222", bd=1, height=self.winfo_height())
        self.buttom_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.buttom_frame.propagate(False)

        self.sno_label = tk.Label(self.buttom_frame, text="S no", bg="#1e2222", foreground="white")
        self.sno_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_sno = tk.Entry(self.buttom_frame)
        self.entry_sno.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.name_label = tk.Label(self.buttom_frame, text="Teacher Name", bg="#1e2222", foreground="white")
        self.name_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_name = tk.Entry(self.buttom_frame)
        self.entry_name.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.roll_label = tk.Label(self.buttom_frame, text="Teacher ID", bg="#1e2222", foreground="white")
        self.roll_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_roll = tk.Entry(self.buttom_frame)
        self.entry_roll.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.email_label = tk.Label(self.buttom_frame, text="Email ID", bg="#1e2222", foreground="white")
        self.email_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_email = tk.Entry(self.buttom_frame)
        self.entry_email.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.add_label = tk.Label(self.buttom_frame, text="Address", bg="#1e2222", foreground="white")
        self.add_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.add_entry = tk.Entry(self.buttom_frame)
        self.add_entry.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.gender_label = tk.Label(self.buttom_frame, text="Gender (Male/Female/Other)", bg="#1e2222",
                                     foreground="white")
        self.gender_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.gender_entry = tk.Entry(self.buttom_frame)
        self.gender_entry.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.DOB_label = tk.Label(self.buttom_frame, text="Date Of Birth", bg="#1e2222", foreground="white")
        self.DOB_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_date = tkcalendar.DateEntry(self.buttom_frame, width=12)
        self.entry_date.bind("<<DateEntrySelected>>", self.handle_date_selection)
        self.entry_date.pack(padx=10, pady=10, anchor=tk.W)

        def submit_clicked():
            # Retrieve values from the entry fields
            sno = self.entry_sno.get()
            name = self.entry_name.get()
            teacher_id = self.entry_roll.get()
            email = self.entry_email.get()
            gender = self.gender_entry.get()
            address = self.add_entry.get()
            dob = self.entry_date.get()

            # Create a connection to the MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                port='3307',
                user='root',
                password='root',
                database='summer_project'
            )
            cursor = conn.cursor()

            # Insert data into the students table
            query = "UPDATE teachers SET name=%s, teacher_id=%s, email=%s, address=%s, gender=%s, dob=%s where id =%s"
            data = (name, teacher_id, email, address, gender, dob, sno)
            cursor.execute(query, data)

            # Commit the changes and close the cursor and connection
            conn.commit()
            cursor.close()
            conn.close()

        self.submit = tk.Button(self.buttom_frame, text="Submit", command=submit_clicked)
        self.submit.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )

        def display_teacher_data():
            # Create a connection to the MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                port='3307',
                user='root',
                password='root',
                database='summer_project'
            )

            # Create a cursor object to execute queries
            cursor = conn.cursor()

            # Execute the SQL query to select all data from the Students table
            cursor.execute("SELECT id, name, teacher_id, email, address, gender, dob from teachers")

            # Fetch all the rows returned by the query
            rows = cursor.fetchall()

            # Create a new Tkinter window to display the table
            window = tk.Tk()
            window.title("Teacher Data")

            # Create a treeview widget to display the data in a table format
            tree = ttk.Treeview(window)
            tree["columns"] = ("id", "name", "teacher_id", "email", "address", "gender", "dob")

            # Configure the treeview columns
            tree.column("#0", width=0, stretch=tk.NO)
            tree.column("id", width=50)
            tree.column("name", width=100)
            tree.column("teacher_id", width=100)
            tree.column("email", width=150)
            tree.column("address", width=100)
            tree.column("gender", width=50)
            tree.column("dob", width=100)

            # Add column headings
            tree.heading("id", text="ID")
            tree.heading("name", text="Name")
            tree.heading("teacher_id", text="Teacher ID")
            tree.heading("email", text="Email")
            tree.heading("address", text="Address")
            tree.heading("gender", text="Gender")
            tree.heading("dob", text="DOB")

            # Insert data into the treeview
            for row in rows:
                tree.insert("", tk.END, values=row)

            # Pack the treeview widget
            tree.pack(fill="both", expand=True)

            # Main event loop for the Tkinter window
            window.mainloop()

            # Call the function to display subject data in a table

        display_teacher_data()

###################################################################################################

    def add_student(self):
        # destroy any existing frame in right_frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # create new frame with desired content
        self.top_frame = tk.Frame(self.right_frame, bg="#181a1b", bd=1, height=80)
        self.top_frame.place(relx=0.2, rely=0, relwidth=1, relheight=1)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.top_frame.propagate(False)

        self.top_label = tk.Label(self.top_frame, text="Student Admission", bg="#181a1b", foreground="white", font=5,
                                  height=4)
        self.top_label.pack(anchor=tk.NW, padx=10)
        self.top_label.propagate(True)

        self.buttom_frame = tk.Frame(self.right_frame, bg="#1e2222", bd=1, height=self.winfo_height())
        self.buttom_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.buttom_frame.propagate(False)

        self.name_label = tk.Label(self.buttom_frame, text="Student Name", bg="#1e2222", foreground="white")
        self.name_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_name = tk.Entry(self.buttom_frame)
        self.entry_name.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.roll_label = tk.Label(self.buttom_frame, text="Roll ID", bg="#1e2222", foreground="white")
        self.roll_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_roll = tk.Entry(self.buttom_frame)
        self.entry_roll.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.email_label = tk.Label(self.buttom_frame, text="Email ID", bg="#1e2222", foreground="white")
        self.email_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_email = tk.Entry(self.buttom_frame)
        self.entry_email.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.gender_label = tk.Label(self.buttom_frame, text="Gender (Male/Female/Other)", bg="#1e2222",
                                     foreground="white")
        self.gender_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.gender_entry = tk.Entry(self.buttom_frame)
        self.gender_entry.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.class_label = tk.Label(self.buttom_frame, text="Class", bg="#1e2222", foreground="white")
        self.class_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.class_entry = tk.Entry(self.buttom_frame)
        self.class_entry.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.section_label = tk.Label(self.buttom_frame, text="Section", bg="#1e2222", foreground="white")
        self.section_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_section = tk.Entry(self.buttom_frame)
        self.entry_section.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.DOB_label = tk.Label(self.buttom_frame, text="Date Of Birth", bg="#1e2222", foreground="white")
        self.DOB_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_date = tkcalendar.DateEntry(self.buttom_frame, width=12)
        self.entry_date.bind("<<DateEntrySelected>>", self.handle_date_selection)
        self.entry_date.pack(padx=10, pady=10, anchor=tk.W)

        def submit_clicked():
            # Retrieve values from the entry fields
            name = self.entry_name.get()
            roll_id = self.entry_roll.get()
            email = self.entry_email.get()
            gender = self.gender_entry.get()
            class_name = self.class_entry.get()
            section = self.entry_section.get()
            dob = self.entry_date.get()

            # Create a connection to the MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                port='3307',
                user='root',
                password='root',
                database='summer_project'
            )
            cursor = conn.cursor()

            # Insert data into the students table
            query = "INSERT INTO Students (student_name, roll_id, email, gender, class_name, section, dob) " \
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            data = (name, roll_id, email, gender, class_name, section, dob)
            cursor.execute(query, data)

            # Commit the changes and close the cursor and connection
            conn.commit()
            cursor.close()
            conn.close()

            # # Clear the entry fields
            # self.entry_name.delete(0, tk.END)
            # self.entry_roll.delete(0, tk.END)
            # self.entry_email.delete(0, tk.END)
            # self.gender_entry.delete(0, tk.END)
            # self.class_entry.delete(0, tk.END)
            # self.entry_section.delete(0, tk.END)
            # self.entry_date.delete(0, tk.END)

        self.submit = tk.Button(self.buttom_frame, text="Submit", command=submit_clicked)
        self.submit.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )

################################################################

    def manage_student(self):
        # destroy any existing frame in right_frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # create new frame with desired content
        self.top_frame = tk.Frame(self.right_frame, bg="#181a1b", bd=1, height=80)
        self.top_frame.place(relx=0.2, rely=0, relwidth=1, relheight=1)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.top_frame.propagate(False)

        self.top_label = tk.Label(self.top_frame, text="Student Manage", bg="#181a1b", foreground="white", font=5,
                                  height=4)
        self.top_label.pack(anchor=tk.NW, padx=10)
        self.top_label.propagate(True)

        self.buttom_frame = tk.Frame(self.right_frame, bg="#1e2222", bd=1, height=self.winfo_height())
        self.buttom_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.buttom_frame.propagate(False)

        self.sno_label = tk.Label(self.buttom_frame, text="S.no", bg="#1e2222", foreground="white")
        self.sno_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_sno = tk.Entry(self.buttom_frame)
        self.entry_sno.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.name_label = tk.Label(self.buttom_frame, text="Student Name", bg="#1e2222", foreground="white")
        self.name_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_name = tk.Entry(self.buttom_frame)
        self.entry_name.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.roll_label = tk.Label(self.buttom_frame, text="Roll ID", bg="#1e2222", foreground="white")
        self.roll_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_roll = tk.Entry(self.buttom_frame)
        self.entry_roll.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.email_label = tk.Label(self.buttom_frame, text="Email ID", bg="#1e2222", foreground="white")
        self.email_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_email = tk.Entry(self.buttom_frame)
        self.entry_email.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.gender_label = tk.Label(self.buttom_frame, text="Gender (Male/Female/Other)", bg="#1e2222",
                                     foreground="white")
        self.gender_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.gender_entry = tk.Entry(self.buttom_frame)
        self.gender_entry.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.class_label = tk.Label(self.buttom_frame, text="Class", bg="#1e2222", foreground="white")
        self.class_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.class_entry = tk.Entry(self.buttom_frame)
        self.class_entry.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.section_label = tk.Label(self.buttom_frame, text="Section", bg="#1e2222", foreground="white")
        self.section_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_section = tk.Entry(self.buttom_frame)
        self.entry_section.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        self.DOB_label = tk.Label(self.buttom_frame, text="Date Of Birth", bg="#1e2222", foreground="white")
        self.DOB_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_date = tkcalendar.DateEntry(self.buttom_frame, width=12)
        self.entry_date.pack(padx=10, pady=10, anchor=tk.W)

        def submit_clicked():
            # Retrieve values from the entry fields
            sno = self.entry_sno.get()
            name = self.entry_name.get()
            roll_id = self.entry_roll.get()
            email = self.entry_email.get()
            gender = self.gender_entry.get()
            class_name = self.class_entry.get()
            section = self.entry_section.get()
            dob = self.entry_date.get()

            # Create a connection to the MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                port='3307',
                user='root',
                password='root',
                database='summer_project'
            )
            cursor = conn.cursor()

            # Insert data into the students table
            query = "UPDATE Students SET student_name =%s, roll_id=%s, email=%s, gender=%s, class_name=%s, section=%s, dob=%s where sno =%s"
            data = (name, roll_id, email, gender, class_name, section, dob, sno)
            cursor.execute(query, data)

            # Commit the changes and close the cursor and connection
            conn.commit()
            cursor.close()
            conn.close()

        self.submit = tk.Button(self.buttom_frame, text="Update", command=submit_clicked)
        self.submit.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )

        def display_subject_data():
            # Create a connection to the MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                port='3307',
                user='root',
                password='root',
                database='summer_project'
            )

            # Create a cursor object to execute queries
            cursor = conn.cursor()

            # Execute the SQL query to select all data from the Students table
            cursor.execute("SELECT sno, student_name, roll_id, email, gender, class_name, section, dob FROM Students")

            # Fetch all the rows returned by the query
            rows = cursor.fetchall()

            # Create a new Tkinter window to display the table
            window = tk.Tk()
            window.title("Student Data")

            # Create a treeview widget to display the data in a table format
            tree = ttk.Treeview(window)
            tree["columns"] = ("sno", "student_name", "roll_id", "email", "gender", "class_name", "section", "dob")

            # Configure the treeview columns
            tree.column("#0", width=0, stretch=tk.NO)
            tree.column("sno", width=50)
            tree.column("student_name", width=100)
            tree.column("roll_id", width=50)
            tree.column("email", width=150)
            tree.column("gender", width=50)
            tree.column("class_name", width=50)
            tree.column("section", width=50)
            tree.column("dob", width=100)

            # Add column headings
            tree.heading("sno", text="Sno")
            tree.heading("student_name", text="Student Name")
            tree.heading("roll_id", text="Roll ID")
            tree.heading("email", text="Email")
            tree.heading("gender", text="Gender")
            tree.heading("class_name", text="Class")
            tree.heading("section", text="Section")
            tree.heading("dob", text="DOB")

            # Insert data into the treeview
            for row in rows:
                tree.insert("", tk.END, values=row)

            # Pack the treeview widget
            tree.pack(fill="both", expand=True)

            # Main event loop for the Tkinter window
            window.mainloop()

        # Call the function to display subject data in a table
        display_subject_data()

    ########################################################################################################################
    def add_result(self):
        # destroy any existing frame in right_frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # create new frame with desired content
        self.top_frame = tk.Frame(self.right_frame, bg="#181a1b", bd=1, height=80)
        self.top_frame.place(relx=0.2, rely=0, relwidth=1, relheight=1)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.top_frame.propagate(False)

        self.top_label = tk.Label(self.top_frame, text="Declare Result", bg="#181a1b", foreground="white", font=5,
                                  height=4)
        self.top_label.pack(anchor=tk.NW, padx=10)
        self.top_label.propagate(True)

        self.buttom_frame = tk.Frame(self.right_frame, bg="#1e2222", bd=1, height=self.winfo_height())
        self.buttom_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.buttom_frame.propagate(False)

        self.class_label = tk.Label(self.buttom_frame, text="Class", bg="#1e2222", foreground="white")
        self.class_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_class = tk.Entry(self.buttom_frame)
        self.entry_class.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)
        self.entry_class.bind("<KeyRelease>", self.grade_entry)

    def grade_entry(self, event):
        # Get the selected class entry
        class_entry = self.entry_class.get()

        ##########
        # Create new frame with desired content based on class entry
        if class_entry == "one" or class_entry == "One" or class_entry == "1":

            label1 = tk.Label(self.buttom_frame, text="Student Name", bg="#1e2222", fg="white")
            label1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry1 = tk.Entry(self.buttom_frame)
            entry1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label2 = tk.Label(self.buttom_frame, text="Roll no", bg="#1e2222", fg="white")
            label2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry2 = tk.Entry(self.buttom_frame)
            entry2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label3 = tk.Label(self.buttom_frame, text="Term", bg="#1e2222", fg="white")
            label3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry3 = tk.Entry(self.buttom_frame)
            entry3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label4 = tk.Label(self.buttom_frame, text="Science", bg="#1e2222", fg="white")
            label4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry4 = tk.Entry(self.buttom_frame)
            entry4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label5 = tk.Label(self.buttom_frame, text="Social", bg="#1e2222", fg="white")
            label5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry5 = tk.Entry(self.buttom_frame)
            entry5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label6 = tk.Label(self.buttom_frame, text="English", bg="#1e2222", fg="white")
            label6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry6 = tk.Entry(self.buttom_frame)
            entry6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label7 = tk.Label(self.buttom_frame, text="Nepali", bg="#1e2222", fg="white")
            label7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry7 = tk.Entry(self.buttom_frame)
            entry7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label8 = tk.Label(self.buttom_frame, text="Maths", bg="#1e2222", fg="white")
            label8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry8 = tk.Entry(self.buttom_frame)
            entry8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            def submit_data():
                student_name = entry1.get()
                roll_id = entry2.get()
                term = entry3.get()
                science = entry4.get()
                social = entry5.get()
                english = entry6.get()
                nepali = entry7.get()
                maths = entry8.get()

                # Assuming you are using SQLite as the database
                conn = mysql.connector.connect(
                    host='localhost',
                    port='3307',
                    user='root',
                    password='root',
                    database='summer_project'
                )
                cursor = conn.cursor()

                # Insert data into the students table
                query = "INSERT INTO class_one (student_name, roll_no, term, science, social, english, nepali, maths) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                data = (student_name, roll_id, term, science, social, english, nepali, maths)
                cursor.execute(query, data)

                # Commit the changes and close the cursor and connection
                conn.commit()
                cursor.close()
                conn.close()

                # Clear the entry fields after submitting
                entry1.delete(0, tk.END)
                entry2.delete(0, tk.END)
                entry3.delete(0, tk.END)
                entry4.delete(0, tk.END)
                entry5.delete(0, tk.END)
                entry6.delete(0, tk.END)
                entry7.delete(0, tk.END)
                entry8.delete(0, tk.END)

            self.submit = tk.Button(self.buttom_frame, text="Submit", command=submit_data)
            self.submit.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )
            self.buttom_frame.update()
        #########
        elif class_entry == "two" or class_entry == "Two" or class_entry == "2":
            label1 = tk.Label(self.buttom_frame, text="Student Name", bg="#1e2222", fg="white")
            label1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry1 = tk.Entry(self.buttom_frame)
            entry1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label2 = tk.Label(self.buttom_frame, text="Roll no", bg="#1e2222", fg="white")
            label2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry2 = tk.Entry(self.buttom_frame)
            entry2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label3 = tk.Label(self.buttom_frame, text="Term", bg="#1e2222", fg="white")
            label3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry3 = tk.Entry(self.buttom_frame)
            entry3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label4 = tk.Label(self.buttom_frame, text="Science", bg="#1e2222", fg="white")
            label4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry4 = tk.Entry(self.buttom_frame)
            entry4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label5 = tk.Label(self.buttom_frame, text="Social", bg="#1e2222", fg="white")
            label5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry5 = tk.Entry(self.buttom_frame)
            entry5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label6 = tk.Label(self.buttom_frame, text="English", bg="#1e2222", fg="white")
            label6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry6 = tk.Entry(self.buttom_frame)
            entry6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label7 = tk.Label(self.buttom_frame, text="Nepali", bg="#1e2222", fg="white")
            label7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry7 = tk.Entry(self.buttom_frame)
            entry7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label8 = tk.Label(self.buttom_frame, text="Maths", bg="#1e2222", fg="white")
            label8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry8 = tk.Entry(self.buttom_frame)
            entry8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label9 = tk.Label(self.buttom_frame, text="Moral", bg="#1e2222", fg="white")
            label9.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry9 = tk.Entry(self.buttom_frame)
            entry9.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            def submit_data():
                student_name = entry1.get()
                roll_id = entry2.get()
                term = entry3.get()
                science = entry4.get()
                social = entry5.get()
                english = entry6.get()
                nepali = entry7.get()
                maths = entry8.get()
                moral = entry9.get()

                # Assuming you are using SQLite as the database
                conn = mysql.connector.connect(
                    host='localhost',
                    port='3307',
                    user='root',
                    password='root',
                    database='summer_project'
                )
                cursor = conn.cursor()

                # Insert data into the students table
                query = "INSERT INTO class_two (student_name, roll_no, term, science, social, english, nepali, maths, moral) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                data = (student_name, roll_id, term, science, social, english, nepali, maths, moral)
                cursor.execute(query, data)

                # Commit the changes and close the cursor and connection
                conn.commit()
                cursor.close()
                conn.close()

                # Clear the entry fields after submitting
                entry1.delete(0, tk.END)
                entry2.delete(0, tk.END)
                entry3.delete(0, tk.END)
                entry4.delete(0, tk.END)
                entry5.delete(0, tk.END)
                entry6.delete(0, tk.END)
                entry7.delete(0, tk.END)
                entry8.delete(0, tk.END)
                entry9.delete(0, tk.END)

            self.submit = tk.Button(self.buttom_frame, text="Submit", command=submit_data)
            self.submit.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )
            self.buttom_frame.update()
        ##########
        elif class_entry == "three" or class_entry == "Three" or class_entry == "3":
            label1 = tk.Label(self.buttom_frame, text="Student Name", bg="#1e2222", fg="white")
            label1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry1 = tk.Entry(self.buttom_frame)
            entry1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label2 = tk.Label(self.buttom_frame, text="Roll no", bg="#1e2222", fg="white")
            label2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry2 = tk.Entry(self.buttom_frame)
            entry2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label3 = tk.Label(self.buttom_frame, text="Term", bg="#1e2222", fg="white")
            label3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry3 = tk.Entry(self.buttom_frame)
            entry3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label4 = tk.Label(self.buttom_frame, text="Science", bg="#1e2222", fg="white")
            label4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry4 = tk.Entry(self.buttom_frame)
            entry4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label5 = tk.Label(self.buttom_frame, text="Social", bg="#1e2222", fg="white")
            label5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry5 = tk.Entry(self.buttom_frame)
            entry5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label6 = tk.Label(self.buttom_frame, text="English", bg="#1e2222", fg="white")
            label6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry6 = tk.Entry(self.buttom_frame)
            entry6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label7 = tk.Label(self.buttom_frame, text="Nepali", bg="#1e2222", fg="white")
            label7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry7 = tk.Entry(self.buttom_frame)
            entry7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label8 = tk.Label(self.buttom_frame, text="Maths", bg="#1e2222", fg="white")
            label8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry8 = tk.Entry(self.buttom_frame)
            entry8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label9 = tk.Label(self.buttom_frame, text="Moral/comm", bg="#1e2222", fg="white")
            label9.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry9 = tk.Entry(self.buttom_frame)
            entry9.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            def submit_data():
                student_name = entry1.get()
                roll_id = entry2.get()
                term = entry3.get()
                science = entry4.get()
                social = entry5.get()
                english = entry6.get()
                nepali = entry7.get()
                maths = entry8.get()
                moral = entry9.get()

                # Assuming you are using SQLite as the database
                conn = mysql.connector.connect(
                    host='localhost',
                    port='3307',
                    user='root',
                    password='root',
                    database='summer_project'
                )
                cursor = conn.cursor()

                # Insert data into the students table
                query = "INSERT INTO class_three (student_name, roll_no, term, science, social, english, nepali, maths, moral_comm) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                data = (student_name, roll_id, term, science, social, english, nepali, maths, moral)
                cursor.execute(query, data)

                # Commit the changes and close the cursor and connection
                conn.commit()
                cursor.close()
                conn.close()

                # Clear the entry fields after submitting
                entry1.delete(0, tk.END)
                entry2.delete(0, tk.END)
                entry3.delete(0, tk.END)
                entry4.delete(0, tk.END)
                entry5.delete(0, tk.END)
                entry6.delete(0, tk.END)
                entry7.delete(0, tk.END)
                entry8.delete(0, tk.END)
                entry9.delete(0, tk.END)

            self.submit = tk.Button(self.buttom_frame, text="Submit", command=submit_data)
            self.submit.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )
        ##########
        elif class_entry == "four" or class_entry == "Four" or class_entry == "4":
            label1 = tk.Label(self.buttom_frame, text="Student Name", bg="#1e2222", fg="white")
            label1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry1 = tk.Entry(self.buttom_frame)
            entry1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label2 = tk.Label(self.buttom_frame, text="Roll no", bg="#1e2222", fg="white")
            label2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry2 = tk.Entry(self.buttom_frame)
            entry2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label3 = tk.Label(self.buttom_frame, text="Term", bg="#1e2222", fg="white")
            label3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry3 = tk.Entry(self.buttom_frame)
            entry3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label4 = tk.Label(self.buttom_frame, text="Science", bg="#1e2222", fg="white")
            label4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry4 = tk.Entry(self.buttom_frame)
            entry4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label5 = tk.Label(self.buttom_frame, text="Social+moral", bg="#1e2222", fg="white")
            label5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry5 = tk.Entry(self.buttom_frame)
            entry5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label6 = tk.Label(self.buttom_frame, text="English", bg="#1e2222", fg="white")
            label6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry6 = tk.Entry(self.buttom_frame)
            entry6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label7 = tk.Label(self.buttom_frame, text="Nepali", bg="#1e2222", fg="white")
            label7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry7 = tk.Entry(self.buttom_frame)
            entry7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label8 = tk.Label(self.buttom_frame, text="Maths", bg="#1e2222", fg="white")
            label8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry8 = tk.Entry(self.buttom_frame)
            entry8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label9 = tk.Label(self.buttom_frame, text="Comm", bg="#1e2222", fg="white")
            label9.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry9 = tk.Entry(self.buttom_frame)
            entry9.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            def submit_data():
                student_name = entry1.get()
                roll_id = entry2.get()
                term = entry3.get()
                science = entry4.get()
                social = entry5.get()
                english = entry6.get()
                nepali = entry7.get()
                maths = entry8.get()
                moral = entry9.get()

                # Assuming you are using SQLite as the database
                conn = mysql.connector.connect(
                    host='localhost',
                    port='3307',
                    user='root',
                    password='root',
                    database='summer_project'
                )
                cursor = conn.cursor()

                # Insert data into the students table
                query = "INSERT INTO class_four (student_name, roll_no, term, science, social_moral, english, nepali, maths, comm) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                data = (student_name, roll_id, term, science, social, english, nepali, maths, moral)
                cursor.execute(query, data)

                # Commit the changes and close the cursor and connection
                conn.commit()
                cursor.close()
                conn.close()

                # Clear the entry fields after submitting
                entry1.delete(0, tk.END)
                entry2.delete(0, tk.END)
                entry3.delete(0, tk.END)
                entry4.delete(0, tk.END)
                entry5.delete(0, tk.END)
                entry6.delete(0, tk.END)
                entry7.delete(0, tk.END)
                entry8.delete(0, tk.END)
                entry9.delete(0, tk.END)

            self.submit = tk.Button(self.buttom_frame, text="Submit", command=submit_data)
            self.submit.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )
        ##########
        elif class_entry == "five" or class_entry == "Five" or class_entry == "5":
            label1 = tk.Label(self.buttom_frame, text="Student Name", bg="#1e2222", fg="white")
            label1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry1 = tk.Entry(self.buttom_frame)
            entry1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label2 = tk.Label(self.buttom_frame, text="Roll no", bg="#1e2222", fg="white")
            label2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry2 = tk.Entry(self.buttom_frame)
            entry2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label3 = tk.Label(self.buttom_frame, text="Term", bg="#1e2222", fg="white")
            label3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry3 = tk.Entry(self.buttom_frame)
            entry3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label4 = tk.Label(self.buttom_frame, text="Science", bg="#1e2222", fg="white")
            label4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry4 = tk.Entry(self.buttom_frame)
            entry4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label5 = tk.Label(self.buttom_frame, text="Social+moral", bg="#1e2222", fg="white")
            label5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry5 = tk.Entry(self.buttom_frame)
            entry5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label6 = tk.Label(self.buttom_frame, text="English", bg="#1e2222", fg="white")
            label6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry6 = tk.Entry(self.buttom_frame)
            entry6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label7 = tk.Label(self.buttom_frame, text="Nepali", bg="#1e2222", fg="white")
            label7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry7 = tk.Entry(self.buttom_frame)
            entry7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label8 = tk.Label(self.buttom_frame, text="Maths", bg="#1e2222", fg="white")
            label8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry8 = tk.Entry(self.buttom_frame)
            entry8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label9 = tk.Label(self.buttom_frame, text="Comm", bg="#1e2222", fg="white")
            label9.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry9 = tk.Entry(self.buttom_frame)
            entry9.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            def submit_data():
                student_name = entry1.get()
                roll_id = entry2.get()
                term = entry3.get()
                science = entry4.get()
                social = entry5.get()
                english = entry6.get()
                nepali = entry7.get()
                maths = entry8.get()
                moral = entry9.get()

                # Assuming you are using SQLite as the database
                conn = mysql.connector.connect(
                    host='localhost',
                    port='3307',
                    user='root',
                    password='root',
                    database='summer_project'
                )
                cursor = conn.cursor()

                # Insert data into the students table
                query = "INSERT INTO class_five (student_name, roll_no, term, science, social_moral, english, nepali, maths, comm) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                data = (student_name, roll_id, term, science, social, english, nepali, maths, moral)
                cursor.execute(query, data)

                # Commit the changes and close the cursor and connection
                conn.commit()
                cursor.close()
                conn.close()

                # Clear the entry fields after submitting
                entry1.delete(0, tk.END)
                entry2.delete(0, tk.END)
                entry3.delete(0, tk.END)
                entry4.delete(0, tk.END)
                entry5.delete(0, tk.END)
                entry6.delete(0, tk.END)
                entry7.delete(0, tk.END)
                entry8.delete(0, tk.END)
                entry9.delete(0, tk.END)

            self.submit = tk.Button(self.buttom_frame, text="Submit", command=submit_data)
            self.submit.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )

    ########################################################################################################################

    def manage_mark(self):
        # destroy any existing frame in right_frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # create new frame with desired content
        self.top_frame = tk.Frame(self.right_frame, bg="#181a1b", bd=1, height=80)
        self.top_frame.place(relx=0.2, rely=0, relwidth=1, relheight=1)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.top_frame.propagate(False)

        self.top_label = tk.Label(self.top_frame, text="Result Manage", bg="#181a1b", foreground="white", font=5,
                                  height=4)
        self.top_label.pack(anchor=tk.NW, padx=10)
        self.top_label.propagate(True)

        self.buttom_frame = tk.Frame(self.right_frame, bg="#1e2222", bd=1, height=self.winfo_height())
        self.buttom_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.buttom_frame.propagate(False)

        self.class_label = tk.Label(self.buttom_frame, text="Class", bg="#1e2222", foreground="white")
        self.class_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        self.entry_class = tk.Entry(self.buttom_frame)
        self.entry_class.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)
        self.entry_class.bind("<KeyRelease>", self.manage_entry)

    ########################################################################################################################
    def manage_entry(self, event):
        # Get the selected class entry
        class_entry = self.entry_class.get()

        # Create new frame with desired content based on class entry
        if class_entry == "one" or class_entry == "One" or class_entry == "1":

            # Create a connection to the MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                port='3307',
                user='root',
                password='root',
                database='summer_project'
            )

            # Create a cursor object to execute queries
            cursor = conn.cursor()

            # Execute the SQL query to select all data from the class_one table
            cursor.execute(
                "SELECT sno, student_name, roll_no, term, social, science, maths, nepali, english FROM class_one")

            # Fetch all the rows returned by the query
            rows = cursor.fetchall()

            # Create a new Tkinter window to display the table
            window = tk.Tk()
            window.title("Grade 1")

            # Create a treeview widget to display the data in a table format
            tree = ttk.Treeview(window)
            tree["columns"] = (
                "sno", "student_name", "roll_no", "term", "social", "science", "maths", "nepali", "english")

            # Configure the treeview columns
            tree.column("#0", width=0, stretch=tk.NO)
            tree.column("sno", width=50)
            tree.column("student_name", width=100)
            tree.column("roll_no", width=50)
            tree.column("term", width=50)
            tree.column("social", width=50)
            tree.column("science", width=50)
            tree.column("maths", width=50)
            tree.column("nepali", width=50)
            tree.column("english", width=50)

            # Add column headings
            tree.heading("sno", text="Sno")
            tree.heading("student_name", text="Student Name")
            tree.heading("roll_no", text="Roll ID")
            tree.heading("term", text="Term")
            tree.heading("social", text="Social")
            tree.heading("science", text="Science")
            tree.heading("maths", text="Maths")
            tree.heading("nepali", text="Nepali")
            tree.heading("english", text="English")

            # Insert data into the treeview
            for row in rows:
                tree.insert("", tk.END, values=row)

            # Pack the treeview widget
            tree.pack(fill="both", expand=True)

            label0 = tk.Label(self.buttom_frame, text="s no", bg="#1e2222", fg="white")
            label0.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry0 = tk.Entry(self.buttom_frame)
            entry0.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label1 = tk.Label(self.buttom_frame, text="Student Name", bg="#1e2222", fg="white")
            label1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry1 = tk.Entry(self.buttom_frame)
            entry1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label2 = tk.Label(self.buttom_frame, text="Roll no", bg="#1e2222", fg="white")
            label2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry2 = tk.Entry(self.buttom_frame)
            entry2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label3 = tk.Label(self.buttom_frame, text="Term", bg="#1e2222", fg="white")
            label3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry3 = tk.Entry(self.buttom_frame)
            entry3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label4 = tk.Label(self.buttom_frame, text="Social", bg="#1e2222", fg="white")
            label4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry4 = tk.Entry(self.buttom_frame)
            entry4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label5 = tk.Label(self.buttom_frame, text="Science", bg="#1e2222", fg="white")
            label5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry5 = tk.Entry(self.buttom_frame)
            entry5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label6 = tk.Label(self.buttom_frame, text="Maths", bg="#1e2222", fg="white")
            label6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry6 = tk.Entry(self.buttom_frame)
            entry6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label7 = tk.Label(self.buttom_frame, text="Nepali", bg="#1e2222", fg="white")
            label7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry7 = tk.Entry(self.buttom_frame)
            entry7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label8 = tk.Label(self.buttom_frame, text="English", bg="#1e2222", fg="white")
            label8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry8 = tk.Entry(self.buttom_frame)
            entry8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            def submit_data():
                sn = entry0.get()
                student_name = entry1.get()
                roll_no = entry2.get()
                term = entry3.get()
                science = entry4.get()
                social = entry5.get()
                english = entry6.get()
                nepali = entry7.get()
                maths = entry8.get()

                # Assuming you are using SQLite as the database
                conn = mysql.connector.connect(
                    host='localhost',
                    port='3307',
                    user='root',
                    password='root',
                    database='summer_project'
                )
                cursor = conn.cursor()

                # Insert data into the students table
                query = "UPDATE class_one SET student_name=%s, roll_no=%s, term=%s, science=%s, social=%s, " \
                        "english=%s, nepali=%s, maths=%s where sno=%s"
                data = (student_name, roll_no, term, science, social, english, nepali, maths, sn)
                cursor.execute(query, data)

                # Commit the changes and close the cursor and connection
                conn.commit()
                cursor.close()
                conn.close()

                # Clear the entry fields after submitting
                entry1.delete(0, tk.END)
                entry2.delete(0, tk.END)
                entry3.delete(0, tk.END)
                entry4.delete(0, tk.END)
                entry5.delete(0, tk.END)
                entry6.delete(0, tk.END)
                entry7.delete(0, tk.END)
                entry8.delete(0, tk.END)

            self.submit = tk.Button(self.buttom_frame, text="Submit", command=submit_data)
            self.submit.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )
            self.buttom_frame.update()

        # ---------------------------------------------------------------------------------------------------------------------#

        elif class_entry == "two" or class_entry == "Two" or class_entry == "2":

            # Create a connection to the MySQL database
            conn = mysql.connector.connect(
                host='localhost',
                port='3307',
                user='root',
                password='root',
                database='summer_project'
            )

            # Create a cursor object to execute queries
            cursor = conn.cursor()

            # Execute the SQL query to select all data from the class_one table
            cursor.execute(
                "SELECT sno, student_name, roll_no, term, social, science, maths, nepali, english, moral FROM class_two")

            # Fetch all the rows returned by the query
            rows = cursor.fetchall()

            # Create a new Tkinter window to display the table
            window = tk.Tk()
            window.title("Mark Sheet")

            # Create a treeview widget to display the data in a table format
            tree = ttk.Treeview(window)
            tree["columns"] = (
                "sno", "student_name", "roll_no", "term", "social", "science", "maths", "nepali", "english", "moral")

            # Configure the treeview columns
            tree.column("#0", width=0, stretch=tk.NO)
            tree.column("sno", width=50)
            tree.column("student_name", width=100)
            tree.column("roll_no", width=50)
            tree.column("term", width=50)
            tree.column("social", width=50)
            tree.column("science", width=50)
            tree.column("maths", width=50)
            tree.column("nepali", width=50)
            tree.column("english", width=50)
            tree.column("moral", width=50)

            # Add column headings
            tree.heading("sno", text="Sno")
            tree.heading("student_name", text="Student Name")
            tree.heading("roll_no", text="Roll ID")
            tree.heading("term", text="Term")
            tree.heading("social", text="Social")
            tree.heading("science", text="Science")
            tree.heading("maths", text="Maths")
            tree.heading("nepali", text="Nepali")
            tree.heading("english", text="English")
            tree.heading("moral", text="Moral")

            # Insert data into the treeview
            for row in rows:
                tree.insert("", tk.END, values=row)

            # Pack the treeview widget
            tree.pack(fill="both", expand=True)

            label0 = tk.Label(self.buttom_frame, text="s no", bg="#1e2222", fg="white")
            label0.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry0 = tk.Entry(self.buttom_frame)
            entry0.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label1 = tk.Label(self.buttom_frame, text="Student Name", bg="#1e2222", fg="white")
            label1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry1 = tk.Entry(self.buttom_frame)
            entry1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label2 = tk.Label(self.buttom_frame, text="Roll no", bg="#1e2222", fg="white")
            label2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry2 = tk.Entry(self.buttom_frame)
            entry2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label3 = tk.Label(self.buttom_frame, text="Term", bg="#1e2222", fg="white")
            label3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry3 = tk.Entry(self.buttom_frame)
            entry3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label4 = tk.Label(self.buttom_frame, text="Social", bg="#1e2222", fg="white")
            label4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry4 = tk.Entry(self.buttom_frame)
            entry4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label5 = tk.Label(self.buttom_frame, text="Science", bg="#1e2222", fg="white")
            label5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry5 = tk.Entry(self.buttom_frame)
            entry5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label6 = tk.Label(self.buttom_frame, text="Maths", bg="#1e2222", fg="white")
            label6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry6 = tk.Entry(self.buttom_frame)
            entry6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label7 = tk.Label(self.buttom_frame, text="Nepali", bg="#1e2222", fg="white")
            label7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry7 = tk.Entry(self.buttom_frame)
            entry7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label8 = tk.Label(self.buttom_frame, text="English", bg="#1e2222", fg="white")
            label8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry8 = tk.Entry(self.buttom_frame)
            entry8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label9 = tk.Label(self.buttom_frame, text="Moral", bg="#1e2222", fg="white")
            label9.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry9 = tk.Entry(self.buttom_frame)
            entry9.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            def submit_data():
                sn = entry0.get()
                student_name = entry1.get()
                roll_no = entry2.get()
                term = entry3.get()
                science = entry4.get()
                social = entry5.get()
                english = entry6.get()
                nepali = entry7.get()
                maths = entry8.get()
                moral = entry9.get()

                # Assuming you are using SQLite as the database
                conn = mysql.connector.connect(
                    host='localhost',
                    port='3307',
                    user='root',
                    password='root',
                    database='summer_project'
                )
                cursor = conn.cursor()

                # Insert data into the students table
                query = "UPDATE class_two SET student_name=%s, roll_no=%s, term=%s, science=%s, social=%s, " \
                        "english=%s, nepali=%s, maths=%s, moral=%s where sno=%s"
                data = (student_name, roll_no, term, science, social, english, nepali, maths, moral, sn)
                cursor.execute(query, data)

                # Commit the changes and close the cursor and connection
                conn.commit()
                cursor.close()
                conn.close()

                # Clear the entry fields after submitting
                entry0.delete(0, tk.END)
                entry1.delete(0, tk.END)
                entry2.delete(0, tk.END)
                entry3.delete(0, tk.END)
                entry4.delete(0, tk.END)
                entry5.delete(0, tk.END)
                entry6.delete(0, tk.END)
                entry7.delete(0, tk.END)
                entry8.delete(0, tk.END)

            self.submit = tk.Button(self.buttom_frame, text="Submit", command=submit_data)
            self.submit.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )
            self.buttom_frame.update()

        # ---------------------------------------------------------------------------------------------------------------------#

        elif class_entry == "three" or class_entry == "Three" or class_entry == "3":

            conn = mysql.connector.connect(
                host='localhost',
                port='3307',
                user='root',
                password='root',
                database='summer_project'
            )

            # Create a cursor object to execute queries
            cursor = conn.cursor()

            # Execute the SQL query to select all data from the class_one table
            cursor.execute(
                "SELECT sno, student_name, roll_no, term, social, science, maths, nepali, english, moral_comm FROM class_three")

            # Fetch all the rows returned by the query
            rows = cursor.fetchall()

            # Create a new Tkinter window to display the table
            window = tk.Tk()
            window.title("Mark Sheet")

            # Create a treeview widget to display the data in a table format
            tree = ttk.Treeview(window)
            tree["columns"] = (
                "sno", "student_name", "roll_no", "term", "social", "science", "maths", "nepali", "english",
                "moral_comm")

            # Configure the treeview columns
            tree.column("#0", width=0, stretch=tk.NO)
            tree.column("sno", width=50)
            tree.column("student_name", width=100)
            tree.column("roll_no", width=50)
            tree.column("term", width=50)
            tree.column("social", width=50)
            tree.column("science", width=50)
            tree.column("maths", width=50)
            tree.column("nepali", width=50)
            tree.column("english", width=50)
            tree.column("moral_comm", width=50)

            # Add column headings
            tree.heading("sno", text="Sno")
            tree.heading("student_name", text="Student Name")
            tree.heading("roll_no", text="Roll ID")
            tree.heading("term", text="Term")
            tree.heading("social", text="Social")
            tree.heading("science", text="Science")
            tree.heading("maths", text="Maths")
            tree.heading("nepali", text="Nepali")
            tree.heading("english", text="English")
            tree.heading("moral_comm", text="Moral/Comm")

            # Insert data into the treeview
            for row in rows:
                tree.insert("", tk.END, values=row)

            # Pack the treeview widget
            tree.pack(fill="both", expand=True)

            label0 = tk.Label(self.buttom_frame, text="s no", bg="#1e2222", fg="white")
            label0.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry0 = tk.Entry(self.buttom_frame)
            entry0.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label1 = tk.Label(self.buttom_frame, text="Student Name", bg="#1e2222", fg="white")
            label1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry1 = tk.Entry(self.buttom_frame)
            entry1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label2 = tk.Label(self.buttom_frame, text="Roll no", bg="#1e2222", fg="white")
            label2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry2 = tk.Entry(self.buttom_frame)
            entry2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label3 = tk.Label(self.buttom_frame, text="Term", bg="#1e2222", fg="white")
            label3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry3 = tk.Entry(self.buttom_frame)
            entry3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label4 = tk.Label(self.buttom_frame, text="Science", bg="#1e2222", fg="white")
            label4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry4 = tk.Entry(self.buttom_frame)
            entry4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label5 = tk.Label(self.buttom_frame, text="Social", bg="#1e2222", fg="white")
            label5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry5 = tk.Entry(self.buttom_frame)
            entry5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label6 = tk.Label(self.buttom_frame, text="English", bg="#1e2222", fg="white")
            label6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry6 = tk.Entry(self.buttom_frame)
            entry6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label7 = tk.Label(self.buttom_frame, text="Nepali", bg="#1e2222", fg="white")
            label7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry7 = tk.Entry(self.buttom_frame)
            entry7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label8 = tk.Label(self.buttom_frame, text="Maths", bg="#1e2222", fg="white")
            label8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry8 = tk.Entry(self.buttom_frame)
            entry8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label9 = tk.Label(self.buttom_frame, text="Moral/comm", bg="#1e2222", fg="white")
            label9.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry9 = tk.Entry(self.buttom_frame)
            entry9.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            def submit_data():
                sn = entry0.get()
                student_name = entry1.get()
                roll_no = entry2.get()
                term = entry3.get()
                science = entry4.get()
                social = entry5.get()
                english = entry6.get()
                nepali = entry7.get()
                maths = entry8.get()
                moral = entry9.get()

                # Assuming you are using SQLite as the database
                conn = mysql.connector.connect(
                    host='localhost',
                    port='3307',
                    user='root',
                    password='root',
                    database='summer_project'
                )
                cursor = conn.cursor()

                # Insert data into the students table
                query = "UPDATE class_three SET student_name=%s, roll_no=%s, term=%s, science=%s, social=%s, " \
                        "english=%s, nepali=%s, maths=%s, moral_comm=%s where sno=%s"
                data = (student_name, roll_no, term, science, social, english, nepali, maths, moral, sn)
                cursor.execute(query, data)

                # Commit the changes and close the cursor and connection
                conn.commit()
                cursor.close()
                conn.close()

                # Clear the entry fields after submitting
                entry0.delete(0, tk.END)
                entry1.delete(0, tk.END)
                entry2.delete(0, tk.END)
                entry3.delete(0, tk.END)
                entry4.delete(0, tk.END)
                entry5.delete(0, tk.END)
                entry6.delete(0, tk.END)
                entry7.delete(0, tk.END)
                entry8.delete(0, tk.END)

            self.submit = tk.Button(self.buttom_frame, text="Submit", command=submit_data)
            self.submit.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )

        # ---------------------------------------------------------------------------------------------------------------------#

        elif class_entry == "four" or class_entry == "Four" or class_entry == "4":

            conn = mysql.connector.connect(
                host='localhost',
                port='3307',
                user='root',
                password='root',
                database='summer_project'
            )

            # Create a cursor object to execute queries
            cursor = conn.cursor()

            # Execute the SQL query to select all data from the class_one table
            cursor.execute(
                "SELECT sno, student_name, roll_no, term, social_moral, science, maths, nepali, english, comm FROM class_four")

            # Fetch all the rows returned by the query
            rows = cursor.fetchall()

            # Create a new Tkinter window to display the table
            window = tk.Tk()
            window.title("Mark Sheet")

            # Create a treeview widget to display the data in a table format
            tree = ttk.Treeview(window)
            tree["columns"] = (
                "sno", "student_name", "roll_no", "term", "social_moral", "science", "maths", "nepali", "english",
                "comm")

            # Configure the treeview columns
            tree.column("#0", width=0, stretch=tk.NO)
            tree.column("sno", width=50)
            tree.column("student_name", width=100)
            tree.column("roll_no", width=50)
            tree.column("term", width=50)
            tree.column("social_moral", width=50)
            tree.column("science", width=50)
            tree.column("maths", width=50)
            tree.column("nepali", width=50)
            tree.column("english", width=50)
            tree.column("comm", width=50)

            # Add column headings
            tree.heading("sno", text="Sno")
            tree.heading("student_name", text="Student Name")
            tree.heading("roll_no", text="Roll ID")
            tree.heading("term", text="Term")
            tree.heading("social_moral", text="Social+moral")
            tree.heading("science", text="Science")
            tree.heading("maths", text="Maths")
            tree.heading("nepali", text="Nepali")
            tree.heading("english", text="English")
            tree.heading("comm", text="Comm")

            # Insert data into the treeview
            for row in rows:
                tree.insert("", tk.END, values=row)

            # Pack the treeview widget
            tree.pack(fill="both", expand=True)

            label0 = tk.Label(self.buttom_frame, text="s no", bg="#1e2222", fg="white")
            label0.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry0 = tk.Entry(self.buttom_frame)
            entry0.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label1 = tk.Label(self.buttom_frame, text="Student Name", bg="#1e2222", fg="white")
            label1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry1 = tk.Entry(self.buttom_frame)
            entry1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label2 = tk.Label(self.buttom_frame, text="Roll no", bg="#1e2222", fg="white")
            label2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry2 = tk.Entry(self.buttom_frame)
            entry2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label3 = tk.Label(self.buttom_frame, text="Term", bg="#1e2222", fg="white")
            label3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry3 = tk.Entry(self.buttom_frame)
            entry3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label4 = tk.Label(self.buttom_frame, text="Science", bg="#1e2222", fg="white")
            label4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry4 = tk.Entry(self.buttom_frame)
            entry4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label5 = tk.Label(self.buttom_frame, text="Social+moral", bg="#1e2222", fg="white")
            label5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry5 = tk.Entry(self.buttom_frame)
            entry5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label6 = tk.Label(self.buttom_frame, text="English", bg="#1e2222", fg="white")
            label6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry6 = tk.Entry(self.buttom_frame)
            entry6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label7 = tk.Label(self.buttom_frame, text="Nepali", bg="#1e2222", fg="white")
            label7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry7 = tk.Entry(self.buttom_frame)
            entry7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label8 = tk.Label(self.buttom_frame, text="Maths", bg="#1e2222", fg="white")
            label8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry8 = tk.Entry(self.buttom_frame)
            entry8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label9 = tk.Label(self.buttom_frame, text="Comm", bg="#1e2222", fg="white")
            label9.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry9 = tk.Entry(self.buttom_frame)
            entry9.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            def submit_data():
                sn = entry0.get()
                student_name = entry1.get()
                roll_no = entry2.get()
                term = entry3.get()
                science = entry4.get()
                social = entry5.get()
                english = entry6.get()
                nepali = entry7.get()
                maths = entry8.get()
                moral = entry9.get()

                # Assuming you are using SQLite as the database
                conn = mysql.connector.connect(
                    host='localhost',
                    port='3307',
                    user='root',
                    password='root',
                    database='summer_project'
                )
                cursor = conn.cursor()

                # Insert data into the students table
                query = "UPDATE class_four SET student_name=%s, roll_no=%s, term=%s, science=%s, social_moral=%s, " \
                        "english=%s, nepali=%s, maths=%s, comm=%s where sno=%s"
                data = (student_name, roll_no, term, science, social, english, nepali, maths, moral, sn)
                cursor.execute(query, data)

                # Commit the changes and close the cursor and connection
                conn.commit()
                cursor.close()
                conn.close()

                # Clear the entry fields after submitting
                entry0.delete(0, tk.END)
                entry1.delete(0, tk.END)
                entry2.delete(0, tk.END)
                entry3.delete(0, tk.END)
                entry4.delete(0, tk.END)
                entry5.delete(0, tk.END)
                entry6.delete(0, tk.END)
                entry7.delete(0, tk.END)
                entry8.delete(0, tk.END)

            self.submit = tk.Button(self.buttom_frame, text="Submit", command=submit_data)
            self.submit.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )

        # ---------------------------------------------------------------------------------------------------------------------#

        elif class_entry == "five" or class_entry == "Five" or class_entry == "5":

            conn = mysql.connector.connect(
                host='localhost',
                port='3307',
                user='root',
                password='root',
                database='summer_project'
            )

            # Create a cursor object to execute queries
            cursor = conn.cursor()

            # Execute the SQL query to select all data from the class_one table
            cursor.execute(
                "SELECT sno, student_name, roll_no, term, social_moral, science, maths, nepali, english, comm FROM class_five")

            # Fetch all the rows returned by the query
            rows = cursor.fetchall()

            # Create a new Tkinter window to display the table
            window = tk.Tk()
            window.title("Mark Sheet")

            # Create a treeview widget to display the data in a table format
            tree = ttk.Treeview(window)
            tree["columns"] = (
                "sno", "student_name", "roll_no", "term", "social_moral", "science", "maths", "nepali", "english",
                "comm")

            # Configure the treeview columns
            tree.column("#0", width=0, stretch=tk.NO)
            tree.column("sno", width=50)
            tree.column("student_name", width=100)
            tree.column("roll_no", width=50)
            tree.column("term", width=50)
            tree.column("social_moral", width=50)
            tree.column("science", width=50)
            tree.column("maths", width=50)
            tree.column("nepali", width=50)
            tree.column("english", width=50)
            tree.column("comm", width=50)

            # Add column headings
            tree.heading("sno", text="Sno")
            tree.heading("student_name", text="Student Name")
            tree.heading("roll_no", text="Roll ID")
            tree.heading("term", text="Term")
            tree.heading("social_moral", text="Social+moral")
            tree.heading("science", text="Science")
            tree.heading("maths", text="Maths")
            tree.heading("nepali", text="Nepali")
            tree.heading("english", text="English")
            tree.heading("comm", text="Comm")

            # Insert data into the treeview
            for row in rows:
                tree.insert("", tk.END, values=row)

            label0 = tk.Label(self.buttom_frame, text="s no", bg="#1e2222", fg="white")
            label0.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry0 = tk.Entry(self.buttom_frame)
            entry0.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label1 = tk.Label(self.buttom_frame, text="Student Name", bg="#1e2222", fg="white")
            label1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry1 = tk.Entry(self.buttom_frame)
            entry1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label2 = tk.Label(self.buttom_frame, text="Roll no", bg="#1e2222", fg="white")
            label2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry2 = tk.Entry(self.buttom_frame)
            entry2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label3 = tk.Label(self.buttom_frame, text="Term", bg="#1e2222", fg="white")
            label3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry3 = tk.Entry(self.buttom_frame)
            entry3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label4 = tk.Label(self.buttom_frame, text="Science", bg="#1e2222", fg="white")
            label4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry4 = tk.Entry(self.buttom_frame)
            entry4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label5 = tk.Label(self.buttom_frame, text="Social+moral", bg="#1e2222", fg="white")
            label5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry5 = tk.Entry(self.buttom_frame)
            entry5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label6 = tk.Label(self.buttom_frame, text="English", bg="#1e2222", fg="white")
            label6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry6 = tk.Entry(self.buttom_frame)
            entry6.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label7 = tk.Label(self.buttom_frame, text="Nepali", bg="#1e2222", fg="white")
            label7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry7 = tk.Entry(self.buttom_frame)
            entry7.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label8 = tk.Label(self.buttom_frame, text="Maths", bg="#1e2222", fg="white")
            label8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry8 = tk.Entry(self.buttom_frame)
            entry8.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            label9 = tk.Label(self.buttom_frame, text="Comm", bg="#1e2222", fg="white")
            label9.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

            entry9 = tk.Entry(self.buttom_frame)
            entry9.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

            def submit_data():
                sn = entry0.get()
                student_name = entry1.get()
                roll_no = entry2.get()
                term = entry3.get()
                science = entry4.get()
                social = entry5.get()
                english = entry6.get()
                nepali = entry7.get()
                maths = entry8.get()
                moral = entry9.get()

                # Assuming you are using SQLite as the database
                conn = mysql.connector.connect(
                    host='localhost',
                    port='3307',
                    user='root',
                    password='root',
                    database='summer_project'
                )
                cursor = conn.cursor()

                # Insert data into the students table
                query = "UPDATE class_five SET student_name=%s, roll_no=%s, term=%s, science=%s, social_moral=%s, " \
                        "english=%s, nepali=%s, maths=%s, comm=%s where sno=%s"
                data = (student_name, roll_no, term, science, social, english, nepali, maths, moral, sn)
                cursor.execute(query, data)

                # Commit the changes and close the cursor and connection
                conn.commit()
                cursor.close()
                conn.close()

                # Clear the entry fields after submitting
                entry0.delete(0, tk.END)
                entry1.delete(0, tk.END)
                entry2.delete(0, tk.END)
                entry3.delete(0, tk.END)
                entry4.delete(0, tk.END)
                entry5.delete(0, tk.END)
                entry6.delete(0, tk.END)
                entry7.delete(0, tk.END)
                entry8.delete(0, tk.END)

            self.submit = tk.Button(self.buttom_frame, text="Submit", command=submit_data)
            self.submit.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )

    ########################################################################################################################
    def change_password(self):
        # destroy any existing frame in right_frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # create new frame with desired content
        self.top_frame = tk.Frame(self.right_frame, bg="#181a1b", bd=1, height=80)
        self.top_frame.place(relx=0.2, rely=0, relwidth=1, relheight=1)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.top_frame.propagate(False)

        self.top_label = tk.Label(self.top_frame, text="Change Password", bg="#181a1b", foreground="white", font=5,
                                  height=4)
        self.top_label.pack(anchor=tk.NW, padx=10)
        self.top_label.propagate(True)

        self.buttom_frame = tk.Frame(self.right_frame, bg="#1e2222", bd=1, height=self.winfo_height())
        self.buttom_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.buttom_frame.propagate(False)

        user_label = tk.Label(self.buttom_frame, text='Username:', bg="#1e2222", fg="white")
        user_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )

        user_entry = tk.Entry(self.buttom_frame)
        user_entry.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        old_label = tk.Label(self.buttom_frame, text='Old Password:', bg="#1e2222", fg="white")
        old_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )

        old_entry = tk.Entry(self.buttom_frame, show='*')
        old_entry.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        new_label = tk.Label(self.buttom_frame, text='New Password:', bg="#1e2222", fg="white")
        new_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )

        new_entry = tk.Entry(self.buttom_frame, show='*', font=12, width=25, borderwidth='2', relief='ridge')
        new_entry.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        confirm_label = tk.Label(self.buttom_frame, text='Confirm Password:', bg="#1e2222", fg="white")
        confirm_label.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        confirm_entry = tk.Entry(self.buttom_frame, show='*', font=12, width=25, borderwidth='2', relief='ridge')
        confirm_entry.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        def submit_button_clicked():
            # Retrieve the username from the log_demo file
            username = user_entry.get()

            # Retrieve the entered passwords
            old_password = old_entry.get()
            new_password = new_entry.get()
            confirm_password = confirm_entry.get()

            # Connect to the MySQL database
            db_connection = mysql.connector.connect(
                host="localhost",
                user="your_username",
                password="your_password",
                database="your_database"
            )

            # Create a cursor object to execute SQL queries
            cursor = db_connection.cursor()

            # Retrieve the stored password from the database
            cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
            result = cursor.fetchone()

            if result:
                stored_password = result[0]

                if old_password == stored_password and new_password == confirm_password:
                    # Update the password in the database
                    cursor.execute("UPDATE users SET password = %s WHERE username = %s", (new_password, username))
                    db_connection.commit()

                    # Password change successful
                    print("Password changed successfully.")
                else:
                    # Invalid password or passwords do not match
                    print("Invalid password or passwords do not match.")
            else:
                # Username not found in the database
                print("Username not found.")

            # Close the cursor and database connection
            cursor.close()
            db_connection.close()

            # Clear the entry fields
            old_entry.delete(0, tk.END)
            new_entry.delete(0, tk.END)
            confirm_entry.delete(0, tk.END)

        self.submit = tk.Button(self.buttom_frame, text="Submit", command=submit_button_clicked)
        self.submit.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )

    ################################################################################################################

    def send_mail(self):
        # destroy any existing frame in right_frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # create new frame with desired content
        self.top_frame = tk.Frame(self.right_frame, bg="#181a1b", bd=1, height=80)
        self.top_frame.place(relx=0.2, rely=0, relwidth=1, relheight=1)
        self.top_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.top_frame.propagate(False)

        self.top_label = tk.Label(self.top_frame, text="Send mail", bg="#181a1b", foreground="white", font=5,
                                  height=4)
        self.top_label.pack(anchor=tk.NW, padx=10)
        self.top_label.propagate(True)

        self.buttom_frame = tk.Frame(self.right_frame, bg="#1e2222", bd=1, height=self.winfo_height())
        self.buttom_frame.pack(side=tk.TOP, fill=tk.BOTH)
        self.buttom_frame.propagate(False)

        label1 = tk.Label(self.buttom_frame, text="Student Name", bg="#1e2222", fg="white")
        label1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        entry1 = tk.Entry(self.buttom_frame)
        entry1.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        label2 = tk.Label(self.buttom_frame, text="Roll no", bg="#1e2222", fg="white")
        label2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        entry2 = tk.Entry(self.buttom_frame)
        entry2.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        label3 = tk.Label(self.buttom_frame, text="Class", bg="#1e2222", fg="white")
        label3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        entry3 = tk.Entry(self.buttom_frame)
        entry3.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        label4 = tk.Label(self.buttom_frame, text="Term", bg="#1e2222", fg="white")
        label4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        entry4 = tk.Entry(self.buttom_frame)
        entry4.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        label5 = tk.Label(self.buttom_frame, text="Email", bg="#1e2222", fg="white")
        label5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5)

        entry5 = tk.Entry(self.buttom_frame)
        entry5.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, fill=tk.X)

        def generate_pdf(data):
            class_no = entry3.get()
            name = entry1.get()
            roll_no = entry2.get()
            term = entry4.get()

            conn = mysql.connector.connect(
                host='localhost',
                port='3307',
                user='root',
                password='root',
                database='summer_project'
            )
            cursor = conn.cursor()

            if class_no.lower() in ['1', 'one', 'One']:
                class_table = 'class_one'
            elif class_no.lower() in ['2', 'two', 'Two']:
                class_table = 'class_two'
            elif class_no.lower() in ['3', 'three', 'Three']:
                class_table = 'class_three'
            elif class_no.lower() in ['4', 'four', 'Four']:
                class_table = 'class_four'
            elif class_no.lower() in ['5', 'five', 'Five']:
                class_table = 'class_five'
            else:
                messagebox.showerror("Error", "Invalid class number")
                return

            # Retrieve data from the database
            query = f"SELECT * FROM {class_table} WHERE student_name = %s AND roll_no = %s AND term = %s"
            cursor.execute(query, (name, roll_no, term))
            data = cursor.fetchall()

            # Create a PDF document
            pdf_path = "table.pdf"
            doc = SimpleDocTemplate(pdf_path, pagesize=letter)
            elements = []

            if class_no.lower() in ['1', 'one', 'One']:
                table_data = [
                    ['sno', 'student name', 'roll no', 'term', 'social', 'science', 'maths', 'nepali', 'english']]
            elif class_no.lower() in ['2', 'two', 'Two']:
                table_data = [
                    ['sno', 'student name', 'roll no', 'term', 'social', 'science', 'maths', 'nepali', 'english',
                     'moral']]
            elif class_no.lower() in ['3', 'three', 'Three']:
                table_data = [
                    ['sno', 'student name', 'roll no', 'term', 'social', 'science', 'maths', 'nepali', 'english',
                     'moral/com']]
            elif class_no.lower() in ['4', 'four', 'Four']:
                table_data = [
                    ['sno', 'student name', 'roll no', 'term', 'social+moral', 'science', 'maths', 'nepali', 'english',
                     'comm']]
            elif class_no.lower() in ['5', 'five', 'Five']:
                table_data = [
                    ['sno', 'student name', 'roll no', 'term', 'social+moral', 'science', 'maths', 'nepali', 'english',
                     'comm']]
            else:
                messagebox.showerror("Error", "Invalid class number")
                return

            for row in data:
                table_data.append(row)

            table_style = TableStyle(
                [
                    ('BACKGROUND', (0, 0), (-1, 0), None),
                    ('TEXTCOLOR', (0, 0), (-1, 0), None),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 14),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), None),
                    ('GRID', (0, 0), (-1, -1), 1, None),
                ]
            )
            # Create the table and apply styles
            table = Table(table_data)
            table.setStyle(table_style)

            # Add the table to the PDF document
            elements.append(table)

            # Build the PDF document
            doc.build(elements)
            return pdf_path

        def submit_email():
            # Fetch the values from the entry fields
            student_name = entry1.get()
            roll_no = entry2.get()
            class_no = entry3.get()
            term = entry4.get()
            receiver_email = entry5.get()

            conn = mysql.connector.connect(
                host='localhost',
                port='3307',
                user='root',
                password='root',
                database='summer_project',
            )
            cursor = conn.cursor()

            # Define the SQL query to retrieve student information
            query = "SELECT email FROM students WHERE student_name = %s AND roll_id = %s "
            cursor.execute(query, (student_name, roll_no))
            result = cursor.fetchone()

            if result == (receiver_email,):
                # Fetch data from the appropriate class table based on class_no and term
                if class_no.lower() in ['1', 'one']:
                    class_table = 'class_one'
                elif class_no.lower() in ['2', 'two']:
                    class_table = 'class_two'
                elif class_no.lower() in ['3', 'three']:
                    class_table = 'class_three'
                elif class_no.lower() in ['4', 'four']:
                    class_table = 'class_four'
                elif class_no.lower() in ['5', 'five']:
                    class_table = 'class_five'
                else:
                    messagebox.showerror("Error", "Invalid class number")
                    return

                query = f"SELECT * FROM {class_table} WHERE student_name = %s AND roll_no = %s AND term = %s"
                cursor.execute(query, (student_name, roll_no, term))
                data = cursor.fetchone()

                query = f"SELECT * FROM {class_table} WHERE student_name = %s AND roll_no = %s AND term = %s"
                cursor.execute(query, (student_name, roll_no, term))
                data = cursor.fetchone()

                if data:
                    # Generate the PDF file
                    pdf_path = generate_pdf(data)

                    # Email details
                    sender_email = 'oshan9814158662@gmail.com'  # Your email address
                    sender_password = 'chamal9814158662'  # Your email password

                    # Create the email message
                    message = MIMEMultipart()
                    message['From'] = sender_email
                    message['To'] = receiver_email
                    message['Subject'] = 'Results'

                    with open(pdf_path, 'rb') as attachment:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', "attachment; filename= %s" % pdf_path)
                        message.attach(part)

                        # Connect to the SMTP server and send the email
                    try:
                        server = smtplib.SMTP('smtp.gmail.com', 587)  # Use the appropriate SMTP server and port
                        server.starttls()
                        server.login(sender_email, sender_password)
                        server.send_message(message)
                        server.quit()

                        print("Email sent successfully!")
                    except smtplib.SMTPException as e:
                        print("Failed to send email:", str(e))

                # Close the database connection
            conn.close()

        self.submit = tk.Button(self.buttom_frame, text="Submit", command=submit_email)
        self.submit.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=5, )

    def handle_selection(self, event):
        selected_option = self.combobox.get()
        selected_class = self.combobox.get()

    def handle_date_selection(self, event):
        selected_date = self.entry_date.get_date()


# Example usage:
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x1000")
    split_window = SplitWindow(root)

    split_window.pack(fill="both", expand=True)
    root.mainloop()
