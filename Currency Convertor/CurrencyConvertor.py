from tkinter import *    #Imported Whole Module
class CurrencyConvertor():
    def __init__(self):
        win = Tk()
        win.title("Curency Convertor")
        win.config(bg='yellow')
        
        # Adding label widgets to application window
        Label(win, font='Arial 12 bold', bg = 'yellow',text = 'Amount to convert').grid(row=1, column=1, sticky=W)
        Label(win, font='Arial 12 bold', bg = 'yellow',text = 'Amount to convert').grid(row=2, column=1, sticky=W)
        Label(win, font='Arial 12 bold', bg = 'yellow',text = 'Amount to convert').grid(row=3, column=1, sticky=W)

        #Create objects and add entry functions
        self.AmountToConvertVar = StringVar()
        Entry(win, textvariable=self.AmountToConvertVar, justify = RIGHT).grid(row=1, column=2)
        self.ConvertionRateVar = StringVar()
        Entry(win, textvariable=self.ConvertionRateVar, justify = RIGHT).grid(row=2, column=2)
        self.ConvertetAmountVar = StringVar()  
        lblConvertedAmout = Label(win, font="arial 12 bold",textvariable=self.ConvertetAmountVar).grid(row=3, column=2,sticky=E)
        
        #Create convert and clear button
        Convertbtn = Button(win,text="Convert",font="arial 12 bold",bg='blue',fg='white',command=self.ConvertedRate).grid(row=4,column=2,sticky=E)
        Clrbtn = Button(win,text="Clear",font="arial 12 bold",bg='blue',fg='white',command=self.ClearAll).grid(row=4,column=6,padx=25,pady=25,sticky=E)
        win.mainloop()

    def ConvertedRate(self):
        amt = float(self.ConvertionRateVar.get())
        convertedAmountVar = float(self.AmountToConvertVar.get()) * amt
        self.ConvertetAmountVar.set(format(convertedAmountVar,'10.2f'))
    
    def ClearAll(self):
        self.AmountToConvertVar.set("")
        self.ConvertionRateVar.set("")
        self.ConvertetAmount.set("")

CurrencyConvertor()

        
        