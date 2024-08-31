import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from DataFile import Data
from Subjects import Subject

class enrolWindow():
    def __init__(self, student_detail, all_details):
        self.student_det = student_detail[0]
        self.all_details = all_details
        self.name=self.student_det["Name"].split()[0]
        self.id = self.student_det["Student_id"]
        self.full_name = self.student_det["Name"]
        self.email = self.student_det["Email"]
        self.subjects = eval(self.student_det["Subjects"])
        self.window = Tk()
        self.window.geometry("700x600")
        self.window.resizable(width=False, height=False)
        self.window.title("Student Portal")

        self.options_frame = tk.Frame(self.window, highlightbackground="grey", bg="light grey", highlightthickness=2)
        self.options_frame.pack(side=tk.LEFT)
        self.options_frame.pack_propagate(False)
        self.options_frame.configure(width=170, height=600)

        self.main_frame = tk.Frame(self.window, highlightbackground="black", highlightthickness=2)
        self.main_frame.pack(side=tk.LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(width=530, height=600)

        #Adding image of university on TOP side of the window
        self.uni_logo = Image.open("GUI App\\uts2.jpg")
        self.uni_logo_resized = self.uni_logo.resize((700, 100))
        image1 = ImageTk.PhotoImage(self.uni_logo_resized)
        self.uni_logo_label = tk.Label(self.main_frame, image=image1)
        self.uni_logo_label.pack(fill=BOTH, side=TOP)
        self.wel_label = tk.Label(self.main_frame, text="Welcome to Student Portal", font=("Bold", 30))
        self.wel_label.pack()

        self.home_btn = tk.Button(self.options_frame, text="My Profile", font=("Bold", 14), 
                                  fg="Black", bd=0, bg="light grey",command=lambda : self.highlight(self.home_ind, self.profile_page))
        self.home_btn.place(x=5, y=100)
        self.enrol_btn = tk.Button(self.options_frame, text="Enrol", font=("Bold", 14), 
                                   fg="Black", bd=0, bg="light grey",command=lambda : self.highlight(self.enrol_ind, self.enrol_page))
        self.enrol_btn.place(x=5, y=175)
        self.view_results_btn = tk.Button(self.options_frame, text="Subjects/Results", font=("Bold", 14), 
                                          fg="Black", bd=0, bg="light grey",command=lambda : self.highlight(self.view_ind, self.subs_page))
        self.view_results_btn.place(x=5, y=250)

        self.home_ind = tk.Label(self.options_frame, text='', bg='light grey')
        self.home_ind.place(x=1, y=100, width=5, height=40)
        self.enrol_ind = tk.Label(self.options_frame, text='', bg='light grey')
        self.enrol_ind.place(x=1, y=175, width=5, height=40)
        self.view_ind = tk.Label(self.options_frame, text='', bg='light grey')
        self.view_ind.place(x=1, y=250, width=5, height=40)
        self.window.mainloop()

    def delete_pg(self):
        for frames in self.main_frame.winfo_children():
            frames.destroy()

    def hide_indicate(self):
        self.home_ind.config(bg="light grey")
        self.enrol_ind.config(bg="light grey")
        self.view_ind.config(bg="light grey")

    def highlight(self, label_name, page):
        self.hide_indicate()
        label_name.config(bg="black")
        self.delete_pg()
        page()

    def profile_page(self):
        pro_label = tk.Label(self.main_frame, text=f"Hi {self.name.title()}!", font=('Bold', 30)).place(x=210, y=50)
        id_label = tk.Label(self.main_frame, text="Student ID", bg="grey", width=15, font=("bold", 12)).place(x=50, y=200)
        name_label = tk.Label(self.main_frame, text="Full Name", bg="grey", width=15, font=("bold", 12)).place(x=50, y=250)
        email_label = tk.Label(self.main_frame, text="Email", bg="grey", width=15, font=("bold", 12)).place(x=50, y=300)
        id_txt = tk.Label(self.main_frame, text=self.id, bg="light grey", width=30, font=("bold", 12)).place(x=200, y=200)
        name_txt = tk.Label(self.main_frame, text=self.full_name, bg="light grey", width=30, font=("bold", 12)).place(x=200, y=250)
        email_txt = tk.Label(self.main_frame, text=self.email, bg="light grey", width=30, font=("bold", 12)).place(x=200, y=300)

    def subs_page(self):
        if len(self.subjects) >= 1:
            sub_label = tk.Label(self.main_frame, text="Your Current Subjects and Results are:", font=('Bold', 20)).place(x=30, y=50)
            sub_id_label = tk.Label(self.main_frame, text="Subject ID", bg="grey", width=15, font=("Bold", 12)).place(x=50, y=200)
            sub_mark_label = tk.Label(self.main_frame, text="Marks", bg="grey", width=15, font=("Bold", 12)).place(x=200, y=200)
            sub_grade_label = tk.Label(self.main_frame, text="Grade", bg="grey", width=15, font=("Bold", 12)).place(x=350, y=200)
            sub_count = 230 + (len(self.subjects)*25)
            for sub,j in zip(self.subjects, list(range(230, sub_count, 25))):
                id_txt = tk.Label(self.main_frame, text=sub["id"], bg="light grey", width=15, font=("bold", 12)).place(x=50, y=j)
                mark_txt = tk.Label(self.main_frame, text=sub["marks"], bg="light grey", width=15, font=("bold", 12)).place(x=200, y=j)
                grade_txt = tk.Label(self.main_frame, text=sub["grade"], bg="light grey", width=15, font=("bold", 12)).place(x=350, y=j)
        else:
            no_sub_label = tk.Label(self.main_frame, text="You have not enrolled in any subjects.", font=('Bold', 20)).place(x=30, y=100)
            no_sub_txt = tk.Label(self.main_frame, text="Instructions: Go to Enrol Menu to add new subjects", font=('Bold', 14)).place(x=30, y=200)
    
    def enrol_page(self):
        enrol_label = tk.Label(self.main_frame, text="Enrol Subjects", width=30,bg="grey", font=('Bold', 20)).place(x=25, y=50)
        enrol_txt = tk.Label(self.main_frame, text=f"You are currently enrolled in {len(self.subjects)} subjects:", font=('Bold', 14)).place(x=30, y=100)
        add_sub_label = tk.Label(self.main_frame, text="Click on Enrol to add new subjects", font=('Bold', 10)).place(x=30, y=150)
        enrol_btn = tk.Button(self.main_frame, text="Enrol", bg="green", fg='white', width=30, font=("Bold", 10), command=self.enrol_sub).place(x=30, y=250)

    def enrol_sub(self):
        if len(self.subjects) == 4:
            messagebox.showerror("Maximum limit", "You have already enrolled in the maximum number of subjects")
        else:
            # Add new Subject
            new_subject = Subject(self.subjects).assign_sub()
            # Add the subject to the student's enrolled subjects
            self.subjects.append(new_subject)
            self.student_det["Subjects"] = str(self.subjects)
            for stud in self.all_details:
                if stud["Email"] == self.email:
                    stud = self.student_det
            # Save the updated student data
            Data.write_data(self.all_details)
            # Print the enrolled subject details
            enrol_sub_txt = tk.Label(self.main_frame, text=f"Enrolling in Subject - {new_subject["id"]}", font=('Bold', 14)).place(x=30, y=350)
            messagebox.showinfo("Successful Enrolment", f"You are now enrolled in {len(self.subjects)} out of 4 subjects")