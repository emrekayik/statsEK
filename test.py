from tkinter import ttk
import tkinter as tk
from tkinter import *

my_w=tk.Tk()
my_w.geometry('400x500')
my_w.title("Stats")
trv=ttk.Treeview(my_w,selectmode='browse')
trv.grid(row=1,column=1,columnspan=4,padx=20,pady=20)
trv["columns"]=("1","2","3","4","5")
trv['show']='headings'
trv.column("1",width=30,anchor='c')
trv.column("2",width=80,anchor='c')
trv.column("3",width=80,anchor='c')
trv.column("4",width=80,anchor='c')
trv.column("5",width=80,anchor='c')
trv.heading("1",text="id")
trv.heading("2",text="Name")
trv.heading("3",text="Class")
trv.heading("4",text="Mark")
trv.heading("5",text="Gender")
i=1
trv.insert("",'end',iid=i,
		values=(i,'Alex','Four',78,'Male'))

l0 = tk.Label(my_w,  text='Add Student',
              font=('Helvetica', 16), width=30,anchor="c" )  
l0.grid(row=2,column=1,columnspan=4) 

l1 = tk.Label(my_w,  text='Name: ', width=10,anchor="c" )  
l1.grid(row=3,column=1) 

# add one text box
t1 = tk.Text(my_w,  height=1, width=10,bg='white') 
t1.grid(row=3,column=2) 

l2 = tk.Label(my_w,  text='Class: ', width=10 )  
l2.grid(row=3,column=3) 

# add list box for selection of class
options = StringVar(my_w)
options.set("") # default value

opt1 = OptionMenu(my_w, options, "Three", "Four", "Five")
opt1.grid(row=3,column=4)

l3 = tk.Label(my_w,  text='Mark: ', width=10 )  
l3.grid(row=5,column=1) 

# add one text box
t3 = tk.Text(my_w,  height=1, width=4,bg='white') 
t3.grid(row=5,column=2) 

radio_v = tk.StringVar()
radio_v.set('Female')
r1 = tk.Radiobutton(my_w, text='Male', variable=radio_v, value='Male')
r1.grid(row=5,column=3)

r2 = tk.Radiobutton(my_w, text='Female', variable=radio_v, value='Female')
r2.grid(row=5,column=4)

b1 = tk.Button(my_w,  text='Add Record', width=10, 
               command=lambda: add_data())  
b1.grid(row=6,column=2) 
my_str = tk.StringVar()
l5 = tk.Label(my_w,  textvariable=my_str, width=10 )  
l5.grid(row=8,column=1) 
def add_data():
     
     my_name=t1.get("1.0",END) # read name
     my_class=options.get()    # read class
     my_mark=t3.get("1.0",END) # read mark
     my_gender=radio_v.get()   # read gender 
     global i
     i=i+1
     trv.insert("",'end',
                values=(i,my_name,my_class,my_mark,my_gender))
     t1.delete('1.0',END)  # reset the text entry box
     t3.delete('1.0',END)  # reset the text entry box
     my_str.set("Data added ")
     t1.focus()   
     l5.after(3000, lambda: my_str.set('') ) # remove the message   
my_w.mainloop()