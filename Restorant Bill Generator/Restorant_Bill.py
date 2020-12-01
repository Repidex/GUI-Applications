from tkinter import*
class Bill_App:
    def __init__(self,win):
        self.win=win
        self.win.geometry("1350x700+0+0")
        self.win.title("Bill Generator")
        title=Label(self.win,text='Bill Generator Softwear',relief=GROOVE,bg='blue',fg='white',bd=10,font=('times new roman',20,'bold'),pady=2).pack(fill=X)

        #==========================Customer Details=================================================
        f1=LabelFrame(self.win,text='Customer Details',bd=10,relief=GROOVE,font=('times new roman',15,'bold'),fg='gold',bg='grey')
        f1.place(x=0,y=80,relwidth=1)
        
        cname_lbl=Label(f1,text='Customer Name',fg='black',bg='grey',font=('times new roman',18,'bold')).grid(row=0,column=0,padx=20,pady=5)
        cname_ent=Entry(f1,width=15,bd=5,relief=SUNKEN,font='arial').grid(row=0,column=1,pady=5,padx=10)
        
        cphn_lbl=Label(f1,text='Phone No.',fg='black',bg='grey',font=('times new roman',18,'bold')).grid(row=0,column=2,padx=20,pady=5)
        cphn_ent=Entry(f1,width=15,bd=5,relief=SUNKEN,font='arial').grid(row=0,column=3,pady=5,padx=10)
        
        cbill_lbl=Label(f1,text='BIll No.',fg='black',bg='grey',font=('times new roman',18,'bold')).grid(row=0,column=4,padx=20,pady=5)
        cbill_ent=Entry(f1,width=15,bd=5,relief=SUNKEN,font='arial').grid(row=0,column=5,pady=5,padx=10)
        
        bill_btn=Button(f1,text='Search',bg='purple',fg='white',width=10,bd=7,font='arial').grid(row=0,column=6,padx=5,pady=10)

        #========================================Cosmetics Frame====================================
        f2=LabelFrame(self.win,bd=10,relief=GROOVE,text='Cosmetics',font=('times new roman',20,'bold'),fg='gold',bg='dark blue')
        f2.place(x=5,y=180,width=325,height=370)
        
        bath_lbl=Label(f2,text='Bath Soap',font=('times new roman',16,'bold'),bg='dark blue',fg='lightgreen').grid(row=0,column=0,padx=10,pady=10,sticky=W)
        bath_ent=Entry(f2,width=10,bd=5,relief=SUNKEN,font='arial').grid(row=0,column=1,pady=5,padx=10)
        
        face_lbl=Label(f2,text='Face Cream',font=('times new roman',16,'bold'),bg='dark blue',fg='lightgreen').grid(row=1,column=0,padx=10,pady=10,sticky=W)
        face_ent=Entry(f2,width=10,bd=5,relief=SUNKEN,font='arial').grid(row=1,column=1,pady=5,padx=10)
        
        Hair_lbl=Label(f2,text='Hair Gell',font=('times new roman',16,'bold'),bg='dark blue',fg='lightgreen').grid(row=2,column=0,padx=10,pady=10,sticky=W)
        Hair_ent=Entry(f2,width=10,bd=5,relief=SUNKEN,font='arial').grid(row=2,column=1,pady=5,padx=10)
        
        loshan_lbl=Label(f2,text='Body Loashan',font=('times new roman',16,'bold'),bg='dark blue',fg='lightgreen').grid(row=3,column=0,padx=10,pady=10,sticky=W)
        bath_ent=Entry(f2,width=10,bd=5,relief=SUNKEN,font='arial').grid(row=3,column=1,pady=5,padx=10)

        faceWash_lbl=Label(f2,text='Face Wash',font=('times new roman',16,'bold'),bg='dark blue',fg='lightgreen').grid(row=4,column=0,padx=10,pady=10,sticky=W)
        faceWash_ent=Entry(f2,width=10,bd=5,relief=SUNKEN,font='arial').grid(row=4,column=1,pady=5,padx=10)
        
        Hspray_lbl=Label(f2,text='Hair Sprey',font=('times new roman',16,'bold'),bg='dark blue',fg='lightgreen').grid(row=5,column=0,padx=10,pady=10,sticky=W)
        bath_ent=Entry(f2,width=10,bd=5,relief=SUNKEN,font='arial').grid(row=5,column=1,pady=5,padx=10)
        
        f3=LabelFrame(self.win,text='Grocery',bd=10,relief=GROOVE,font=('arial',18,'bold'),fg='gold',bg='dark blue')
        f3.place(x=332,y=180,width=325,height=370)
        
        Rice_lbl=Label(f3,text='Rice',font=('times new roman',16,'bold'),bg='dark blue',fg='lightgreen').grid(row=0,column=0,padx=10,pady=10,sticky=W)
        Rice_ent=Entry(f3,width=10,bd=5,relief=SUNKEN,font='arial').grid(row=0,column=1,pady=5,padx=10)
        
        food_lbl=Label(f3,text='Food oil',font=('times new roman',16,'bold'),bg='dark blue',fg='lightgreen').grid(row=1,column=0,padx=10,pady=10,sticky=W)
        food_ent=Entry(f3,width=10,bd=5,relief=SUNKEN,font='arial').grid(row=1,column=1,pady=5,padx=10)
        
        Daal_lbl=Label(f3,text='Daal',font=('times new roman',16,'bold'),bg='dark blue',fg='lightgreen').grid(row=2,column=0,padx=10,pady=10,sticky=W)
        Daal_ent=Entry(f3,width=10,bd=5,relief=SUNKEN,font='arial').grid(row=2,column=1,pady=5,padx=10)
        
        wheat_lbl=Label(f3,text='Wheat',font=('times new roman',16,'bold'),bg='dark blue',fg='lightgreen').grid(row=3,column=0,padx=10,pady=10,sticky=W)
        wheat_ent=Entry(f3,width=10,bd=5,relief=SUNKEN,font='arial').grid(row=3,column=1,pady=5,padx=10)

        sugar_lbl=Label(f3,text='Sugar',font=('times new roman',16,'bold'),bg='dark blue',fg='lightgreen').grid(row=4,column=0,padx=10,pady=10,sticky=W)
        sugar_ent=Entry(f3,width=10,bd=5,relief=SUNKEN,font='arial').grid(row=4,column=1,pady=5,padx=10)
        
        tea_lbl=Label(f3,text='Tea',font=('times new roman',16,'bold'),bg='dark blue',fg='lightgreen').grid(row=5,column=0,padx=10,pady=10,sticky=W)
        tea_ent=Entry(f3,width=10,bd=5,relief=SUNKEN,font='arial').grid(row=5,column=1,pady=5,padx=10)
        
        #=======================================Cold Drink=====================================================
        f4=LabelFrame(self.win,text='Cold Drink',bd=10,relief=GROOVE,font=('arial',18,'bold'),fg='gold',bg='dark blue')
        f4.place(x=659,y=180,width=325,height=370)
        
        Pepsi_lbl=Label(f4,text='Pepsi',font=('times new roman',16,'bold'),bg='dark blue',fg='lightgreen').grid(row=0,column=0,padx=10,pady=10,sticky=W)
        Pepsi_ent=Entry(f4,width=10,bd=5,relief=SUNKEN,font='arial').grid(row=0,column=1,pady=5,padx=10)
        
        Limka_lbl=Label(f4,text='Limka',font=('times new roman',16,'bold'),bg='dark blue',fg='lightgreen').grid(row=1,column=0,padx=10,pady=10,sticky=W)
        Limka_ent=Entry(f4,width=10,bd=5,relief=SUNKEN,font='arial').grid(row=1,column=1,pady=5,padx=10)
        
        Appy_lbl=Label(f4,text='Appy',font=('times new roman',16,'bold'),bg='dark blue',fg='lightgreen').grid(row=2,column=0,padx=10,pady=10,sticky=W)
        Appy_ent=Entry(f4,width=10,bd=5,relief=SUNKEN,font='arial').grid(row=2,column=1,pady=5,padx=10)
        
        Mango_lbl=Label(f4,text='Mango juice',font=('times new roman',16,'bold'),bg='dark blue',fg='lightgreen').grid(row=3,column=0,padx=10,pady=10,sticky=W)
        wheat_ent=Entry(f4,width=10,bd=5,relief=SUNKEN,font='arial').grid(row=3,column=1,pady=5,padx=10)

        Orange_lbl=Label(f4,text='Orange',font=('times new roman',16,'bold'),bg='dark blue',fg='lightgreen').grid(row=4,column=0,padx=10,pady=10,sticky=W)
        Orange_ent=Entry(f4,width=10,bd=5,relief=SUNKEN,font='arial').grid(row=4,column=1,pady=5,padx=10)
        
        Sprite_lbl=Label(f4,text='Sprite',font=('times new roman',16,'bold'),bg='dark blue',fg='lightgreen').grid(row=5,column=0,padx=10,pady=10,sticky=W)
        Sprite_ent=Entry(f4,width=10,bd=5,relief=SUNKEN,font='arial').grid(row=5,column=1,pady=5,padx=10)
        
        #========================================Bill Area=========================================================
        f4=Frame(self.win,bd=10,relief=GROOVE)
        f4.place(x=1010,y=180,width=325,height=370)
        f5=Label(f4,text='Bill Receipt',bd=10,relief=GROOVE,fg='Grey',font=('arial',16,'bold')).pack(fill=X)
        scrol_y=Scrollbar(f4,orient=VERTICAL)
        self.txtarea=Text(f4,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        #==============================ButtonFrame==============================================================
        f6=LabelFrame(self.win,text='Billing Menu',bd=10,relief=GROOVE,font=('arial',18,'bold'),fg='gold',bg='dark blue')
        f6.place(x=0,y=560,relwidth=1,height=140)
        
        b1_lbl=Label(f6,text='Total Cosmetic Price',bg='dark blue',fg='white',font=('arial',14,'bold')).grid(row=0,column=0,padx=20,pady=1,sticky=W)
        b1_txt=Entry(f6,width=18,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        b2_lbl=Label(f6,text='Total Grocery Price',bg='dark blue',fg='white',font=('arial',14,'bold')).grid(row=1,column=0,padx=20,pady=1,sticky=W)
        b2_txt=Entry(f6,width=18,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
        
        b3_lbl=Label(f6,text='Total Cold_Drink Price',bg='dark blue',fg='white',font=('arial',14,'bold')).grid(row=2,column=0,padx=20,pady=1,sticky=W)
        b3_txt=Entry(f6,width=18,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
        
        c1_lbl=Label(f6,text='Cosmetic Tax',bg='dark blue',fg='white',font=('arial',14,'bold')).grid(row=0,column=2,padx=20,pady=1,sticky=W)
        c1_txt=Entry(f6,width=18,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        c2_lbl=Label(f6,text='Grocery Tax',bg='dark blue',fg='white',font=('arial',14,'bold')).grid(row=1,column=2,padx=20,pady=1,sticky=W)
        c2_txt=Entry(f6,width=18,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
        
        c3_lbl=Label(f6,text='Cold_Drink Tax',bg='dark blue',fg='white',font=('arial',14,'bold')).grid(row=2,column=2,padx=20,pady=1,sticky=W)
        c3_txt=Entry(f6,width=18,font='arial 10 bold',bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
        
        btn_frm=Frame(f6,bd=7,relief=SUNKEN)
        btn_frm.place(x=775,width=550,height=100)
        
        total_btn=Button(btn_frm,text='Total',bg='cadetblue',bd=4,fg='black',pady=15,width=8,font='arial 16 bold').grid(row=0,column=0,padx=5,pady=5)
        Gbill_btn1=Button(btn_frm,text='Generate Bill',bg='cadetblue',bd=4,fg='black',pady=15,width=10,font='arial 16 bold').grid(row=0,column=1,padx=5,pady=5)
        clear_btn2=Button(btn_frm,text='Clear',bg='cadetblue',bd=4,fg='black',pady=15,width=8,font='arial 16 bold').grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_frm,text='Exit',bg='cadetblue',bd=4,fg='black',pady=15,width=8,font='arial 16 bold').grid(row=0,column=3,padx=5,pady=5)
        
 
win=Tk() 
obj=Bill_App(win)       
win.mainloop()