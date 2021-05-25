from tkinter import *
from tkinter.messagebox import *

root=Tk()
root.geometry("500x500")
root.title("Simple Calculator")

f=("Times New Roman",24,"bold")
lbl1=Label(root,text="Enter First Integer:",font=f)
lbl1.pack()
ent_num1=Entry(root,bd=1,font=f)
ent_num1.pack()

lbl1=Label(root,text="Enter Second Integer:",font=f)
lbl1.pack()
ent_num2=Entry(root,bd=1,font=f)
ent_num2.pack()



def add():
	n1=float(ent_num1.get())
	n2=float(ent_num2.get())
	if n1==0 or n2==0:
		showinfo("Addition:","0")
	else:
		res=n1+n2
		showinfo("Addition:",res)

def sub():
	n1=float(ent_num1.get())
	n2=float(ent_num2.get())
	if n1==0 or n2==0:
		showinfo("Substraction:","0")
	else:
		res=n1-n2
		showinfo("Substraction:",res)

def mul():
	n1=float(ent_num1.get())
	n2=float(ent_num2.get())
	if n1==0 or n2==0:
		showinfo("Multiplication:","0")
	else:
		res=n1*n2
		showinfo("Multiplication:",res)
	
	

def div():
	n1=float(ent_num1.get())
	n2=float(ent_num2.get())
	
	if n2==0 or n1==0:
		a="Number connot be zero"
		showinfo("Error",a )

	else:
		res=n1/n2
		showinfo("Division:",res)
b1=Button(root,text="Addition",font=f,command=add)
b1.pack()

b1=Button(root,text="Substraction",font=f,command=sub)
b1.pack()

b1=Button(root,text="Multiplication",font=f,command=mul)
b1.pack()
b1=Button(root,text="Division",font=f,command=div)
b1.pack()
root.mainloop()