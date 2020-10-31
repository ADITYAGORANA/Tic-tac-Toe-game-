from tkinter import *
from tkinter import messagebox


root = Tk()
root.config(bg='black')

LblTitle = Label(font=('arial',30,'bold'), text='Tic Tac Toe',bd=20,fg='white',bg='black',justify=CENTER,width=18).pack(fill=X,side=TOP)
#upperFrame=Frame(root, bg='red', pady=0, width=456, height=100, relief=RIDGE).pack(side=TOP)

UpperFrame=Frame(root, bg='blue', pady=0, width=456, height=100, relief=RIDGE)
UpperFrame.pack(side=TOP)
MiddleFrame=Frame(root, bg='grey', pady=0, width=456, height=500,bd=20, relief=RIDGE)
MiddleFrame.pack(side=TOP)
LowerFrame=Frame(root, bg='black', pady=0, width=456, height=130, relief=RIDGE)
LowerFrame.pack(side=TOP)

#Declaration of the variables
PlayerX = IntVar()
PlayerO = IntVar()
click=True
count=0

def Reset():
    global count
    count=0
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    b1 = Button(MiddleFrame, text=" ", font=('arial', 30, 'bold'), height=2, width=6, bg='white',command=lambda: b_click(b1))
    b1.grid(row=0, column=0, sticky=S + N + E + W)

    b2 = Button(MiddleFrame, text=" ", font=('arial', 30, 'bold'), height=2, width=6, bg='white',command=lambda: b_click(b2))
    b2.grid(row=0, column=1, sticky=S + N + E + W)

    b3 = Button(MiddleFrame, text=" ", font=('arial', 30, 'bold'), height=2, width=6, bg='white',command=lambda: b_click(b3))
    b3.grid(row=0, column=2, sticky=S + N + E + W)

    b4 = Button(MiddleFrame, text=" ", font=('arial', 30, 'bold'), height=2, width=6, bg='white',command=lambda: b_click(b4))
    b4.grid(row=1, column=0, sticky=S + N + E + W)

    b5 = Button(MiddleFrame, text=" ", font=('arial', 30, 'bold'), height=2, width=6, bg='white',command=lambda: b_click(b5))
    b5.grid(row=1, column=1, sticky=S + N + E + W)

    b6 = Button(MiddleFrame, text=" ", font=('arial', 30, 'bold'), height=2, width=6, bg='white',command=lambda: b_click(b6))
    b6.grid(row=1, column=2, sticky=S + N + E + W)

    b7 = Button(MiddleFrame, text=" ", font=('arial', 30, 'bold'), height=2, width=6, bg='white',command=lambda: b_click(b7))
    b7.grid(row=2, column=0, sticky=S + N + E + W)

    b8 = Button(MiddleFrame, text=" ", font=('arial', 30, 'bold'), height=2, width=6, bg='white',command=lambda: b_click(b8))
    b8.grid(row=2, column=1, sticky=S + N + E + W)

    b9 = Button(MiddleFrame, text=" ", font=('arial', 30, 'bold'), height=2, width=6, bg='white',command=lambda: b_click(b9))
    b9.grid(row=2, column=2, sticky=S + N + E + W)
