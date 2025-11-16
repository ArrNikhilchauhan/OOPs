class Counter():

    __counter=1

    def __init__(self):
        self.serial=Counter.__counter
        Counter.__counter+=1
    @staticmethod
    def get_counter():
        return Counter.__counter
    @staticmethod
    def set_counter(val):
        Counter.__counter=val
    


a1=Counter()#2
a2=Counter()#3
a3=Counter()#4

print(Counter.get_counter())#4 because __counter is a static/class variable which do not change at instance it increses on each object creation