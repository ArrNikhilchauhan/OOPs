class parent:
    
    def money(self):
        print("Money")
    def rules(self):
        print("Rules")


class Children:
    def toys(self):
        print("Toys")

    def sweets(self):
        print("Sweets")


class Shop(parent,Children):

    pass

    

obj=Shop()

obj.money()
obj.sweets()
obj.rules()
obj.toys()
