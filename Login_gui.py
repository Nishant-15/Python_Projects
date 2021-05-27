from tkinter import *
from tkinter.messagebox import *

root=Tk()
root.geometry("500x500")
root.title("Login App by Nishant Patil.")

def check():
	username=ent_un.get()
	pwd=ent_pwd.get()
	if username=="Nishant" and pwd=="1234":
		showinfo("Message","Login Success")
	else:
		showinfo("Error","Invalid Username or password")

f=("Arial",20,"bold")
lbl_un=Label(root,text="Enter Username:",font=f)
ent_un=Entry(root,font=f,bd=4)
lbl_pwd=Label(root,text="Enter Username:",font=f)
ent_pwd=Entry(root,font=f,bd=4,show="*")
btn=Button(root,text="Login",bd=4,font=f,command=check)
lbl_un.pack(pady=10)
ent_un.pack(pady=10)
lbl_pwd.pack(pady=10)
ent_pwd.pack(pady=10)
btn.pack(pady=10)
root.mainloop()