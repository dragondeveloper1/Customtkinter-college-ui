# ui/signup_window.py

from customtkinter import *

class SignupWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Signup")
        self.master.geometry("400x450")

        CTkLabel(master, text="Create an Account", font=("Arial", 20, "bold")).pack(pady=20)

        self.fullname_entry = CTkEntry(master, placeholder_text="Full Name", corner_radius=50)
        self.fullname_entry.pack(pady=10, fill="x", padx=40)

        self.username_entry = CTkEntry(master, placeholder_text="Username", corner_radius=50)
        self.username_entry.pack(pady=10, fill="x", padx=40)

        self.password_entry = CTkEntry(master, placeholder_text="Password", show="*", corner_radius=50)
        self.password_entry.pack(pady=10, fill="x", padx=40)

        self.confirm_password_entry = CTkEntry(master, placeholder_text="Confirm Password", show="*", corner_radius=50)
        self.confirm_password_entry.pack(pady=10, fill="x", padx=40)

        self.user_type_combo = CTkOptionMenu(master, values=["student", "professor", "admin"], corner_radius=50)
        self.user_type_combo.set("Select Role")
        self.user_type_combo.pack(pady=10)

        CTkButton(master, text="Sign Up", command=self.signup, corner_radius=50).pack(pady=20)

        self.message_label = CTkLabel(master, text="")
        self.message_label.pack()

    def signup(self):
        fullname = self.fullname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        user_type = self.user_type_combo.get()

        if not all([fullname, username, password, confirm_password]) or user_type == "Select Role":
            self.message_label.configure(text="Please fill in all fields.", text_color="red")
        elif password != confirm_password:
            self.message_label.configure(text="Passwords do not match.", text_color="red")
        else:
            print(f"User registered: {username} ({user_type})")
            self.message_label.configure(text="Account created successfully!", text_color="green")
