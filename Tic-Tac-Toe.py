from tkinter import *
root=Tk()
root.geometry("550x550")
#Title of Window
root.title("Tic Tac Toe")

frame1=Frame(root)
frame1.pack() # to Display frame 1
titleLabel=Label(frame1,text="Tic Tac Toe " ,font=("Arial",30),bg="cyan",width=20)
titleLabel.grid(row=0,column=0)
optionFrame=Frame(root,bg="grey")# This is for Single and Multiple Buttons
optionFrame.pack()

#-------------------------------------------
# Boards of Tic Tac Toe

frame2=Frame(root)
frame2.pack()
board={1:" ",2:" ",3:" ",
       4:" ",5:" ",6:" ",
       7:" ",8:" ",9:" " }
turn="x"
game_stop=False # variable to stop the Game after win or lose or Draw
mode="SinglePlayer" #default Mode

def ChangeModeToSinglePlayer():
   global mode
   mode="SinglePlayer"
   SinglePlayerButton["bg"]="violet" 
   MultiplePlayerButton["bg"]="grey"

   
def ChangeModeToMultiplePlayer():
   global mode
   mode="MultiplePlayer"
   MultiplePlayerButton["bg"]="violet"
   SinglePlayerButton["bg"]="grey" 

   
   

def UpdateBoard():
   #This Function Player vs Computer
   for key in board.keys():
      buttons[key-1]["text"] =board[key]
def CheckForWin(player):
   # Rows 
   if board[1]==board[2] and board[2]==board[3] and board[3]==player: 
      return True
   elif board[4]==board[5] and board[5]==board[6] and board[6]==player:
      return True
   elif board[7]==board[8] and board[8]==board[9] and board[9]==player:
      return True
   # Columns 
   if board[1]==board[4] and board[4]==board[7] and board[7]==player:
      return True
   elif board[2]==board[5] and board[5]==board[8] and board[8]==player:
      return True
   elif board[3]==board[6] and board[6]==board[9] and board[9]==player:
      return True
   # Diagonals 
   if board[1]==board[5] and board[5]==board[9] and board[9]==player:
      return True
   elif board[3]==board[5] and board[5]==board[7] and board[7]==player:
      return True
def CheckForDraw():
   for i in board.keys():
      if board[i]==" ":
         return False
   return True    
     

   

def minimax(board , isMaximizing): #isMaximizing To Know Player Turn or Not
    
    if CheckForWin("o"):
        return 1 
    
    if CheckForWin("x"):
        return -1
    
    if CheckForDraw():
        return 0
    
    if isMaximizing:
        bestScore = -100

        for key in board.keys():
            if board[key] == " ":
                board[key] = "o"
                score = minimax(board , False) # minimax
                board[key] = " "
                if score > bestScore : 
                    bestScore = score 
        
        return bestScore
    
    else:
        bestScore = 100

        for key in board.keys():
            if board[key] == " ":
                board[key] = "x"
                score = minimax(board , True) # minimax
                board[key] = " "
                if score < bestScore : 
                    bestScore = score 
        
        return bestScore
           

def PlayComputer():
    bestScore = -100
    bestMove = 0

    for key in board.keys():
        if board[key] == " ":
            board[key] = "o"
            score = minimax(board , False) # minimax
            board[key] = " "
            if score > bestScore : 
                bestScore = score 
                bestMove = key

    board[bestMove] = "o"


         


def play(event):
    global turn ,game_stop
    
    if game_stop:
       return # Stop
    button=event.widget  # widget --> Draw x or o on Screen
    # without change button Type The Type is class from tkinter
    buttonText=str(button)
    clicked=buttonText[-1] #override
    print(clicked)
    if clicked=="n":
       clicked=1
    else:
       clicked=int(clicked)
      
    if button["text"]==" ":
      if turn=="x":
         board[clicked]=turn
         if CheckForWin(turn):
            winLabel=Label(frame1,text=f"{turn} Wining The Game ",bg="cyan",font=("Arial",25),width=20)
            winLabel.grid(row=0,column=0,columnspan=3)
            game_stop=True
         turn="o"

         UpdateBoard()


         if mode == "SinglePlayer":
            
            
            PlayComputer()
           # This message For Computer When it Wins
            if CheckForWin(turn):
               
               winLabel=Label(frame1,text=f"{turn} Wining The Game ",bg="cyan",font=("Arial",25),width=20)
               winLabel.grid(row=0,column=0,columnspan=3)
               game_stop=True
            turn="x"
            UpdateBoard()



      else:
        button["text"]="O" 
        board[clicked]=turn
        UpdateBoard()

        if CheckForWin(turn):
           winLabel=Label(frame1,text=f"{turn} Wining The Game ",bg="cyan",font=("Arial",25),width=20 )
           winLabel.grid(row=0,column=0,columnspan=3)
           game_stop=True
        turn="x"
  
      if CheckForDraw():
         drawLabel=Label(frame1,text=f"Game Draw ",bg="cyan",font=("Arial",25),width=20 )
         drawLabel.grid(row=0,column=0,columnspan=3) 
         game_stop=True  


# UI 
#Change Mode Options
SinglePlayerButton=Button(optionFrame,text="SinglePlayer",width=13,height=1,font=("Arial",15),bg="grey",borderwidth=2,command=ChangeModeToSinglePlayer,)
SinglePlayerButton.grid(row=0,column=0,columnspan=1,sticky=NW)
MultiplePlayerButton=Button(optionFrame,text="MultiPlayer",width=13,height=1,font=("Arial",15),bg="grey",borderwidth=2,command=ChangeModeToMultiplePlayer)
MultiplePlayerButton.grid(row=0,column=1,columnspan=1,sticky=NW)



#first Row
button1=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),borderwidth=5,bg="silver")
button1.grid(row=0,column=0)
# bind take 2 parameter 1) Tkinter method 2)action such function
button1.bind("<Button>",play) 

button2=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),borderwidth=5,bg="silver")
button2.grid(row=0,column=1)
button2.bind("<Button>",play)

button3=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),borderwidth=5,bg="silver")
button3.grid(row=0,column=2)
button3.bind("<Button>",play)

#second Row
button4=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),borderwidth=5,bg="silver")
button4.grid(row=1,column=0)
button4.bind("<Button>",play)

button5=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),borderwidth=5,bg="silver")
button5.grid(row=1,column=1)
button5.bind("<Button>",play)

button6=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),borderwidth=5,bg="silver")
button6.grid(row=1,column=2)
button6.bind("<Button>",play)


#Third Row
button7=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),borderwidth=5,bg="silver")
button7.grid(row=2,column=0)
button7.bind("<Button>",play)



button8=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),borderwidth=5,bg="silver")
button8.grid(row=2,column=1)
button8.bind("<Button>",play)

button9=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),borderwidth=5,bg="silver")
button9.grid(row=2,column=2)
button9.bind("<Button>",play)






buttons=[button1,button2,button3,button4,button5,button6,button7,button8,button9]



root.mainloop()