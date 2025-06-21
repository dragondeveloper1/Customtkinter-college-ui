from tkinter import *
import customtkinter as ctk
# importing all the modules to connect
import login
class App:
    def __init__(self, user_type):
        super().__init__()
        self.user_type = user_type
        self.window = ctk.CTk()
        self.window.title("HWIC Knockoff Carbon Copy")
        self.user = None

    def run(self):
        self.window.mainloop()

# Start the Application with Login
if __name__ == "__main__":
    root = ctk.CTk()
    login_window = login.LoginWindow(root)
    root.mainloop()
