from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox 
from time import strftime
from datetime import datetime

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #title
        lbl_title=Label(self.root,text="ROOM BOOKING",font=("impact",18),bg="black",fg="white",relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        #logo
        img2=Image.open(r"C:\Users\Sarnika\OneDrive\Desktop\hotel management system\hotel2.jpg")
        img2 = img2.resize((100, 40))
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=5,y=5,width=230,height=40)

        
        #label frame
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Add new room.",font=("impact",12),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)

        #floor
        lbl_floor=Label(labelframeleft,text="Floor ",font=("impact",12),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("impact",13))
        entry_floor.grid(row=0,column=1,sticky=W)

        #room number
        lbl_roomNo=Label(labelframeleft,text="Room Number  ",font=("impact",12),padx=2,pady=6)
        lbl_roomNo.grid(row=1,column=0,sticky=W)

        self.var_roomNo=StringVar()
        entry_roomNo=ttk.Entry(labelframeleft,textvariable=self.var_roomNo,width=20,font=("impact",13))
        entry_roomNo.grid(row=1,column=1,sticky=W)

        #room type
        lbl_roomType=Label(labelframeleft,text="Room Type ",font=("impact",12),padx=2,pady=6)
        lbl_roomType.grid(row=2,column=0,sticky=W)

        self.var_roomType=StringVar()
        entry_roomType=ttk.Entry(labelframeleft,textvariable=self.var_roomType,width=20,font=("impact",13))
        entry_roomType.grid(row=2,column=1,sticky=W)

        #buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=250,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("impact",12),bg="black",fg="white",width=10)
        btnAdd.grid(row=0,column=0,padx=1,sticky=W)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("impact",12),bg="black",fg="white",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("impact",12),bg="black",fg="white",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset_data,font=("impact",12),bg="black",fg="white",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #Table frame search system
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("impact",12),padx=2)
        Table_Frame.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_Frame,columns=("floor","roomno","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor") 
        self.room_table.heading("roomno", text="Room Number ")
        self.room_table.heading("roomType", text="Room Type")
        
        self.room_table["show"]="headings"
        
        self.room_table.column("floor",width=100)
        self.room_table.column ("roomno", width=100)
        self.room_table.column("roomType", width=100) 

        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    #add data
    def add_data(self):
        if self.var_floor.get()== "" or self.var_roomType.get()=="":
            messagebox.showerror("Error", "All fields required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="ambagelat0",database="dbmspackage")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(self.var_floor.get(), 
                                                                          self.var_roomNo.get(),
                                                                          self.var_roomType.get()
                                                                                       ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room has been added successfully.",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="ambagelat0",database="dbmspackage")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_roomType.set(row[2])

    #update function
    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Error", "Please enter floor number.", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="ambagelat0", database="dbmspackage")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE details SET `Floor`=%s, `RoomNumber`=%s, `RoomType`=%s",
            (
             self.var_floor.get(), self.var_roomNo.get(), self.var_roomType.get(),
            ))
            
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update", "New room details have been updated successfully.",parent=self.root)

    #delete
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this room?",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="ambagelat0", database="dbmspackage")
            my_cursor = conn.cursor()
            query = "DELETE FROM details WHERE `RoomNumber` = %s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
            #my_cursor.execute(query, (self.var_contact.get(),))


        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close

    def reset_data(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_roomType.set("")
    
        
if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()