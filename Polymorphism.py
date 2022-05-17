# Parent Class User
class User:
    name = "Tev"
    email = "tev@gmail.com"
    password = "1234abcd!"

    def getLoginInfo(self):
        entry_name = input("Please enter your name: ")
        entry_email = input("Please enter your email: ")
        entry_password = input("Please enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")


# Child Class Employee
class Employee(User):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"
    
    # This is the same method in the parent class "User".
    # The difference is that, instead of using entry_password, we're using entry_pin.
    
    def getLoginInfo(self):
        entry_name = input("Please enter your name: ")
        entry_email = input("Please enter your email: ")
        entry_pin = input("Please enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect.")


# Child Class Customer
class Customer(User):
    mailing_address = ''
    mailing_list = True
    
    def getLoginInfo(self):
        entry_name = input("Please enter your name: ")
        entry_email = input("Please enter your email: ")
        entry_password = input("Please enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")


# The following code invokes the methods inside each class for User and Employee.

cust = Customer()
cust.getLoginInfo()

manager = Employee()
manager.getLoginInfo()
