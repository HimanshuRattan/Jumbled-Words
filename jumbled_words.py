import random

def choose():
    words=['hello', 'computer', 'mathematics', 'python', 'reverse' , 'palindrome']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word, len(word)))
    return jumbled

def play():
    p1name=input("Name of player one:")
    p2name=input("Name of player two:")
    pp1=0
    pp2=0
    turn=0
    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        print(qn)
        #player 1
        if(turn%2==0):
            print(p1name,", Your turn.")
            ans=input("Whats is in my mind?")
            if(ans==picked_word):
                pp1=pp1+1
                print("Your score:" ,pp1)
            else:
                print("Better luck next time. I thought : ",picked_word )
            c=input("Press 1 to continue and 0 to quit")
            z=int(c)
            if z==0:
                print("Player 1's points=", pp1)
                print("Player 2's points=", pp2)
                print("Thank you")
                break
         #player 2
        else:
            print(p2name,", Your turn.")
            ans=input("Whats is in my mind?")
            if(ans==picked_word):
                pp2=pp2+1
                print("Your score:" ,pp2)
            else:
                print("Better luck next time. I thought : ",picked_word )
            c=input("Press 1 to continue and 0 to quit")
            z=int(c)
            if z==0:
                print("Player 1's points=", pp1)
                print("Player 2's points=", pp2)
                print("Thank you")
                break
        turn=turn+1
play()
                