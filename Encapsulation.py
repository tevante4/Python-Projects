# Defining ProtectedVar() class and initializing _protect_var variable.
class ProtectedVar:
    def __init__(self):
        self._protected_var = 0

# Created instance, assigned value, and printed value.
object1 = ProtectedVar()
object1._protected_var = 34
print(object1._protected_var)

# Defining PrivateVar() class and initializing __private_var variable.
class PrivateVar():
    def __init__(self):
        self.__private_var = 12

    # Defined printPrivateVar() class to print the variable.
    def printPrivateVar(self):
        print(self.__private_var)

    # Defined setPrivateVar() class to set the variable.
    def setPrivateVar(self, private):
        self.__private_var = private

# Created instance, printed value of variable, set new value to variable, and printed new value.
object2 = PrivateVar()
object2.printPrivateVar()
object2.setPrivateVar(32)
object2.printPrivateVar()
