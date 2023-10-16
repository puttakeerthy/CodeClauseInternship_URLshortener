import pyshorteners
import webbrowser
from tkinter import *
import tkinter as tk 


root=Tk()
root.geometry("500x300")
root.title("URL_SHORTENER")

def open():
    webbrowser.open(entry_2.get())

def shortenurl():
    url=entry.get()
    s=pyshorteners.Shortener()
    #entry.delete(0,END)
    entry_2.insert(0,s.tinyurl.short(url))

label=tk.Label(root,text="Enter longer URL ",fg="purple",bg="pink",padx=20,pady=20)
label.grid(row=1,column=1,padx=80,pady=30)
entry=tk.Entry(root,bg="lightgreen",fg="brown",width=100)
entry.grid(row=1,column=2)
button=tk.Button(root,text="generate shortener URL",bg="skyblue",fg="blue",padx=10,pady=10,command=shortenurl)
button.grid(row=3,column=3)
label_2=tk.Label(root,text=" the generated Shortener URL",fg="purple",bg="pink",padx=20,pady=20)
label_2.grid(row=2,column=1)
entry_2=tk.Entry(root,bg="lightgreen",fg="brown",width=100)
entry_2.grid(row=2,column=2)
button_2=tk.Button(root,text="open",bg="skyblue",fg="blue",padx=10,pady=10,command=open)
button_2.grid(row=2,column=3)
root.mainloop()