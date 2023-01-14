# random module :- it is a built in module with many functions in it
import random
import os
l1=["stone","paper","scissor"]
print("The choices are \n1.Stone \n2.Paper \n3.Scissor")
ch=int(input("Enter the choice : "))
print("**************************************************")
print("Your choice is : ",ch)
computer_choice=random.choice(l1)
print("Computer choice is :",computer_choice)
if((ch==1 and computer_choice=="stone") or (ch==2 and computer_choice=="paper") or (ch==3 and computer_choice=="scissor")):
    print("DRAW")
elif((ch==1 and computer_choice=="paper")):
    print("Player Win")
elif((ch==1 and computer_choice=="scissor")):
    print("Computer Win")
elif((ch==2 and computer_choice=="stone")):
    print("Player Win")
elif((ch==2 and computer_choice=="scissor")):
    print("Computer Win")
elif((ch==3 and computer_choice=="stone")):
    print("Computer Win")
elif((ch==3 and computer_choice=="paper")):
    print("Player Win")
else:
    print("Wrong operation entered")
