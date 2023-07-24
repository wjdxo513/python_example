#Matplotlib_labels_two.py
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

fig = Figure(figsize=(12,8), facecolor='white')
xValues = [1,2,3,4]
yValues = [5,7,6,8]

axis1 = fig.add_subplot(221) #2열 2컬럼 그래프
axis2 = fig.add_subplot(222, sharex=axis1, sharey=axis1)
axis3 = fig.add_subplot(223, sharex=axis1, sharey=axis1)
axis4 = fig.add_subplot(224, sharex=axis1, sharey=axis1)

axis1.plot(xValues, yValues)
axis1.set_xlabel('Horizontal Label1')
axis1.set_ylabel('Vertical Label1')
axis1.grid(linestyle='-')

axis2.plot(xValues, yValues)
axis2.set_xlabel('Horizontal Label2')
axis2.set_ylabel('Vertical Label2')
axis2.grid(linestyle='-')

axis3.plot(xValues, yValues)
axis3.set_xlabel('Horizontal Label3')
axis3.set_ylabel('Vertical Label3')
axis3.grid(linestyle='-')

axis4.plot(xValues, yValues)
axis4.set_xlabel('Horizontal Label4')
axis4.set_ylabel('Vertical Label4')
axis4.grid(linestyle='-')

def _destroyWindow():
    root.quit()
    root.destroy()

root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.update()
root.deiconify()
root.mainloop()
