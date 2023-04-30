cc='scissors'
uc=input("Do you want rock,paper or scissors?\n")
if uc==cc:
    print("Tie")
elif(uc=='rock' and cc=='scissors'):
    print("user wins")
elif(uc=='paper' and cc=='scissors'):
    print("Computer wins")
elif(uc=='paper' and cc=='rock'):
    print("User wins")
else:


    
    print("You lose")
     