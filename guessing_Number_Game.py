import random

def main():
    num=0
    myNum=random.randint(0,101)
    
    while(num>=0):
        num=int(input("Guess the number(0-100): "))
    
        if(num == myNum):
            print("WOOOOO.....HOOOOOO.....\nYou Guess the correct number. . .")
            break
        elif(num>myNum):
            print("Number is too large! ! !")
        else:
            print("Number is too small! ! !")
    
    print("My number is {}\nGame Finish. . . .".format(myNum))

if __name__ == "__main__":
    main()
