#overloading >= operator
class Age():
    def __init__(self,age):
        self.age=age

    def __ge__(self,other):
        result = self.age >= other.age
        return result

A_age = int(input("Enter age of person A: "))
B_age = int(input("Enter age of person B: "))
personA = Age(A_age)
personB = Age(B_age)

print("Is Person_A's age >= Person_B's age? ", personA >= personB)


