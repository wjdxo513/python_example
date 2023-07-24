#GUI_embedded_frame.py
import tkinter as tk
from tkinter import ttk 
from tkinter import scrolledtext 

#인스턴스 생성
win = tk.Tk()

#타이틀 추가
win.title("Python GUI")

#모든 다른 위젯들을 담는 컨테이너 프레임을 생성한다.
mighty = ttk.LabelFrame(win, text= ' Mighty Python ')
mighty.grid(column=0, row=0, padx=8, pady=4)

#win 대신에 부모로써 mighty를 사용하는 라벨을 추가하도록 수정한다.
a_label = ttk.Label(mighty, text='이름 입력:')
a_label.grid(column=0, row=0, sticky='W')

def click_me():
    action.configure(text="Hello " + name.get())

#Entry widget텍스트박스 추가하기
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky=tk.W)

#버튼 추가
action = ttk.Button(mighty, text="click me", command=click_me)
action.grid(column=2, row=1)

#체크박스 생성

ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()

#콤보박스를 추가
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number)
number_chosen["values"] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

#체크박스 추가
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty, text="UnChecked", variable=chVarUn)
check2.deselect() 
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

#scrolled textbox
scrol_w = 30
scrol_h = 3 
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h,
    wrap=tk.WORD)
scr.grid(column=0, row=5)

#리스트 안에 전역변수를 추가
colors = ["Blue", "Gold", "Red"]

#Radio button callback
def radCall():
    radSel = radVar.get()
    if radSel == 1: mighty.configure(background=colors[0])
    elif radSel == 2: mighty.configure(background=colors[1])
    elif radSel == 3: mighty.configure(background=colors[2])

#create radio button
radVar = tk.IntVar() 

#하나의 변수로 라디오버튼 생성하기
radVar = tk.IntVar() 

radVar.set(99)

#하나의 루프에서 라디오버튼을 생성하기
for col in range(3):
    curRad = tk.Radiobutton(mighty, text=colors[col], variable=radVar, 
        value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)

#Create a container to hold label
buttons_frame = ttk.LabelFrame(mighty, text=' Labels in a Frame')
#패딩을 사용해서 공간 추가하기 
buttons_frame.grid(column=1, row=7) 


#컨테이너 요소로 라벨을 위치
ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0)
ttk.Label(buttons_frame, text="Label2").grid(column=0, row=1)
ttk.Label(buttons_frame, text="Label3").grid(column=0, row=2)

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)

#name엔트리에 커서두기 
name_entered.focus()

#GUI시작
win.mainloop()

