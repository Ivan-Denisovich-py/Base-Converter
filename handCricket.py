# Hand Cricket Game
# Author: Ivan Denisovich
# Acknowledgements: Manganazzo the Mango, The Coconut Tree and of course all of it's leaves


import random
#Definitions
#________________________________________________________

def bat():
    out=0
    score=0
    while out!=3:
        try:
            batt=int(input("Choose a number between 1-6:\n"))
            ball=random.randint(1,6)
            if batt<1 or batt>6:
                print('No Cheating')
                continue
            if ball==batt:
                out+=1
                if out==3:
                    print('ALL OUT! Your final score:',score)
                    return score
                else:
                    print ('OUT! Current score:',score,':',out)
            else:
                score+=batt
                print('Your score is',score)
                continue
        except ValueError:
            print('Invalid input! Please enter a valid input.')
            continue


def bowl():
    out=0
    score=0
    while out!=3:
        batt=random.randint(1,6)
        try:
            ball=int(input("Choose a number between 1-6 to bowl:\n"))
            if ball>6 or ball<1:
                print('BETWEEN 1 TO 6!')
                continue
            if batt==ball:
                out+=1
                if out==3:
                    print("All out! Computer's score:",score)
                    return score
                else:
                    print('OUT!',out,'wicket',end='')
                    if out>1:
                        print(' ',end='')
                    else:
                        print('s ',end='')
                    print('taken.',3-out,"to go!\nComputer's score:",score,':',out)
            else:
                score+=batt
                print('Computer chose',batt)
                print("Computer's score:",score)
        except ValueError:
            print('Invalid input! Please enter a valid input.')
            continue

#Match
#-------------------------------------------------------------------------
print ('Welcome to Hand Cricket Game.')
while True:
    print ('Please enter h/t, where h and t denotes Heads or Tails, respectively:')
    call=input()
    if call=='h':
        call=0
        break
    elif call=='t':
        call=1
        break
    else:
        print('Please choose between h or t.')
        continue
outcome=random.randint(0,1)
print ('Toss result:')
if outcome==0:
    print ('h')
elif outcome==1:
    print ('t')
    
# User wins the toss 
print()
if outcome==call:
    print("You've won the toss.")
    while True:
        print('Would you like to bat first?')
        dec=input('Enter yes or no:')

   
# A)   User chose to bat    
    
        if dec=='yes':
            print('Alright. You chose to bat. Let the game begin!\nPress Enter to start.')
            input()
            yourScore=int(bat())
            print('Now computer starts to bat. Get ready to start bowling.\nPress ENTER to start.')
            input()
            cScore=int(bowl())
            break
        
# B) User chose to bowl 
        
        elif dec=='no':
            print('Alright. You chose to bowl. Let the game begin!\nPress Enter to start.')
            input()
            cScore=int(bowl())
            target=cScore+1
            print("Now it's time for you to bat.n\Your target:",target,"\nComputer\nPress ENTER to start.")
            input()
            yourScore=int(bat())
            break
        else:
            print("Please enter either 'yes' or 'no'.")
            continue

# C) Computer wins the toss
        
elif outcome!=call:
    print("You've lost the toss.")
    cCall=random.randint(0,1)
    if cCall==0:
        
# C.1) Computer chose to bat
        print('Computer chose to bat. Get ready to bowl.\nPress ENTER to start the game.')
        input()
        cScore=int(bowl())
        target=cScore+1
        print('OK. Now it is time for you to bat.\nYour target is:',target,'\nGet ready!\nPress ENTER to start the game.')
        input()
        yourScore=int(bat())        
# C.2) Computer chose to bowl
    else:
        print('Computer chose to bowl. Get ready to bat!\nPress ENTER to start the game.')
        input()
        yourScore=int(bat())
        print('OK. Now it is time for you to bowl. Get ready!\nPress ENTER to start the game.')
        input()
        cScore=int(bowl())

# Results
a,b,c='-------------','|',' _____________'
print('\n\n')
print('Game over.\n')
print(c,'\n'+b,'           ',b)
print(b+' Score Board '+b)
print(b+a+b,'\n'+b+'  You   '+b+' '+str(yourScore),end='')
if yourScore<100:
    print(' |')
else:
    print(b)
print(b+a+b,'\n'+b+'Computer'+b+' '+str(cScore),end='')
if cScore<100:
    print(' |')
else:
    print(b)
print(b+'_____________'+b)
print()
diff=abs(cScore-yourScore)
if cScore>yourScore:
    print('You lose. Computer wins for',diff,'run(s).')
elif cScore<yourScore:
    print('Congrats! You win for',diff,'run(s).')
else:
    print("Match draw. Wow. That's rare.")
