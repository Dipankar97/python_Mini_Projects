import random
import os

def check(userPoint):
    r = ""
    best = ""
    if not os.path.exists("game_result.txt"):
        f = open("game_result.txt","w")
        f.write(userPoint)
        f.close()
    else:
        f = open("game_result.txt","r")
        r = f.read()
        f.close()
        if (int(userPoint) > int(r)):
            f = open("game_result.txt","w")
            f.write(str(userPoint))
            f.close()
            best = userPoint
        else:
            best = r
    return best

def main():
    diff = 0
    userPoint = 0
    myPoint = 0
    userChoice = 0
    myChoice = 0
    choice = ["Rock", "Paper", "Sizer"]

    round = int(input("Enter game rounds: "))

    while (round>0):
        myChoice = random.randint(1, 3)
        userChoice = int(input("1.Rock\n2.Paper\n3.Sizer\nEnter your choice (ONLY NUMBER): "))

        round = round - 1

        if ((userChoice == 1 and myChoice == 3) or (userChoice == 2 and myChoice == 1) or(userChoice == 3 and myChoice == 2)):
            print ("\nYou chose {} and chif chose {}".format(choice[userChoice - 1], choice[myChoice - 1]))
            print ("\nWOOOO.....HOOOOO.........You bit chef.......\nOnly {} round left\n".format(round))
            userPoint = userPoint + 100

        elif ((userChoice == 1 and myChoice == 1) or (userChoice == 2 and myChoice == 2) or (userChoice == 3 and myChoice == 3)):
            print ("\nYou chose {} and chif chose {}".format(choice[userChoice - 1], choice[myChoice - 1]))
            print ("\nDraw....You and chef chose same......Try to bit her! ! !\nOnly {} round left\n".format(round))
            if (userPoint >= 50):
                userPoint = userPoint - 50
            elif (myPoint >= 50):
                myPoint = myPoint - 50

        elif (userChoice > 3 or userChoice <= 0):
            print ("\nWrong input.....Try again! ! !\n")
            round = round + 1

        else:
            print ("\nYou chose {} and chif chose {}".format(choice[userChoice - 1], choice[myChoice - 1]))
            print ("\nBOOOO.....Chef bit you....Try to bit her! ! !\nOnly {} round left\n".format(round))
            myPoint = myPoint + 100

    all_Time_Best_Score = check(str(userPoint))

    print("\n\n####################\n")

    if (userPoint > myPoint):
        print ("\nHURHHHH..........\nYou WON this game\n\nYour score: {}\nChif's score: {}\n".format(userPoint, myPoint))
    elif (userPoint < myPoint):
        diff = myPoint - userPoint
        print ("\nBOOHHHH..........\nYou LOSE! ! !\n\nYour score: {}\nChif's score: {}\nYou need just {} to win this game\n".format(userPoint, myPoint, diff))
    else:
        print ("\nGame Draw! ! !\n\nYour score: {}\nChif's score: {}\n".format(userPoint, myPoint))

    print("\n\nAll time best score [Highest score {}]\nGame finished. . . . . .\n".format(all_Time_Best_Score))
    print("\n#######################\n\n")

if __name__ == "__main__":
    main()
