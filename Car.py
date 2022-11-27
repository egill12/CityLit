'''
Session 1 City Lit
'''

class Car:
    def __init__(self, pos, vel,make, colour):
        # w have them in the function here as these are initial conditions that need to be set to start.
        # but indicator = false means all inital cars set up will not be indicating.
        self.pos = pos
        self.vel = vel
        self.make = make
        self.colour = colour
        self.indicating = False

    def toggle_indicate(self):
        if self.indicating:
            self.indicating = False
        else:
            self.indicating = True

    def move(self, dx, dy):
        x = self.pos[0]
        y = self.pos[1]
        self.pos = [x+dx, y+dy]



if __name__ == "__main__":
    # when we run a specific file , then we are running the file, if we import this file then we will not run the code in the if statement
    tim_car = Car(pos = [0,0], vel = [1,0], make = "Ford", colour = "Grey")
    artur_car = Car(pos = [10,0], vel = [0,1], make = "Audi", colour = "Black")

    print(tim_car.indicating)
    tim_car.toggle_indicate()
    print(tim_car.indicating)