#-*-coding: UTF-8-*-
import random,string
#03.set variables
draw=False
width_min=2
width_max=5
#07. takes all digits in str and stacks them.
def str_to_int(a):
    str_to_int_output=""
    for i in range(len(a)):
        for b in range(10):
            if a[i]==str(b):
                str_to_int_output+=a[i]
    return int(str_to_int_output)
#16. Random name for bship
def ship_id_gen(b=string.ascii_uppercase,c=string.digits):
    id=random.choice(b)
    id+=random.choice(b)
    id+="-"
    id+=random.choice(c)
    return id
for i in range(10):
    print ship_id_gen()
#14.welcoming
print
print "Let's play Battleship!"
print
#18.players list, empty
player=["AI"]
maxscore_owner=0
#21.set players name 
for i in range(2):
    name=str(raw_input("Enter name for Player "+str(i+1)+":"))
    if len(name)==0:
        name="Player "+str(i+1)
    player.append(name)
    print
    print "Welcome "+name+"!!!"
    print
#30.field as list of lists, empty
board = []
#32.set width for field and fill it 
width=str(raw_input("Enter field width("+str(width_min)+"-"+str(width_max)+"):"))
if width=="444" or width=="777":
    if width=="444":
        player=["AI","BST","JIRO"]
    if width=="777":
        player=["AI","JIRO","BST"]
    for i in range(1,3):
        print "Welcome "+str(player[i])+"!"
    print
    width=str(raw_input("Enter field width("+str(width_min)+"-"+str(width_max)+"):"))
for i in range(15):
    print
if len(width)==0:
    width=random.randint(width_min,width_max)
else:
    width=str_to_int(width)
    if width>=width_max:
        width=width_max
    elif width<=width_min:
        width=width_min
print "Field width is "+str(width)+"x"+str(width)+"."
for x in range(width):
    board.append(["#"] * width)
#56.Top and Bottom lines with digits
width_column_text_top="/ "
width_column_text_bot="\ "
for i in range(width):
    width_column_text_top+=str(i+1)+" "
    width_column_text_bot+=str(i+1)+" "
width_column_text_top+="\ "
width_column_text_bot+="/ "
#64.f for field and field lines display with space symbol between elements
def print_board(board):
    print
    print width_column_text_top
    for i in range(width):
        print str(i+1)+" "+" ".join(board[i])+" "+str(i+1)
    print width_column_text_bot
    print
#72.amount of ships
ships_number=0
for i in range(0,width-(width_min+2)):
    ships_number+=random.randint(3,5)
if width==2:
    ships_number=1
if width==3:
    ships_number=random.randint(1,3)
print "There are "+str(ships_number)+" ships in the field!"
ships_dead=ships_number
#83.filling ships lists
ships_id={0:"STEALTH"}
for i in range(ships_number):
    ships_id[i+1]=[str(i+1)]
#86.goal, maximum score and scores list, empty
scores=[0,0,0]
maxscore=0
winscore=int(ships_number/2+1)
print "Player with "+str(winscore)+" scores wins the game!"
print
#92.#first player to play by roll
currentplayer=random.randint(1,2)
print "Game starts with "+player[currentplayer]+"!"
print
raw_input("Press ENTER to start!")
for i in range(15):
    print
#99. set f for ships placement
def random_row(board):
    return random.randint(0, len(board) - 1)
def random_col(board):
    return random.randint(0, len(board[0]) - 1)
#104. set turn
turn=1
#106. place ships in the field
for i in range(ships_number):
    print
ship_row = random_row(board)
ship_col = random_col(board)
#111.game
while winscore>maxscore:
    if turn>1:
        for i in range(20):
            print
    print ("*"*40)
    print
    raw_input("Turn "+str(turn)+" by "+str(player[currentplayer])+", press ENTER.")
    print_board(board)
    guess_row = int(raw_input("Guess Row:"))-1
    guess_col = int(raw_input("Guess Col:"))-1
    for i in range(15):
        print
    if (guess_row < 0 or guess_row > width-1) or (guess_col < 0 or guess_col > width-1):
        print_board(board)
        raw_input("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
        print_board(board)
        raw_input("You guessed that one already.")
    elif guess_row == ship_row and guess_col == ship_col:
        board[guess_row][guess_col] = "$"
        print_board(board)
        print "You sunk the battleship!"
        scores[currentplayer]+=1
        raw_input(str(player[currentplayer])+" got +1 score.")
        ships_dead-=1
        if maxscore<scores[currentplayer]:
            maxscore=scores[currentplayer]
            maxscore_owner=currentplayer
        if winscore<=maxscore:
            break
        if ships_dead==0:
            draw=True
            break
    else:
        board[guess_row][guess_col] = "X"
        print_board(board)
        raw_input("You missed")
    print
    for i in range(1,3):
        print str(player[i])+": "+str(scores[i])+" scores"
    if currentplayer==1:
        currentplayer=2
    else:
        currentplayer=1
    turn+=1
    print 
    raw_input("Press ENTERT to continue...")
    print ("*"*40)
#160. Victory and draw text
for i in range(20):
    print
if draw==True:
    raw_input("Not BAD and not GOOD but DRAW!!!")
else:
    print ("*"*15)+"!CONGRATULATIONS!"+("*"*15)
    print
    print str(player[maxscore_owner])+" has won!!!!"
    print
    raw_input(str(player[3-maxscore_owner])+" is FUCKING LOSER!!!!!!1111")



import string,random
def ship_id_gen(b=string.ascii_uppercase,c=string.digits):
    id=random.choice(b)
    id+=random.choice(b)
    id+="-"
    id+=random.choice(c)
    return id


ships_id={0:"STEALTH"}
name=""
for i in range(12):
    while name==ships_id[i] and len(name)==0:
        name+=random.choice("123")
        name+=random.choice("123")
        print str(i)+" has same name "+str(name)
    ships_id[i+1]=name
print ships_id
