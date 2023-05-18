current_movies={'RRR':'11:00',
                'KKK':'02:00',
                'BBB':'06:00',
                'AAA':'09:00'}
for i in (current_movies):
    print(i)
movie=input("What movie would you like to select:")
showtime=current_movies.get(movie)
if(showtime==None):
    print(movie+" is not playing")
else:
    print(movie+" is playing at "+showtime)        
