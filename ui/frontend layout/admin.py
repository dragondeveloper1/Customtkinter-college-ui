from tkinter import *
import customtkinter as ctk
from PIL import Image,ImageTk
from main_layout import Main_structure
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

##########################Admin Menu Options##################
class Admin(Main_structure):
    def create_buttons(self):
        # Create admin-specific buttons inside the topframe or any other frame
        #using the common tab view used in main class
        #creating tabs for each sub menu
        admin_dept_tab=self.home_tab.add("Departments")
        admin_program_tab=self.home_tab.add("Programs")
        admin_stu_tab=self.home_tab.add("Students")
        admin_event_tab=self.home_tab.add("Events")

        # --- Tabs to show contents
        admin_dept_menu = self.create_menu_frame(admin_dept_tab)
        admin_program_menu = self.create_menu_frame(admin_program_tab)
        admin_stu_menu=self.create_menu_frame(admin_stu_tab)
        admin_event_menu=self.create_menu_frame(admin_event_tab)

        # --- Frames and Loaders ---
        self.admin_dept_frames = {
            "Departments": self.create_content_frame(admin_dept_tab),
            "Add Professor": self.create_content_frame(admin_dept_tab),
            "Examination": self.create_content_frame(admin_dept_tab),
            "Results": self.create_content_frame(admin_dept_tab),
            "Complain": self.create_content_frame(admin_dept_tab),
            "Leave Requests": self.create_content_frame(admin_dept_tab)
        }
        self.admin_dept_loaders = {
            "Departments": self.load_admin_depaetment_content,
            "Add Professsor": self.load_admin_add_professor__content,
            "Examination": self.load_admin_exam_control_content,
            "Results": self.load_admin_results_content,
            "Complain": self.load_admin_complain_content,
            "Leave": self.load_admin_leave_content
            }

        self.admin_program_frames = {
            "Available Programs": self.create_content_frame(admin_program_tab),
            "Add Program": self.create_content_frame(admin_program_tab),
            "Delete Program": self.create_content_frame(admin_program_tab)
        }
        self.admin_program_loaders = {
            "Available Programs": self.load_admin_available_program_content,
            "Add Program": self.load_admin_add_proram_content,
            "Delete Program": self.load_admin_delete_program_content
        }
        
        self.admin_student_frames={
            "Add Student":self.create_content_frame(admin_stu_tab),
            "Remove Student":self.create_content_frame(admin_stu_tab)
        }
        self.admin_student_loaders = {
            "Add Student": self.load_admin_add_student_content,
            "Remove Student": self.load_admin_remove_student_content
        }
        
        self.admin_event_frames={
            "Events":self.create_content_frame(admin_event_tab),
            "Coordinator":self.create_content_frame(admin_event_tab),
            "Prizes":self.create_content_frame(admin_event_tab)
        }
        self.admin_event_loaders = {
            "Events": self.load_admin_events_content,
            "Coordinator": self.load_admin_coordinator_content,
            "Prizes":self.load_admin_prizes_content
        }
        
        # --- Function call to make navigation buttons ---
        self.create_nav_buttons(admin_dept_menu, self.admin_dept_frames, self.admin_dept_loaders, default="Departments")
        self.create_nav_buttons(admin_program_menu, self.admin_program_frames, self.admin_program_loaders, default="Available Programs")
        self.create_nav_buttons(admin_stu_menu, self.admin_student_frames, self.admin_student_loaders, default="Add Student")
        self.create_nav_buttons(admin_event_menu,self.admin_event_frames,self.admin_event_loaders,default="Events")
        
    # creates  menu frames when the function is called
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
    # ---- Starting from Admin Departments 
    def load_admin_depaetment_content(self, frame):
        self.clear_frame(frame)
        depaerment_label=ctk.CTkLabel(frame,text="Depaerments",font=("Helvetica", 20, "bold")).grid(row=0,column=0)

    def load_admin_add_professor__content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="🗓️ Routine", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkButton(frame, text="Download Routine PDF").pack(pady=10)

    def load_admin_exam_control_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="📚 Library", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkEntry(frame, placeholder_text="Search for books...").pack(pady=5)
        ctk.CTkButton(frame, text="Search").pack(pady=5)

    def load_admin_results_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="📄 Lecture Notes", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkButton(frame, text="Download All Notes").pack(pady=10)

    def load_admin_complain_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="📝 Complain Box", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkTextbox(frame, width=500, height=100).pack(pady=10)
        ctk.CTkButton(frame, text="Submit Complain").pack(pady=5)

    def load_admin_leave_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="📆 Leave Application", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkEntry(frame, placeholder_text="Reason for leave").pack(pady=5)
        ctk.CTkButton(frame, text="Submit Request").pack(pady=10)
    
    
    # ---- Program buttons functions
    def load_admin_available_program_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="📆 Question Paper", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkButton(frame, text="View Schedule").pack(pady=10)

    def load_admin_add_proram_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="📊  Subject Markings", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkButton(frame, text="Download Result").pack(pady=10)
    
    def load_admin_delete_program_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="📊  Subject Markings", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkButton(frame, text="Download Result").pack(pady=10)
    
    #--- student button functions
    def load_admin_add_student_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="💬 Exam routine", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkTextbox(frame, width=500, height=100).pack(pady=10)
        ctk.CTkButton(frame, text="Send Feedback").pack(pady=5)
    
    def load_admin_remove_student_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="💬 Exam routine", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkTextbox(frame, width=500, height=100).pack(pady=10)
        ctk.CTkButton(frame, text="Send Feedback").pack(pady=5)
    
    #-- Amdin event butto functons
    def load_admin_events_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="💬 Exam routine", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkTextbox(frame, width=500, height=100).pack(pady=10)
        ctk.CTkButton(frame, text="Send Feedback").pack(pady=5)
    
    def load_admin_coordinator_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="💬 Exam routine", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkTextbox(frame, width=500, height=100).pack(pady=10)
        ctk.CTkButton(frame, text="Send Feedback").pack(pady=5)
    
    def load_admin_prizes_content(self, frame):
        self.clear_frame(frame)
        ctk.CTkLabel(frame, text="💬 Exam routine", font=("Helvetica", 20, "bold")).pack(pady=15)
        ctk.CTkTextbox(frame, width=500, height=100).pack(pady=10)
        ctk.CTkButton(frame, text="Send Feedback").pack(pady=5)