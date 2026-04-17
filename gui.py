from tkinter import*#call library
import tkinter as tk
import sys,time,datetime,os
import tkinter.font as tkFont
from tkinter import scrolledtext,messagebox
from library import Library

library = Library()
win = Tk()
win.title("")

win.geometry("1280x720+250-170")    #set GUI original size
win.minsize(width=400,height=200)   #set GUI Minimun size
win.maxsize(width=1980,height=1080)     #set GUI Maximun size
win.resizable(False,False)  #user can(Ture/1)or can't(False/0)change GUI's size
win.config(bg="skyblue")    #transparency,"alpha"=ture,0.5=50%,eg:win.attributes("-alpha",number)
win.attributes("-alpha",1)  #on top,e.g.:win.attributes("-topmost",True/False")
win.attributes("-topmost",True)

fontStyle = tkFont.Font(family="Lucida Grande", size=40)    #text size
fontStyle1 = tkFont.Font(family="Lucida Grande", size=25)
fontStyle2 = tkFont.Font(family="Lucida Grande", size=60)

def tool_set():
    btn_NBBR = tk.Button(win,font=fontStyle1,text="New Books & Books Record",bg= 'skyblue',command=NBBR)
    btn_NBBR.place(anchor=CENTER,x=220,y=30)
    btn_SRCH = tk.Button(win,font=fontStyle1,text="Book searching",bg= 'skyblue',command=SRCH)
    btn_SRCH.place(anchor=CENTER,x=570,y=30)


def New_Books_Books_Record():
    global ety_bt, ety_at, ety_yr, rec_box

    lab_ab = tk.Label(win,font=fontStyle1,text="Adding New Books",bg= 'skyblue')    #labal for add book
    lab_ab.place(anchor=CENTER,x=650,y=80)

    lab_bt = tk.Label(win,font=fontStyle1,text="Book Title",bg= 'skyblue')  #labal for book title
    lab_bt.place(anchor=CENTER,x=100,y=170)
    ety_bt = tk.Entry(win,font=fontStyle1,bg= 'skyblue')    #entry blank for book title
    ety_bt.place(anchor=CENTER,x=400,y=170)

    lab_at = tk.Label(win,font=fontStyle1,text="Author",bg= 'skyblue')  #label blank for book author
    lab_at.place(anchor=CENTER,x=680,y=170)
    ety_at = tk.Entry(win,font=fontStyle1,bg= 'skyblue')    #entry blank for book author
    ety_at.place(anchor=CENTER,x=950,y=170)

    lab_yr = tk.Label(win,font=fontStyle1,text="Year",bg= 'skyblue')    #label blank for book publish year
    lab_yr.place(anchor=CENTER,x=150,y=220)
    ety_yr = tk.Entry(win,font=fontStyle1,bg= 'skyblue')    #entry blank for book publish year
    ety_yr.place(anchor=CENTER,x=400,y=220)

    btn_enter = tk.Button(win,font=fontStyle1,text="Enter",bg='skyblue',command = add_book)  #button for comfirm to add book
    btn_enter.place(anchor=CENTER,x=1200,y=170)

    lab_br = tk.Label(win,font=fontStyle1,text="Recent Added Books Record",bg= 'skyblue')
    lab_br.place(anchor=CENTER,x=225,y=310)
    rec_box = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=70, height=10,bg='skyblue',font=fontStyle1)    #show the book that user added recently
    rec_box.place(anchor=CENTER,x=620,y=520)
    rec_box.config(state='disabled')

def Search():
    global ety_bt, ety_at, ety_yr, rec_box 

    lab_SRHB = tk.Label(win,font=fontStyle1,text="Searching Books",bg= 'skyblue')
    lab_SRHB.place(anchor=CENTER,x=650,y=80)


    lab_bt = tk.Label(win,font=fontStyle1,text="Book Title",bg= 'skyblue')
    lab_bt.place(anchor=CENTER,x=100,y=170)
    ety_bt = tk.Entry(win,font=fontStyle1,bg= 'skyblue')
    ety_bt.place(anchor=CENTER,x=400,y=170)

    lab_at = tk.Label(win,font=fontStyle1,text="Author",bg= 'skyblue')
    lab_at.place(anchor=CENTER,x=680,y=170)
    ety_at = tk.Entry(win,font=fontStyle1,bg= 'skyblue')
    ety_at.place(anchor=CENTER,x=950,y=170)

    lab_yr = tk.Label(win,font=fontStyle1,text="Year",bg= 'skyblue')
    lab_yr.place(anchor=CENTER,x=150,y=220)
    ety_yr = tk.Entry(win,font=fontStyle1,bg= 'skyblue')
    ety_yr.place(anchor=CENTER,x=400,y=220)

    btn_enter = tk.Button(win,font=fontStyle1,text="Search",bg='skyblue',command = search_book)  
    btn_enter.place(anchor=CENTER,x=1200,y=170)

    lab_br = tk.Label(win,font=fontStyle1,text="Search Result",bg= 'skyblue')
    lab_br.place(anchor=CENTER,x=130,y=310)
    rec_box = scrolledtext.ScrolledText(win, wrap=tk.WORD,width=70, height=10,bg='skyblue',font=fontStyle1)
    rec_box.place(anchor=CENTER,x=620,y=520)
    rec_box.config(state='disabled')
    

def NBBR():
    clear()
    New_Books_Books_Record()

def SRCH():
    clear()
    Search()

def add_book():
    title = ety_bt.get().strip()
    author = ety_at.get().strip()
    year_str = ety_yr.get().strip()

    if not title or not author or not year_str:
        messagebox.showerror("Error", "Please fill Book Title / Author / Year") #make sure that is no blank input
        return

    try:
        year = int(year_str)
    except ValueError:
        messagebox.showerror("Error", "Year must be a number")  #aviod false input
        return

    library.add_book(title, author, year)   #call add_book function from library.py 

    rec_box.config(state="normal")
    rec_box.insert(tk.END, library.books[-1].get_info() + "\n") #refresh rec box
    rec_box.config(state="disabled")

    library.save_books()

    ety_bt.delete(0, tk.END)  #clear all the input entry
    ety_at.delete(0, tk.END)
    ety_yr.delete(0, tk.END)

def search_book():
    title = ety_bt.get().strip().lower()
    author = ety_at.get().strip().lower()
    year = ety_yr.get().strip()

    rec_box.config(state="normal")
    rec_box.delete("1.0", tk.END)   #clear the old record

    found = False

    for book in library.books:

        match = True

        if title and title not in book.title.lower():
            match = False

        if author and author not in book.author.lower():
            match = False

        if year:
            if not year.isdigit() or int(year) != book.year:
                match = False

        if match:
            rec_box.insert(tk.END, book.get_info() + "\n")
            found = True

    if not found:
        rec_box.insert(tk.END, "No matching books found.\n")

    rec_box.config(state="disabled")

def clear():
    x = win.winfo_children()
    for x in x:
        x.destroy()
    tool_set()


tool_set()
New_Books_Books_Record()
win.mainloop()