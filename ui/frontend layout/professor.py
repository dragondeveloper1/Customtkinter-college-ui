from tkinter import *
import customtkinter as ctk
from PIL import Image,ImageTk
import db_connect
import main_layout
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

##################################Professor Menu Options################
##################################################Student Menu Option###################################
class Professor(main_layout.Main_structure):
  
    def create_buttons(self):
        academic_tab = self.home_tab.add("Academic")
        exam_tab = self.home_tab.add("Examination")
        attendance_tab=self.home_tab.add("Attendande")

        # --- Tabs to show contents --
        acad_menu = self.create_menu_frame(academic_tab)
        exam_menu = self.create_menu_frame(exam_tab)
        attendance_menu=self.create_menu_frame(attendance_tab)

        # --- Frames and Loaders ---
        self.acad_frames = {
            "Assignment": self.create_content_frame(academic_tab),
            "Routine": self.create_content_frame(academic_tab),
            "Library": self.create_content_frame(academic_tab),
            "Lecture Notes": self.create_content_frame(academic_tab),
            "Complain": self.create_content_frame(academic_tab),
            "Leave": self.create_content_frame(academic_tab)
        }
        self.acad_loaders = {
            "Assignment": self.load_assignment_content,
            "Routine": self.load_routine_content,
            "Library": self.load_library_content,
            "Lecture Notes": self.load_notes_content,
            "Complain": self.load_complain_content,
            "Leave": self.load_leave_content
        }
        
        self.exam_frames = {
            "Exam Routine": self.create_content_frame(exam_tab),
            "Question Paper": self.create_content_frame(exam_tab),
            "Subject Grading": self.create_content_frame(exam_tab)
        }
        self.exam_loaders = {
            "Exam Routine": self.load_exam_routine_content,
            "Question Paper": self.load_question_paper_content,
            "Subject Grading": self.load_subject_grading_content
        }
        
        # --- Function call to make navigation buttons ---
        self.create_nav_buttons(acad_menu, self.acad_frames, self.acad_loaders, default="Assignment")
        self.create_nav_buttons(exam_menu, self.exam_frames, self.exam_loaders, default="Exam Routine")
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
        ctk.CTkLabel(frame, text="📘 Assignment", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkButton(frame, text="Submit Assignment", width=200).pack(pady=10)

    def load_routine_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="🗓️ Routine", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkButton(frame, text="Download Routine PDF").pack(pady=10)

    def load_library_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="📚 Library", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkEntry(frame, placeholder_text="Search for books...").pack(pady=5)
        ctk.CTkButton(frame, text="Search").pack(pady=5)

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

    def load_question_paper_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="📆 Question Paper", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkButton(frame, text="View Schedule").pack(pady=10)

    def load_subject_grading_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="📊  Subject Markings", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkButton(frame, text="Download Result").pack(pady=10)

    def load_exam_routine_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="💬 Exam routine", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkTextbox(frame, width=500, height=100).pack(pady=10)
        ctk.CTkButton(frame, text="Send Feedback").pack(pady=5)

