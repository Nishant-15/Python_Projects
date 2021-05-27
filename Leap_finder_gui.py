from tkinter import *
from tkinter.messagebox import *

root=Tk()
root.geometry("500x500")
root.title("Leap or Not By Nishant Patil.")
root.iconbitmap("calci.ico")

def Leap():
	year=int(ent.get())
	if year%4==0:
		showinfo("Result","Leap Year.")
	else:
		showinfo("Result","Not a Leap Year.")

f=("Times new roman",20,"bold")
labl=Label(root,text="Enter Year",font=f)
labl.pack(pady=10)
ent=Entry(root,bd=4,font=f)
ent.pack(pady=10)
btn=Button(root,text="Leap or Not",bd=4,font=f,command=Leap)
btn.pack()
root.mainloop()