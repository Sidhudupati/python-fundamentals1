menu = {'Breakfast':['idly','wada','sambar'],
        'Lunch':['Biryani','curry','curd'],
        'Dinner':['Roti','curry','milk']}
print("Breakfast:",menu['Breakfast'])   
for name,menu in menu.items():
    print(name,":",menu)
#print("Breakfast:",menu.get('Breakfast'))                  
