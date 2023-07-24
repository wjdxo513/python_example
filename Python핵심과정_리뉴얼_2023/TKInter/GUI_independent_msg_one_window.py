# GUI_independent_msg_one_window.py
from tkinter import messagebox as msg 
from tkinter import Tk 

root = Tk() 
root.withdraw() 
msg.showinfo('여기에서 타이틀에 출력', 'Python GUI using tkinter\n올해는 2018년')
