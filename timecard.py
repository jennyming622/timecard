import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import StringVar
from datetime import datetime
win = tk.Tk()
win.wm_title("time card")
win.minsize(width=500,height=500)
win.maxsize(width=500,height=500)
background_image = ImageTk.PhotoImage(Image.open("ttt.jpg"))
background_label = tk.Label(win, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



def event1():
    global label2Str# Label1 的文字 變數
    global history
    x=datetime.now()

    x=str(x)
    print(x)
    name=comboExample1.get()
    history=history+x+comboExample2.get()+name+"\n"
    label2Str.set(history)
    fr = open('all.csv', 'a')
    if comboExample2.get()=="上班":
        fr.write('"' + str(x) + '","'+name+'","V","","",""\n')
    if comboExample2.get()=="下班":
        fr.write('"' + str(x) + '","'+name+'","","V","",""\n')
    if comboExample2.get() == "下休":
        fr.write('"' + str(x) + '","'+name+'","","","V",""\n')
    if comboExample2.get() == "休息結束":
        fr.write('"' + str(x) + '","'+name+'","","","","V"\n')

    fr.close()
history=""
comboExample1 = ttk.Combobox (win,
                            values=[
                                    "李名鈞",
                                    "吳曉明",
                                    "陳大名",
                                    "黃珍珍"])
comboExample1.place(x=0,y=50)
comboExample1.current(1)

comboExample2 = ttk.Combobox (win,
                            values=[
                                    "上班",
                                    "下班",
                                    "下休",
                                    "休息結束"])
comboExample2.place(x=0,y=0)
comboExample2.current(1)


btn1 =tk.Button(win,text="打卡",command=event1)
btn1.place(x=0,y=100)


label2Str=StringVar()
label2=tk.Label(win,text="...",textvariable=label2Str)
label2.place(x=100,y=100)



win.mainloop()
