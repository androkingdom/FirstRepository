txt = ''

def strtbar():
    pass
def getter(etry):
    global txt
    stxt = etry.get()
    ntxt = int(stxt)
    txt = f'You Are Thinking About {ntxt} !!'

def change(label):
    label.config(text=txt)


import tkinter as tk
from tkinter import ttk

def NewWin():
    root1 = tk.Tk()
    root1.title('Reading Mind')
    label = ttk.Label(root1 , text=txt)
    
    label.pack()
    root1.mainloop()

def Newin():
    root1 = tk.Tk()
    root1.title('Reading Mind')
    root1.geometry('100x100')
    label = ttk.Label(root1 , text='Decoding Thought.....')
    button = ttk.Button(root1 , text='Click Me' , command=lambda:[root1.destroy() , root.destroy()])

    label.pack()
    button.pack()
    root1.mainloop()

root = tk.Tk()
root.geometry('250x100')
root.title("Mind Reader.....")

label = ttk.Label(root , text='Think Number Between 1 To 10')
labe2 = ttk.Label(root , text='')
entry = ttk.Entry(root , justify='center')
button = ttk.Button(root , text='Read My Mind' , command=lambda: [getter(entry) , Newin() ,NewWin()])

label.pack()
entry.pack()
button.pack()
root.mainloop()