#Matplotlib_labels_two_charts_not_scaled.py

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

#그림판을 그린다. 
fig = Figure(figsize=(12,5), facecolor='white')

axis = fig.add_subplot(111) #1열, 1컬럼 

#데이터를 셋팅 
xValues = [1,2,3,4]

yValues0 = [6,7.5,8,7.5]
yValues1 = [5.5,6.5,50,6]  #1개의 매우 높은 값(50)
yValues2 = [6.5,7,8,7]
#새로 추가
yAll = [yValues0, yValues1, yValues2]
#리스트에서 최소값 가져오기
minY = min([y for yValues in yAll for y in yValues])

yUpperLimit = 20
#리스트의 리스트에서 한계값이 있는 최대값 가져오기
maxY = max([y for yValues in yAll for y in yValues if y < yUpperLimit])

#동적인 제한 
axis.set_ylim(minY, maxY)
axis.set_xlim(min(xValues), max(xValues))

t0, = axis.plot(xValues, yValues0)
t1, = axis.plot(xValues, yValues1)
t2, = axis.plot(xValues, yValues2)


axis.set_ylabel('Vertical Label')
axis.set_xlabel('Horizontal Label')
axis.grid()

fig.legend((t0,t1,t2), ('First line', 'Second line', 'Third line'), 'upper light')

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
