#Matplotlib_labels_two_charts.py
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

#그림판을 그린다. 
fig = Figure(figsize=(12,8), facecolor='white')
#데이터를 셋팅 
xValues = [1,2,3,4]
yValues = [5,7,6,8]

axis = fig.add_subplot(211)
axis.plot(xValues, yValues)
axis.set_xlabel('Horizontal Label1')
axis.set_ylabel('Vertical Label1')
axis.grid(linestyle='-')

axis1 = fig.add_subplot(212)
xValues1 = [1,2,3,4]
yValues1 = [5,7,6,8]
axis1.plot(xValues1, yValues1)
axis1.grid() 

def _destroyWindow():
    root.quit()
    root.destroy()

#윈도우를 생성한다. 
root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.update()
root.deiconify()
root.mainloop()
