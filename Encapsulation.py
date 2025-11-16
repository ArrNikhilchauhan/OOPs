# Encapsulation : It is the way to control access on our data and methods ,in python nothing is private truly*/

class Atm():
    def __init__(self):
        self._pin=1234 # convention of  protected data member (single underscore)
        self.__balance=1000 #convention of private data member (double underscore)
        self.age=32  # Public Data member we can access from any object
        print(self)
        self.menu()

 # We use property in python for encapsulation it makes our task very much easy  
 # property is a class  under hood and it has four callbles in __init__
 # obj.balance will call getter automatically
 # obj.balance=321 it will call setter 
 # del obj.balance will call delete function 


    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,bal):
        if type(bal)==int:
            self.__balance=bal
            print("Balance Updated")
        else:
            print("Something is wrong")
    def menu(self):
        user_input=input("""
            How you like to proceed:
                1.Create PIN
                2.Deposit Cash
                3.Withdraw Cash
                4.Show Balance
                5.Exit 
""")
        if int(user_input)==1:
            self.create_pin()
        elif int(user_input)==2:
            self.deposit_balance()
        elif int(user_input)==3:
            self.withdraw()
        elif int(user_input)==4:
            self.show_balance()
        elif int(user_input)==5:
            print("Exit bye bye")

    def create_pin(self):
        input_pin=input("Enter Your PIN")
        self._pin=int(input_pin)

        print("PIN Changed Succesfully")
        print(type(self._pin),self._pin)
        self.menu()
    
    def deposit_balance(self):
        check=int(input("Enter Your PIN to deposit"))
        if check==self._pin:
            amount=input("Enter the Amount")
            self.__balance+=int(amount)
            print("Amount Added Succesfully",self.__balance)
        else:
            print("Invalid PIN")

        self.menu()
    
    def withdraw(self):
        check=int(input("Enter Your PIN to withdraw"))
        if check==self._pin:
            amount=int(input("Enter the Amount to withdraw"))

            if amount>self.__balance:
                print("Insufficient Balance")
            else:
                self.__balance-=amount
                print("Amount withdrawn successfully",self.__balance)
        else:
            print("Invalid PIN")

        self.menu()

    def show_balance(self):
        check=int(input("Enter Your PIN to show balance"))
        if check==self._pin:
            print("Amount :",self.__balance)

        self.menu()

        

sbi=Atm()


sbi.balance="kasie ho"
print(sbi.balance)