#Disable function
def Disable():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
# Funtion to check if won
def Cheker():
    global winner,PlayerX,PlayerO
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    winner=False
    if b1['text']=="X" and b2['text']=="X" and b3['text']=="X":
        b1.config(bg="#90ff0a")
        b2.config(bg="#90ff0a")
        b3.config(bg="#90ff0a")
        winner=True
        Disable()
        PlayerX.set(int(PlayerX.get()) + 1)
        messagebox.showinfo("Tic Tac Toe",Xname.get() + " Won!!")
    elif b4['text']=="X" and b5['text']=="X" and b6['text']=="X":
        b4.config(bg="#90ff0a")
        b5.config(bg="#90ff0a")
        b6.config(bg="#90ff0a")
        winner=True
        Disable()
        PlayerX.set(int(PlayerX.get()) + 1)
        messagebox.showinfo("Tic Tac Toe",Xname.get() + " Won!!")
    elif b7['text']=="X" and b8['text']=="X" and b9['text']=="X":
        b7.config(bg="#90ff0a")
        b8.config(bg="#90ff0a")
        b9.config(bg="#90ff0a")
        winner=True
        Disable()
        PlayerX.set(int(PlayerX.get()) + 1)
        messagebox.showinfo("Tic Tac Toe",Xname.get() + " Won!!")
    elif b1['text']=="X" and b4['text']=="X" and b7['text']=="X":
        b1.config(bg="#90ff0a")
        b4.config(bg="#90ff0a")
        b7.config(bg="#90ff0a")
        winner=True
        Disable()
        PlayerX.set(int(PlayerX.get()) + 1)
        messagebox.showinfo("Tic Tac Toe",Xname.get() + " Won!!")
    elif b8['text']=="X" and b2['text']=="X" and b5['text']=="X":
        b8.config(bg="#90ff0a")
        b2.config(bg="#90ff0a")
        b5.config(bg="#90ff0a")
        winner=True
        Disable()
        PlayerX.set(int(PlayerX.get()) + 1)
        messagebox.showinfo("Tic Tac Toe", Xname.get() + " Won!!")
    elif b9['text']=="X" and b6['text']=="X" and b3['text']=="X":
        b9.config(bg="#90ff0a")
        b6.config(bg="#90ff0a")
        b3.config(bg="#90ff0a")
        winner=True
        Disable()
        PlayerX.set(int(PlayerX.get()) + 1)
        messagebox.showinfo("Tic Tac Toe", Xname.get() + " Won!!")
    elif b1['text']=="X" and b5['text']=="X" and b9['text']=="X":
        b1.config(bg="#90ff0a")
        b5.config(bg="#90ff0a")
        b9.config(bg="#90ff0a")
        winner=True
        Disable()
        PlayerX.set(int(PlayerX.get()) + 1)
        messagebox.showinfo("Tic Tac Toe", Xname.get() + " Won!!")
    elif b7['text']=="X" and b5['text']=="X" and b3['text']=="X":
        b7.config(bg="#90ff0a")
        b5.config(bg="#90ff0a")
        b3.config(bg="#90ff0a")
        winner=True
        Disable()
        PlayerX.set(int(PlayerX.get()) + 1)
        messagebox.showinfo("Tic Tac Toe", Xname.get() + " Won!!")
    elif b1['text']=="O" and b2['text']=="O" and b3['text']=="O":
        b1.config(bg="#90ff0a")
        b2.config(bg="#90ff0a")
        b3.config(bg="#90ff0a")
        winner=True
        Disable()
        PlayerO.set(int(PlayerO.get()) + 1)
        messagebox.showinfo("Tic Tac Toe", Oname.get() + " Won!!")
    elif b4['text']=="O" and b5['text']=="O" and b6['text']=="O":
        b4.config(bg="#90ff0a")
        b5.config(bg="#90ff0a")
        b6.config(bg="#90ff0a")
        winner=True
        Disable()
        PlayerO.set(int(PlayerO.get()) + 1)
        messagebox.showinfo("Tic Tac Toe", Oname.get() + " Won!!")
    elif b7['text']=="O" and b8['text']=="O" and b9['text']=="O":
        b7.config(bg="#90ff0a")
        b8.config(bg="#90ff0a")
        b9.config(bg="#90ff0a")
        winner=True
        Disable()
        PlayerO.set(int(PlayerO.get()) + 1)
        messagebox.showinfo("Tic Tac Toe", Oname.get() + " Won!!")
    elif b1['text']=="O" and b4['text']=="O" and b7['text']=="O":
        b1.config(bg="#90ff0a")
        b4.config(bg="#90ff0a")
        b7.config(bg="#90ff0a")
        winner=True
        Disable()
        PlayerO.set(int(PlayerO.get()) + 1)
        messagebox.showinfo("Tic Tac Toe", Oname.get() + " Won!!")
    elif b8['text']=="O" and b2['text']=="O" and b5['text']=="O":
        b8.config(bg="#90ff0a")
        b2.config(bg="#90ff0a")
        b5.config(bg="#90ff0a")
        winner=True
        Disable()
        PlayerO.set(int(PlayerO.get()) + 1)
        messagebox.showinfo("Tic Tac Toe", Oname.get() + " Won!!")
    elif b9['text']=="O" and b6['text']=="O" and b3['text']=="O":
        b9.config(bg="#90ff0a")
        b6.config(bg="#90ff0a")
        b3.config(bg="#90ff0a")
        winner=True
        Disable()
        PlayerO.set(int(PlayerO.get()) + 1)
        messagebox.showinfo("Tic Tac Toe", Oname.get() + " Won!!")
    elif b1['text']=="O" and b5['text']=="O" and b9['text']=="O":
        b1.config(bg="#90ff0a")
        b5.config(bg="#90ff0a")
        b9.config(bg="#90ff0a")
        winner=True
        Disable()
        PlayerO.set(int(PlayerO.get()) + 1)
        messagebox.showinfo("Tic Tac Toe", Oname.get() + " Won")
    elif b7['text']=="O" and b5['text']=="O" and b3['text']=="O":
        b7.config(bg="#90ff0a")
        b5.config(bg="#90ff0a")
        b3.config(bg="#90ff0a")
        winner=True
        Disable()
        PlayerO.set(int(PlayerO.get()) + 1)
        messagebox.showinfo("Tic Tac Toe", Oname.get() + " Won!!")
    elif winner==False and count==9:
        messagebox.showinfo("Tic Tac Toe", "Its a tie")
        Disable()
