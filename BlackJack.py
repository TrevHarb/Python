# Trevor Harbin
# 1/12 Start Date
# Attempt at BlackJack with GUI

import tkinter
import random

dsuit=['Spade', 'Club', 'Heart', 'Diamond']
dcolor=['Black','Red']
dface =['A','K','Q','J','10','9','8','7','6','5','4','3','2','1']
dvalue=[10,9,8,7,6,5,4,3,2,1]
hand=[]
ucards=[]
dcards=[]
dhand=[]
deck=[]
dealertext='Dealer Value: 00'
usertext='User Value: 00'
bj=21
balance=1000
balancetext="Balance: "
bettext="Bet: "



def alterbal(val, inc=True):
    temp=balance
    if inc:
        temp+=val
    else:
        temp-=val
    return temp

def shuffledeck():
    for i in range(0,6):
        random.shuffle(deck)
    half=deck[:int(len(deck)/2)]
    deck[:int(len(deck)/2)]=deck[int(len(deck)/2):]
    deck[int(len(deck)/2):]=half
    

def createdeck():
    for s in range(1,3):
        for i in range(0,13):
            for l in range(0,4):
                deck.append(Card(l,i))
    

def resetdeck():
    if len(deck)>1:
        deck.clear()
    createdeck()
    shuffledeck()


def showtopcard():
    card = deck.pop(0)
    print(card)
    print(len(deck))
    if len(deck)<1:
        print('Low Deck')

class Card:
    def __init__(self,suit,face):
        self.suit = dsuit[suit]
        if suit > 1:
            self.color = dcolor[1]
        else:
            self.color = dcolor[0]
        self.face = dface[face]
        if face < 5 and face>0:
            self.value = dvalue[0]
        elif face==0:
            self.value=11
        else:
            self.value = dvalue[face-4]
    def __str__(self):
        return f"{self.suit}({self.face})"

resetdeck()

for i in deck:
    print(i)
print('----------------------------------')
##Cards are created and shuffled into a random order.

def hit(dealer=False):
    if dealer:
        dcards.append(tkinter.Button(fdealer, text=dcard(),height=height, width=width))
        dcards[len(dcards)-1].pack(side=tkinter.LEFT)
    else:
        ucards.append(tkinter.Button(fhand, text=ucard(),height=height, width=width))
        ucards[len(ucards)-1].pack(side=tkinter.LEFT)

def dcard():
    dhand.append(deck[0])
    return showtopcard()
def ucard():
    hand.append(deck[0])
    return showtopcard()

def showtopcard():
    card = deck.pop(0)
    print(card)
    print(len(deck))
    if len(deck)<1:
        print('Low Deck - Reloading...')
        resetdeck()
    checkval()
    return card

def checkval():
    dealerval()
    userval()

def dealerval():
    smol=0
    aces=False
    for i in dhand:
        if i.value==11:
            aces = True
        smol+=i.value
    if aces and smol > bj:
        for i in dhand:
            if i.value==11 and aces:
                i.value = 1
                aces=False
    if len(str(smol))<2:
        vd.config(text=dealertext[:len(dealertext)-2]+'0'+str(smol))
    else:
        vd.config(text=dealertext[:len(dealertext)-2]+str(smol))
    
def endgame():
    endwindow = tkinter.Toplevel(bg, bg='LightBlue')
    endwindow.geometry('300x300')
    tkinter.Label(endwindow, text='You have run out of Money!\n\nThanks for Playing!', bg='LightBlue').pack(pady=50)
    tkinter.Button(endwindow, text='Keep Playing', command=lambda: keepplaying()).pack(pady=50)
    endwindow.protocol("WM_DELETE_WINDOW",lambda: bg.destroy())
    
    def keepplaying():
        endwindow.destroy()
        global balance
        balance=1000
        finbalance=balancetext+str(balance)
        bal.config(text=finbalance)
        resetdeck()
        resetgame()

def userval():
    aces=False
    larg=0
    for i in hand:
        if i.value==11:
            aces = True
        larg+=i.value
    if aces and larg > bj:
        for i in hand:
            if i.value==11 and aces:
                i.value=1
                aces=False
                larg-=10
    if larg>bj:
        win(1, str(larg))
    elif len(str(larg))<2:
        vu.config(text=usertext[:len(usertext)-2]+'0'+str(larg))
    else:
        vu.config(text=usertext[:len(usertext)-2]+str(larg))


def resetgame():
    print('---------------------------------')
    nh.pack_forget()
    h.pack(side=tkinter.LEFT, padx=20,pady=50)
    s.pack(side=tkinter.LEFT, padx=20,pady=50)
    hand.clear()
    dhand.clear()
    for i in dcards:
        i.destroy()
    for i in ucards:
        i.destroy()
    dcards.clear()
    ucards.clear()
    if len(deck)<60:
        resetdeck()
    waitforbet()
    # Hand and dhand does not clear when reset game is called - Card is still drawn after game is reset, Not sure why, Value does not reset
