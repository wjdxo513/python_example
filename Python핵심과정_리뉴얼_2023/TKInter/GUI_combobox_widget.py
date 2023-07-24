# GUI_combobox_widget.py
#GUI_textbox_widget.py
import tkinter as tk
from tkinter import ttk 

#인스턴스 생성
win = tk.Tk()

#타이틀 추가
win.title("Python GUI")

#크기 조정을 막기 
#win.resizable(False, False)

#라벨 추가
ttk.Label(win, text="A Label").grid(column=0, row=0)

def click_me():
    action.configure(text="Hello " + name.get())

#Entry widget텍스트박스 추가하기
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

#버튼 추가
action = ttk.Button(win, text="click me", command=click_me)
action.grid(column=1, row=1)

ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()

#콤보박스를 추가
number_chosen = ttk.Combobox(win, width=12, textvariable=number)
number_chosen["values"] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

#name엔트리에 커서두기 
name_entered.focus()

#GUI시작
win.mainloop()


