from tkinter import ttk
import tkinter as tk
from tkinter import *
import sqlite3

my_w = tk.Tk()
my_w.geometry("400x500")
my_w.title("Stats")

def connect():
    conn = sqlite3.connect("a.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, x INTEGER)")
    conn.commit()
    conn.close()

trv = ttk.Treeview(my_w, selectmode="browse")
trv.grid(row=1, column=1, columnspan=4, padx=20, pady=20)
trv["columns"] = ("1", "2")
trv["show"] = "headings"
trv.column("1", width=30, anchor="c")
trv.column("2", width=80, anchor="c")
trv.heading("1", text="")
trv.heading("2", text="X")

i = 0
# veri tabanından verileri çekme
def veriCek():
    conn = sqlite3.connect("a.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM test")
    rows = cur.fetchall()
    for row in rows:
        i = i + 1
        trv.insert("", "end", values=(i, row[1]))
    conn.close()
veriCek()

l0 = tk.Label(my_w, text="Veri Ekle", font=("Helvetica", 16), width=30, anchor="c")
l0.grid(row=2, column=1, columnspan=4)

l1 = tk.Label(my_w, text="X = ", width=10, anchor="c")
l1.grid(row=3, column=1)

# add one text box
t1 = tk.Text(my_w, height=1, width=10, bg="white")
t1.grid(row=3, column=2)


b1 = tk.Button(my_w, text="Veriyi Ekle", width=10, command=lambda: add_data())
b1.grid(row=6, column=2)
my_str = tk.StringVar()
l5 = tk.Label(my_w, textvariable=my_str, width=10)
l5.grid(row=8, column=1)

connect()  #  DB oluşturuldu
def add_data():
    x = t1.get("1.0", END)
    global i
    i = i + 1
    trv.insert("", "end", values=(i, x))
    t1.delete("1.0", END)  # reset the text entry box
    my_str.set("Veri eklendi ")
    t1.focus()
    l5.after(1000, lambda: my_str.set(""))

    #DB ekleme
    conn = sqlite3.connect("a.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO test VALUES (NULL, ?)", (x,))
    conn.commit()
    conn.close()



my_w.mainloop()