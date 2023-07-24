#GUI_textbox_widget.py
import tkinter as tk

#인스턴스 생성
win = tk.Tk()

#타이틀 추가
win.title("Python GUI")

#크기 조정을 막기 
#win.resizable(False, False)

#라벨 추가
tk.Label(win, text="A Label").grid(column=0, row=0)

def click_me():
    action.configure(text="Hello " + name.get())

#Entry widget텍스트박스 추가하기
name = tk.StringVar()
name_entered = tk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

#버튼 추가
action = tk.Button(win, text="click me", command=click_me)
action.grid(column=1, row=1)

#name엔트리에 커서두기 
name_entered.focus()

#GUI시작
win.mainloop()


