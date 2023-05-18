import random
def diceroll():
    roll= random.randint(1,6)+random.randint(1,6)
    return roll
def main():
    a=input("Enter a name:")
    b=input("Enter another ")
    roll1 = diceroll()
    roll2 = diceroll()
    print(a,"rolled",roll1)
    print(b,"rolled",roll2)

    if roll1>roll2:
        print(a,"wins")
    elif roll2>roll1:
        print(b,"wins")
    else:
        print("Tie")        
main()