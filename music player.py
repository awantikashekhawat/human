from tkinter import *

root = Tk()
root.geometry("485x700+300+10")
root.title("PythonFlood-Musi Player")
root.resizable(False,False)

lbl=Label(root)
lbl.place(x=0,y=0)
# root.after(0, update , 0)

menu = PhotoImage(file='menu.png')
lb_menu = Label(root,image=menu,width=485, height=120)
lb_menu.place(x=0,y=580)

root.mainloop()
