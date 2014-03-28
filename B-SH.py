#-*-coding: UTF-8-*-
import random
#03.set variables
draw=False
width_min=2
width_max=5
letters=""
digits=""
for i in range(65,91):
    letters+=chr(i)
for i in range(48,58):
    digits+=chr(i)
name_error=True



#017. takes all digits in str and stacks them.
def str_to_int(a):
    str_to_int_output=""
    for i in range(len(a)):
        for b in range(10):
            if a[i]==str(b):
                str_to_int_output+=a[i]
    return int(str_to_int_output)
#25. Random name for bship
def ship_id_gen():
    id=random.choice(letters)
    id+=random.choice(letters)
    id+="-"
    id+=random.choice(digits)
    return id
#32.welcoming
print
print "Let's play Battleship!"
print
#36.players list, empty
player=["AI"]
maxscore_owner=0
#39.set players name 
for i in range(2):
    name=str(raw_input("Enter name for Player "+str(i+1)+":"))
    if len(name)==0:
        name="Player "+str(i+1)
    player.append(name)
    print
    print "Welcome "+name+"!!!"
    print
#48.field as list of lists, empty
board = []
#50.set width for field and fill it 
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
#74.amount of ships
ships_number=0
for i in range(width-(width_min+1)):
    ships_number+=width*width/3+random.randint(1,6)
if width==2:
    ships_number=1
if width==3:
    ships_number=random.randint(1,3)
print "There are "+str(ships_number)+" ships in the field!"
ships_dead=ships_number
#84. filling ships names list
ships_id={0:"STEALTH"}
ships_unnamed=ships_number
name=ship_id_gen()
while ships_unnamed!=0:
    for i in range(ships_number):
        for x in range(len(ships_id)):
            while name_error==True:
                name_error=False
                if name==ships_id[i]:
                    name=ship_id_gen()
                    name_error=True
                for y in range(len(ships_id)):
                    if name==ships_id[y]:
                        name=ship_id_gen()
                        name_error=True
            name_error=True
        ships_id[i+1]=name
        ships_unnamed-=1
#103. ships placement
ships_xy={0:"everywhere"}
ships_unplaced=ships_number
name=random.choice(digits[1:width+1])+random.choice(digits[1:width+1])
while ships_unplaced!=0:
    for i in range(ships_number):
        for x in range(len(ships_xy)):
            while name_error==True:
                name_error=False
                if name==ships_xy[i]:
                    name=random.choice(digits[1:width+1])+random.choice(digits[1:width+1])
                    name_error=True
                for y in range(len(ships_xy)):
                    if name==ships_xy[y]:
                        name=random.choice(digits[1:width+1])+random.choice(digits[1:width+1])
                        name_error=True
            name_error=True
        ships_xy[i+1]=name
        ships_unplaced-=1
#122. goal, maximum score and scores list, empty
scores=[0,0,0]
maxscore=0
winscore=int(ships_number/2+1)
print "Player with "+str(winscore)+" scores wins the game!"
print
#128.#first player to play by roll
currentplayer=random.randint(1,2)
print "Game starts with "+player[currentplayer]+"!"
print
raw_input("Press ENTER to start!")
for i in range(15):
    print
#135. set turn
turn=1
#137.Top and Bottom lines with digits
width_column_text_top="/ "
width_column_text_bot="\ "
for i in range(width):
    width_column_text_top+=str(i+1)+" "
    width_column_text_bot+=str(i+1)+" "
width_column_text_top+="\ "
width_column_text_bot+="/ "
#129.f for field and field lines display with space symbol between elements
def print_board(board):
    print
    print width_column_text_top
    for i in range(width):
        print str(i+1)+" "+" ".join(board[i])+" "+str(i+1)
    print width_column_text_bot
    print
#153.game
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
        print "You sunk the battleship "+"X"+"!"
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
#202. Victory and draw text
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
