Board=[i for i in range(1,10)]
def displayboard():
    print("|",Board[0],"|",Board[1],"|",Board[2],"|")
    print("|",Board[3],"|",Board[4],"|",Board[5],"|")
    print("|",Board[6],"|",Board[7],"|",Board[8],"|")

player_1=""
player_2=""
icon=input("Enter player I's icon >>> ")
if icon=="X":
    player_1="X"
    player_2="O"
elif icon=="O":
    player_1="O"
    player_2="X"
print("Player I:",player_1)
print("Player II:",player_2)

def check_conditions(player):
    conditions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[2,4,6],[0,4,8]]
    for i in conditions:
        if Board[i[0]]==player and Board[i[1]]==player and Board[i[2]]==player :
            return 1

    else:
        return 0

def Startgame():
    displayboard()
    while True:
        while True:

            player_option=input(f'{player_1} ,Enter yours choice [1 to 9]:')

            if player_option not in [str(i) for i in range(1,10)]:
                print("PLease Enter a Number 1 to 9 ")
                continue

            if Board[int(player_option)-1] in [i for i in range(1,10)]:
                Board[int(player_option)-1]= player_1
                displayboard()
                if check_conditions(player_1):
                    return f'PLAYER 1 ({player_1}) WON THE MATCH'
                break

            else:
                print("This place was already occupied PLease enter Empty slot number")

        if len([j for j in Board if j in [i for i in range(1,10)]])==0:
            return "Match is TIE play again"

        while True:

            player_option=input(f'{player_2} ,Enter yours choice [1 to 9]:')

            if player_option not in [str(i) for i in range(1,10)]:
                print("PLease Enter a Number 1 to 9 ")
                continue

            if Board[int(player_option)-1] in [i for i in range(1,10)]:
                Board[int(player_option)-1]= player_2
                displayboard()
                if check_conditions(player_2):
                    return f'PLAYER 2 ({player_2}) WON THE MATCH'
                break

            else:
                print("This place was already occupied PLease enter Empty slot number")

print(Startgame())
alist=["YES","Yes","yes"]
while True:

    p_a=input("Do you want play again,Enter yes or no:")

    if p_a in alist:
        Board=[i for i in range(1,10)]
        print(Startgame())

    else:
        print("Thanks for play,BYE!")
        exit()