# Function to choose the click
def b_click(b):
    global click,count
    if b['text'] == " " and click == True and count<9:
        b['text'] = "X"
        click = False
        count += 1
        Cheker()
    elif b['text'] == " " and click == False and count<9:
        b['text'] = "O"
        click = True
        count += 1
        Cheker()
    else:
        messagebox.showerror("Tic Tac Toe", "Invalid Input")
#New Game function
def New_Game():
    global Xname,Oname,PlayerX,PlayerO
    PlayerX.set(0)
    PlayerO.set(0)
    Xname= StringVar()
    Oname= StringVar()
    Click = True
    Reset()

    nameO = Entry(UpperFrame, font=('arial', 30), fg='grey', bd=3, textvariable=Oname, width=12)
    nameX = Entry(UpperFrame, font=('arial', 30), fg='grey', bd=3, textvariable=Xname, width=12)
    ScoreO = Label(UpperFrame, font=('arial', 30), fg='grey', bd=5, textvariable=PlayerO, width=4, justify=CENTER)
    ScoreX = Label(UpperFrame, font=('arial', 30), fg='grey', bd=5, textvariable=PlayerX, width=4, justify=CENTER)
    PlyrO = Label(UpperFrame, font=('arial', 30), fg='grey', bd=5, text='O', width=5, justify=CENTER)
    PlyrX = Label(UpperFrame, font=('arial', 30), fg='grey', bd=5, text='X', width=5, justify=CENTER)
    nameO.grid(row=1, column=0, sticky=W + E + S + N)
    nameX.grid(row=0, column=0, sticky=W + E + S + N)
    ScoreO.grid(row=1, column=2, sticky=W + E + S + N)
    ScoreX.grid(row=0, column=2, sticky=W + E + S + N)
    PlyrO.grid(row=1, column=1, sticky=W + E + S + N)
    PlyrX.grid(row=0, column=1, sticky=W + E + S + N)

New_Game()


Resetbtn = Button(LowerFrame, text="Reset", font=('arial', 31),bd=3, width=10, bg='white',command=Reset).grid(row=0,column=0,sticky=W)
Newgamebtn= Button(LowerFrame, text="New Game", font=('arial', 31),bd=3, width=10, bg='white',command=New_Game).grid(row=0,column=1,sticky=E)


root.mainloop()

