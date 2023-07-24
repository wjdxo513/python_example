#GUI_long_label.py

import tkinter as tk
from tkinter import ttk 
from tkinter import scrolledtext 
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
action.grid(column=2, row=1)

#체크박스 생성

ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()

#콤보박스를 추가
number_chosen = ttk.Combobox(win, width=12, textvariable=number)
number_chosen["values"] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

#체크박스 추가
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect() 
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

#리스트 안에 전역변수를 추가
colors = ["Blue", "Gold", "Red"]

#Radio button callback
def radCall():
    radSel = radVar.get()
    if radSel == 1: win.configure(background=colors[0])
    elif radSel == 2: win.configure(background=colors[1])
    elif radSel == 3: win.configure(background=colors[2])

#create radio button
radVar = tk.IntVar() 

#하나의 변수로 라디오버튼 생성하기
radVar = tk.IntVar() 

radVar.set(99)

#하나의 루프에서 라디오버튼을 생성하기
for col in range(3):
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, 
        value=col, command=radCall)
    curRad.grid(column=col, row=5, sticky=tk.W)

#Create a container to hold label
buttons_frame = ttk.LabelFrame(win, text=' Labels in a Frame')
#패딩을 사용해서 공간 추가하기 
buttons_frame.grid(column=0, row=7, padx=20, pady=40)


#컨테이너 요소로 라벨을 위치
ttk.Label(buttons_frame, text="Label1 너무 긴 라벨을 추가하면 어떻게 되는지 살펴본다").grid(column=0, row=0)
ttk.Label(buttons_frame, text="Label2").grid(column=0, row=1)
ttk.Label(buttons_frame, text="Label3").grid(column=0, row=2)

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)

#name엔트리에 커서두기 
name_entered.focus()

#GUI시작
win.mainloop()

