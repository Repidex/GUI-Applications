from tkinter import*
def callback(n,m):
    global player
    
    if player=="😍" and states[n][m]==0 and stop_game==False:     #We Can also use Hash Value of Emoji
        b[n][m].configure(text='😍',fg='blue',bg='white')
        states[n][m]='😍'
        player='💔' 
        
    if player=="💔" and states[n][m]==0 and stop_game==False:
        b[n][m].configure(text='💔',fg='orange',bg='black')
        states[n][m]='💔'
        player='😍'
    check_for_winner()
    
def check_for_winner():
    global stop_game
    for i in range(3):
        if states[i][0]==states[i][1]==states[i][2]!=0:
            b[i][0].config(bg='gray')
            b[i][1].config(bg='gray')
            b[i][2].config(bg='gray')
            stop_game=True
    for i in range(3):
        if states[0][i]==states[1][i]==states[2][i]!=0:
            b[0][i].config(bg='gray')
            b[1][i].config(bg='gray')
            b[2][i].config(bg='gray')
            stop_game=True 
            
        if states[0][0]==states[1][1]==states[2][2]!=0:
            b[0][1].config(bg='gray')
            b[1][1].config(bg='gray')
            b[2][2].config(bg='gray')
            stop_game=True 
        if states[2][0]==states[1][1]==states[0][2]!=0:
            b[2][0].config(bg='gray')
            b[1][1].config(bg='gray')
            b[0][2].config(bg='gray')
            stop_game=True 
root=Tk()
root.title("TIC TAC TOE ")

b=[[0,0,0,],
   [0,0,0,],
   [0,0,0]]
states=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(3):
    for j in range(3):
        b[i][j]=Button(font=("Arial",60),width=4,bg='powder blue',
                       command=lambda n=i,m=j: callback(n,m))
        b[i][j].grid(row=i,column=j)
player='😍'
stop_game=False
root.mainloop()
        