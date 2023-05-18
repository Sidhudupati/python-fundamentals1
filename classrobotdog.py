class Robot_dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):  #we create class method same like function
        print("Woof woof!")    
my_dog=Robot_dog('spot','chichua')
print(my_dog.name)
print(my_dog.breed)
my_dog.bark()