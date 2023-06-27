from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector as c

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title('Registration Window')
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='black')

        # #------------Big Image---------------
        self.bg=ImageTk.PhotoImage(file="images/p2.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)

        #----------- left side images ------------------
        self.left=ImageTk.PhotoImage(file='images/p1.jpg')
        bg=Label(self.root, image=self.left).place(x=100,y=80,width=350,height=500)


        #-------- right side register frame --------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>
        frame1=Frame(self.root, bg='white')
        frame1.place(x=450,y=80,width=700,height=500)

        # -----------inside frame ----------------
        title=Label(frame1,text="REGISTRATION FORM",font=('Times New Roman',20,'bold'),bg='white',fg='green').place(x=200,y=27)

        b='black'
        #------------- row 1 -------------------------------------------------------------->>>>>>>>>>>>>>>>

        f_name=Label(frame1,text="First Name", font=('Times New Roman',14,'bold'),bg='white',fg=b).place(x=65,y=85)
        self.txt_fname=Entry(frame1,font=('Times New Roman',13),bg='lightgray')
        self.txt_fname.place(x=70,y= 115,width=210)

        l_name=Label(frame1,text="Last Name", font=('Times New Roman',14,'bold'),bg='white',fg=b).place(x=420,y=85)
        self.txt_lname=Entry(frame1,font=('Times New Roman',13),bg='lightgray')
        self.txt_lname.place(x=425,y= 115,width=210)

        # -------------row 2 ------------------------------------------->>>>>>>>>>>>>>>>>>>>>>

        contact_no=Label(frame1,text='Contact No',font=('Times New Roman',14,'bold'),bg='white',fg=b).place(x=65,y=155)
        self.txt_contactno = Entry(frame1, font=('Times New Roman', 13), bg='lightgray')
        self.txt_contactno.place(x=70, y=185, width=210)

        email=Label(frame1,text='Email',font=('Times New Roman',14,'bold'), bg='white', fg=b).place(x=420,y=155)
        self.txt_email = Entry(frame1, font=('Times New Roman', 13), bg='lightgray')
        self.txt_email.place(x=425, y=185, width=210)

        # ------------- row 3 ---------------------------------------------------->>>>>>>>>>>>>>.

        security = Label(frame1, text='Security Question', font=('Times New Roman', 14, 'bold'), bg='white', fg=b).place(x=65, y=225)
        self.cmb_ques=ttk.Combobox(frame1, font=('Times New Roman', 13), state='readonly',justify='center')
        self.cmb_ques["values"]=("Select","Your First Pet Name","Your Birth Place","Your GrandParent Name")
        self.cmb_ques.place(x=70, y=255,width=210)
        self.cmb_ques.current(0)

        answer = Label(frame1, text='Answer', font=('Times New Roman', 14, 'bold'), bg='white', fg=b).place(x=420,y=225)
        self.txt_ans = Entry(frame1, font=('Times New Roman', 13), bg='lightgray')
        self.txt_ans.place(x=425, y=255, width=210)

        #---------------------------- row 4 ------------------------------------------>>>>

        password = Label(frame1, text='Password', font=('Times New Roman', 14, 'bold'), bg='white', fg=b).place(x=65, y=295)
        self.txt_password = Entry(frame1, font=('Times New Roman', 13), bg='lightgray')
        self.txt_password.place(x=70, y=325, width=210)

        cnf_pass = Label(frame1, text='Confirm Password', font=('Times New Roman', 14, 'bold'), bg='white', fg=b).place(x=420,y=295)
        self.txt_cnfpass = Entry(frame1, font=('Times New Roman', 13), bg='lightgray')
        self.txt_cnfpass.place(x=425, y=325, width=210)

        #-------------- checkbox ----------------

        self.var_chk=IntVar()
        chk=Checkbutton(frame1, text='I agree to the terms and conditions',bg='white',onvalue=1,offvalue=0,font=('Times New Roman',14),cursor='hand2',variable=self.var_chk).place(x=65,y=365)


        # ---------------- submit button ----------------------------
        self.button=ImageTk.PhotoImage(file='images/register3.png')
        btn_register = Button(frame1,image=self.button,bg='white',borderwidth=0,bd=0,cursor='hand2',command=self.register_data).place(x=250, y=415, width=220, height=50)
        btn_login = Button(self.root,text='Sign In',font=('Times New Roman',20),bd=0,cursor='hand2').place(x=210, y=505,width=140,height=50)

    def register_data(self):
        if self.txt_fname.get() == '' or self.txt_lname.get() == '' or self.txt_contactno.get() =='' or  self.txt_email.get() == '' or self.cmb_ques.get() =='Select' or self.txt_ans.get() == ''or self.txt_password.get()=='' or self.txt_cnfpass.get() =='' :
            messagebox.showerror('Error Found','All the fields are required',parent=self.root)
        elif len(self.txt_contactno.get())!=10:
            messagebox.showerror('Error Found','Length of contact number should be 10 digit.',parent=self.root)
        elif self.txt_password.get() != self.txt_cnfpass.get():
            messagebox.showerror('Error','Password and Conform Password should be same.',parent=self.root )
        elif self.var_chk.get()==0:
            messagebox.showwarning('Error','Please tick checkbox',parent=self.root)
        else:
            try:
                con=c.connect(host="localhost",user='root',password='Palash@123',database='project')
                cur=con.cursor()
                cur.execute("insert into register_details(f_name, l_name, contact_no, email, question, answer, password) values (%s, %s, %s, %s, %s, %s, %s)",
                (self.txt_fname.get(),self.txt_lname.get(),self.txt_contactno.get(),self.txt_email.get(),self.cmb_ques.get(),self.txt_ans.get(),self.txt_password.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Register Success',parent=self.root)
                self.clear()
            except Exception as e:
                messagebox.showwarning('Error', f'Error due to{e}', parent=self.root)

        # print(self.txt_fname.get(),self.txt_lname.get(), self.txt_contactno.get(), self.txt_email.get(),self.cmb_ques.get(),self.txt_ans.get(),self.txt_password.get(),self.txt_cnfpass.get())

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0, END)
        self.txt_contactno.delete(0, END)
        self.txt_email.delete(0, END)
        self.cmb_ques.current(0)
        self.txt_ans.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cnfpass.delete(0, END)

root=Tk()
obj=Register(root)
root.mainloop()
