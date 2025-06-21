from tkinter import *
import customtkinter as ctk
from PIL import Image,ImageTk
import db_connect
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
class Main_structure:
    def __init__(self, master):
        self.master = master
        self.mode = "light"
        
        #######################App Structure##################################################
        # top frame
        self.topframe = ctk.CTkFrame(self.master,fg_color="transparent",width=3)
        self.topframe.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        # creating frames for each main buttons
        # menu frame
        self.menuframe = ctk.CTkScrollableFrame(self.master,corner_radius=50)
        self.menuframe.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        self.home_tab=ctk.CTkTabview(self.menuframe,
                    corner_radius=50,
                    segmented_button_selected_color="#007acc",
                    anchor=CENTER)
        self.home_tab.pack(padx=5,pady=10,fill="both",expand=True)
        # notice frame
        self.noticeframe = ctk.CTkScrollableFrame(self.master,corner_radius=50)
        self.noticeframe.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        
        # library frame
        self.libraryframe = ctk.CTkScrollableFrame(self.master,corner_radius=50)
        self.libraryframe.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        
        #analysis frame
        self.analysisframe = ctk.CTkScrollableFrame(self.master,corner_radius=50)
        self.analysisframe.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        # profile frame
        self.profileframe = ctk.CTkScrollableFrame(self.master,corner_radius=50)
        self.profileframe.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        
        # settings frame
        self.settingsframe = ctk.CTkScrollableFrame(self.master,corner_radius=50)
        self.settingsframe.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        # profile menu frames
        self.pr1 = ctk.CTkFrame(self.profileframe,corner_radius=50)
        self.pr1.grid(pady=20, padx=450, row=450, column=0, rowspan=2, sticky="ns")
        

        self.homeicon = ctk.CTkImage(Image.open('images/home.png'))
        self.home_button = ctk.CTkButton(self.topframe, text="Home", corner_radius=50,
                                          command=lambda: self.show_frame(self.menuframe),fg_color="transparent",text_color="#A9A9A9")
        self.home_button.configure(image=self.homeicon, compound=LEFT, font=("Helvetica", 30,"bold","italic"))
        self.home_button.grid(row=0, column=0, padx=30)  # Use grid for positioning
        # notice Menu
        self.noticeicon = ctk.CTkImage(Image.open("images/notice.png"))
        self.notice_button = ctk.CTkButton(self.topframe, text="Notice", corner_radius=50,
                                            command=lambda: self.show_frame(self.noticeframe),fg_color="transparent",text_color="#A9A9A9")
        self.notice_button.configure(image=self.noticeicon, compound=LEFT, font=("Helvetica", 30,"bold","italic"))
        self.notice_button.grid(row=0, column=1, padx=30)  # Use grid for positioning
        # library menu
        self.libraryicon = ctk.CTkImage(Image.open("images/library.png"))
        self.library_button = ctk.CTkButton(self.topframe, text="Library", corner_radius=50,
                                          command=lambda: self.show_frame(self.libraryframe),fg_color="transparent",text_color="#A9A9A9")
        self.library_button.configure(image=self.libraryicon, compound=LEFT, font=("Helvetica", 30,"bold","italic"))
        self.library_button.grid(row=0, column=2, padx=30)  # Use grid for positioning
        #analysis menu
        self.analysisicon = ctk.CTkImage(Image.open("images/library.png"))
        self.analysis_button = ctk.CTkButton(self.topframe, text="Analysis", corner_radius=50,
                                          command=lambda: self.show_frame(self.analysisframe),fg_color="transparent",text_color="#A9A9A9")
        self.analysis_button.configure(image=self.analysisicon, compound=LEFT, font=("Helvetica", 30,"bold","italic"))
        self.analysis_button.grid(row=0, column=3, padx=30)  # Use grid for positioning
        # profile
        self.profileicon = ctk.CTkImage(Image.open("images/profile.png"))
        self.profile_button = ctk.CTkButton(self.topframe, text="Profile", corner_radius=50,
                                             command=lambda: self.show_frame(self.profileframe),fg_color="transparent",text_color="#A9A9A9")
        self.profile_button.configure(image=self.profileicon, compound=LEFT, font=("Helvetica", 30,"bold","italic"))
        self.profile_button.grid(row=0, column=4, padx=30, sticky="ew") 
        # settings
        self.settingicon = ctk.CTkImage(Image.open("images/settings.png"))
        self.setting_button = ctk.CTkButton(self.topframe, text="Setting", corner_radius=50,
                                             command=lambda: self.show_frame(self.settingsframe),fg_color="transparent",text_color="#A9A9A9")
        self.setting_button.configure(image=self.settingicon, compound=LEFT, font=("Helvetica", 30,"bold","italic"))
        self.setting_button.grid(row=0, column=5, padx=30, sticky="ew") 


        # Dynamically resizing: make grid rows and columns resizable
        self.master.grid_rowconfigure(0, weight=0)  # Top frame doesn't need to grow
        self.master.grid_columnconfigure(0, weight=0)  # Left column doesn't grow
        self.master.grid_rowconfigure(1, weight=1)  # Right and center frames grow
        self.master.grid_columnconfigure(1, weight=1)  # Center frame grows

        ################# notice frame buttons and features default########################################
        notice_image=ctk.CTkImage(light_image=Image.open('images/nn.png'),
                    dark_image=Image.open('images/nn.png'),
                size=(600,700))
        notice_label=ctk.CTkLabel(self.noticeframe,text="",image=notice_image)
        notice_label.pack(pady=10)

        ############################## Profile buttonsdefaults #############################################
        #frame 1 Buttons
        ###########These will be inherited by users and accessed according to need
        self.view_profile=ctk.CTkButton(self.pr1,text="View Profile",
                                         font=("Helvetica",20), corner_radius=50)
        self.view_profile.pack(padx=30,pady=20)
        self.change_pass=ctk.CTkButton(self.pr1,text="Change Password",
                                         font=("Helvetica",20), corner_radius=50)
        self.change_pass.pack(padx=30,pady=20)
        self.poli_cy=ctk.CTkButton(self.pr1,text="Privacy Policy",
                                         font=("Helvetica",20), corner_radius=50)
        self.poli_cy.pack(padx=30,pady=20)
        self.log_out=ctk.CTkButton(self.pr1,text="Log Out",
                                         font=("Helvetica",20), corner_radius=50)
        self.log_out.pack(padx=30,pady=20)

        ######################## settings butons#################################
        self.dark_theme=ctk.CTkButton(self.settingsframe,text="Change Theme",
                                         font=("Helvetica",20), corner_radius=50,
                                         command=self.light_dark)
        self.dark_theme.pack(padx=30,pady=20)
        self.follow_us=ctk.CTkButton(self.settingsframe,text="Follow US",
                                         font=("Helvetica",20), corner_radius=50)
        self.follow_us.pack(padx=30,pady=20)
        self.terms=ctk.CTkButton(self.settingsframe,text="Terms and Conditions",
                                         font=("Helvetica",20), corner_radius=50)
        self.terms.pack(padx=30,pady=20)

        # Hide all frames initially
        self.hide_all_frames()
        # Show the default frame (Home)
        self.show_frame(self.menuframe)
    def light_dark(self):
        if self.mode == "light":
            ctk.set_appearance_mode("dark")
            self.mode = "dark"
        else:
            ctk.set_appearance_mode("light")
            self.mode = "light"


    def show_frame(self, frame):
        """Hide all frames and show the requested one."""
        self.hide_all_frames()
        frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)  # Ensure the frame is shown

    def hide_all_frames(self):
        """Hide all frames by calling grid_forget."""
        self.menuframe.grid_forget()
        self.noticeframe.grid_forget()
        self.libraryframe.grid_forget()
        self.analysisframe.grid_forget()
        self.profileframe.grid_forget()
        self.settingsframe.grid_forget()
    def create_buttons(self):
        raise NotImplementedError("Subclasses should implement this method.")
    def all_seeying_calender(self):
        pass

#