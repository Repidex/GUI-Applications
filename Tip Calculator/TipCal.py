from tkinter import Tk,Radiobutton,Button,Label,StringVar,IntVar,Entry
class TipCalculator():
    def __init__(self):
        win=Tk()
        win.title("Tip Calculator")
        win.configure(background="sky blue")
        win.geometry("500x350")
        win.resizable(width=False,height=False)
        
        
        self.meal_cost=StringVar()
        self.tip_percent=IntVar()
        self.tip=StringVar()
        self.total_cost=StringVar()
        
        tip_percent=Label(win,text="Tip Percents",bg="black",fg='red',font=('Arial',16,'bold'))
        tip_percent.grid(column=0,row=1,padx=15)
        
        bill_amount=Label(win,text="Bill Amount",bg="black",fg="red",font=('arial',16,'bold'))
        bill_amount.grid(column=1,row=1,padx=15)
        
        bill_amount_entry=Entry(win,textvariable=self.meal_cost,width=14,bd=4)
        bill_amount_entry.grid(column=2,row=1,padx=15)
        
        #=====================radiobutton=================================
        five_percent_tip=Radiobutton(win,text="0.5%",variable=self.tip_percent,width=14,value=5)
        five_percent_tip.grid(column=0,row=3)
        
        ten_percent_tip=Radiobutton(win,text="10%",variable=self.tip_percent,width=14,value=10)
        ten_percent_tip.grid(column=0,row=4)
        
        fifteen_percent_tip=Radiobutton(win,text="15%",variable=self.tip_percent,width=14,value=15)
        fifteen_percent_tip.grid(column=0,row=5)
        
        twenty_percent_tip=Radiobutton(win,text="20%",variable=self.tip_percent,width=14,value=20)
        twenty_percent_tip.grid(column=0,row=6)
        
        twentyFive_percent_tip=Radiobutton(win,text="25%",variable=self.tip_percent,width=14,value=25)
        twentyFive_percent_tip.grid(column=0,row=7)
        
        tip_amount_lbl=Label(win,text="Tip Amount",bg="brown",fg='white',font=('arial',12,'bold'))
        tip_amount_lbl.grid(column=1,row=4,padx=10)
        tip_amount_entry=Entry(win,textvariable=self.tip,width=14,bd=4)
        tip_amount_entry.grid(column=2,row=4)
        
        bill_total_lbl=Label(win,text="Bill Total",bg="brown",fg='white',font=('arial',12,'bold'))
        bill_total_lbl.grid(column=1,row=6,padx=10)
        bill_total_entry=Entry(win,textvariable=self.total_cost,width=14,bd=4)
        bill_total_entry.grid(column=2,row=6)
        
        calculation_btn=Button(win,text='Calculate',bg='green',bd=4,font=('arial',16,'bold'),fg='white',command=self.calculate)
        calculation_btn.grid(column=1,row=9,padx=15)
        
        clr_btn=Button(win,text=' Clear ',bg='green',bd=4,font=('arial',14,'bold'),fg='white',command=self.clear)
        clr_btn.grid(column=2,row=9,padx=15)
        
        win.mainloop()

    
    def calculate(self):
        pre_tip = float(self.meal_cost.get())
        percentage = self.tip_percent.get() / 100
        tip_amount_entry = pre_tip * percentage
        self.tip.set(tip_amount_entry)
        
        final_bill = pre_tip  + tip_amount_entry
        self.total_cost.set(final_bill)   
    
    def clear(self):
        self.total_cost.set("")
        self.meal_cost.set("")
        self.tip.set("")             
        
        
        
TipCalculator()