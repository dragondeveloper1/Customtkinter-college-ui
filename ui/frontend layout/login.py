# ui/login_window.py

from customtkinter import *
from PIL import Image
import db_logics as db_logics
from signup import SignupWindow
from student import Student
from professor import Professor
from admin import Admin

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Page")
        self.master.geometry("800x500")
        set_appearance_mode("system")

        self.main_frame = CTkFrame(master)
        self.main_frame.pack(fill="both", expand=True)

        # Left Panel
        self.left_panel = CTkFrame(self.main_frame, width=400, fg_color="#32aaff")
        self.left_panel.pack(side="left", fill="both", expand=True)

        CTkLabel(self.left_panel, text="HWIC", font=("Arial", 28, "bold"), text_color="white").place(relx=0.1, rely=0.1)
        CTkLabel(self.left_panel, text="Welcome to \n HWIC", font=("Arial", 26, "bold"), text_color="white").place(relx=0.1, rely=0.3)
        CTkLabel(self.left_panel,
                 text="Please Login using your username and password\n Sign-in by clicking New User? Sign-up ",
                 wraplength=300, font=("Arial", 12, "bold", "italic"), text_color="white").place(relx=0.1, rely=0.5)

        # Right Panel
        self.right_panel = CTkFrame(self.main_frame, width=400)
        self.right_panel.pack(side="right", fill="both", expand=True)

        CTkLabel(self.right_panel, text="Login", font=("Arial", 22, "bold")).place(relx=0.3, rely=0.1)
        CTkLabel(self.right_panel, text="Login to get amazing discounts and offers only for you.",
                 font=("Arial", 12)).place(relx=0.1, rely=0.18)

        self.username_entry = CTkEntry(self.right_panel, placeholder_text="User Name")
        self.username_entry.place(relx=0.1, rely=0.3, relwidth=0.8)

        self.password_entry = CTkEntry(self.right_panel, placeholder_text="Password", show="*")
        self.password_entry.place(relx=0.1, rely=0.4, relwidth=0.8)

        self.user_type_entry = CTkComboBox(self.right_panel, values=["student", "professor", "admin"])
        self.user_type_entry.place(relx=0.1, rely=0.5, relwidth=0.8)

        self.remember_me = CTkCheckBox(self.right_panel, text="Remember me")
        self.remember_me.place(relx=0.1, rely=0.6)

        CTkButton(self.right_panel, text="LOGIN", command=self.login).place(relx=0.1, rely=0.7, relwidth=0.8)

        signup_label = CTkLabel(self.right_panel, text="New User? Sign-up", text_color="blue", cursor="hand2")
        signup_label.place(relx=0.1, rely=0.8)
        signup_label.bind("<Button-1>", lambda e: self.open_signup_window())

        CTkLabel(self.right_panel, text="Forgot your password?", text_color="gray", font=("Arial", 10)).place(relx=0.6, rely=0.9)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user_type = self.user_type_entry.get()

        if self.authenticate(username, password, user_type):
            db_logics.login_query(username, password, user_type)
            self.master.destroy()
            self.open_app(user_type)
        else:
            self.show_error_message()

    def authenticate(self, username, password, user_type):
        return username == "user" and password == "password" and user_type in ["student", "professor", "admin"]

    def show_error_message(self):
        CTkLabel(self.right_panel, text="Invalid credentials, please try again", text_color="red").place(relx=0.1, rely=0.85)

    def open_signup_window(self):
        top = CTkToplevel(self.master)
        SignupWindow(top)

    def open_app(self, user_type):
        root = CTk()
        if user_type == "student":
            app = Student(root)
        elif user_type == "professor":
            app = Professor(root)
        elif user_type == "admin":
            app = Admin(root)
        else:
            print("Unknown user type.")
            return
        app.create_buttons()
        root.mainloop()
