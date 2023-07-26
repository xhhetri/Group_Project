#loginform
import subprocess
import tkinter as tk
from mysql.connector import Error
import mysql.connector
from tkinter import messagebox

root = tk.Tk()


# create a function to close the window
def close_window():
    root.destroy()


# width and height
w = 600
h = 260


class loginForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        # start center window
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = (ws - w) / 2
        y = (hs - h) / 2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # end center window

        # start create widgets
        self.frame = tk.Frame(self.master, bg='#fff')

        self.btnsFrame = tk.Frame(self.frame, bg='#fff', padx=40, pady=15)

        self.windowTitle = tk.Label(self.frame, text='Login Window', bg='#fff',
                                    fg='black', font=20, pady=30)

        self.usernameLabel = tk.Label(self.frame, text='Username:', bg='#fff',
                                      font= 8)
        self.usernameTextbox = tk.Entry(self.frame, font=12, width=25,
                                        borderwidth='2', relief='ridge')

        self.passwordLabel = tk.Label(self.frame, text='Password:', bg='#fff',
                                      font=8)
        self.passwordTextbox = tk.Entry(self.frame, show='*', font= 12,
                                        width=25, borderwidth='2', relief='ridge')

        self.btnLogin = tk.Button(self.btnsFrame, text='Login', bg='light grey',
                                  font=2, fg='black', padx=25,
                                  pady=5, command=self.login_func)
        self.btnCancel = tk.Button(self.btnsFrame, text='Cancel', bg='light grey',
                                   font=2, fg='black', padx=25,
                                   pady=5, command=close_window)

        # end create widgets

        # start place widgets
        self.frame.pack(fill='both')
        self.windowTitle.grid(row=0, column=0, columnspan=2)
        self.usernameLabel.grid(row=1, column=0)
        self.usernameTextbox.grid(row=1, column=1)
        self.passwordLabel.grid(row=2, column=0, pady=(10, 0))
        self.passwordTextbox.grid(row=2, column=1, pady=(10, 0))
        self.btnsFrame.grid(row=3, column=0, columnspan=2, pady=10)
        self.btnLogin.grid(row=0, column=0, padx=(0, 35))
        self.btnCancel.grid(row=0, column=1)
        # end place widgets

    # create a function to login
    def login_func(self):
        username = self.usernameTextbox.get()
        password = self.passwordTextbox.get()

        # Establish a connection to the MySQL database
        db = mysql.connector.connect(
            host='localhost',
            port='3307',
            user='root',
            password='root',
            database='summer_project'
        )

        cursor = db.cursor()

        select_query = 'SELECT * FROM login_data WHERE username = %s and password = %s'
        vals = (username, password,)

        cursor.execute(select_query, vals)
        user = cursor.fetchone()

        if user is not None:
            self.master.destroy()
            subprocess.run(["python", "Admin.py"])
            # self.master.destroy()

        else:
            messagebox.showwarning('Error', 'Enter a Valid Username & Password')

        cursor.close()
        db.close()


def main():
    my_frame = loginForm(root)
    root.mainloop()

if __name__ == '__main__':
    main()


def username():
    return username()