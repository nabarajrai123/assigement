from tkinter import *
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("student management system")
        self.root.geometry("800x450+0+0")

        title=Label(root,text="student management system",bd=10,relief=GROOVE,font=("times new roman",34,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)
#======manage frame===================

        manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        manage_frame.place(x=10,y=100,width=200,height=330)

        m_title=Label(manage_frame,text="manage student",font=("times new roman",34,"bold"),bg="yellow",fg="red")




#======detail frame============


        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        detail_frame.place(x=250,y=100,width=520,height=330)
        
root=Tk()
ob=Student(root)
root.mainloop()