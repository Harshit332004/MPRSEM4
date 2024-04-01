from tkinter import *

def login_screen():
    ro = Tk()
    ro.title("Login")
    ro.geometry("380x400")
    ro.config(bg="#f0f0f0")  # Light gray background

    Label(
        ro,
        text="LOGIN",
        font=("Arial", 20, "bold"),
        bg="#f0f0f0",
        fg="#333333",  # Dark gray text
        padx=10,
        pady=20
    ).pack()

    # Username Entry
    username_label = Label(
        ro,
        text="Username",
        font=("Arial", 12),
        bg="#f0f0f0",
        fg="#333333"
    )
    username_label.place(x=40, y=100)
    entry_username = Entry(
        ro,
        width=20,
        font=("Arial", 12),
        borderwidth=2,
        fg="#333333",
        bg="#ffffff"  # White background
    )
    entry_username.place(x=160, y=100)

    # Password Entry
    password_label = Label(
        ro,
        text="Password",
        font=("Arial", 12),
        bg="#f0f0f0",
        fg="#333333"
    )
    password_label.place(x=40, y=150)
    entry_password = Entry(
        ro,
        width=20,
        font=("Arial", 12),
        borderwidth=2,
        fg="#333333",
        bg="#ffffff",  # White background
        show="*"  # Show asterisks for password
    )
    entry_password.place(x=160, y=150)

    # "I am not a robot" Checkbox
    not_robot_var = IntVar()
    not_robot_check = Checkbutton(
        ro,
        text="I am not a robot",
        font=("Arial", 10),
        bg="#f0f0f0",
        fg="#333333",
        variable=not_robot_var,
        onvalue=1,
        offvalue=0
    )
    not_robot_check.place(x=40, y=200)

    # Login Button
    login_button = Button(
        ro,
        text="Login",
        font=("Arial", 12),
        bg="#4CAF50",  # Green button
        fg="#ffffff",  # White text
        borderwidth=0,
        padx=10,
        pady=5,
        command=lambda: login(entry_username.get(), entry_password.get())
    )
    login_button.place(x=160, y=250)

    # "Did not sign up yet?" Label and Sign Up Button
    signup_label = Label(
        ro,
        text="Did not sign up yet?",
        font=("Arial", 8),
        bg="#f0f0f0",
        fg="#333333",
        height=1,
        padx=2,
        pady=10
    )
    signup_label.place(x=125, y=300)
    signup_button = Button(
        ro,
        text="Sign up",
        font=("Helvetica", 8),
        height=1,
        width=12,
        bg="#4CAF50",  # Green button
        fg="#ffffff",  # White text
        borderwidth=0,
        padx=9,
        pady=4,
        relief="groove",
        command=lambda: signup()
    )
    signup_button.place(x=140, y=330)

    ro.mainloop()

def login(username, password):
    # Add your login logic here
    print("Username:", username)
    print("Password:", password)

def signup():
    # Add your signup logic here
    print("Signing up...")

login_screen()
