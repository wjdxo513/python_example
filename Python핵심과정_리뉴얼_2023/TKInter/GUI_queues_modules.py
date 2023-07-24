# GUI_queues_modules.py

#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time import  sleep         
import ToolTip as tt
#쓰레드를 사용하기 위해서 threading모듈에서 Thread클래스를 임포트해야 한다. 
from threading import Thread
#큐를 추가한다.
from queue import Queue 
#미리 준비한 큐모듈을 로딩한다.
import Queues as bq 
#내장된 다이알로그박스 사용
from tkinter import filedialog as fd 
from os import path 
from os import makedirs

#모듈 레벨 GLOBALS
GLOBAL_CONST = 42
fDir = path.dirname(__file__)
netDir = fDir + 'Backup'
if not path.exists(netDir):
    makedirs(netDir, exist_ok=True)

def __init__(self):
    self.create_widgets()
    self.defaultFileEntries()

def defaultFileEntries(self):
    self.fileEntry.delete(0, tk.END)
    self.fileEntry.insert(0, fDir)
    if len(fDir) > self.entryLen:
        self.fileEntry.config(width=len(fDir) + 3)
        self.fileEntry.config(state='readonly')
        self.netwEntry.delete(0, tk.END)
        self.netwEntry.insert(0, netDir)
        if len(netDir) > self.entryLen:
            self.netwEntry.config(width=len(netDir) + 3)

