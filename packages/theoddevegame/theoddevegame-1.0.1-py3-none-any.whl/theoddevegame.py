#below are the pics of the finger gesture for the game
ODDEVE_PICS = ["""
           .-.
           | |
           | |
           | |
    _.-.-.-| | 
   ; \\( \\    |
   |\\_)\\ \\   | 
   |    ) \\  |
   |   (    / 
    \\______/ """, """
       .-.
       | |    / )
       | |   / /
       | |  / /
    _.-| |_/ / 
   ; \\( \\    |
   |\\_)\\ \\   | 
   |    ) \\  |
   |   (    / 
    \\______/ """, """
      _.-.
    _| | | 
   | | | | 
   | | | | _ 
   | i ' i\\_|
   |      (_ |
   |      _| |
   |     ;   | 
   |        /
    \\______/ """, """
   .-.-.-.-.
   | | | | |
   | | | | |    
   | | | | |
   | | | | |
   |  ( \\  \\
   |   \\ \\  | 
   |    ) \\ |
   |   (   / 
    \\_____/ """, """
      _.-._
    _| | | |
   | | | | |
   | | | | |  __
   | i ' i | / /
   |       |/ /
   |       ' /
   |      ;  | 
   |        /
    \\______/ """, """
    _
   ( (
    \\=\\ 
   __\\_`-\\
  (____))( \\---
  (____)) _
   (____))
    (__))___/--- """
]

import random,time
##randomise the way whose chance will come first. The TOSS!!!
def chance():
    print("Here is the toss. Let's go!!!\n")
    time.sleep(1)      
    a=random.randint(0,1)
    if a==0:
        print("I won the toss.")
        return True
    else:
        print("You have won the toss")
        return False

#define the SuperOver
def SuperOver(h=1):
    ipo=input("\nDo you first bat or bowl")
    if ipo.lower().startswith("bat"):
        x=utscore()
        w=mtscore()
        if w>x:
            print("I win")
        else:
            print("you win")
    else:
        w=mtscore()
        x=utscore()
        if w>x:
            print("I win")
        else:
            print("you win")

#define userscore in SuperOver
def utscore(h=1):
    n=6 #number of balls
    run=0
    while n>0:
        print("your turn")
        a=validnum(1)#check if input is valid
        a=int(a)
        print("Now my turn. ")
        b=random.randint(1,6)#computer chance
        pic(a,"your")
        pic(b,"my")
        if a==b:#player dont get out, and runs also dont get count.
            run+=0
        else:
            run+=a
        n-=1
    print("your score is",run)
    return run

#define computer score in Super over
def mtscore(h=1):        
    n=6
    runs=0
    while n>0:
        print("my turn")
        b=random.randint(1,6)
        print("Now your turn")
        a=validnum(1)
        a=int(a)
        pic(a, "your")
        pic(b, "my")
        if a==b:
            runs+=0
        else:
            runs+=b
        n-=1
    print("my score is",runs)
    return runs

        
def iscompchance(odd,eve):#if comp won the toss
    c=random.randint(0,1)
    if c==0:
        print("I will take", eve)
        return 1 
    else:
        print("I will take", odd)
        return 0

def isplayerchance(odd, eve, o, e):#if player won toss
    print(odd,"or",eve)
    b=input()
    if b.lower().startswith(o):
        return 0
    elif b.lower().startswith(e):
        return 1
    else:
        return isplayerchance(odd, eve, o, e)

def pic(e, my):#print the pics corresponding to the runs
    print(my,"number is",e,end=" ")
    print(ODDEVE_PICS[e-1])

def validnum(h):
    while True:
        print("Enter your number, between 1 to 6 : ")
        guess = input()
        if len(guess) != 1:
            print('Please enter a single number.')
        elif guess not in '123456':
            print('Please enter a valid number.')
        else:
            return guess
