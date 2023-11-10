# Object Oriented Programming
# Homework Assignment

# 1. Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        print(f'Distance of a line: {distance}')

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        slope = ((y2 - y1) / (x2 - x1))

        print(f'Slope of a line: {slope}')

# coordinate1 = (3,2)
# coordinate2 = (8,10)

# li = Line(coordinate1,coordinate2)
# li.distance()
# li.slope()


# 2. Fill in the class

class Cylinder:

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        volume = self.pi*(self.radius**2)*self.height
        print('Volume of a cylinder of radius {self.radius} is ',volume)

    def surface_area(self):
        area = 2*self.pi*self.radius*self.height + 2*self.pi*(self.radius**2)
        print('Surface area of a cylider of radius {self.radius} is ', area)

# c = Cylinder(2, 3)

# c.volume()
# c.surface_area()

# Object Oriented Programming Challenge
# 3. For this challenge, create a bank account class that has 

# two attributes:
# owner
# balance

# and two methods:
# deposit
# withdraw

# As an added requirement, withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self, balance):
        self.balance = self.balance + balance
        print('Deposit Accepted!')

    def withdraw(self, balance):
        if self.balance >= balance:
            print('Withdrawal Accepted!')
            self.balance = self.balance - balance
        else:
            print('Funds Unavailable!')

acct1 = Account('Jose', 100)

# print(acct1.owner)
# print(acct1.balance)

acct1.deposit(100)
print(acct1.balance)
acct1.withdraw(50)
acct1.withdraw(400)
print(acct1.balance)
