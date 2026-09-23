
'''
1 for sanke
-1 for water
0 for gun
'''
computer= -1
youstr=input("Enter your choice:").lower()
youDict={"s": 1, "w":-1,"g":0}
reverseDict={1:"Sanke",-1:"Water",0:"Gun"}
you=youDict[youstr]
print(F"You chose{reverseDict[you]}\nComputer chouse{reverseDict[computer]}")
if(computer==you):
    print("its is draw")

else:

    if(computer==-1 and you==1):
     print("You win!")

    elif(computer==-1 and you==0):
     print("You lose!")

    elif(computer==1 and you==-1):
     print("You lose!")

    elif(computer==1 and you==0):
     print("You win!")

    elif(computer==0 and you==-1):
     print("You win!")

    elif(computer==0 and you==1):
     print("You lose!")

    else:
     print("something want wrong!")





