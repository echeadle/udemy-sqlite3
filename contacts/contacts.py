#!/usr/bin/env python3
# import from tkinter
from tkinter import Tk, Button, PhotoImage, Label, LabelFrame
from tkinter import W, E, N,S, Entry, END, StringVar, Scrollbar, Toplevel
from tkinter import ttk

class Contacts:
    def __init__(self, root):
        self.root = root
        self.create_gui()
        ttk.style = ttk.Style()
        ttk.style.configure("Treeview", font=('helvetica',10))
        ttk.style.configure("Treeview.Heading", font=('helvetica', 12, 'bold'))
    
    def create_gui(self):
         self.create_left_icon()
         self.create_label_frame()
         self.create_message_area()
         self.create_tree_view()
         self.create_scrollbar()
         self.create_bottom_buttons()


    def create_left_icon(self):
        photo = PhotoImage(file='icons/logo.gif')
        label = Label(image=photo)
        label.image = photo
        label.grid(row=0,column=0)


    def create_label_frame(self):
        labelframe = LabelFrame(self.root, text='Create New Contact', bg="sky blue",
                                font="helvetica 10")
        labelframe.grid(row=0, column=1, padx=8, pady=8, sticky='ew')
        Label(labelframe, text='Name', bg="green", fg="white").grid(row=1, column=1,
                sticky=W, pady=2, padx=15)
        self.namefield = Entry(labelframe)
        self.namefield.grid(row=1, column=2, sticky=W, padx=5, pady=2)
        Label(labelframe, text='Email', bg="brown", fg="white").grid(row=2, column=1,
                sticky=W, pady=2, padx=15)
        self.emailfield = Entry(labelframe)
        self.emailfield.grid(row=2, column=2, sticky=W, padx=5, pady=2)
        Label(labelframe, text='Number', bg="black", fg="white").grid(row=3, column=1,
                sticky=W, pady=2, padx=15)
        self.numfield = Entry(labelframe)
        self.numfield.grid(row=3, column=2, sticky=W, padx=5, pady=2)
        Button(labelframe, text='Add Contact', command="", bg="blue", 
                fg="white").grid(row=4, column=2, sticky=E, padx=5, pady=5)

    def create_message_area(self):
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=1, sticky=W)


    def create_tree_view(self):
        self.tree = ttk.Treeview(height=10, columns=("email", "number"))
        self.tree.grid(row=6, column=0, columnspan=3)
        self.tree.heading('#0', text='Name', anchor=W)
        self.tree.heading("email", text='Email Address', anchor=W)
        self.tree.heading("number",text='Contact Number', anchor=W)
    
    def create_scrollbar(self):
        self.scrollbar = Scrollbar(orient='vertical', command=self.tree.yview)
        self.scrollbar.grid(row=6,column=3,rowspan=10,sticky='sn')
    
    def create_bottom_buttons(self):
        Button(text='Delete Selected', command="",bg="red",fg="white").grid(row=8,
                column=0, sticky=W, pady=10, padx=20)
        Button(text='Modify Selected', command="",bg="purple",fg="white").grid(
                row=8, column=1, sticky=W)

if __name__ == '__main__':
    root = Tk()
    root.title('My Contact List')
    application = Contacts(root)
    root.mainloop()



