# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 12:50:38 2019

@author: z3525552
"""

from tkinter import *
window=Tk()

window.wm_title("Researcher")

l1=Label(window,text="Zid")
l1.grid(row=0,column=0)

l2=Label(window,text="Last Name")
l2.grid(row=0,column=2)

l3=Label(window,text="First Name")
l3.grid(row=1,column=0)

l4=Label(window,text="Scopus Id")
l4.grid(row=1,column=2)

unsw_id=StringVar()
e1=Entry(window,textvariable=unsw_id)
e1.grid(row=0,column=1)

author_last=StringVar()
e2=Entry(window,textvariable=author_last)
e2.grid(row=0,column=3)

author_first=StringVar()
e3=Entry(window,textvariable=author_first)
e3.grid(row=1,column=1)

scopus_id=StringVar()
e4=Entry(window,textvariable=scopus_id)
e4.grid(row=1,column=3)

list1=Listbox(window, height=12,width=75)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=12)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="View all", width=12)
b1.grid(row=2,column=3)

b2=Button(window,text="Search", width=12)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Researcher", width=16)
b3.grid(row=4,column=3)

b4=Button(window,text="Update Researcher", width=16)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete Researcher", width=16)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12)
b6.grid(row=7,column=3)

window.mainloop()