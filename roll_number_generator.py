import random

def main():
    alert = 0
    roll = ""
    s_r = ""
    r = 0
    while(True):
        n = int(input("Enter school roll number: "))
        for i in range(12):
            r = random.randint( 0, 9)
            roll = roll + str(abs(r - n) % 5)
        roll[:12]
        ch = input("Please enter your correct choice from flowlling:--"
                   "\n1.Andhra Pradesh\n2.Bihar\n3.Maharashtra\n4.Uttar Pradesh\n5.West Bengal\nPlease Enter number only: ")
        if  (ch == '1'):
            s_r = "AP011{}".format(roll)
            print("\nYour Unique Roll for Andhra Pradesh State: {}\n".format(s_r))
            r = 0
            roll = ""
            s_r = ""
            alert = 0
        elif (ch == '2'):
            s_r = "BH021{}".format(roll)
            print("\nYour Unique Roll for Bihar State: {}\n".format(s_r))
            r = 0
            roll = ""
            s_r = ""
            alert = 0
        elif (ch == '3'):
            s_r = "MH013{}".format(roll)
            print("\nYour Unique Roll for Maharastra State: {}\n".format(s_r))
            r = 0
            roll = ""
            s_r = ""
            alert = 0
        elif (ch == '4'):
            s_r = "UP031{}".format(roll)
            print("\nYour Unique Roll for Uttar Pradesh State: {}\n".format(s_r))
            r = 0
            roll = ""
            s_r = ""
            alert = 0
        elif (ch == '5'):
            s_r = "WB014{}".format(roll)
            print("\nYour Unique Roll for West Bengal State: {}\n".format(s_r))
            r = 0
            roll = ""
            s_r = ""
            alert = 0
        else:
            if (alert == 2):
                print("\nSystem use roughly! ! !\n")
                break
            else:
                alert += 1
                if (alert == 2):
                    print("\nPlease enter correct choice! ! !\nSystem Alert (Wrong Input! ! !) [{}/3][Last Chance]\n".format(alert))
                else:
                    print("\nPlease enter correct choice! ! !\nSystem Alert (Wrong Input! ! !) [{}/3]\n".format(alert))
                r = 0
                roll = ""
                s_r = ""

if __name__ == "__main__":
    main()