def gamelogic(d, point):#the main gamelogic which runs the game.
    if d:
        print("my chance.")#comp. bat first
        time.sleep(1)
        e=random.randint(1,6)
        print("I have played my chance, Your turn.")
        f=validnum(1)
        f=int(f)
        pic(e, "my")
        pic(f, "your")
        if e==f:#its, out and the chasing starts
            n=point+1
            pointa=0
            print("Oh, I got out, you need", n, "runs to win")
            print("your batting")
            while pointa<n:#while runs are less than required runs keep going
                time.sleep(1)
                h=validnum(1)
                h=int(h)
                
                print("You have played your chance, my turn.")
                i=random.randint(1,6)
                pic(i, "my")
                pic(h, "your")
                if h==i:#batsman out before winning
                    if point==pointa:#same point superover starts
                        SuperOver()
                        break
                    elif point>pointa:
                        print("Oh, you lost by", point-pointa, "runs. Better luck next time.")
                        break
                else:
                    pointa+=h
                    print("Now you need",n-pointa,"runs")
                    print("your score is", pointa)
                print("you will win, because you are a champ.")
                
        else:
            point+=e
            print("my score is", point)
            gamelogic(d, point)
            return point
    else:
        print("your chance.")
        time.sleep(1)
        e=validnum(1)
        e=int(e)
        
        print("You have played your chance, my turn.")
        f=random.randint(1,6)
        pic(e, "your")
        pic(f, "my")
        if f==e:
            n=point+1
            pointa=0
            print("Oh, you got out, I need", n, "runs to win")
            print("my batting")
            while pointa<n:
                time.sleep(1)
                i=random.randint(1,6)
                print("I have played my chance, your turn.")
                h=validnum(1)
                h=int(h)
                pic(i, "my")
                pic(h, "your")
                if h==i:
                    if point==pointa:
                        SuperOver()
                        break
                    else:
                        print("Oh, I lost by", point-pointa, "runs. Congratulation on winning.")
                        break
                else:
                    pointa+=i
                    print("Now I need",n-pointa,"runs")
                    print("my score is", pointa)
                print("I will win, because i am a winner.")

        else:
            point+=e
            print("your score is", point)
            gamelogic(d, point)
            return point

def rules():#rules of the game
    print("""Hello there everyone this is the game of odd/eve or odd/evens what you say.
But wait here is the twist it is a odd/eve cricket game or digitised version of hand cricket.\n
This docstring is here to announce the rules for the game.
  Toss: unlike typical coin toss, in this game the toss is randmised by the program itself \
but it will let you know whose turn is first.\
If you won the toss you have the option to bat or bowl. if program won the toss,\
it will let you know.\n
  Bat: Anyone who decides to bat first will have the chance to create a huge score like in cricket.\
You have to throw the numbers until the player got out.\n
  Bowl: if chosen to bowl the player to try to get out the other player by throwing same number.\n
  Out: If both players throw the same number, the player who is batting get out and the other player \
has to chase.\n
  Chase: player to bat in 2nd turn has to make 1 run more than other player who bat first.\
if he fails to do so player who bat first won, else who bats second win.\n
  Super Over: If both player got out in same runs, there will be 6 more balls which decide who won \
in the tiebraker.\n
  Runs: Player who is batting, his number thrown will be added till he got out.

""")

def game():
    #below is the preview image of the game.
    print("""
          __      __  __        __    ___  __       __   __   __       __         __
    |  | |   |   |   |  | |\\/| |       |  |  |     |  | |  \\ |  \\   / |   \\    / |
    |  | |-- |   |   |  | |  | |--     |  |  |     |  | |  | |  |  /  |--  \\  /  |--
    |/\\| |__ |__ |__ |__| |  | |__     |  |__|     |__| |__; |__; /   |__   \\/   |__
    """)
    v=input("Want to know about rules, if yes press y, else press any key to continue.\n")
    if v.lower().startswith("y"):
        rules()
    while True:#game starts.
        point=0
        d=chance()
        if d:
            j=iscompchance("odd", "eve")
            k=iscompchance("bowling", "batting")
            gamelogic(k, point)
        else:
            j=isplayerchance("odd","eve","o","e")
            k=isplayerchance("batting","bowling","bat","bowl")
            gamelogic(k, point)

        q=input("To quit press q else press enter key: ")
        if q.lower().startswith("q"):
            break

game()
