# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 12:50:38 2019

@author: z3525552
"""
import backend
from tkinter import *

#Selection the data from GUI
def get_selected_row(event):
    
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    
    except(RuntimeError, TypeError, NameError):
         print ('An Error has occured!')
        
#View All data from the database

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

#Search data from the list box

def search_command():
    list1.delete(0,END)
    for row in backend.search(unsw_id.get(),author_last.get(),author_first.get(),scopus_id.get()):
        list1.insert(END,row)

#Insert data to the database

def add_command():
    backend.insert(unsw_id.get(),author_last.get(),author_first.get(),scopus_id.get())        
    list1.delete(0,END)
    list1.insert(END,(unsw_id.get(),author_last.get(),author_first.get(),scopus_id.get()))

# Delete the data from the database
    
def delete_command():
    backend.delete(selected_tuple[1])


window=Tk()
#Title of the window object
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

list1.bind('<<ListboxSelect>>', get_selected_row)

b1=Button(window,text="View all", width=12,command=view_command)
b1.grid(row=2,column=4)

b2=Button(window,text="Search", width=12, command=search_command)
b2.grid(row=3,column=4)

b3=Button(window,text="Add Researcher", width=16, command=add_command)
b3.grid(row=4,column=4)

b4=Button(window,text="Update Researcher", width=16)
b4.grid(row=5,column=4)

b5=Button(window,text="Delete Researcher", width=16, command=delete_command)
b5.grid(row=6,column=4)

b6=Button(window,text="Close", width=12)
b6.grid(row=7,column=4)

window.mainloop()