from tkinter import *
from tkinter.messagebox import *

root=Tk()
root.title("Tables Calculator by Nishant Patil.")
root.geometry("500x800")
root.configure(bg="black")

def tables():
	num=int(ent.get())
	if num<=0:
		showinfo("Error","Invalid Number")
	else:
		i=1
		while i<=10:
			prod=num*i
			
			tlbl=Label(root,text=str(num)+"X"+str(i)+"="+str(prod),font=f,bg="black",fg="#fff")
			tlbl.pack()
			i=i+1
			
			
			

f=("curiore",24,"bold")
lbl=Label(root,text="Enter the Number:",bg="black",fg="white",font=f)
ent=Entry(root,bd=4,font=f)
btn=Button(root,text="Generate Table",font=f,bg="black",fg="white",command=tables)


lbl.pack(pady=10)
ent.pack(pady=10)
btn.pack(pady=10)

root.mainloop()