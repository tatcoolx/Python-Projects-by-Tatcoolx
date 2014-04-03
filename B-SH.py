#-*-coding: UTF-8-*-
import random,string
#03.set variables
exit=False
draw=False
stat=False
width_min=2
width_max=9
letters=""
digits=""
for i in range(65,91):
    letters+=chr(i)
for i in range(48,58):
    digits+=chr(i)
name_error=True
bot_lag=[0,0,0]
bot_hack=[0,0,0]
shot_out=[0,0,0]
shot_miss=[0,0,0]
shot_dead=[0,0,0]
shot_kill=[0,0,0]
#019. takes all digits in str and stacks them.
def str_to_int(a):
    if len(str(a))==0:
        print "error, in str_to_int, length=0"
    else:
        if type(a)==int:
            return a
        if type(a)==str:
            str_to_int_output=""
            for i in range(len(str(a))):
                for b in range(10):
                    if a[i]==str(b):
                        str_to_int_output+=a[i]
            if len(str(str_to_int_output))==0:
                str_to_int_output=0
            return int(str_to_int_output)
#31. bot name generators and lists
bot_id_pre=["SUPER","SIMPLE","EXTRA","BONUS","EASY","ONE","LONELY","SWEET"]
bot_id_suf=["CODE","STRING","VIRUS","BRAIN","SCRIPT","GAME"]
bot_id_dig=[""," 007"," 0101011"," 333"," 777"," 666"," 999"," 2000"," 1488"," 3000"," 9999"]
def bot_id_gen():
    id=bot_id_pre[random.randint(0,len(bot_id_pre)-1)]
    id+=bot_id_suf[random.randint(0,len(bot_id_suf)-1)]
    id+=bot_id_dig[random.randint(0,len(bot_id_dig)-1)]
    return id
bot_id_pre2=["SUPER","SIMPLE","EXTRA","BONUS","EASY","ONE","LONELY","SWEET","ULTRA","BRUTAL","GREEN"]
bot_id_suf2=["CODE","STRING","VIRUS","BRAIN","SCRIPT","GAME","DOMINATOR","LORD","TERMINAL","WIN32.Trojan"]
bot_id_dig2=["","","","",""," 007"," 0101011"," 333"," 777"," 666"," 999"," 2000"," 1488"," 3000"," 9999"," XXX"," QWERTY"," WASD"]
def bot_id_gen2():
    id=bot_id_pre2[random.randint(0,len(bot_id_pre2)-1)]
    id+=bot_id_suf2[random.randint(0,len(bot_id_suf2)-1)]
    id+=bot_id_dig2[random.randint(0,len(bot_id_dig2)-1)]
    return id
#31. Random name for bship
def ship_id_gen():
    id=random.choice(letters)
    id+=random.choice(letters)
    id+="-"
    id+=random.choice(digits)
    return id
#38. statistic
def statistic():
    print
    print ("*"*18)+"!STATISTIC!"+("*"*18)
    print
    print "Field width is "+str(width)+"x"+str(width)+"."
    print "There are "+str(ships_number)+" ships in the field!"
    print "Player with "+str(winscore)+" scores wins the game!"
    print
    print "Name:"+(" "*18)+player_st[1]+"  "+player_st[2]
    print "Total Shots:           "+str(turn/2+1)+(" "*(17-len(str(turn/2+1))))+str(turn/2)+(" "*(15-len(str(turn/2))))
    print "Missed Shots:          "+str(shot_miss[1])+(" "*(17-len(str(shot_miss[1]))))+str(shot_miss[2])+(" "*(15-len(str(shot_miss[2]))))
    print "Outside of ocean:      "+str(shot_out[1])+(" "*(17-len(str(shot_out[1]))))+str(shot_out[2])+(" "*(15-len(str(shot_out[2]))))
    print "Corpse shots:          "+str(shot_dead[1])+(" "*(17-len(str(shot_dead[1]))))+str(shot_dead[2])+(" "*(15-len(str(shot_dead[2]))))
    print "Battleships destroyed: "+str(shot_kill[1])+(" "*(17-len(str(shot_kill[1]))))+str(shot_kill[2])+(" "*(15-len(str(shot_kill[2]))))
    print "Scores:                "+str(scores[1])+(" "*(17-len(str(scores[1]))))+str(scores[2])+(" "*(15-len(str(scores[2]))))
    print
    raw_input("Press ENTERT to continue...")
    new_screen()
#50. print a lot of empty strings
def new_screen():
    for i in range(50):
        print
