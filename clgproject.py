def confirm():
    e=input("Do you want to make any changes in your booking?\n1.Yes  2.No\n")
    if(e=='1'):
        print("No worries! Please restart your booking")
        exit()
    elif(e=='2'):
        payments(chooseSeat())

def chooseSeat():
        print("=================================================================================")
        print("[G1] [G2] [G3] [G4] [G5] [G6] [G7] [G8] [G9] [G10] [G11] [G12] [G13] [G14] [G15]")
        print("[F1] [F2] [F3] [F4] [F5] [F6] [F7] [F8] [F9] [F10] [F11] [F12] [F13] [F14] [F15]")
        print("  [E1] [E2] [E3] [E4] [E5] [E6] [E7] [E8] [E9] [E10] [E11] [E12] [E13] [E14]")
        print("  [D1] [D2] [D3] [D4] [D5] [D6] [D7] [D8] [D9] [D10] [D11] [D12] [D13] [D14]")
        print("  [C1] [C2] [C3] [C4] [C5] [C6] [C7] [C8] [C9] [C10] [C11] [C12] [C13] [C14]")
        print("       [B1] [B2] [B3] [B4] [B5] [B6] [B7] [B8] [B9] [B10] [B11] [B12]")
        print("       [A1] [A2] [A3] [A4] [A5] [A6] [A7] [A8] [A9] [A10] [A11] [A12]")
        print("=================================================================================")
        print("----------------------------[[[------SCREEN------]]]-----------------------------")
        print("=================================================================================")

        seats=list(map(str,input("Choose Seats : ").split()))#input should be taken by spearting with spaces
    #user has the access to modify no of seats while giving input

        return seats

def payments(seatCount):
    no_Of_Seats=len(seatCount)
    print("Seats          Price")
    for i in seatCount:
        print(i.upper(),"    ||     Rs 500")
    print("TOTAL PAYABLE AMOUNT :",no_Of_Seats*500,"/-")

    x=input("Choose the payment option from below:\n1.CARD  2.UPI\n")
    if(x=='1'):
        print("Swipe your card at the box office")
    elif(x=='2'):
        print("Scan the QR code at box office and make the payment") 

print("Welcome to Easy Booking!!")
m=input("Choose the nearest cinemas!\n1.INOX(KUKATPALLY)\n2.PVR(PANJAGUTTA)\n3.PRASADS(HYDERABAD)\n4.PVR(BANJARAHILLS)\n5.INOX(GACHIBOWLI)\n")
print("The following movies are playing right now!")
print("Please select the movie from below")
now_movies=['1.The Kerala Story','2.Guardians of the Galaxy 3','3.Fast X']
current_movies={'3':'1.08:30am  2.03:30pm   3.09:30pm',
                '4':'1.11:30am  2.06:30pm',
                '1':'1.10:30am  2.01:30pm    3.06:30pm',                
                '2':'1.03:30pm  2.10:30pm',                
                '5':'1.09:30am  2.08:30pm',                
                '6':'1.04:30pm  2.11:30pm',                       
                }
for i in now_movies:
    print(i)
a=input()
if(a=='1'): #kerala story
    b=input("Choose language\n1.Hindi   2.Telugu\n")
    print("Choose Showtime")
    if(b=='1'):
        showtime=current_movies.get('1')
        print(showtime)
        c=input()
        if(c=='1'):
            d=input("Please confirm your booking:\nYou have selected the Movie THE KERALA STORY in HINDI at 10:30AM\n1.Yes  2.No\n")
            if(d=='1'):
                payments(chooseSeat())
            else:
                confirm()    
        elif(c=='2'):
             d=input("Please confirm your booking:\nYou have selected the Movie THE KERALA STORY in HINDI at 01:30PM\n1.Yes  2.No\n")
             if(d=='1'):
                payments(chooseSeat())
             else:
                confirm() 
        elif(c=='3'):
             d=input("Please confirm your booking:\nYou have selected the Movie THE KERALA STORY in HINDI at 06:30PM\n1.Yes  2.No\n")
             if(d=='1'):
                payments(chooseSeat())
             else:
                confirm()
    elif(b=='2'):
        showtime=current_movies.get('2')   
        print(showtime)
        c=input() 
        if(c=='1'):
            d=input("Please confirm your booking:\nYou have selected the Movie THE KERALA STORY in TELUGU at 03:30PM\n1.Yes  2.No\n")
            if(d=='1'):
                payments(chooseSeat())
            else:
                confirm()   
        elif(c=='2'):
             d=input("Please confirm your booking:\nYou have selected the Movie THE KERALA STORY in TELUGU at 10:30PM\n1.Yes  2.No\n")
             if(d=='1'):
                payments(chooseSeat())
             else:
                confirm()  
