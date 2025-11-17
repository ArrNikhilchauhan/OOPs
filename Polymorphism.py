# Method Overriding
# Method Overloading
# Operator Overloading

#################################### Method Overriding ##########################################

class phone():
    def __init__(self,name,price,company):
        print("Inside a Phone")
        self.name=name
        self.price=price
        self.company=company

    def buy(self):
        print("Buying a Phone")

class SmartPhone(phone):

    def buy(self):
        print("Buying a SmartPhone")


s=SmartPhone("Galaxy j4",20000,"Samsung")

s.buy() # it will call self buy function not parent buy function it shows method over riding


###################################### use of Super() #############################################

class phone():
    def __init__(self,name,price,company):
        print("Inside a Phone")
        self.name=name
        self.price=price
        self.company=company

    def buy(self):
        print("Buying a Phone")

class SmartPhone(phone):

    def __init__(self, name, price, company):
        print("Inside a Smartphone")
        super().__init__(name, price, company) ## now we initialize the parent constructor in child class 

    def buy(self):
        print("Buying a SmartPhone")


s=SmartPhone("Galaxy j4",20000,"Samsung")
        

# super() gives the reference to parent class and we can use directly the parent class methods and all by using super function
# concept of self: in child class we can use parent variable with self. because self is nothing same as the object reference so if we can acces it from outside then we can access from inside also using self
# self=reference to same object that is calling that class