#54. welcoming
new_screen()
raw_input("Let's play Battleship!")
new_screen()
#58. players lists, empty
player=["REMBO"]
player_st=["REMBO"]
player_bot=[False,False,False]
maxscore_owner=0
#62. set players name 
for i in range(2):
    print "Enter the name for Player "+str(i+1)+"."
    print "(max 15 char, or type\"bot\" for A.I. control)"
    name=str(raw_input(""))
    if string.lower(name)=="bot":
        name=bot_id_gen()
        player_bot[i+1]=True
        bot_lag[i+1]=6
        bot_hack[i+1]=3
    if string.lower(name)=="ultrabot":
        name=bot_id_gen2()
        player_bot[i+1]=True
        bot_lag[i+1]=3
        bot_hack[i+1]=11
    if len(name)==0:
        name="Player "+str(i+1)
    elif len(name)>15:
        name=name[:15]
    player.append(name)
    player_st.append(name)
    new_screen()
    raw_input("Welcome "+name+"!!!")
    new_screen()
for i in range(1,3):
    for x in range (15-len(player_st[i])):
        player_st[i]+=" "
#77. field as list of lists, empty
board = []
#79. set width for field and fill it 
width=str(raw_input("Enter field width("+str(width_min)+"-"+str(width_max)+"):"))
if width=="444" or width=="777":
    if width=="444":
        player=["AI","BST","JIRO"]
    if width=="777":
        player=["AI","JIRO","BST"]
    new_screen()
    for i in range(1,3):
        print "Welcome "+str(player[i])+"!"
    print
    width=str(raw_input("Enter field width("+str(width_min)+"-"+str(width_max)+"):"))
if len(width)==0:
    width=random.randint(width_min,width_max)
else:
    width=str_to_int(width)
    if width>=width_max:
        width=width_max
        raw_input("Width reseted to "+str(width))
    elif width<=width_min:
        width=width_min
        raw_input("Width reseted to "+str(width))
new_screen()
raw_input("Field width is "+str(width)+"x"+str(width)+".")
for x in range(width):
    board.append(["#"] * width)
#102. amount of ships
ships_number=((width*width/3)+random.randint(1,6))
if width==2:
    ships_number=1
if width==3:
    ships_number=random.randint(1,3)
raw_input("There are "+str(ships_number)+" ships in the field!")
ships_dead=ships_number
#110. filling ships names list
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
#129. ships placement
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
#148. ships statuses list
ships_status={0:"INVICTIBLE"}
for i in range(ships_number):
    ships_status[i+1]="alive"
#152. coordinates status list
coor_status={}
for i in range(width):
    for x in range(width):
                coor_status[str(i+1)+str(x+1)]="empty"
for i in ships_xy:
    if i>0:
        coor_status[ships_xy[i]]="alive"+str(i)
#160. goal, maximum score and scores list, empty
scores=[0,0,0]
maxscore=0
winscore=int(ships_number/2+1)
raw_input("Player with "+str(winscore)+" scores wins the game!")
new_screen()
#166.#first player to play by roll
currentplayer=random.randint(1,2)
print "Game starts with "+player[currentplayer]+"!"
print
raw_input("Press ENTER to start!")
new_screen()
#172. set turn
turn=1
#17\. place ships in the field
for i in range(ships_number):
    print
#177.Top and Bottom lines with digits
width_column_text_top="/ "
width_column_text_bot="\ "
for i in range(width):
    width_column_text_top+=str(i+1)+" "
    width_column_text_bot+=str(i+1)+" "
width_column_text_top+="\ "
width_column_text_bot+="/ "
#185.f for field and field lines display with space symbol between elements
def print_board(board):
    print
    print width_column_text_top
    for i in range(width):
        print str(i+1)+" "+" ".join(board[i])+" "+str(i+1)
    print width_column_text_bot
    print
