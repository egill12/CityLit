import pickle
import datetime
import pandas as pd
import math

class Tamagotchi:
    def __init__(self, name,colour, breed, personality, size, weight, height ):
        self.name = name
        self.colour = colour
        self.breed = breed
        self.personality = personality
        self.size = size
        self.weight = weight
        self.height = height

        # all Tamas start off with the below. its a set IC
        self.hunger = 0
        self.tiredness = 0
        self.boredom = 0

        self.last_played = datetime.datetime.now()
        self.last_meal = datetime.datetime.now()

    def save(self):
        with open(f'[self.name].p', "wb") as f:
            pickle.dump(self, f)

    def get_hungry(self):
        time_last_meal = (datetime.datetime.now() - self.last_meal)/pd.Timedelta(minutes = 1)

        if time_last_meal > 0.1:
            self.hunger += 50

        if self.hunger > 50:
            print("Feed me!!")

    def feed_animal(self,food_size, water_size):
        self.hunger = self.hunger - (food_size + water_size**2)

    def play_time(self,play_game, complexity):

        self.tiredness += play_game*(complexity/2)

        if self.tiredness >50:
            print("I dont want to play any more, leave me alone!")
        self.boredom -= play_game*(complexity**0.7)
        self.last_played = datetime.datetime.now()

    def update_all_feelings(self):
        time_last_meal = (datetime.datetime.now() - self.last_meal) / pd.Timedelta(minutes=1)
        min_since_played = (datetime.datetime.now() - self.last_played) / pd.Timedelta(minutes=1)

        self.hunger += time_last_meal*5
        self.boredom += min_since_played*3
        self.tiredness += (time_last_meal+min_since_played)**0.5

    def check_feelings(self):
        #update_all_feelings
        if self.tiredness > 10:
            print(" I'm getting sleepy...ZZZZ")
        else:
            print(" I'm ready for play time!")
        if self.boredom >5:
            print(" I'm getting bored, you're boring me...")
        if self.hunger > 15:
            print("I'm so hungry my belly hurts...")
        else:
            print("Wow I am soooo stuffed")

if __name__ == "__main__":
    Derek = Tamagotchi("Derek", "Purple", "Donkey", "Needy", "Large", 100, 5)
    Derek.get_hungry()
    Derek.update_all_feelings
    print(Derek.check_feelings())
    print(Derek.hunger)
    

