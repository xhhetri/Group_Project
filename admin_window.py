import tkinter as tk
import os
from PIL import Image

# Create a new window
window = tk.Tk()

# Set the window size
window.geometry("800x500")

# Create a frame for the buttons in the left 25% part of the window
sidebar = tk.Frame(window, width=100, height=500, bg="gray")

#set color change while hovering
def on_enter(e):
    e.widget['background'] = 'light gray'

def on_leave(e):
    e.widget['background'] = 'gray'

#Create Icons
admin_icon = tk.PhotoImage(file="C:\\Users\\oshan\\OneDrive\\Desktop\\icons\\homepage-icon.png", )
student_icon = tk.PhotoImage(file="C:\\Users\\oshan\\OneDrive\\Desktop\\icons\\student-icon.png")
attendance_icon = tk.PhotoImage(file="C:\\Users\\oshan\\OneDrive\\Desktop\\icons\\attendance.png")
schedule_icon = tk.PhotoImage(file="C:\\Users\\oshan\\OneDrive\\Desktop\\icons\\Exam (1).png")
question_icon = tk.PhotoImage(file="C:\\Users\\oshan\\OneDrive\\Desktop\\icons\\Exam (2).png")
setting_icon = tk.PhotoImage(file="C:\\Users\\oshan\\OneDrive\\Desktop\\icons\\Settings.png")

# Create buttons in the button frame
admin_dashboard_button = tk.Button(sidebar, text="Admin Dashboard", bd=0, bg="gray", image=admin_icon, compound="left",
                                   default=tk.ACTIVE)
student_button = tk.Button(sidebar, text="Student", bd=0, bg="gray", image=student_icon)
attendance_button = tk.Button(sidebar, text="Attendance", bd=0, bg="gray", image=attendance_icon)
exam_schedule_button = tk.Button(sidebar, text="Exam Schedule", bd=0, bg="gray", image=schedule_icon)
Question_button = tk.Button(sidebar, text="Question", bd=0, bg="gray", image=question_icon)
Setting_button = tk.Button(sidebar, text="Setting", bd=0, bg="gray", image=setting_icon)


# to change the icon size
new_size = (32, 32)

# Loop over the icon files in a directory
icon_dir = "C:\\Users\\oshan\\OneDrive\\Desktop\\icons\\"
for filename in os.listdir(icon_dir):
    if filename.endswith(".png"):
        # Open the icon image
        icon_path = os.path.join(icon_dir, filename)
        icon = tk.Image.open(icon_path)

        # Resize the icon to the new size
        resized_icon = icon.resize(new_size)

        # Save the resized icon to a new file
        resized_icon_path = os.path.join(icon_dir, f"re_{filename}")
        resized_icon.save(resized_icon_path)



# Add the buttons to the button frame
admin_dashboard_button.pack(pady=10, fill="x")
student_button.pack(pady=10, fill="x")
attendance_button.pack(pady=10, fill="x")
exam_schedule_button.pack(pady=10, fill="x")
Question_button.pack(pady=10, fill="x")
Setting_button.pack(padx=10, fill="x")

# Bind the buttons to the Enter and Leave events
admin_dashboard_button.bind("<Enter>", on_enter)
admin_dashboard_button.bind("<Leave>", on_leave)
student_button.bind("<Enter>", on_enter)
student_button.bind("<Leave>", on_leave)
attendance_button.bind("<Enter>", on_enter)
attendance_button.bind("<Leave>", on_leave)
exam_schedule_button.bind("<Enter>", on_enter)
exam_schedule_button.bind("<Leave>", on_leave)
Question_button.bind("<Enter>", on_enter)
Question_button.bind("<Leave>", on_leave)
Setting_button.bind("<Enter>", on_enter)
Setting_button.bind("<Leave>", on_leave)

# Pack the button frame to the left side of the window
sidebar.pack(side="left", fill="y")

#other half of the frame of the window
sidebar = tk.Frame(window, width=100, height=500, bg="red")



# Run the window
window.mainloop()