#193.game
while winscore>maxscore:
    if turn>1:
        new_screen()
    print ("*"*40)
    print
    raw_input("Turn "+str(turn)+" by "+str(player[currentplayer])+".")
    while True:
        print_board(board)
        if player_bot[currentplayer]==False:
            print "Select row and column. You can also type:"
            print "\"exit\" to end the game"
            print "\"stat\" to view statistic"
            print
            stat=False
            guess_row=raw_input("Guess Row:")
            if string.lower(str(guess_row))=="exit":
                exit=True
                break
            if string.lower(str(guess_row))=="stat":
                new_screen()
                statistic()
                stat=True
            if len(str(guess_row))==0:
                guess_row=random.randint(1,width)-1
                raw_input("Randomly selected "+str(guess_row+1)+".")
            else:
                if guess_row=="0":
                    guess_row=-1
                else:
                    guess_row=str_to_int(guess_row)-1
            if stat==False:
                print
                guess_col=raw_input("Guess Col:")
                if string.lower(str(guess_col))=="exit":
                    exit=True
                    break
                if string.lower(str(guess_col))=="stat":
                    new_screen()
                    statistic()
                if len(str(guess_col))==0:
                    guess_col=random.randint(1,width)-1
                    raw_input("Randomly selected "+str(guess_col+1)+".")
                    print
                else:
                    if guess_col=="0":
                        guess_coll=-1
                    else:
                        guess_col=str_to_int(guess_col)-1
        else:
            raw_input(player[currentplayer]+" is thinking....")
            guess_row=random.randint(1,width)-1
            guess_col=random.randint(1,width)-1
            if random.randint(0,100)<=bot_lag[currentplayer]:
                guess_row+=random.randint(-22,22)
                raw_input(player[currentplayer]+" laging....")
            if random.randint(0,100)<=bot_lag[currentplayer]:
                guess_row+=random.randint(-22,22)
                raw_input(player[currentplayer]+" laging....")
            if random.randint(0,100)<=bot_hack[currentplayer]:
                for i in range(ships_number):
                    if ships_status[i]=="alive":
                        bot_ship_pick=i
                        break
                guess_row=int(ships_xy[i][0])-1
                guess_col=int(ships_xy[i][1])-1
                raw_input(player[currentplayer]+" uses Wi-Fi to hack the NASA satelite....")            
        if stat==False:
            break
    if exit==True:
        break
    new_screen()
    print "Shot to "+str(guess_row+1)+"-"+str(guess_col+1)+"."
    if (guess_row < 0 or guess_row > width-1) or (guess_col < 0 or guess_col > width-1):
        print_board(board)
        raw_input("Oops, that's not even in the ocean.")
        shot_out[currentplayer]+=1
    elif board[guess_row][guess_col] == "X":
        print_board(board)
        coor_status[str(guess_row+1)+str(guess_col+1)]="X"+str(int(coor_status[str(guess_row+1)+str(guess_col+1)][1:])+1)
        raw_input("Guessed that one already. Times shooted: "+coor_status[str(guess_row+1)+str(guess_col+1)][1:]+".")
        shot_miss[currentplayer]+=1
    elif coor_status[str(guess_row+1)+str(guess_col+1)][:4]=="dead":
        coor_status[str(guess_row+1)+str(guess_col+1)]="X"+str(int(coor_status[str(guess_row+1)+str(guess_col+1)][4:])+1)
        raw_input("Destroyed that one already. Times shooted: "+coor_status[str(guess_row+1)+str(guess_col+1)][4:]+".")
        shot_dead[currentplayer]+=1
    elif coor_status[str(guess_row+1)+str(guess_col+1)][:5]=="alive":
        board[guess_row][guess_col] = "$"
        print_board(board)
        print player[currentplayer]+" sunk the battleship "+ships_id[int(coor_status[str(guess_row+1)+str(guess_col+1)][5:])]+"!"
        scores[currentplayer]+=1
        ships_status[int(coor_status[str(guess_row+1)+str(guess_col+1)][5:])]="dead"
        coor_status[str(guess_row+1)+str(guess_col+1)]="dead1"
        raw_input(str(player[currentplayer])+" got +1 score.")
        shot_kill[currentplayer]+=1
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
        coor_status[str(guess_row+1)+str(guess_col+1)]="X1"
        print_board(board)
        raw_input(player[currentplayer]+" missed.")
        shot_miss[currentplayer]+=1
    print
    for i in range(1,3):
        print str(player_st[i])+": "+str(scores[i])+" scores."
    if currentplayer==1:
        currentplayer=2
    else:
        currentplayer=1
    turn+=1
    print 
    raw_input("Press ENTERT to continue...")
    print ("*"*40)
#272. Exit or Victory + draw text
new_screen()
if exit==False:
    if draw==True:
        raw_input("Not BAD and not GOOD but DRAW!!!")
    else:
        print ("*"*15)+"!CONGRATULATIONS!"+("*"*15)
        print
        print str(player[maxscore_owner])+" has won!!!!"
        print
        raw_input(str(player[3-maxscore_owner])+" is FUCKING LOSER!!!!!!1111")
        statistic()
    new_screen()
print "Made by Tatcoolx with the great help of Jirotakeo!"
print ("*"*10)+" Thanks for playing! Goodbye! "+("*"*1 )
