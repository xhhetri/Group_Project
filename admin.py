import tkinter as tk
import mysql.connector
from admin_window import window

admin_frame = window()

# Create the main window
root = tk.Tk()
root.title("Login Window")
root.geometry("400x200")

# Create the login frame
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

# database connector
connectiondb = mysql.connector.connect(host="localhost", user="root", database="login_dbms")
condb = connectiondb.cursor()

def logged():
    log_message = tk.Frame(root)
    tk.Label(log_message, text="login confirm")
    tk.Label.pack(log_message)
    log_message.pack()


def destroy():
    log_message = tk.Frame(root)
    tk.Label(log_message, text="login failed")
    tk.Label.pack(log_message)
    log_message.pack()


# login database verfication
def login_verify():
    username = username_entry.get()
    password: str = password_entry.get()
    sql = "select privilege from login where username = %s and password = %s"
    condb.execute(sql, [(username), (password)])
    result = condb.fetchall()

    if result == "admin":
        window.show()


    else:
        destroy()

# Add the username label and input field
username_label = tk.Label(login_frame, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1, padx=5, pady=5)

# Add the password label and input field
password_label = tk.Label(login_frame, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Create the login and signup buttons and add them to the frame
login_button = tk.Button(login_frame, text="Login", command=login_verify)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Center the login frame in the main window
root.update_idletasks()
login_frame_width = login_frame.winfo_width()
login_frame_height = login_frame.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (login_frame_width / 2))
y = int((screen_height / 2) - (login_frame_height / 2))




# Start the main event loop
root.mainloop()
