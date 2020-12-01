import tkinter as tk
from tkinter import*
from tkinter import messagebox

val= ""
A=0
operator =""
def btn_1_isclicked():
    global val
    val=val+"1"
    data.set(val)
def btn_2_isclicked():
    global val
    val=val+"2"
    data.set(val)
def btn_3_isclicked():
    global val
    val=val+"3"
    data.set(val)
def btn_4_isclicked():
    global val
    val=val+"4"
    data.set(val)
def btn_5_isclicked():
    global val
    val=val+"5"
    data.set(val)
def btn_6_isclicked():
    global val
    val=val+"6"
    data.set(val)
def btn_7_isclicked():
    global val
    val=val+"7"
    data.set(val)
def btn_8_isclicked():
    global val
    val=val+"8"
    data.set(val)    
def btn_9_isclicked():
    global val
    val=val+"9"
    data.set(val)  
def btn_10_isclicked():
    global val
    val=val+"0"
    data.set(val)    
def btn_11_isclicked():
    global val
    val=val+"="
    data.set(val)
def btn_12_isclicked():
    global val
    val=val+"-"
    data.set(val)    
def btn_13_isclicked():
    global val
    val=val+"*"
    data.set(val)
def btn_14_isclicked():
    global val
    val=val+"/"
    data.set(val)    
def btn_15_isclicked():
    global val
    val=val+"C"
    data.set(val)
def btn_16_isclicked():
    global val
    val=val+"+"
    data.set(val)

def btn_plus_clicked():
    global A 
    global operator
    global val
    A=int(val)
    operator = "+"
    val=val+"+"
    data.set(val)
    
def btn_minus_clicked():
    global A 
    global operator
    global val
    A=int(val)
    operator = "-"
    val=val+"-"
    data.set(val)

def btn_mul_clicked():
    global A 
    global operator
    global val
    A=int(val)
    operator = "*"
    val=val+"*"
    data.set(val)

def btn_div_clicked():
    global A 
    global operator
    global val
    A=int(val)
    operator ="/"
    val=val+"/"
    data.set(val)
    
def c_clicked():
    global A 
    global operator
    global val
    val=""
    A=0
    operator=""
    data.set(val)

def result():
    global A 
    global operator
    global val
    val2=val
    if operator=="+":
        x=int((val2.split("+")[1]))
        C=A+x
        data.set(C)
        val=str(C)
    elif operator=="-":
        x=int((val2.split("-")[1]))
        C=A-x
        data.set(C)
        val=str(C)
    elif operator=="*":
        x=int((val2.split("*")[1]))
        C=A*x
        data.set(C)
        val=str(C)
    elif operator=="/":
        x=int((val2.split("/")[1]))
        if x==0:
            messagebox.showerror("Error","division By 0 Not Supported")
            A=""
            val=""
            data.set(val)
        else:
            C=int(A/x)
            data.set(C)
            val=str(C)    
win=tk.Tk()
win.title("Adavance Calculator")
win.geometry("400x500")
win.resizable(0,0)

data=StringVar()
lbl1=tk.Label(win,text="Label",anchor=SE,font=("Verdana",20),textvariable=data,bg="#ffffff",fg="#000000")

lbl1.pack(expand=True,fill='both')

def doNothing():
    print("Its okk")
menu=tk.Menu(win)
win.config(menu=menu)
subMenu=Menu(menu)
menu.add_cascade(label='CALCULATOR',menu=subMenu)
subMenu.add_command(label="STANDARD",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit",command=doNothing)

"""editMenu=Menu(menu)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Redo",command=doNothing)"""



btnrow1=tk.Frame(win,bg="#000000")
btnrow1.pack(expand=True,fill='both')

btnrow2=tk.Frame(win)
btnrow2.pack(expand=True,fill='both')

btnrow3=tk.Frame(win,bg="#000000")
btnrow3.pack(expand=True,fill='both')


btnrow4=tk.Frame(win)
btnrow4.pack(expand=True,fill='both')

btn1=tk.Button(
    btnrow1,
    text='7',
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_7_isclicked,
)
btn1.pack(side=LEFT,expand=True,fill='both')

btn2=tk.Button(
    btnrow1,
    text='8',
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_8_isclicked,
)
btn2.pack(side=LEFT,expand=True,fill='both')

btn3=tk.Button(
    btnrow1,
    text='9',
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_9_isclicked,
)
btn3.pack(side=LEFT,expand=True,fill='both')

btn4=tk.Button(
    btnrow1,
    text='*',
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_mul_clicked,
)
btn4.pack(side=LEFT,expand=True,fill='both')

btn5=tk.Button(
    btnrow2,
    text='4',
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_4_isclicked,
)
btn5.pack(side=LEFT,expand=True,fill='both')

btn6=tk.Button(
    btnrow2,
    text='5',
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_5_isclicked,
)
btn6.pack(side=LEFT,expand=True,fill='both')

btn7=tk.Button(
    btnrow2,
    text='6',
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_6_isclicked,
)
btn7.pack(side=LEFT,expand=True,fill='both')

btn8=tk.Button(
    btnrow2,
    text='-',
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_minus_clicked,
)
btn8.pack(side=LEFT,expand=True,fill='both')

btn9=tk.Button(
    btnrow3,
    text='1',
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_1_isclicked,
)
btn9.pack(side=LEFT,expand=True,fill='both')

btn10=tk.Button(
    btnrow3,
    text='2',
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_2_isclicked,
)
btn10.pack(side=LEFT,expand=True,fill='both')

btn11=tk.Button(
    btnrow3,
    text='3',
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_3_isclicked,
)
btn11.pack(side=LEFT,expand=True,fill='both')

btn12=tk.Button(
    btnrow3,
    text='/',
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_div_clicked,
)
btn12.pack(side=LEFT,expand=True,fill='both')

btn13=tk.Button(
    btnrow4,
    text='C',
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=c_clicked,
)
btn13.pack(side=LEFT,expand=True,fill='both')

btn14=tk.Button(
    btnrow4,
    text='0 ',
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_10_isclicked,
)
btn14.pack(side=LEFT,expand=True,fill='both')

btn15=tk.Button(
    btnrow4,
    text='=',
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=result,
)
btn15.pack(side=LEFT,expand=True,fill='both')

btn16=tk.Button(
    btnrow4,
    text='+',
    font=("Verdana",22),
    relief=GROOVE,
    border=0,
    command=btn_plus_clicked,
)
btn16.pack(side=LEFT,expand=True,fill='both')



win.mainloop()