#=====================================================
class OOP():
    def __init__(self):         # Initializer method

        #쓰레드에서 TCP/IP서버 시작
        svrT = Thread(target=startServer, daemon=True)
        svrT.start() 
        
        #큐 생성
        self.gui_queue = Queue() 

        # Create instance
        self.win = tk.Tk()   
        
        # Add a title       
        self.win.title("Python GUI")      
        self.create_widgets()

    def use_queues(self):
        while True:
            print(self.gui_queue.get())

    #쓰레드에서 메서드 실행
    #쓰레드를 백그라운드 작업으로 실행하는 방법을 배우게 된다.
    #이 작업을 데몬이라고 한다. 
    #GUI의 메인 쓰레드를 닫으면 모든 데몬도 자동으로 멈추게 된다. 
    def create_thread(self):
        self.run_thread = Thread(target=self.method_in_a_thread, args=[8])
        #아직 쓰레드가 실행되는데 창을 닫으면 런타임 에러가 발생한다. 
        #쓰레드를 데몬으로 변환하면 에러를 해결할 수 있다. 
        self.run_thread.setDaemon(True)
        self.run_thread.start() 
        
        #자체 쓰레드에서 큐 시작
        write_thread = Thread(target=self.use_queues, daemon=True)
        write_thread.start() 

    #쓰레드 생성자에 args = [8]을 추가하고 인수를 기대하도록 대상 메서드를 수정하면
    #쓰레드된 메서드에 인수를 전달할 수 있다. args의 매개변수는 시퀀스여야 하며 
    #파이썬 리스트에 숫자를 넣을 것이다. 
    def method_in_a_thread(self, num_of_loops=10):
        print('Hi, how are you?')
        #실제 문제가 해결되는지를 확인해 본다.
        for idx in range(10):
            #5초를 대기하도록 한다. 
            sleep(1)
            self.scrol.insert(tk.INSERT, str(idx) + 'n')
        sleep(1)
        print('method_in_a_thread():', self.run_thread.isAlive())

    # Modified Button Click Function
    def click_me(self): 
        #현재 클래스 인스턴스 전달(self)
        print(self)
        bq.write_to_scrol(self)

    # Spinbox callback 
    def _spin(self):
        value = self.spin.get()
        print(value)
        self.scrol.insert(tk.INSERT, value + '\n')
        
    # GUI Callback  
    def checkCallback(self, *ignored_args):
        # only enable one checkbutton
        if self.chVarUn.get(): self.check3.configure(state='disabled')
        else:                  self.check3.configure(state='normal')
        if self.chVarEn.get(): self.check2.configure(state='disabled')
        else:                  self.check2.configure(state='normal') 
        
    # Radiobutton Callback
    def radCall(self):
        radSel = self.radVar.get()
        if   radSel == 0: self.mighty2.configure(text='Blue')
        elif radSel == 1: self.mighty2.configure(text='Gold')
        elif radSel == 2: self.mighty2.configure(text='Red')          
        
    # update progressbar in callback loop
    def run_progressbar(self):
        self.progress_bar["maximum"] = 100
        for i in range(101):
            sleep(0.05)
            self.progress_bar["value"] = i   # increment progressbar
            self.progress_bar.update()       # have to call update() in loop
        self.progress_bar["value"] = 0       # reset/clear progressbar  
    
    def start_progressbar(self):
        self.progress_bar.start()
        
    def stop_progressbar(self):
        self.progress_bar.stop()
     
    def progressbar_stop_after(self, wait_ms=1000):    
        self.win.after(wait_ms, self.progress_bar.stop)        

    def usingGlobal(self):
        global GLOBAL_CONST
        print(GLOBAL_CONST)
        GLOBAL_CONST = 777
        print(GLOBAL_CONST)
              
    # Exit GUI cleanly
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit() 


    def getFileName():
        print('Hello from getFileName')
        fDir = path.dirname(__file__)
        fName = df.askopenfilename(parent=self.win, initialdir=fDir)

    from tkinter import messagebox as msg 
    def copyFile():
        #Shutil 은 셀 유틸리티의 짧은 표기법이다. 
        import shutil
        src = self.fileEntry.get() 
        file = src.split('/')[-1]
        dst = self.netwEntry.get() + '' + file 
        try:
            shutil.copy(src, dst)
            msg.showinfo('Copy File to Network', 'Success: File copied.')
        except FileNotFoundError as err:
            msg.showerror('Copy File to network', '*** Filed to copy file! ***\n\n' + 
                str(err))
        except Exception as ex:
            msg.showerror('Copy File to network', '*** Filed to copy file! ***\n\n' + 
                str(ex))

    #####################################################################################       
    def create_widgets(self):    
        tabControl = ttk.Notebook(self.win)          # Create Tab Control
        
        tab1 = ttk.Frame(tabControl)            # Create a tab 
        tabControl.add(tab1, text='Tab 1')      # Add the tab
        tab2 = ttk.Frame(tabControl)            # Add a second tab
        tabControl.add(tab2, text='Tab 2')      # Make second tab visible
        
        tabControl.pack(expand=1, fill="both")  # Pack to make visible
        
        #Manage Files프레임 생성
        mngFilesFrame = ttk.LabelFrame(tab2, text=' Manage Files: ')
        mngFilesFrame.grid(column=0, row=1, sticky='WE', padx=10, pady=5)

        #Manage Files프레임에 위젯 추가
        lb = ttk.Button(mngFilesFrame, text='Browse to File...',
            command=self.getFileName)
        lb.grid(column=0, row=0, sticky=tk.W)

        file =tk.StringVar() 
        self.entryLen = scrol_w 
        self.fileEntry = ttk.Entry(mngFilesFrame, width-self.entryLen,
            textvariable=file)
        self.fileEntry.grid(column=1, row=0, sticky=tk.W)

        logDir = tk.StringVar()
        self.netwEntry = ttk.Entry(mngFilesFrame,
            width=self.entryLen,
            textvariable=logDir)
        self.netwEntry.grid(column=1, row=1, sticky=tk.W)

        cb = ttk.Button(mngFilesFrame, text='Copy File To: ', command=self.copyFile)
        cb.grid(column=0, row=1, sticky=tk.E)

        #각 라벨 주위에 여유 공간 추가
        for child in mngFilesFrame.winfo_children():
            child.grid_configure(padx=6, pady=6)

        # LabelFrame using tab1 as the parent
        mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
        mighty.grid(column=0, row=0, padx=8, pady=4)
        
        # Modify adding a Label using mighty as the parent instead of win
        a_label = ttk.Label(mighty, text="Enter a name:")
        a_label.grid(column=0, row=0, sticky='W')
     
        # 텍스트 박스 엔트리 웨젯 추가 
        self.name = tk.StringVar()
        # with를 24로 늘린다. 
        self.name_entered = ttk.Entry(mighty, width=24, textvariable=self.name)
        self.name_entered.grid(column=0, row=1, sticky='W')               
        self.name_entered.delete(0, tk.END)
        self.name_entered.insert(0, '< default name >')

        # Adding a Button
        self.action = ttk.Button(mighty, text="Click Me!", command=self.click_me)   
        self.action.grid(column=2, row=1)                                
        
        ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
        number = tk.StringVar()
        self.number_chosen = ttk.Combobox(mighty, width=14, textvariable=number, state='readonly')
        self.number_chosen['values'] = (1, 2, 4, 42, 100)
        self.number_chosen.grid(column=1, row=1)
        self.number_chosen.current(0)
        
        # Adding a Spinbox widget
        self.spin = Spinbox(mighty, values=(1, 2, 4, 42, 100), width=5, bd=9, command=self._spin) # using range
        self.spin.grid(column=0, row=2, sticky='W') # align left
        
        #스크롤 가능한 텍스트 컨트롤 사용 
        scrol_w = 40; scrol_h = 10                  # 크기 증가 
        self.scrol = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scrol.grid(column=0, row=3, sticky='WE', columnspan=3)                    
        
        for child in mighty.winfo_children():       # add spacing to align widgets within tabs
            child.grid_configure(padx=4, pady=2) 
         
        #=====================================================================================
        # Tab Control 2 ----------------------------------------------------------------------
        self.mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
        self.mighty2.grid(column=0, row=0, padx=8, pady=4)
        
        # Creating three checkbuttons
        chVarDis = tk.IntVar()
        check1 = tk.Checkbutton(self.mighty2, text="Disabled", variable=chVarDis, state='disabled')
        check1.select()
        check1.grid(column=0, row=0, sticky=tk.W)                   
        
        chVarUn = tk.IntVar()
        check2 = tk.Checkbutton(self.mighty2, text="UnChecked", variable=chVarUn)
        check2.deselect()
        check2.grid(column=1, row=0, sticky=tk.W)                   
        
        chVarEn = tk.IntVar()
        check3 = tk.Checkbutton(self.mighty2, text="Enabled", variable=chVarEn)
        check3.deselect()
        check3.grid(column=2, row=0, sticky=tk.W)                     
        
        # trace the state of the two checkbuttons
        chVarUn.trace('w', lambda unused0, unused1, unused2 : self.checkCallback())    
        chVarEn.trace('w', lambda unused0, unused1, unused2 : self.checkCallback())   
        
        
        # First, we change our Radiobutton global variables into a list
        colors = ["Blue", "Gold", "Red"]   
        
        # create three Radiobuttons using one variable
        self.radVar = tk.IntVar()
        
        # Next we are selecting a non-existing index value for radVar
        self.radVar.set(99)                                 
         
        # Now we are creating all three Radiobutton widgets within one loop
        for col in range(3):                             
            curRad = tk.Radiobutton(self.mighty2, text=colors[col], variable=self.radVar, 
                                    value=col, command=self.radCall)          
            curRad.grid(column=col, row=1, sticky=tk.W)             # row=6
            # And now adding tooltips
            tt.create_ToolTip(curRad, 'This is a Radiobutton control')
                
        # Add a Progressbar to Tab 2
        self.progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=286, mode='determinate')
        self.progress_bar.grid(column=0, row=3, pady=2)         
             
        # Create a container to hold buttons
        buttons_frame = ttk.LabelFrame(self.mighty2, text=' ProgressBar ')
        buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)        
        
        # Add Buttons for Progressbar commands
        ttk.Button(buttons_frame, text=" Run Progressbar   ", command=self.run_progressbar).grid(column=0, row=0, sticky='W')  
        ttk.Button(buttons_frame, text=" Start Progressbar  ", command=self.start_progressbar).grid(column=0, row=1, sticky='W')  
        ttk.Button(buttons_frame, text=" Stop immediately ", command=self.stop_progressbar).grid(column=0, row=2, sticky='W')  
        ttk.Button(buttons_frame, text=" Stop after second ", command=self.progressbar_stop_after).grid(column=0, row=3, sticky='W')  
         
        for child in buttons_frame.winfo_children():  
            child.grid_configure(padx=2, pady=2) 
         
        for child in self.mighty2.winfo_children():  
            child.grid_configure(padx=8, pady=2) 
            
        # Creating a Menu Bar
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)
        
        # Add menu items
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        
        # Display a Message Box
        def _msgBox():
            msg.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2017.')  
            
        # Add another Menu to the Menu Bar and an item
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=_msgBox)   # display messagebox when clicked
        menu_bar.add_cascade(label="Help", menu=help_menu)
        
        # Change the main windows icon
        self.win.iconbitmap('pyc.ico')
        
        # It is not necessary to create a tk.StringVar() 
        # strData = tk.StringVar()
        strData = self.spin.get()
        print("Spinbox value: " + strData)
        
        # call function
        self.usingGlobal()
        
        #self.name_entered.focus()     
        tabControl.select(1)

        # Add Tooltips -----------------------------------------------------
        # Add a Tooltip to the Spinbox
        tt.create_ToolTip(self.spin, 'This is a Spinbox control')   
                
        # Add Tooltips to more widgets
        tt.create_ToolTip(self.name_entered, 'This is an Entry control')  
        tt.create_ToolTip(self.action, 'This is a Button control')                      
        tt.create_ToolTip(self.scrol, 'This is a ScrolledText control')


#네트워크 통신을 위해 TCP/IP 사용하기
from socketserver import BaseRequestHandler, TCPServer
class RequestHandler(BaseRequestHandler):
    #기본클래스 handler메서드 오버라이드
    def handle(self):
        print('Server connected to: ', self.client_address)
        while True:
            rsp = self.request.recv(512)
            if not rsp: break 
            self.request.send(b'Server received: ' + rsp)

    def start_server():
        server = TCPServer(('', 24000), RequestHandler)
        server.serve_forever() 

#======================
# Start GUI
#======================
oop = OOP()

# 쓰레드에서 메서드를 실행한다.
run_thread = Thread(target=oop.method_in_a_thread)


oop.win.mainloop()
