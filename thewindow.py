from tkinter import *
import pyautogui
import time
canvas_width = 500
canvas_height = 150
cor = pyautogui.position()
x= cor[0]-250
y= cor[1]-250


def change(event):
    cor = pyautogui.position()
    x= cor[0]-750
    y= cor[1]-750
    root.geometry("1500x1500+"+str(x)+"+"+str(y)+"")
    
    
root = Tk()
root.attributes('-alpha', 0.01)
root.attributes('-topmost', 1)
root.attributes('-fullscreen',1)

root.geometry("500x500+"+str(x)+"+"+str(y)+"")

root.title("Points")
w = Canvas(root,
           width=canvas_width,
           height=canvas_height)
w.pack(expand=YES, fill=BOTH)
w.configure(bg='#000001')
w.bind("<Motion>",change)



root.update()
root.mainloop()
