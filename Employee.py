class Employee:

    def __init__(self, payband,qualification,address,e_number,job_title,Fname, Sname=None,):
        self.payband = payband
        self.qualification = qualification
        self.address = address
        self.e_number = e_number
        self.job_title = job_title
        self.Fname = Fname
        self.Sname = Sname

        if self.Sname == None:
            self.email = f'{self.Fname}@company.com'
        else:
            self.email = f'{self.Fname}.{self.Sname}@company.com'


    def modify_payband(self, band):
        if isinstance(band, str):
            self.payband = band

    def get_full_name(self):
        return f'{self.Fname} {self.Sname}'


if __name__ == "__main__":
    # when we run a specific file , then we are running the file, if we import this file then we will not run the code in the if statement
    tim= Employee("A", "PhD", "E3", "Researcher", "Tim", "Marley")
    #artur_car = Car(pos = [10,0], vel = [0,1], make = "Audi", colour = "Black")
    tim.payband
    tim.modify_payband("B")
    print(tim.payband)
    print(tim.email)
    #print(tim_car.indicating)
    #tim_car.toggle_indicate()
    #print(tim_car.indicating)

