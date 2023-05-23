print("Welcome to Aadya's Kitchen!")
print("Here's your menu")
print("Soups:\n1.Hot & Sour Veg Soup:'219/-'\n2.Chicken Noodles Soup:'229/-'")
print("Starters:\n3.Veg Manchurian:'259/-'\n4.Paneer 65:'259/-'\n5.Chicken Chilli:'299/-'\n6.Apollo Fish:'329/-'")
print("Curries:\n7.Paneer Butter Masala:'329/-'\n8.Dal Makhani:'329/-'\n9.Butter Chicken:'359/-'\n10.Kadai Chicken:'359/-'")
print("Rotis:\n11.Plain Naan:'59/-'\n12.Butter Naan:'69/-'\n13.Garlic Naan:'79/-'\n14.Roti:'49/-")
print("Main Course:\n15.Veg Pulao:'289/-'\n16.Paneer Pulao:'299/-'\n17.Mushroom Pulao:'299/-'\n18.Curd Rice:'259/-'\n19.Chicken Dum Biryani:'399/-'\n20.Chicken Pulao:'389/-'\n21.Avakaya Mutton Biryani:'419/-'\n22.Fish Pulao:'419/-'")
print("Desserts:\n23.Apricot Delight:'329/-'\n24.Sitaphal Delight:'329/-'\n25.Mango Alphonso:'259/-'")
print("Drinks:\n26.Mineral Water:'39/-'\n27.Coke:'59/-'\n")
now_menu=['0','1.Hot & Sour Veg Soup:219/-','2.Chicken Noodles Soup:229/-',
          '3.Veg Manchurian:259/-','4.Paneer 65:259/-',
          '5.Chicken Chilli:299/-','6.Apollo Fish:329/-',
          '7.Paneer Butter Masala:329/-','8.Dal Makhani:329/-',
          '9.Butter Chicken:359/-','10.Kadai Chicken:359/-',
          '11.Plain Naan:59/-','12.Butter Naan:69/-',
          '13.Garlic Naan:79/-','14.Roti:49/-',
          '15.Veg Pulao:289/-','16.Paneer Pulao:299/-',
          '17.Mushroom Pulao:299/-','18.Curd Rice:259/-',
          '19.Chicken Dum Biryani:399/-','20.Chicken Pulao:389/-',
          '21.Avakaya Mutton Biryani:419/-','22.Fish Pulao:419/-',
          '23.Apricot Delight:329/-','24.Sitaphal Delight:329/-',
          '25.Mango Alphonso:259/-','26.Mineral Water:39/-',
          '27.Coke:59/-' ,
          ]
our_menu=[0,219,229,259,259,299,329,329,329,359,359,59,69,79,49,289,299,299,259,399,389,419,419,329,329,259,39,59]
list1=[]

def selection():
    sel=list(map(int,input("Enter dishes no: ").split()))
    for i in sel:
        list1.append(now_menu[i])
    return sel
def payments(p):
    sum=0
    for i in p:
        sum+=our_menu[i]
    for i in list1:
        print(i)
    print("Total:",sum,"/-")

payments(selection())
