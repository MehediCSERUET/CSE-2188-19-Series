from tkinter import *
import tkinter.messagebox
import backend
root=Tk()
root.title('MTE LAB MANAGEMENT SYSTEM')

def callback():
  if tkinter.messagebox.askokcancel("quit","Do You really want to quit?"):
    root.destroy()

def clear():
  e1.delete(0,END)
  e2.delete(0,END)
  e3.delete(0,END)
  e4.delete(0,END)

def add_entry():
  backend.insert(equipement_name_txt.get(),company_name_txt.get(),date_of_entry_txt.get(),index1_txt.get())
  listing.delete(0,END)
  listing.insert(END,(equipement_name_txt.get(),company_name_txt.get(),date_of_entry_txt.get(),index1_txt.get()))
  clear()

def view_all():
  listing.delete(0,END)
  for row in backend.view():
    listing.insert(END,row)
  clear()

def update():
  global selected_tuple
  backend.update(selected_tuple[0],equipement_name_txt.get(),company_name_txt.get(),date_of_entry_txt.get(),index1_txt.get())
  view_all()

def get_selected_row(event):
  global selected_tuple
  clear()
  index=listing.curselection()[0]
  selected_tuple=listing.get(index)
  e1.insert(END,selected_tuple[1])
  e2.insert(END,selected_tuple[3])
  e3.insert(END,selected_tuple[2])
  e4.insert(END,selected_tuple[4])

def delete():
  global selected_tuple
  backend.delete(selected_tuple[0])
  view_all()

def search():
  listing.delete(0,END)
  search_data=backend.search(equipement_name_txt.get(),company_name_txt.get(),date_of_entry_txt.get(),index1_txt.get())
  if len(search_data)!=0:
    for row in search_data:
      listing.insert(END,row)
  else:
    tkinter.messagebox.showinfo('Message','NO RESULT FOUND')
  clear()

selected_tuple=tuple()
equipement_name_txt=StringVar()
company_name_txt=StringVar()
date_of_entry_txt=StringVar()
index1_txt=StringVar()
l=Label(root,text='Equipement Name',fg='red',relief=RAISED)
l.grid(row=0,column=0,padx=5,pady=5,sticky='nswe')
l=Label(root,text='Date of Entry',fg='red',relief=RAISED)
l.grid(row=1,column=0,padx=5,pady=5,sticky='nswe')
e1=Entry(root,textvariable=equipement_name_txt)
e1.grid(row=0,column=1,padx=5,pady=5,sticky='nswe')
e2=Entry(root,textvariable=date_of_entry_txt)
e2.grid(row=1,column=1,padx=5,pady=5,sticky='nswe')

l=Label(root,text='Company Name',fg='red',relief=RAISED)
l.grid(row=0,column=2,padx=5,pady=5,sticky='nswe')
l=Label(root,text='Index',fg='red',relief=RAISED)
l.grid(row=1,column=2,padx=5,pady=5,sticky='nswe')
e3=Entry(root,textvariable=company_name_txt)
e3.grid(row=0,column=3,padx=5,pady=5,sticky='nswe')
e4=Entry(root,textvariable=index1_txt)
e4.grid(row=1,column=3,padx=5,pady=5,sticky='nswe')

b1=Button(root,text='View All',fg='blue',command=view_all)
b1.grid(row=2,column=3,padx=5,pady=5,sticky='nswe')
b2=Button(root,text='Search Entry',fg='blue',command=search)
b2.grid(row=3,column=3,padx=5,pady=5,sticky='nswe')
b3=Button(root,text='Add Entry',fg='blue',command=add_entry)
b3.grid(row=4,column=3,padx=5,pady=5,sticky='nswe')
b4=Button(root,text='Update Selected',fg='blue',command=update)
b4.grid(row=5,column=3,padx=5,pady=5,sticky='nswe')
b5=Button(root,text='Delete Selected',fg='blue',command=delete)
b5.grid(row=6,column=3,padx=5,pady=5,sticky='nswe')
b6=Button(root,text='Close',fg='blue',command=root.destroy)
b6.grid(row=7,column=3,padx=5,pady=5,sticky='nswe')

listing=Listbox(root)
listing.grid(row=2,column=0,rowspan=6,columnspan=3,padx=5,pady=5,sticky='nswe')
listing.bind('<<ListboxSelect>>',get_selected_row)

for i in range(4):
  root.grid_columnconfigure(i,weight=1)
for i in range(8):
  root.grid_rowconfigure(i,weight=1)

root.protocol("WM_DELETE_WINDOW",callback)
root.mainloop()

