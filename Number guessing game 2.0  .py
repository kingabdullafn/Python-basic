import random
import time

number=random.randibt(1, 100)
def intro( ):
    print("May I ask you name?")
    global Name
    name = input( )
    print(name + ", we are going to play a  game. I am thinking of a number between1 and 100")
    if(number%2==0): 
        x='even'
    else:
        x= 'odd'
        print("nThi is an {number}".format(x))
        time.sleep(.5)
        print("Go ahead. Guess!")

def pick( ):
    guessesTaken < 6:

    while guessesTaken < 6:
        time.sleep(.25)
        enter=input("Guess: ")

        try:

            guess = int(enter)


            if guess <=100 and guess>=1:
                guessesTaken=guessesTaken+1
                if guessesTaken<6:
                    if guess<number:
                        print("The guess of the number that you have entered is to low")
                    if guess>number:
                        print("The guess o the number that you have entered is too high")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again!")

                    if guess==number:
                        break
            if guess>100 or guess<1:
                        print("Oii Mandem that aint in the range y a get mee fool me one more time imma chef you up")
                        time.sleep(.25)
                        print("Please enter a number between 1 and 100 or immma chef you up")
        except:
             print("I dont think that "+enter+" is a number. soory ")
    if guess == number:
         guessesTaken = str(guessesTaken)
         print('Good boy !{} guesses!' .format(name, guessesTaken))
    if guess != number:
        print('Nope. The number I was thinking of was ' + str(number))

playagain="yes"
while playagain=="yes" or playagain=="y" or playagain=="Yes":
	intro()
	pick()
	print("Do you want to play again?")
	playagain=input()          
