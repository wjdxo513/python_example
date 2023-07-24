# GUI_progressbar.py

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time import sleep 

#===================================================================
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tip_window = None

    def show_tip(self, tip_text):
        "Display text in a tooltip window"
        if self.tip_window or not tip_text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")      # get size of widget
        x = x + self.widget.winfo_rootx() + 25          # calculate to display tooltip 
        y = y + cy + self.widget.winfo_rooty() + 25     # below and to the right
        self.tip_window = tw = tk.Toplevel(self.widget) # create new tooltip window
        tw.wm_overrideredirect(True)                    # remove all Window Manager (wm) decorations
#         tw.wm_overrideredirect(False)                 # uncomment to see the effect
        tw.wm_geometry("+%d+%d" % (x, y))               # create window size

        label = tk.Label(tw, text=tip_text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()
            
#===================================================================          
def create_ToolTip(widget, text):
    toolTip = ToolTip(widget)       # create instance of class
    def enter(event):
        toolTip.show_tip(text)
    def leave(event):
        toolTip.hide_tip()
    widget.bind('<Enter>', enter)   # bind mouse events
    widget.bind('<Leave>', leave)

#===================================================================

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI")  

tabControl = ttk.Notebook(win)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='Tab 1')      # Add the tab

tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='Tab 2')      # Make second tab visible

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Tab 3')

tabControl.pack(expand=1, fill="both")  # Pack to make visible

#내장 위젯 Canvas를 사용
tab3_frame = tk.Frame(tab3, bg='blue')
tab3_frame.pack() 
for orange_color in range(2):
    canvas = tk.Canvas(tab3_frame, width=150, height=80,
        highlightthickness=0, bg='orange')
    canvas.grid(row=orange_color, column=orange_color)

# LabelFrame using tab1 as the parent
mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
mighty.grid(column=0, row=0, padx=8, pady=4)

# Modify adding a Label using mighty as the parent instead of win
a_label = ttk.Label(mighty, text="Enter a name:")
a_label.grid(column=0, row=0, sticky='W')

# Modified Button Click Function
def click_me(): 
    action.configure(text='Hello ' + name.get() + ' ' + 
                     number_chosen.get())

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky='W')               # align left/West

# Adding a Button
action = ttk.Button(mighty, text="Click Me!", command=click_me)   
action.grid(column=2, row=1)                                

ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

# Spinbox callback 
def _spin():
    value = spin.get()
    print(value)
    scrol.insert(tk.INSERT, value + '\n')
     

# Adding a Spinbox widget
#또 다른 속성을 추가한다.
#bd는 borderwidth속성에 대한 간단한 표기법이다. 
spin = Spinbox(mighty, from_=0, to=10, width=5, bd=8,
    command=_spin)
spin.grid(column=0, row=2)
#툴팁 추가
create_ToolTip(spin, '이것은 첫번째 툴팁입니다')

#두번째 스틴박스 추가하기
spin = Spinbox(mighty, values=(0, 50, 100), width=5, bd=20, 
    command=_spin)
spin.grid(column=1, row=2)

# Using a scrolled Text control    
scrol_w  = 30
scrol_h  =  3
scrol = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scrol.grid(column=0, row=3, sticky='WE', columnspan=3)                    


# Tab Control 2 refactoring  ---------------------------------------------------------
# We are creating a container frame to hold all other widgets -- Tab2
mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
mighty2.grid(column=0, row=0, padx=8, pady=4)

# Creating three checkbuttons
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
check3.deselect()
check3.grid(column=2, row=4, sticky=tk.W)                     

# GUI Callback function 
def checkCallback(*ignoredArgs):
    # only enable one checkbutton
    if chVarUn.get(): check3.configure(state='disabled')
    else:             check3.configure(state='normal')
    if chVarEn.get(): check2.configure(state='disabled')
    else:             check2.configure(state='normal') 

# trace the state of the two checkbuttons
chVarUn.trace('w', lambda unused0, unused1, unused2 : checkCallback())    
chVarEn.trace('w', lambda unused0, unused1, unused2 : checkCallback())   


# First, we change our Radiobutton global variables into a list
colors = ["Blue", "Gold", "Red"]   

# We have also changed the callback function to be zero-based, using the list 
# instead of module-level global variables 
# Radiobutton Callback
def radCall():
    radSel=radVar.get()
    if   radSel == 0: win.configure(background=colors[0])  # zero-based
    elif radSel == 1: win.configure(background=colors[1])  # using list
    elif radSel == 2: win.configure(background=colors[2])

# create three Radiobuttons using one variable
radVar = tk.IntVar()

# Next we are selecting a non-existing index value for radVar
radVar.set(99)                                 
 
# Now we are creating all three Radiobutton widgets within one loop
for col in range(3):                             
    curRad = tk.Radiobutton(mighty2, text=colors[col], variable=radVar, 
                            value=col, command=radCall)          
    curRad.grid(column=col, row=6, sticky=tk.W)             # row=6

# Create a container to hold labels
buttons_frame = ttk.LabelFrame(mighty2, text=' Labels in a Frame ')
buttons_frame.grid(column=0, row=7)        
 
# Place labels into the container element
ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)

#프로그래스바 추가
progress_bar = ttk.Progressbar(tab2, orient='horizontal',
    length=286, mode='determinate')
progress_bar.grid(column=0, row=3, pady=2)

#콜백루프를 프로그래스바 업데이트
def run_progressbar():
    progress_bar["maximum"] = 100 
    for i in range(101):
        sleep(0.05)
        progress_bar["value"] = i
        progress_bar.update()
    progress_bar["value"] = 0 

def start_progressbar():
    progress_bar.start() 

def stop_progressbar():
    progress_bar.stop() 

def progressbar_stop_after(wait_ms=1000):
    win.after(wait_ms, progress_bar.stop)

#프로그래스바 커맨드에 버튼 추가
ttk.Button(buttons_frame, text="Run Progressbar", command=run_progressbar).grid(column=0, row=0, sticky='W')
ttk.Button(buttons_frame, text="Start Progressbar", command=start_progressbar).grid(column=0, row=1, sticky='W')
ttk.Button(buttons_frame, text="Stop Progressbar", command=stop_progressbar).grid(column=0, row=2, sticky='W')
ttk.Button(buttons_frame, text="Stop after second", command=progressbar_stop_after).grid(column=0, row=3, sticky='W')

# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit() 
    
# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Display a Message Box
def _msgBox():
    msg.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2017.')  
    
# Add another Menu to the Menu Bar and an item
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_msgBox)   # display messagebox when clicked
menu_bar.add_cascade(label="Help", menu=help_menu)

# Change the main windows icon
win.iconbitmap('pyc.ico')

name_entered.focus()      # Place cursor into name Entry
#======================
# Start GUI
#======================
win.mainloop()
