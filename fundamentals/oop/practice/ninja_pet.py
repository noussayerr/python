class Pet:
    def __init__(self ,name,type,tricks):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health=0
        self.energy=0
    def sleep(self):
        self.energy+=25
        return self
    def eat(self):
        self.energy+=5
        self.health+=10
        return self
    def play(self):
        self.health+=5
        return self
    def noise(self):
        print("the pet's sound")
class ninja:
    def __init__(self ,first_name,last_name,pet,treats,pet_food):
        self.first_name=first_name
        self.last_name=last_name
        self.pet=pet
        self.treats=treats
        self.pet_food=pet_food
    def walk(self):
        self.pet.play()
    def feed(self):
        self.pet.eat()
    def bathe(self):
        self.pet.noise()
pet_food=["Cookie","Taco","Tuna"]
ninja_treats=["training","Hide-and-seek"]
rsas=Pet("rsas","cat","eat")
noussayer=ninja("rahal","noussayer",rsas,ninja_treats,pet_food)
noussayer.walk()
noussayer.bathe()
noussayer.feed()
print(rsas.energy)
print(rsas.health)