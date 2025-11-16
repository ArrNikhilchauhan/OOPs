# Encapsulation :

class Atm():
    def __init__(self):
        self.__pin=1234
        self.__balance=1000
        print(self)
        # self.menu()


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
        self.__pin=int(input_pin)

        print("PIN Changed Succesfully")
        print(type(self.__pin),self.__pin)
        self.menu()
    
    def deposit_balance(self):
        check=int(input("Enter Your PIN to deposit"))
        if check==self.__pin:
            amount=input("Enter the Amount")
            self.__balance+=int(amount)
            print("Amount Added Succesfully",self.__balance)
        else:
            print("Invalid PIN")

        self.menu()
    
    def withdraw(self):
        check=int(input("Enter Your PIN to withdraw"))
        if check==self.__pin:
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
        if check==self.__pin:
            print("Amount :",self.__balance)

        self.menu()

        

sbi=Atm()


print(sbi.__balance)




