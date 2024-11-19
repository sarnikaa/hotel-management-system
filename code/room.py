from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox 
from time import strftime
from datetime import datetime

class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #variables
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar() 
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar() 
        self.var_total=StringVar()

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
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking",font=("impact",12),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #labels and entries
        #customer contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact ",font=("impact",12),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("impact",13))
        entry_contact.grid(row=0,column=1,sticky=W)

        #fetch data button
        btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("impact",10),bg="black",fg="white",width=10)
        btnFetchData.place(x=347,y=4)
        
        #Check_in Date
        check_in_date=Label(labelframeleft,font=("impact",12),text="Check In Date ",padx=2,pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin, font=("arial",13, "bold"),width=29)
        txtcheck_in_date.grid(row=1, column=1)

        # Check_out Date
        lbl_Check_out=Label(labelframeleft, font=("impact",12), text="Check Out Date ", padx=2, pady=6)
        lbl_Check_out.grid(row=2, column=0, sticky=W)
        txt_Check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout, font=("arial", 13, "bold"),width=29)
        txt_Check_out.grid(row=2, column=1)

        # Room Type
        label_RoomType=Label(labelframeleft, font=("impact",12), text="Room Type ", padx=2, pady=6) 
        label_RoomType.grid(row=3, column=0, sticky=W)
        conn=mysql.connector.connect(host="localhost",username="root",password="ambagelat0",database="dbmspackage")
        my_cursor=conn.cursor()
        my_cursor.execute("select `RoomType` from details")
        ide=my_cursor.fetchall()

        combo_RoomType=ttk. Combobox (labelframeleft,textvariable=self.var_roomtype, font=("arial", 12, "bold"), width=27, state="readonly") 
        combo_RoomType["value"]=ide
        combo_RoomType.grid(row=3, column=1)

        # Available Room
        lblRoomAvailable=Label(labelframeleft, font=("impact",12), text="Available Room ", padx=2, pady=6) 
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        #txtRoomAvailable=ttk.Entry (labelframeleft,textvariable=self.var_roomavailable, font=("arial", 13, "bold"), width=29)
        #txtRoomAvailable.grid(row=4, column=1)

        conn=mysql.connector.connect(host="localhost",username="root",password="ambagelat0",database="dbmspackage")
        my_cursor=conn.cursor()
        my_cursor.execute("select `RoomNumber` from details")
        rows=my_cursor.fetchall()
        
        combo_RoomNo=ttk. Combobox (labelframeleft,textvariable=self.var_roomavailable, font=("arial", 12, "bold"), width=27, state="readonly") 
        combo_RoomNo["value"]=rows
        combo_RoomNo.grid(row=4, column=1)

        # Meal
        lblMeal=Label(labelframeleft, font=("impact",12), text="Meal ", padx=2, pady=6) 
        lblMeal.grid(row=5, column=0, sticky=W)
        txtMeal=ttk.Entry (labelframeleft,textvariable=self.var_meal, font=("arial", 13, "bold"), width=29)
        txtMeal.grid(row=5, column=1)

        # No Of Days
        lblNoOfDays=Label (labelframeleft, font=("impact",12), text="No Of Days ", padx=2,pady=6) 
        lblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays, font=("arial",13, "bold"),width=29)
        txtNoOfDays.grid(row=6, column=1)

        # Paid Tax
        lblNoOfDays=Label (labelframeleft, font=("impact",12), text="Paid Tax ", padx=2, pady=6) 
        lblNoOfDays.grid(row=7, column=0, sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax, font=("arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=7, column=1)

        # Sub Total
        lblNoOfDays=Label (labelframeleft, font=("impact",12), text="Sub Total ", padx=2, pady=6) 
        lblNoOfDays.grid(row=8, column=0, sticky=W)
        txtNoOfDays=ttk. Entry (labelframeleft,textvariable=self.var_actualtotal, font=("arial", 13, "bold"),width=29)
        txtNoOfDays.grid(row=8, column=1)

        # Total Cost
        lblIdNumber=Label (labelframeleft, font=("impact",12), text="Total Cost ", padx=2,pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_total, font=("arial", 13, "bold"),width=29)
        txtIdNumber.grid(row=9, column=1)

        #bill button
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("impact",12),bg="black",fg="white",width=10)
        btnBill.grid(row=10,column=0,padx=1)


        #buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("impact",12),bg="black",fg="white",width=10)
        btnAdd.grid(row=0,column=0,padx=1,sticky=W)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("impact",12),bg="black",fg="white",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("impact",12),bg="black",fg="white",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("impact",12),bg="black",fg="white",width=10)
        btnReset.grid(row=0,column=3,padx=1)

        #Right side image
        img3=Image.open(r"C:\Users\Sarnika\OneDrive\Desktop\hotel management system\hotel6.jpg")
        img3 = img3.resize((520, 200))
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=520,height=200)

        #Table frame search system
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("impact",12),padx=2)
        Table_Frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label (Table_Frame, font=("impact",12), text="Search By ")
        lblSearchBy.grid(row=0, column=0, sticky=W,padx=2)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk. Entry (Table_Frame,textvariable=self.txt_search, font=("arial", 13, "bold"), width=24) 
        txtSearch.grid(row=0, column=2,padx=2)

        btnSearch=Button(Table_Frame,command=self.search,text="Search",font=("impact",12),bg="black",fg="white",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,command=self.fetch_data,text="Show All",font=("impact",12),bg="black",fg="white",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        #Show Data Table
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,columns=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfDays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact") 
        self.room_table.heading("checkin", text="Check-in ")
        self.room_table.heading("checkout", text="Check-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noOfDays", text="NoOfDays")
        
        self.room_table["show"]="headings"
        
        self.room_table.column("contact",width=100)
        self.room_table.column ("checkin", width=100)
        self.room_table.column("checkout", width=100) 
        self.room_table.column("roomtype",width=100)
        self.room_table.column ("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column ("noOfDays", width=100) 
        self.room_table.pack (fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    #add data
    def add_data(self):
        if self.var_contact.get()== "" or self.var_checkin.get()=="":
            messagebox.showerror("Error", "All fields required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="ambagelat0",database="dbmspackage")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_contact.get(),
                                                                                       self.var_checkin.get(),
                                                                                       self.var_checkout.get(),
                                                                                       self.var_roomtype.get(),
                                                                                       self.var_roomavailable.get(), 
                                                                                       self.var_meal.get(),
                                                                                       self.var_noofdays.get()
                                                                                       ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room has been booked.",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="ambagelat0",database="dbmspackage")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
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

        #self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]), 
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])
    
    #update function
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter mobile number.", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="ambagelat0", database="dbmspackage")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE room SET `check_in`=%s, `check_out`=%s, roomtype=%s, `roomavailable`=%s, `meal`=%s, `noOfDays`=%s WHERE `contact`=%s",
            (
             self.var_checkin.get(), self.var_checkout.get(), self.var_roomtype.get(),
            self.var_roomavailable.get(), self.var_meal.get(), self.var_noofdays.get(),self.var_contact.get()
            ))
            
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update", "Room details have been updated successfully.",parent=self.root)

    #delete
    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this booking?",parent=self.root)
        if mDelete>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="ambagelat0", database="dbmspackage")
            my_cursor = conn.cursor()
            #query="delete from customer where Customer Reference=%s"
            query = "DELETE FROM room WHERE `contact` = %s"
            value=(self.var_contact.get(),)
            #my_cursor.execute(query,value)
            my_cursor.execute(query, (self.var_contact.get(),))

        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close

    #reset
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set("")



    #all data fetch
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact Number.",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="ambagelat0",database="dbmspackage")
            my_cursor=conn.cursor()
            query=("select `Customer Name` from customer where `Mobile Number`=%s ")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Number not found.",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=450,y=55,width=300,height=180)
                #name
                lblName=Label(showDataFrame,text="Name : ",font=("impact",12))
                lblName.place(x=0,y=0)

                lbl=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

               #gender 
                conn=mysql.connector.connect(host="localhost",username="root",password="ambagelat0",database="dbmspackage")
                my_cursor=conn.cursor()
                query=("select `Gender` from customer where `Mobile Number`=%s ")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataFrame,text="Gender : ",font=("impact",12))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                #email
                conn=mysql.connector.connect(host="localhost",username="root",password="ambagelat0",database="dbmspackage")
                my_cursor=conn.cursor()
                query=("select `Email` from customer where `Mobile Number`=%s ")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showDataFrame,text="Email : ",font=("impact",12))
                lblemail.place(x=0,y=60)

                lbl3=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)

                #nationality
                conn=mysql.connector.connect(host="localhost",username="root",password="ambagelat0",database="dbmspackage")
                my_cursor=conn.cursor()
                query=("select `Nationality` from customer where `Mobile Number`=%s ")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataFrame,text="Nationality : ",font=("impact",12))
                lblNationality.place(x=0,y=90)

                lbl4=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)

                #address
                conn=mysql.connector.connect(host="localhost",username="root",password="ambagelat0",database="dbmspackage")
                my_cursor=conn.cursor()
                query=("select `Address` from customer where `Mobile Number`=%s ")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblAddress=Label(showDataFrame,text="Address : ",font=("impact",12))
                lblAddress.place(x=0,y=120)

                lbl1=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lbl1.place(x=90,y=120)

            conn.commit()
            conn.close()

    #search system
    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="ambagelat0", database="dbmspackage")
        my_cursor = conn.cursor()
    
        search_query_contact = "SELECT * FROM room WHERE `contact` LIKE %s"
        search_query_room = "SELECT * FROM room WHERE `room` LIKE %s"
    
        search_term = '%' + self.txt_search.get() + '%'  # Construct search term
    
        my_cursor.execute(search_query_contact, (search_term,))
        rows_contact = my_cursor.fetchall()
    
        # Fetch results of the first query before executing the second one
        my_cursor.fetchall()  # Fetching remaining rows to avoid "Unread result found" error
    
        my_cursor.execute(search_query_room, (search_term,))
        rows_room = my_cursor.fetchall()
    
        # Combine results from both queries
        rows = rows_contact + rows_room
    
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
        for i in rows:
            self.room_table.insert("", END, values=i)
            conn.commit()
    
        conn.close()


    
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)    
            tax="Rs."+str("%.2f"%((q5)*0.1))
            st="Rs."+str("%.2f"%((q5)))
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(total)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)    
            tax="Rs."+str("%.2f"%((q5)*0.09))
            st="Rs."+str("%.2f"%((q5)))
            total="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(total)

        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Duplex"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)    
            tax="Rs."+str("%.2f"%((q5)*0.09))
            st="Rs."+str("%.2f"%((q5)))
            total="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(st)
            self.var_total.set(total)
        
    

if __name__=="__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()