import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Colleges")
root.geometry("300x300")
global top
top = tk.Frame(root)
top.grid()
global bottom
bottom = tk.Frame(root)
bottom.grid()

def hide_bottom():
    for widget in bottom.winfo_children():
        widget.destroy()


def newCollege():
    hide_bottom()
    l1 = Label(bottom, text="College Id: ")
    l1.grid(column=0, row=1)
    txt1 = Entry(bottom, width=30)
    txt1.grid(column=1, row=1, columnspan=2)
    l2 = Label(bottom, text="College Name: ")
    l2.grid(column=0, row=2)
    txt2 = Entry(bottom, width=30)
    txt2.grid(column=1, row=2, columnspan=2)
    l3 = Label(bottom, text="Course: ")
    l3.grid(column=0, row=3)
    txt3 = Entry(bottom, width=30)
    txt3.grid(column=1, row=3, columnspan=2)
    l4 = Label(bottom, text="City: ")
    l4.grid(column=0, row=4)
    txt4 = Entry(bottom, width=30)
    txt4.grid(column=1, row=4, columnspan=2)
    l5 = Label(bottom, text="Fees: ")
    l5.grid(column=0, row=5)
    txt5 = Entry(bottom, width=30)
    txt5.grid(column=1, row=5, columnspan=2)
    l6 = Label(bottom, text="Pincode: ")
    l6.grid(column=0, row=6)
    txt6 = Entry(bottom, width=30)
    txt6.grid(column=1, row=6, columnspan=2)
    btn = Button(bottom, text="Submit")
    btn.grid(columnspan=3, row=7)


def searchCollege():
    hide_bottom()
    l1 = Label(bottom, text="College Name: ")
    l1.grid(column=0, row=1)
    txt1 = Entry(bottom, width=30)
    txt1.grid(column=1, row=1, columnspan=2)
    l2 = Label(bottom, text="Course: ")
    l2.grid(column=0, row=2)
    txt2 = Entry(bottom, width=30)
    txt2.grid(column=1, row=2, columnspan=2)
    btn = Button(bottom, text="Submit")
    btn.grid(columnspan=3, row=3)


def removeCollege():
    hide_bottom()
    l1 = Label(bottom, text="College Id: ")
    l1.grid(column=0, row=1)
    txt1 = Entry(bottom, width=30)
    txt1.grid(column=1, row=1, columnspan=2)
    btn = Button(bottom, text="Submit")
    btn.grid(columnspan=3, row=2)


bt1 = Button(top, text="Register College", command=newCollege)
bt1.grid(column=0, row=0)
bt2 = Button(top, text="Search Colleges", command=searchCollege)
bt2.grid(column=1, row=0)
bt3 = Button(top, text="Remove College", command=removeCollege)
bt3.grid(column=2, row=0)

root.mainloop()
