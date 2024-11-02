import random
lst=[str(i) for i in range(100,0,-1)]
p_1="[P1]"
p_2="[P2]"
displacment1=0
displacment2=0
Laders={1:38,4:14,8:30,28:77,12:42,50:67,71:92,89:98}
Snakes={36:6,32:10,62:18,88:24,48:26,95:56,97:78}
print("|------------------SNAKES AND LADDERS----------------|")
print()
print("LADDERS:")
for i in Laders:
    print(f"  {i} to {Laders[i]}")
print("SNAKES:")
for i in Snakes:
    print(f"  {Snakes[i]} to {i}")
print()

def board():
    print("|-----------------SNAKES AND LADDERS---------------|")
    print()
    count=0
    for i in lst:
        if i in ["1","4","8","12","28","50","71","89"]:
            print("",i+"(L)","|",end="")
            count+=1
        elif i in ["32","36","62","88","48","95","97"]:
            print("",i+"(S)","|",end="")
            count+=1
        elif i in [str(i) for i in range(1,10)]:
            print("",i+"    ","|",end="")
            count+=1
        else:
            print("",i,"   |",end="")
            count+=1
        if count==10:
            print("\n")
            count=0


def startgame(dis1,dis2):
    while True:
        while True:
            input("Player-1 Press The Enter To Roll The Dice >>> ")
            dice1=random.randint(1,6)
            print(f"\nPlayer-1 You Got {dice1} in Dice.")

            if dis1==95:
                if dice1==6:
                    break
            elif dis1==96:
                if dice1 in [5,6]:
                    break
            elif dis1==97:
                if dice1 in [4,5,6]:
                    break
            elif dis1==98:
                if dice1 in [3,4,5,6]:
                    break
            elif dis1==99:
                if dice1!=1:
                    break
            elif dis1==100:
                break

            dis1+=dice1
            if dis1 in [i for i in Laders]:
                for i in Laders:
                    if dis1==i:
                        dis1+=Laders[i]-i
            elif dis1 in [i for i in Snakes]:
                for i in Snakes:
                    if dis1==i:
                        dis1-=i-Snakes[i]
            print("Player-1 position >>>",dis1)
        
            if p_1 in lst:
                index=lst.index(p_1)
                lst[index]=str(100-index)
            elif p_1+","+p_2 in lst:
                index=lst.index(p_1+","+p_2)
                lst[index]=p_2
            
            if lst[100-dis1]==p_2:
                lst[100-dis1]=p_2+","+p_1
            else:
                lst[100-dis1]=p_1

            for i in Laders:
                if dis1==i:
                    lst[100-dis1]=str(100-(lst.index(p_1)))
                    lst[100-Laders[i]]=p_1
                    print("You Reached",i,"And Climbed Ladder to",Laders[i])
            
            for i in Snakes:
                if dis1==i:
                    lst[100-dis1]=str(100-(lst.index(p_1)))
                    lst[100-Laders[i]]=p_1
                    print("You Reached",i,"And The Snake Sent you to",Laders[i])

            board()
            break

        if lst[0]==p_1:
            print("Player-1 Won The Match!")
            break
        elif lst[0]==p_2:
            print("Player-2 Won The Match!")
            break

        while True:
            input("PLayer-2 Press The Enter To Roll The Dice >>> ")
            dice2=random.randint(1,6)
            print(f"\nPlayer-2 You Got {dice2} in Dice.")
            
            if dis2==95:
                if dice2==6:
                    break
            elif dis2==96:
                if dice2 in [5,6]:
                    break
            elif dis2==97:
                if dice2 in [4,5,6]:
                    break
            elif dis2==98:
                if dice2 in [3,4,5,6]:
                    break
            elif dis2==99:
                if dice2!=1:
                    break
            elif dis1==100:
                break

            dis2+=dice2
            if dis2 in [i for i in Laders]:
                for i in Laders:
                    if dis2==i:
                        dis2+=Laders[i]-i
            elif dis2 in [i for i in Snakes]:
                for i in Snakes:
                    if dis2==i:
                        dis2-=i-Snakes[i]
            print("Player-2 position >>>",dis2)

            if p_2 in lst:
                index=lst.index(p_2)
                lst[index]=str(100-index)
            elif p_2+","+p_1 in lst:
                index=lst.index(p_2+","+p_1)
                lst[index]=p_1

            if lst[100-dis2]==p_1:
                lst[100-dis2]=p_1+","+p_2
            else:
                lst[100-dis2]=p_2

            for i in Laders:
                if dis2==i:
                    lst[100-dis2]=str(100-(lst.index(p_2)))
                    lst[100-Laders[i]]=p_2
                    print("You Reached",i,"And Climbed Ladder to",Laders[i])

            for i in Snakes:
                if dis2==i:
                    lst[100-dis2]=str(100-(lst.index(p_2)))
                    lst[100-Laders[i]]=p_2
                    print("You Reached",i,"And The Snake Sent you to",Laders[i])

            board()
            break

        if lst[0]==p_1:
            print("Player-1 Won The Match!")
            break
        elif lst[0]==p_2:
            print("Player-2 Won The Match!")
            break

startgame(displacment1,displacment2)
