from tkinter import *
from tkinter import ttk

class MainApplication(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("StatsEK")
        self.geometry('{}x{}'.format(460, 350))
        self.label = ttk.Label(self, text="StatsEK")
        self.label.pack()
        self.button = ttk.Button(self, text="Open Window", command=self.open_window)
        self.button.pack()

        self.notebook = ttk.Notebook(self)
        self.notebook.pack()
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Tab 1")
        self.notebook.add(self.tab2, text="Tab 2")
        self.label1 = ttk.Label(self.tab1, text="Tab 1")
        self.label1.pack()
        self.button1 = ttk.Button(self.tab1, text="Open Window", command=self.open_window)
        self.button1.pack()
        self.label2 = ttk.Label(self.tab2, text="Tab 2")
        self.label2.pack()


    def open_window(self):
        self.newWindow = Toplevel(self)
        self.app = NewWindow(self.newWindow)

class NewWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("New Window")
        self.master.geometry('{}x{}'.format(520, 350))

        self.button = ttk.Button(self.master, text="Close Window", command=self.close_window)
        self.button.pack()

        self.tree= ttk.Treeview(self.master, column=("c1", "c2","c3"), show= 'headings')
        self.tree.column("# 1",anchor=CENTER)
        self.tree.heading("# 1", text= "ID")
        self.tree.column("# 2", anchor= CENTER)
        self.tree.heading("# 2", text= "FName")
        self.tree.column("# 3", anchor= CENTER)
        self.tree.heading("# 3", text="LName")

        # Insert the data in Treeview widget
        self.tree.insert('', 'end',text= "1",values=('XYZ', 'ABC','123'))
        self.tree.pack()


    def close_window(self):
        self.master.destroy()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()

