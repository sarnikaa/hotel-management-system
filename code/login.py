from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
from tkinter import messagebox
from hotel import HotelManagementSystem
import random
import time
import datetime

class LoginWindow:
    def __init__(self,root):
        self.root=root
        self.root.title("Login ")
        self.root.geometry("1550x900+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Sarnika\OneDrive\Desktop\hotel management system\login.jpg")
        lbl_background=Label(self.root,image=self.bg)
        lbl_background.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\Sarnika\OneDrive\Desktop\hotel management system\login icon.jpg")
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),bg="white")
        get_str.place(x=95,y=100)

        #Label
        username=Label(frame,text="Username",font=("times new roman",15,"bold"),bg="white")
        username.place(x=30,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15))
        self.txtuser.place(x=30,y=180,width=270)

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        password.place(x=30,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15))
        self.txtpass.place(x=30,y=250,width=270)

        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,bg="white")
        loginbtn.place(x=110,y=350,width=120,height=35)

        # Initialize self.new_window
        self.new_window = None

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required.")
        elif self.txtuser.get()=="kavya" and self.txtpass.get()=="sar":
            open_main=messagebox.askyesno("yesno","access only admin")
            if open_main>0:
                # Create new Toplevel window
                self.new_window=Toplevel(self.root)
                self.app=HotelManagementSystem(self.new_window)
            else:
                if not open_main:
                    return
        else:
            messagebox.showerror("Error","Invalid username and password")

    def logout(self):
        self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj=LoginWindow(root)
    root.mainloop()