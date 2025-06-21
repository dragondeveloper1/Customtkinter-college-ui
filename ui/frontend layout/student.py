from tkinter import *
import customtkinter as ctk
from PIL import Image,ImageTk
import db_connect
from main_layout import Main_structure
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

##################################################Student Menu Option###################################
class Student(Main_structure):
    user_type_fixed="Student"
    def create_buttons(self):
        academic_tab = self.home_tab.add("Academic")
        exam_tab = self.home_tab.add("Examination")
        acc_tab = self.home_tab.add("Account")

        # --- Tabs to show contents --
        acad_menu = self.create_menu_frame(academic_tab)
        exam_menu = self.create_menu_frame(exam_tab)
        acc_menu = self.create_menu_frame(acc_tab)

        # --- Frames and Loaders ---
        self.acad_frames = {
            "Assignment": self.create_content_frame(academic_tab),
            "Routine": self.create_content_frame(academic_tab),
            "Lecture Notes": self.create_content_frame(academic_tab),
            "Complain": self.create_content_frame(academic_tab),
            "Leave": self.create_content_frame(academic_tab)
        }
        self.acad_loaders = {
            "Assignment": self.load_assignment_content,
            "Routine": self.load_routine_content,
            "Lecture Notes": self.load_notes_content,
            "Complain": self.load_complain_content,
            "Leave": self.load_leave_content
        }
        
        self.exam_frames = {
            "Exam Routine": self.create_content_frame(exam_tab),
            "Result": self.create_content_frame(exam_tab),
            "Feedback": self.create_content_frame(exam_tab)
        }
        self.exam_loaders = {
            "Exam Routine": self.load_exam_routine_content,
            "Result": self.load_result_content,
            "Feedback": self.load_feedback_content
        }
        
        self.acc_frames = {
            "Bill Info": self.create_content_frame(acc_tab)
        }
        self.acc_loaders = {
            "Bill Info": self.load_bill_info_content
        }
        
        # --- Function call to make navigation buttons ---
        self.create_nav_buttons(acad_menu, self.acad_frames, self.acad_loaders, default="Assignment")
        self.create_nav_buttons(exam_menu, self.exam_frames, self.exam_loaders, default="Exam Routine")
        self.create_nav_buttons(acc_menu, self.acc_frames, self.acc_loaders, default="Bill Info")

        # -- calling library menu function
        self.library_menu_function(self.libraryframe) # passing main frame as variable

    # creates  menu frames 
    def create_menu_frame(self, parent):
        menu = ctk.CTkFrame(parent, fg_color="transparent",corner_radius=50)
        menu.pack(fill="both", pady=10, padx=10)
        return menu

    # create content frames
    def create_content_frame(self, parent):
        frame = ctk.CTkFrame(parent, corner_radius=50,fg_color="transparent", border_width=5, border_color="#d0d0d0",)
        return frame

    # deletes frames content
    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
    
    # shows only the semected frame
    def show_only(self, frame_dict, show_key, loader_func):
        for frame in frame_dict.values():
            frame.pack_forget()
        frame_dict[show_key].pack(fill="both", expand=True, padx=20, pady=10)
        loader_func(frame_dict[show_key])

    def create_nav_buttons(self, menu, frames_dict, loader_dict, default):
        for idx, key in enumerate(frames_dict):
            btn = ctk.CTkButton(menu, text=key, width=130, height=32,
                                corner_radius=10,
                                fg_color="#e0e0e0",
                                hover_color="#007acc",
                                text_color="#333",anchor=CENTER,
                                command=lambda k=key: self.show_only(frames_dict, k, loader_dict[k]))
            btn.grid(row=0, column=idx, padx=5, pady=5)
        self.show_only(frames_dict, default, loader_dict[default])

    # --- Content Loaders ---
    def load_assignment_content(self, frame):
        self.clear_frame(frame)
        

    def load_routine_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="🗓️ Routine", font=("Helvetica", 20, "bold")).pack(pady=15)
        student_routune=ctk.CTkButton(frame, text="Download Routine PDF")
        student_routune.pack(pady=10)

    def load_notes_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="📄 Lecture Notes", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkButton(frame, text="Download All Notes").pack(pady=10)

    def load_complain_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="📝 Complain Box", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkTextbox(frame, width=500, height=100).pack(pady=10)
        ctk.CTkButton(frame, text="Submit Complain").pack(pady=5)

    def load_leave_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="📆 Leave Application", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkEntry(frame, placeholder_text="Reason for leave").pack(pady=5)
        ctk.CTkButton(frame, text="Submit Request").pack(pady=10)

    def load_exam_routine_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="📆 Exam Routine", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkButton(frame, text="View Schedule").pack(pady=10)

    def load_result_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="📊 Results", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkButton(frame, text="Download Result").pack(pady=10)

    def load_feedback_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="💬 Feedback", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkTextbox(frame, width=500, height=100).pack(pady=10)
        ctk.CTkButton(frame, text="Send Feedback").pack(pady=5)

    def load_bill_info_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="💵 Bill Information", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkButton(frame, text="View Details").pack(pady=10)
    
    # library  menus
    def library_menu_function(self, frame):
        self.clear_frame(frame)
        # Title label
        title_label = ctk.CTkLabel(frame, text="📚 Library Menu", font=("Helvetica", 24, "bold"))
        title_label.grid(row=0, column=0, columnspan=4, pady=(20, 10))

        # Borrow Frame
        borrow_frame = ctk.CTkFrame(frame,corner_radius=20,fg_color="transparent",border_width=5,border_color="#cccccc")
        borrow_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        borrow_label = ctk.CTkLabel(borrow_frame, text="Borrow Book", font=("Helvetica", 18))
        borrow_label.pack(padx=20, pady=20)

        borrow_button = ctk.CTkButton(borrow_frame, text="Open Borrow Menu", corner_radius=10)
        borrow_button.pack(pady=(10, 20))

        # All Tasks Frame
        all_task_frame = ctk.CTkFrame(frame,corner_radius=20,fg_color="transparent",border_width=5,border_color="#cccccc")
        all_task_frame.grid(row=1, column=1, padx=20, pady=20,sticky="nsew")

        task_label = ctk.CTkLabel(all_task_frame, text="Detail Pannel", font=("Helvetica", 18))
        task_label.pack(padx=20, pady=20)

        # Example Buttons
        task_buttons = ["Search Book", "Return Book", "Manage Inventory", "User Accounts"]
        for task in task_buttons:
            btn = ctk.CTkButton(all_task_frame, text=task, corner_radius=10)
            btn.pack(pady=5, padx=10)

        # Configure grid weights for responsiveness
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
