from tkinter import ttk
import tkinter as tk
from tkinter import *

from func import *

app = tk.Tk()
app.geometry("400x500")
app.title("StatsEK")

trv = ttk.Treeview(app, selectmode="browse")
trv.grid(row=1, column=1, columnspan=4, padx=20, pady=20)
trv["columns"] = ("1", "2")
trv["show"] = "headings"
trv.column("1", width=30, anchor="c")
trv.column("2", width=80, anchor="c")
trv.heading("1", text="")
trv.heading("2", text="X")

i = 0
dizi = []

l0 = tk.Label(app, text="Veri Ekle", font=("Helvetica", 16), width=30, anchor="c")
l0.grid(row=2, column=1, columnspan=4)

l1 = tk.Label(app, text="X = ", width=10, anchor="c")
l1.grid(row=3, column=1)

# add one text box
t1 = tk.Text(app, height=1, width=10, bg="white")
t1.grid(row=3, column=2)


b1 = tk.Button(app, text="Veriyi Ekle", width=10, command=lambda: add_data())
b1.grid(row=6, column=2)
my_str = tk.StringVar()
l5 = tk.Label(app, textvariable=my_str, width=10)
l5.grid(row=8, column=1)

# İstatistikler
""" ortalamaButon = tk.Button(app, text="Ortalama", width=10, command=lambda: ortalama())
ortalamaButon.grid(row=9, column=1)

medyanButon = tk.Button(app, text="Medyan", width=10, command=lambda: print(medyanBul(dizi)))
medyanButon.grid(row=9, column=2)

standartSapmaButon = tk.Button(app, text="Standart Sapma", width=10, command=lambda: print(standartSapmaBul(dizi)))
standartSapmaButon.grid(row=9, column=3)

varyansButon = tk.Button(app, text="Varyans", width=10, command=lambda: print(varyansBul(dizi)))
varyansButon.grid(row=9, column=4)

modButon = tk.Button(app, text="Mod", width=10, command=lambda: print(modBul(dizi)))
modButon.grid(row=10, column=1)

minButon = tk.Button(app, text="Min", width=10, command=lambda: print(minBul(dizi)))
minButon.grid(row=10, column=2)

maxButon = tk.Button(app, text="Max", width=10, command=lambda: print(maxBul(dizi)))
maxButon.grid(row=10, column=3) 

def ortalama():
    print(len(trv.get_children()))
    for child in trv.get_children():
        print(trv.item(child)["values"][1])
        print(dizi)
        print(type(dizi[1]))
        print(ortalamaBul(dizi))
    
"""

istatislikButon = tk.Button(app, text="İstatistikler", width=10, command=lambda: statsView())
istatislikButon.grid(row=10, column=4)


def add_data():
    x = t1.get("1.0", END)
    global i, dizi
    i = i + 1
    trv.insert("", "end", values=(i, x))
    dizi.append(int(x.strip('\n')))
    t1.delete("1.0", END)  # reset the text entry box
    my_str.set("Veri eklendi ")
    t1.focus()
    l5.after(1000, lambda: my_str.set(""))



def statsView():
    statApp = tk.Tk()
    statApp.geometry("620x500")
    statApp.title("StatsEK - Stats View")

    statsLabel = tk.Label(statApp, text="İstatistikler", font=("Helvetica", 16), width=30, anchor="c")
    statsLabel.grid(row=0, column=1, columnspan=4)

    treeViewStats = ttk.Treeview(statApp, selectmode="browse")
    treeViewStats.grid(row=1, column=1, columnspan=1, padx=20, pady=20)
    treeViewStats["columns"] = ("1", "2", "3", "4", "5", "6", "7")
    treeViewStats["show"] = "headings"
    treeViewStats.column("1", width=80, anchor="c")
    treeViewStats.column("2", width=80, anchor="c")
    treeViewStats.column("3", width=120, anchor="c")
    treeViewStats.column("4", width=80, anchor="c")
    treeViewStats.column("5", width=70, anchor="c")
    treeViewStats.column("6", width=70, anchor="c")
    treeViewStats.column("7", width=70, anchor="c")
    treeViewStats.heading("1", text="Ortalama")
    treeViewStats.heading("2", text="Medyan")
    treeViewStats.heading("3", text="Standart Sapma")
    treeViewStats.heading("4", text="Varyans")
    treeViewStats.heading("5", text="Mod")
    treeViewStats.heading("6", text="Min")
    treeViewStats.heading("7", text="Max")

    treeViewStats.insert(
        "", 
        "end", 
        values=(
            ortalamaBul(dizi), 
            medyanBul(dizi), 
            standartSapmaBul(dizi), 
            varyansBul(dizi), 
            modBul(dizi), 
            minBul(dizi), 
            maxBul(dizi)
            )
        )

    statApp.mainloop()


app.mainloop()