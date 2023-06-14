import tkinter as tk
from tkinter import ttk
import time as tt

root = tk.Tk()
label = ttk.Label(root , text='Hello World')

label.pack()

tt.sleep(1)
print('Closing')
root.destroy
root.mainloop()