#
#   1 - Player Bust 
#   2 - Dealer Bust
#   3 - Tie
#   4 - Player has better Hand
#   5 - Dealer Has better hand
#   Add thise^^^
def win(who, val):
    s.pack_forget()
    h.pack_forget()
    global balance
    match who:
        case 1:
            vu.config(text='You Busted! Value = '+val)
            finbalance=balancetext+str(balance)
            bal.config(text=finbalance)
        case 2:
            vd.config(text='Dealer Loses! You win! Value = '+val)
            balance=alterbal((2*(bet.get())))
            finbalance=balancetext+str(balance)
            bal.config(text=finbalance)
        case 3:
            vu.config(text='Draw!! Value = '+val)
            vd.config(text='Draw!! Value = '+val)
            balance=alterbal(bet.get())
            finbalance=balancetext+str(balance)
            bal.config(text=finbalance)
        case 4:
            vu.config(text='You had a better hand, You Win! Value = '+val)
            balance=alterbal((2*(bet.get())))
            finbalance=balancetext+str(balance)
            bal.config(text=finbalance)
        case 5:
            vd.config(text='Dealer has a better hand! Value = '+val)
            finbalance=balancetext+str(balance)
            bal.config(text=finbalance)
    
    if balance < 1:
        endgame()
    else:
        nh.pack(side=tkinter.LEFT, padx=20,pady=50)
    


def dealcards():
    if len(ucards)>0:
        ucards[0].destroy()
    hit()
    hit(True)
    hit()
    dcards.append(tkinter.Button(fdealer, text="Dealer 2", height=height, width=width))
    dcards[len(dcards)-1].pack(side=tkinter.LEFT)


def dealersturn():
    dcards[3].destroy()
    sma=0
    while sma<17:
        sma=0
        hit(True)
        for i in dhand:
            sma+=i.value
        
    tes=0
    for i in hand:
        tes+=i.value
    
    if sma>21:    
        win(2, str(sma))
    elif tes==sma:
        win(3, str(sma))
    elif tes>sma:
        win(4,str(tes))
    else:
        win(5,str(sma))


finbalance=balancetext+str(balance)

#Balance is not recognized as a variable, Not sure why, I keep defining it. 
def setbet():
    fslider.pack_forget()
    global balance
    balance=alterbal(bet.get(), False)
    print(balancetext+str(balance))
    print(bettext+str(bet.get()))
    finbet=bettext+str(bet.get())
    finbalance=balancetext+str(balance)
    bal.config(text=finbalance)
    lbet.config(text=finbet)
    for i in dcards:
        i.destroy()
    for i in ucards:
        i.destroy()
    dealcards()
    checkval()
    h.pack(side=tkinter.LEFT, padx=20,pady=50)
    s.pack(side=tkinter.LEFT, padx=20,pady=50)

def waitforbet():
    dcards.append(tkinter.Button(fdealer, text="Dealer 1", height=height, width=width))
    dcards.append(tkinter.Button(fdealer, text="Dealer 2", height=height, width=width))
    ucards.append(tkinter.Button(fhand, text="User 1", height=height, width=width))
    ucards.append(tkinter.Button(fhand, text="User 2", height=height, width=width))
    better.config(to=balance)
    better.set(20)
    better.pack()
    finbalance=balancetext+str(balance)
    bal.config(text=finbalance)
    fslider.pack(side='right')
    lbet.config(text=bettext)
    vu.config(text='Place a Bet to Play!')
    vd.config(text='Place a Bet to Play!')
    h.pack_forget()
    s.pack_forget()
    for i in dcards:
        i.pack(side=tkinter.LEFT)
    for i in ucards:
        i.pack(side=tkinter.LEFT)


bettext="Bet: "


height, width = 13, 10

bg = tkinter.Tk()
bg.winfo_toplevel().title("BlackJack")
bg.geometry("460x650")
bg.configure(background='LightGreen')

bet=tkinter.IntVar()


m1=tkinter.PanedWindow(bg, orient='vertical', bg='LightGreen')
m1.pack(side='left',padx=50)
fdealer = tkinter.Frame(m1)
fhand = tkinter.Frame(m1)
foptions = tkinter.Frame(m1)
fbet=tkinter.Frame(bg)
dealervalue=tkinter.Frame(m1)
uservalue=tkinter.Frame(m1)
ftext=tkinter.Frame(fbet)
fslider=tkinter.Frame(fbet)



#Need to create a new frame for the label text and include bet and Balance, have seperate text then combine before updating

better=tkinter.Scale(fslider, tickinterval=100, from_=0, to=balance,orient='vertical', label='Bet Amount',length=200, variable=bet)
finbet=bettext+str(bet.get())


bal = tkinter.Label(ftext, text=finbalance, width=width)
lbet = tkinter.Label(ftext, text=bettext, width=width)


pb=tkinter.Button(fslider, text='Place Bet', command=setbet)
vd=tkinter.Label(dealervalue, bd=2, text=dealertext)
vu=tkinter.Label(uservalue, bd=1, text=usertext)
dealervalue.pack()
fdealer.config(bg='LightGreen',pady=15)
fhand.config(bg='LightGreen',pady=15)
fdealer.pack()
uservalue.pack()
fhand.pack()
foptions.config(bg='LightGreen' ,height=100)
foptions.pack()
ftext.config(bg="LightGreen")
fslider.config(bg="LightGreen")
ftext.pack()
fslider.pack()

fbet.config(height=500,bg='LightGreen')
fbet.pack(side='right')



vd.pack(side=tkinter.TOP)
vu.pack(side=tkinter.TOP)
nh = tkinter.Button(foptions, text="Next Hand", command=resetgame, background='Orange')
h = tkinter.Button(foptions, text="Hit",command=hit, background='Pink')
s = tkinter.Button(foptions, text='Stand',command=dealersturn, background='LightBlue')
bal.pack(padx=20,pady=50)
lbet.pack(padx=20)
better.pack( padx=20,pady=50)
pb.pack(padx=20,pady=50)


waitforbet()



bg.mainloop()





















