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
    statApp.geometry("400x500")
    statApp.title("StatsEK - Stats View")

    ortalamaLabel = tk.Label(statApp, text="Ortalama = {}".format(ortalamaBul(dizi)), width=10, anchor="c")
    ortalamaLabel.grid(row=3, column=1)
    medyanLabel = tk.Label(statApp, text="Medyan = {}".format(medyanBul(dizi)), width=10, anchor="c")
    medyanLabel.grid(row=3, column=2)
    standartSapmaLabel = tk.Label(statApp, text="Standart Sapma = {}".format(standartSapmaBul(dizi)), width=10, anchor="c")
    standartSapmaLabel.grid(row=3, column=3)
    varyansLabel = tk.Label(statApp, text="Varyans = {}".format(varyansBul(dizi)), width=10, anchor="c")
    varyansLabel.grid(row=3, column=4)
    modLabel = tk.Label(statApp, text="Mod = {}".format(modBul(dizi)), width=10, anchor="c")
    modLabel.grid(row=4, column=1)
    minLabel = tk.Label(statApp, text="Min = {}".format(minBul(dizi)), width=10, anchor="c")
    minLabel.grid(row=4, column=2)
    maxLabel = tk.Label(statApp, text="Max = {}".format(maxBul(dizi)), width=10, anchor="c")
    maxLabel.grid(row=4, column=3)

    statApp.mainloop()


app.mainloop()