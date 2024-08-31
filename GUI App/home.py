import tkinter as tk
from tkinter import *
from tkinter import messagebox
import re
from PIL import Image, ImageTk
from DataFile import Data

class homeWindow:
    def __init__(self):
        self.data_initialise()
        self.win = Tk()
        self.win.geometry("500x500")
        self.win.configure(bg="grey")
        self.win.resizable(width=False, height=False)
        self.win.title("University Student Portal")
        self.email_entry =  tk.StringVar()
        self.password_entry = tk.StringVar() 
        
        self.uni_logo = Image.open("GUI App\\uts_logo1.jpg")
        self.uni_logo_resized = self.uni_logo.resize((500, 100))
        self.image1 = ImageTk.PhotoImage(self.uni_logo_resized)
        self.uni_logo_label = tk.Label(self.win, image=self.image1)
        self.uni_logo_label.pack(fill=BOTH)

        self.applabel = tk.Label(self.win, text="GUIUniApp", bg="grey", width=20, font=("sans-serif", 22, "bold")).place(x=59, y=110)
        self.displaylabel = tk.Label(self.win, text="Login", bg="grey", width=20, font=("sans-serif", 20)).place(x=75, y=170)

        #Defining labels for highlighting input fields - email address and password
        self.emaillabel = tk.Label(self.win, text="Email ID*", bg="grey", width=15, font=("bold", 12)).place(x=35, y=250)
        self.pwdlabel = tk.Label(self.win, text="Password*", bg="grey", width=15, font=("bold", 12)).place(x=35, y=290)
        self.notelabel = tk.Label(self.win, text="* means mandatory field", bg="grey", width=20, font=("bold", 8)).place(x=75, y=420)

        #Defining the entries for input fields - email address and password
        self.email_input = tk.Entry(self.win, width=30, textvariable=self.email_entry, borderwidth=3, fg="black").place(x=200, y=250)
        self.pwd_input = tk.Entry(self.win, width=30, textvariable=self.password_entry, borderwidth=3, fg="black", show="*")
        self.pwd_input.place(x=200, y=290)

        #Defining the buttons for user login and show passsword
        self.show_pass_button = tk.Checkbutton(self.win, text="show password", bg="grey", font=("bold", 8), command=self.show_password)
        self.show_pass_button.place(x=200, y=320)
        self.login_button = tk.Button(self.win, text="Login", bg="green", fg='white', width=38, font=("bold", 10), command=self.verifyLogin).place(x=75, y=370)
        self.win.mainloop()
    def data_initialise(self):
        file_check = Data.check_file()
        if file_check:
            self.student_list = Data.read_data()

    def show_password(self):
        if self.pwd_input.cget('show') == '*':
            self.pwd_input.config(show= '')
        else:
            self.pwd_input.config(show= '*')

    def verifyLogin(self):
        from student_view import enrolWindow
        email = self.email_entry.get().lower()
        pwd = self.password_entry.get()
        password = "".join([student["Password"] for student in self.student_list if student["Email"].lower() == email])
        email_regex = r"(^[a-zA-Z]+\.+[a-zA-Z]+@+university+\.+com+$)"
        email_match = re.match(email_regex, email)
        email_lst = [student["Email"] for student in self.student_list]

        if not email or not pwd:
            messagebox.showerror("Empty login credentials", "Email ID and password are mandatory fields")
        elif not email_match:
            messagebox.showerror("Invalid email format", "Valid Email ID should be in the format - firstname.lastname@university.com")
        elif email_match and email not in email_lst:
            messagebox.showerror("Credentials not available", "Login Credentials not registered")
        elif email in email_lst and pwd != password:
                messagebox.showerror("Password mismatch", "Incorrect Password. Try again!")
        else:
            student_det = [student for student in self.student_list if student["Email"].lower() == email]
            messagebox.showinfo("Success", "Login Successful")
            self.win.destroy()
            enrolWindow(student_det, self.student_list)

def main():
    homeWindow()

if __name__ == "__main__":
    main()
