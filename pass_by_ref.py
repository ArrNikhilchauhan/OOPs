class Customer():
    def __init__(self,name):
        self.name=name


def greet(Customer):
    print("Before",id(Customer.name))
    Customer.name+=" naam h mera"
    print("After",id(Customer.name))     
    return "Aise nhi bolte"

obj=Customer("Nikhil")
obj1=Customer("Preeti")

greet(obj)
greet(obj1)

print("Final",id(obj.name))
print("Final",id(obj1.name))