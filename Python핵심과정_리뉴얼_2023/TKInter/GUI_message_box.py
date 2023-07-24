# GUI_message_box.py
import tkinter as tk
from tkinter import ttk 
from tkinter import scrolledtext 
from tkinter import Menu 
from tkinter import messagebox as msg 

win = tk.Tk()
win.title("Python GUI")

#탭컨트롤 생성하기 
tabControl = ttk.Notebook(win)

#탭을 생성하기 
tab1 = ttk.Frame(tabControl)
#탭을 추가 
tabControl.add(tab1, text="Tab 1")
#두번째 탭을 추가 
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Tab 2")

#더 간단한 레이아웃 관리자를 사용할 수 있으면 pack도 그중에 하나이다. 
tabControl.pack(expand=1, fill="both")

#부모로써 tab1을 사용하는 LabelFrame
mighty = ttk.LabelFrame(tab1, text=" Mighty Python ")
mighty.grid(column=0, row=0, padx=8, pady=4)

#부모로써 mighty를 사용하는 라벨
a_label = ttk.Label(mighty, text="이름을 입력:")
a_label.grid(column=0, row=0, sticky="W")

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

#두번째 LabelFrame을 작성해서 위젯의 컨테이너가 되도록 Tab2로 배치한다.
mighty2 = ttk.LabelFrame(tab2, text=" The Snake ")
mighty2.grid(column=0, row=0, padx=8, pady=4)


#체크박스 추가
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty2, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2, text="UnChecked", variable=chVarUn)
check2.deselect() 
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2, text="Enabled", variable=chVarEn)
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
#더이상 색깔이 변경되지 않으니 text를 변경해 본다. 
def radCall():
    radSel = radVar.get()
    if radSel == 1: mighty2.configure(text="Blue")
    elif radSel == 2: mighty2.configure(text="Gold")
    elif radSel == 3: mighty2.configure(text="Red")

#create radio button
radVar = tk.IntVar() 

#하나의 변수로 라디오버튼 생성하기
radVar = tk.IntVar() 

radVar.set(99)

#하나의 루프에서 라디오버튼을 생성하기
for col in range(3):
    curRad = tk.Radiobutton(mighty2, text=colors[col], variable=radVar, 
        value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)

#Create a container to hold label
buttons_frame = ttk.LabelFrame(mighty2, text=' Labels in a Frame')
#패딩을 사용해서 공간 추가하기 
buttons_frame.grid(column=1, row=7) 


#컨테이너 요소로 라벨을 위치
ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0)
ttk.Label(buttons_frame, text="Label2").grid(column=0, row=1)
ttk.Label(buttons_frame, text="Label3").grid(column=0, row=2)

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)

#GUI종료하기
def _quit():
    win.quit()
    win.destroy()
    exit() 

#메뉴바 생성하기
menu_bar = Menu(win)
win.config(menu=menu_bar)

#메뉴를 생성하고 메뉴 아이템을 추가하기
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label = 'New')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=_quit)
menu_bar.add_cascade(label='File', menu=file_menu)

def _msgBox():
    #msg.showinfo("Python message info bar", "tkinter를 활용한 GUI")
    #약간 수정된 메세지 박스
    #msg.showwarning("Python Message Warning Box", 
    #    "python GUI 프로그래밍\n경고: 이 코드에 버그가 있습니다.")
    #사용자 응답을 처리하기
    answer = msg.askyesnocancel("Python GUI 선택", "정말 이것을 선택합니까?")
    print(answer)

#메뉴바에 About 메뉴를 추가하기
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Help', menu=help_menu)
#여기에 command를 함수로 연결한다. 
help_menu.add_command(label='About', command=_msgBox)


#GUI시작
win.mainloop()

