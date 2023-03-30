import addition
import subtraction
import division
import multiplication



print("MENU :")
print("PRESS 1 FOR ADDITION")
print("PRESS 2 FOR SUBTRACTION")
print("PRESS 3 FOR MULTIPLICATION")
print("PRESS 4 FOR DIVISION")
choice =  int(input())
if choice >0 and choice <5:

    a = int(input("enter a number A :"))
    b = int(input("enter a number b :"))



    if choice == 1:
        addition.addition(a,b)
    elif choice == 2:
        subtraction.subtraction(a,b)
    elif choice == 3:
        multiplication.multiplication(a,b)
    else:
        division.division(a,b)
else:
    print("OOPS! YOU ENTER WRONG CHOICE")