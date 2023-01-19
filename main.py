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

    def close_window(self):
        self.master.destroy()

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()

