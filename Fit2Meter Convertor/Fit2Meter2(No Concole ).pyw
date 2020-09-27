import tkinter as tk
win=tk.Tk()
win.title("Fit2Meter Convertor")
win.geometry("450x300")
win.resizable(width=False,height=False)
win.configure(background='light blue')

def convert():
    value=float(ft_entry.get())
    meter=value*0.3048
    mt_value.set("%.4f" % meter)

def clear():
    ft_value.set("")
    mt_value.set("")


#==================================LABELS=============================
lbl=tk.Label(win,text='Fit 2 Meter Convertor',bd=3,fg='black',bg='orange',font=('arial',16,'bold'))
lbl.grid(row=0,column=1,padx=6,pady=2)

ft_lbl1=tk.Label(win,text='   Fit   ',bd=2,bg='black',fg='red',font=('arial',16,'bold'))
ft_lbl1.grid(row=2,column=0,padx=10,pady=15)

M_lbl2=tk.Label(win,text='Meter ',bd=2,bg='black',fg='red',font=('arial',16,'bold'))
M_lbl2.grid(row=4,column=0,padx=10,pady=15)

#======================Entry Button==============================

ft_value=tk.StringVar()

ft_entry=tk.Entry(win,bd=8,textvariable=ft_value,width=16)
ft_entry.grid(row=2,column=1)
ft_entry.delete(0,'end')

mt_value=tk.DoubleVar()
M_entry=tk.Entry(win,bd=8,textvariable=mt_value,width=16)
M_entry.grid(row=4,column=1)
M_entry.delete(0,'end')

cnvt_btn=tk.Button(win,text='Convert',bd=4,bg='blue',fg='white',width=10,font=('arial','14','bold'),command=convert)
cnvt_btn.grid(row=6,column=0,padx=8,pady=4)

clr_btn=tk.Button(win,text='Clear',bd=4,bg='red',fg='white',width=10,font=('arial','14','bold'),command=clear)
clr_btn.grid(row=6,column=1,padx=8,pady=4)

win.mainloop()  