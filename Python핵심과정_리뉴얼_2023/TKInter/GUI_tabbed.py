# GUI_tabbed.py 

import tkinter as tk
from tkinter import ttk 

win = tk.Tk()
win.title("Python GUI")

#탭컨트롤 생성하기 
tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Tab 1")
#보이도록 만든다. 
tabControl.pack(expand=1, fill="both")
#GUI시작
win.mainloop()