elif(a=='2'): #Guardians
    b=input("Choose version\n1.3D(English)  2.2D(English)\n")
    print("*Please note that the movie is only available in English*")
    print("Choose Showtime")
    if(b=='1'):
        showtime=current_movies.get('3')
        print(showtime)
        c=input()
        if(c=='1'):
            d=input("Please confirm your booking:\nYou have selected the Movie GUARDIANS OF THE GALAXY in 3D at 08:30AM\n1.Yes  2.No\n")
            if(d=='1'):
                payments(chooseSeat())
            else:
                confirm() 
        elif(c=='2'):
             d=input("Please confirm your booking:\nYou have selected the Movie GUARDIANS OF THE GALAXY in 3D at 03:30PM\n1.Yes  2.No\n")
             if(d=='1'):
                payments(chooseSeat())
             else:
                confirm() 
        elif(c=='3'):
             d=input("Please confirm your booking:\nYou have selected the Movie GUARDIANS OF THE GALAXY in 3D at 09:30PM\n1.Yes  2.No\n")
             if(d=='1'):
                payments(chooseSeat())
             else:
                confirm()
    elif(b=='2'):
        showtime=current_movies.get('4')   
        print(showtime)
        c=input() 
        if(c=='1'):
            d=input("Please confirm your booking:\nYou have selected the Movie GUARDIANS OF THE GALAXY in 2D at 11:30AM\n1.Yes  2.No\n")
            if(d=='1'):
                payments(chooseSeat())
            else:
                confirm()   
        elif(c=='2'):
             d=input("Please confirm your booking:\nYou have selected the Movie GUARDIANS OF THE GALAXY in 2D at 06:30PM\n1.Yes  2.No\n")
             if(d=='1'):
                payments(chooseSeat())
             else:
                confirm() 
elif(a=='3'): #FAst X
    b=input("Choose version\n1.3D(English)   2.4DX(English)\n")
    print("*Please note that the movie is only playing in ENGLISH*")
    print("Choose Showtime")
    if(b=='1'):
        showtime=current_movies.get('5')
        print(showtime)
        c=input()
        if(c=='1'):
            d=input("Please confirm your booking:\nYou have selected the Movie Fast X in 3D at 09:30AM\n1.Yes  2.No\n")
            if(d=='1'):
                payments(chooseSeat())
            else:
                confirm()   
        elif(c=='2'):
             d=input("Please confirm your booking:\nYou have selected the Movie Fast X in 3D at 08:30PM\n1.Yes  2.No\n")
             if(d=='1'):
                payments(chooseSeat())
             else:
                confirm()  
    if(b=='2'):
        showtime=current_movies.get('6')
        print(showtime)
        c=input()
        if(c=='1'):
            d=input("Please confirm your booking:\nYou have selected the Movie Fast X in 4DX(3D) at 04:30PM\n1.Yes  2.No\n")
            if(d=='1'):
                payments(chooseSeat())
            else:
                confirm()   
        elif(c=='2'):
             d=input("Please confirm your booking:\nYou have selected the Movie Fast X in 4DX(3D) at 11:30PM\n1.Yes  2.No\n")
             if(d=='1'):
                payments(chooseSeat())
             else:
                confirm()                 


