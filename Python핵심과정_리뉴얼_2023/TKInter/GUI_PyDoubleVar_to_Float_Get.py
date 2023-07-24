import tkinter as tk 

#GUI_PyDoubleVar_to_Float_Get.py

win = tk.Tk()

#DoubleVar생성하기
doubleData = tk.DoubleVar()
print(doubleData.get())
doubleData.set(2.4)
print(type(doubleData))

add_doubles = 1.22222222222222 + doubleData.get()
print(add_doubles)
print(type(add_doubles))